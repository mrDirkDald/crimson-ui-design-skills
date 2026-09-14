\
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LOCAL_MANIFEST = ROOT / "release-manifest.json"
REPO = "mrDirkDald/mrDirkDald-crimson-ui-design-light"
VERSION_URL = f"https://raw.githubusercontent.com/{REPO}/main/version.json"
ARCHIVE_URL = f"https://github.com/{REPO}/archive/refs/heads/main.zip"
MAX_DOWNLOAD = 64 * 1024 * 1024
MAX_UNPACKED = 160 * 1024 * 1024
MAX_ENTRIES = 5000
USER_AGENT = "crimson-ui-design-light-update-checker/1"

class UpdateError(RuntimeError):
    pass

def fetch_bytes(url: str, max_bytes: int = MAX_DOWNLOAD) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read(max_bytes + 1)
        if len(data) > max_bytes:
            raise UpdateError("download exceeds size limit")
        return data

def load_json_bytes(data: bytes) -> dict:
    value = json.loads(data.decode("utf-8"))
    if not isinstance(value, dict):
        raise UpdateError("metadata must be a JSON object")
    return value

def is_symlink(info: zipfile.ZipInfo) -> bool:
    return ((info.external_attr >> 16) & 0o170000) == 0o120000

def verify_remote_version(meta: dict) -> None:
    if meta.get("schema_version") != 1:
        raise UpdateError("unsupported metadata schema")
    if meta.get("repository") != REPO:
        raise UpdateError("repository identity mismatch")
    if meta.get("edition") != "light":
        raise UpdateError("edition mismatch")
    version = meta.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"[0-9A-Za-z._-]{1,64}", version):
        raise UpdateError("invalid version")

def verify_and_extract(data: bytes, target: Path) -> Path:
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as f:
        f.write(data)
        tmp = Path(f.name)
    try:
        with zipfile.ZipFile(tmp) as z:
            infos = z.infolist()
            if len(infos) > MAX_ENTRIES:
                raise UpdateError("too many archive entries")
            total = 0
            required_suffixes = {
                "SKILL.md",
                "scripts/check_for_updates.py",
                "release-manifest.json",
                "subskills/tooling/SKILL.md",
            }
            seen_suffixes = set()
            for info in infos:
                name = info.filename.replace("\\", "/")
                total += info.file_size
                if total > MAX_UNPACKED:
                    raise UpdateError("archive unpacked size exceeds limit")
                if name.startswith("/") or re.match(r"^[A-Za-z]:/", name):
                    raise UpdateError("absolute archive path rejected")
                parts = [p for p in name.split("/") if p not in ("", ".")]
                if ".." in parts:
                    raise UpdateError("path traversal rejected")
                if is_symlink(info):
                    raise UpdateError("symlink rejected")
            roots = sorted({info.filename.split("/", 1)[0] for info in infos if "/" in info.filename})
            if len(roots) != 1:
                raise UpdateError("unexpected repository archive layout")
            repo_root = roots[0]
            repo_prefix = repo_root + "/"

            for info in infos:
                name = info.filename.replace("\\", "/")
                if not name.startswith(repo_prefix):
                    continue
                rel = name[len(repo_prefix):]
                if rel in required_suffixes:
                    seen_suffixes.add(rel)
            missing = required_suffixes - seen_suffixes
            if missing:
                raise UpdateError("archive missing required skill files")

            if target.exists():
                shutil.rmtree(target)
            target.mkdir(parents=True, exist_ok=True)

            allowed_roots = {"agents", "references", "scripts", "subskills"}
            allowed_files = {"SKILL.md", "release-manifest.json"}
            for info in infos:
                name = info.filename.replace("\\", "/")
                if not name.startswith(repo_prefix) or name.endswith("/"):
                    continue
                rel = name[len(repo_prefix):]
                top = rel.split("/", 1)[0]
                if rel not in allowed_files and top not in allowed_roots:
                    continue
                out = target / rel
                out.parent.mkdir(parents=True, exist_ok=True)
                with z.open(info) as src, out.open("wb") as dst:
                    shutil.copyfileobj(src, dst)

            skill = target / "SKILL.md"
            if not skill.exists() or "name: crimson-ui-design" not in skill.read_text(encoding="utf-8")[:1000]:
                raise UpdateError("staged SKILL.md identity check failed")
            return target
    finally:
        tmp.unlink(missing_ok=True)

def default_stage_root() -> Path:
    override = os.environ.get("CRIMSON_UI_LIGHT_UPDATE_CACHE")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".cache" / "crimson-ui-design-light" / "updates"

def emit(**obj) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--stage-dir", type=Path, default=None)
    args = ap.parse_args()

    try:
        local = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
        remote = load_json_bytes(fetch_bytes(VERSION_URL, 64 * 1024))
        verify_remote_version(remote)
        local_version = str(local.get("version", "unknown"))
        remote_version = remote["version"]

        if remote_version == local_version:
            emit(status="current", local_version=local_version, latest_version=remote_version)
            return 0

        if not args.stage:
            emit(status="update-available", local_version=local_version, latest_version=remote_version)
            return 0

        data = fetch_bytes(ARCHIVE_URL)
        stage_root = args.stage_dir or default_stage_root()
        target = stage_root / remote_version / "crimson-ui-design"
        target.parent.mkdir(parents=True, exist_ok=True)
        verify_and_extract(data, target)
        emit(status="staged", verified=True, local_version=local_version, latest_version=remote_version, staged_skill=str(target), executed_remote_code=False)
        return 0

    except urllib.error.HTTPError as e:
        emit(status="blocked", reason=f"GitHub HTTP {e.code}")
        return 2
    except urllib.error.URLError as e:
        emit(status="blocked", reason=f"network unavailable: {e.reason}")
        return 2
    except (UpdateError, json.JSONDecodeError, OSError, zipfile.BadZipFile) as e:
        emit(status="fail", reason=str(e))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
