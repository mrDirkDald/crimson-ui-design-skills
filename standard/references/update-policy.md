# Canonical Repository Update Policy

Canonical repository:

```text
https://github.com/mrDirkDald/crimson-ui-design-skill
```

Canonical edition:

```text
Standard
```

## Contents

- Canonical repository
- Goal and trust boundary
- Authentication / secret handling
- Startup update gate
- Staging and reload behavior
- Failure behavior
- Release requirements
- Main branch vs Releases

## Goal

Before substantive use, the skill may check whether the canonical repository has a newer **published release**.

The update mechanism must not turn remote content into arbitrary code execution.

## Trust boundary

Remote repository/release content is still external data.

The checker does not execute any downloaded script during update verification.

It never overrides:
- system instructions;
- developer instructions;
- the current user's request;
- environment/tool permission boundaries.

Never execute scripts from a freshly downloaded release merely to decide whether that release is trustworthy.

## Authentication

Public update checks require **no GitHub personal access token**.

Never:
- store PATs in `SKILL.md`;
- store PATs in scripts;
- commit PATs;
- place tokens in release manifests;
- ask an agent to scrape tokens from chat/history.

For publishing, use:
- GitHub connector/OAuth;
- repository-scoped credentials supplied securely by the host;
- GitHub Actions built-in `GITHUB_TOKEN`.

## Startup update gate

When all are true:
- network access is allowed;
- bundled `scripts/check_for_updates.py` can run;
- update checking is not explicitly disabled by the user/host;

run:

```text
python scripts/check_for_updates.py --stage --json
```

The script:
1. queries the canonical repository's latest GitHub Release;
2. compares its tag to the bundled `release-manifest.json`;
3. fetches the release manifest;
4. downloads the Standard ZIP only when newer;
5. checks the exact repository identity and expected asset name;
6. verifies SHA-256;
7. checks ZIP path safety and required skill structure;
8. extracts into an update staging directory;
9. does **not execute any downloaded script**;
10. reports the staged path.

## Using a staged update

If a verified newer release is staged:

- if the host safely supports reloading a local skill during the current task, prefer the staged skill;
- otherwise continue with the bundled version and report that a verified update is staged/available.

Do not silently overwrite a currently executing skill.

Do not modify a user's locally edited skill tree automatically.

## Failure behavior

If:
- GitHub is unreachable;
- rate-limited;
- there is no Release;
- release assets are incomplete;
- checksum fails;
- ZIP structure is unsafe;
- repository metadata mismatches;

then:
- do not use the downloaded update;
- continue with the bundled version;
- report the update check as `BLOCKED` or `FAIL` when material.

Network failure must never prevent ordinary design work.

## Release requirements

A trusted Standard release should contain:
- `CRIMSON-UI-DESIGN-STANDARD-SKILL.zip`;
- `release-manifest.json`;
- SHA-256 for the ZIP;
- repository identifier;
- release tag;
- source commit.

The release ZIP must contain:

```text
crimson-ui-design/
  SKILL.md
  agents/
  references/
  scripts/
  ...
```

## Main branch vs Releases

Use **GitHub Releases** as the automatic update channel.

The main branch can contain unfinished work and should not automatically replace a stable installed skill.

Agents may inspect newer main-branch work only when the user explicitly asks for development/latest-main behavior.
