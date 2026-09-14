#!/usr/bin/env python3
"""
Safe update checker for Crimson UI Design Standard.

- Public GitHub API only: no PAT required.
- Downloads only published Release assets.
- Verifies manifest identity + SHA-256 + ZIP path safety.
- Stages the update.
- NEVER executes files from the downloaded release.
- NEVER overwrites the currently running skill.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LOCAL_MANIFEST = ROOT / "release-manifest.json"

OWNER = "mrDirkDald"
REPO = "crimson-ui-design-skill"
REPO_ID = f"{OWNER}/{REPO}"
LATEST_RELEASE_API = f"https://api.github.com/repos/{REPO_ID}/releases/latest"

MAX_DOWNLOAD_BYTES = 64 * 1024 * 1024
MAX_UNPACKED_BYTES = 160 * 1024 * 1024
MAX_ENTRIES = 5000

USER_AGENT = "crimson-ui-design-skill-update-checker/1"


class UpdateError(RuntimeError):
    pass


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_bytes(url: str, *, max_bytes: int = MAX_DOWNLOAD_BYTES) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        length = response.headers.get("Content-Length")
        if length and int(length) > max_bytes:
            raise UpdateError(f"Remote file too large: {length} bytes")
        data = response.read(max_bytes + 1)
        if len(data) > max_bytes:
            raise UpdateError("Remote file exceeded download size limit")
        return data


def fetch_json(url: str) -> dict:
    return json.loads(fetch_bytes(url).decode("utf-8"))


def asset_url(release: dict, name: str) -> str:
    for asset in release.get("assets", []):
        if asset.get("name") == name:
            url = asset.get("browser_download_url")
            if not isinstance(url, str) or not url.startswith("https://github.com/"):
                raise UpdateError(f"Unexpected asset URL for {name}")
            return url
    raise UpdateError(f"Release asset missing: {name}")


def valid_sha256(value: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-fA-F]{64}", value or ""))


def verify_release_manifest(remote: dict, release_tag: str) -> None:
    required = {
        "schema_version",
        "name",
        "edition",
        "repository",
        "release_tag",
        "source_commit",
        "asset_name",
        "sha256",
    }
    missing = sorted(required - set(remote))
    if missing:
        raise UpdateError(f"Remote manifest missing fields: {', '.join(missing)}")

    if remote["schema_version"] != 1:
        raise UpdateError("Unsupported manifest schema")
    if remote["name"] != "crimson-ui-design":
        raise UpdateError("Unexpected skill name")
    if remote["edition"] != "standard":
        raise UpdateError("Unexpected skill edition")
    if remote["repository"] != REPO_ID:
        raise UpdateError("Repository identity mismatch")
    if remote["release_tag"] != release_tag:
        raise UpdateError("Release tag/manifest mismatch")
    if remote["asset_name"] != "CRIMSON-UI-DESIGN-STANDARD-SKILL.zip":
        raise UpdateError("Unexpected Standard asset name")
    if not valid_sha256(remote["sha256"]):
        raise UpdateError("Invalid SHA-256 in remote manifest")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_symlink(info: zipfile.ZipInfo) -> bool:
    mode = (info.external_attr >> 16) & 0o170000
    return mode == 0o120000


def verify_zip_structure(data: bytes) -> None:
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
        tmp.write(data)
        tmp_path = Path(tmp.name)

    try:
        with zipfile.ZipFile(tmp_path) as z:
            infos = z.infolist()
            if len(infos) > MAX_ENTRIES:
                raise UpdateError("ZIP has too many entries")

            total = 0
            required = {
                "crimson-ui-design/SKILL.md",
                "crimson-ui-design/agents/openai.yaml",
                "crimson-ui-design/scripts/check_for_updates.py",
                "crimson-ui-design/release-manifest.json",
            }
            names = set()

            for info in infos:
                name = info.filename.replace("\\", "/")
                names.add(name)
                total += info.file_size

                if total > MAX_UNPACKED_BYTES:
                    raise UpdateError("ZIP unpacked size exceeds limit")
                if name.startswith("/") or re.match(r"^[A-Za-z]:/", name):
                    raise UpdateError(f"Absolute ZIP path rejected: {name}")
                parts = [p for p in name.split("/") if p not in ("", ".")]
                if ".." in parts:
                    raise UpdateError(f"Path traversal rejected: {name}")
                if is_symlink(info):
                    raise UpdateError(f"Symlink rejected: {name}")

            missing = sorted(required - names)
            if missing:
                raise UpdateError(f"ZIP missing required files: {', '.join(missing)}")

            skill_text = z.read("crimson-ui-design/SKILL.md").decode("utf-8", "strict")
            if "name: crimson-ui-design" not in skill_text[:1000]:
                raise UpdateError("Downloaded SKILL.md identity check failed")
    finally:
        tmp_path.unlink(missing_ok=True)


def safe_extract(data: bytes, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    zip_path = target.parent / (target.name + ".zip.tmp")
    zip_path.write_bytes(data)
    try:
        with zipfile.ZipFile(zip_path) as z:
            # verify_zip_structure already rejects traversal/symlinks.
            z.extractall(target)
    finally:
        zip_path.unlink(missing_ok=True)


def default_stage_root() -> Path:
    override = os.environ.get("CRIMSON_UI_UPDATE_CACHE")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".cache" / "crimson-ui-design" / "updates"


def result(**kwargs) -> None:
    print(json.dumps(kwargs, ensure_ascii=False, indent=2))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="Kept for stable invocation; output is JSON.")
    ap.add_argument("--stage", action="store_true", help="Download and stage a newer verified release.")
    ap.add_argument("--stage-dir", type=Path, default=None)
    args = ap.parse_args()

    try:
        local = load_json(LOCAL_MANIFEST)
        release = fetch_json(LATEST_RELEASE_API)
        latest_tag = release.get("tag_name")
        if not latest_tag:
            raise UpdateError("Latest release has no tag_name")

        local_tag = local.get("release_tag", "unreleased")
        if latest_tag == local_tag:
            result(
                status="current",
                repository=REPO_ID,
                local_tag=local_tag,
                latest_tag=latest_tag,
                downloaded=False,
            )
            return 0

        remote_manifest_name = local.get("manifest_asset_name", "release-manifest.json")
        remote_manifest = json.loads(
            fetch_bytes(asset_url(release, remote_manifest_name)).decode("utf-8")
        )
        verify_release_manifest(remote_manifest, latest_tag)

        if not args.stage:
            result(
                status="update-available",
                repository=REPO_ID,
                local_tag=local_tag,
                latest_tag=latest_tag,
                downloaded=False,
                source_commit=remote_manifest["source_commit"],
            )
            return 0

        zip_data = fetch_bytes(asset_url(release, remote_manifest["asset_name"]))
        actual_hash = sha256(zip_data)
        expected_hash = remote_manifest["sha256"].lower()
        if actual_hash.lower() != expected_hash:
            raise UpdateError("Downloaded ZIP SHA-256 mismatch")

        verify_zip_structure(zip_data)

        stage_root = args.stage_dir or default_stage_root()
        stage_target = stage_root / latest_tag
        stage_target.parent.mkdir(parents=True, exist_ok=True)
        safe_extract(zip_data, stage_target)

        metadata = {
            "repository": REPO_ID,
            "release_tag": latest_tag,
            "source_commit": remote_manifest["source_commit"],
            "sha256": actual_hash,
            "staged_skill": str(stage_target / "crimson-ui-design"),
            "executed_remote_code": False,
        }
        (stage_target / "staged-update.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        result(
            status="staged",
            local_tag=local_tag,
            latest_tag=latest_tag,
            verified=True,
            downloaded=True,
            **metadata,
        )
        return 0

    except urllib.error.HTTPError as exc:
        result(status="blocked", reason=f"GitHub HTTP {exc.code}", downloaded=False)
        return 2
    except urllib.error.URLError as exc:
        result(status="blocked", reason=f"Network unavailable: {exc.reason}", downloaded=False)
        return 2
    except (UpdateError, json.JSONDecodeError, OSError, zipfile.BadZipFile) as exc:
        result(status="fail", reason=str(exc), downloaded=False)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
