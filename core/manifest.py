"""Sonic Screwdriver manifest utilities."""

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class SonicManifest:
    usb_device: str
    ventoy_version: str
    repo_root: str
    payload_dir: str
    iso_dir: str
    flash_label: str = "FLASH"
    sonic_label: str = "SONIC"
    vtoyefi_label: str = "VTOYEFI"
    dry_run: bool = False

    def to_dict(self) -> Dict:
        return asdict(self)


def write_manifest(path: Path, manifest: SonicManifest) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest.to_dict(), indent=2))


def read_manifest(path: Path) -> Optional[Dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def default_manifest(repo_root: Path, usb_device: str, ventoy_version: str, dry_run: bool) -> SonicManifest:
    payload_dir = repo_root / "payloads"
    iso_dir = repo_root / "ISOS"
    return SonicManifest(
        usb_device=usb_device,
        ventoy_version=ventoy_version,
        repo_root=str(repo_root),
        payload_dir=str(payload_dir),
        iso_dir=str(iso_dir),
        dry_run=dry_run,
    )
