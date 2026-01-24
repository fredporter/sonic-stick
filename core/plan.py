"""Plan and emit Sonic Screwdriver operations manifest."""

import argparse
from pathlib import Path
from typing import Dict, Optional

from manifest import default_manifest, write_manifest
from os_limits import support_message, is_supported


def build_plan(args: argparse.Namespace) -> Dict:
    repo_root = Path(args.repo_root).resolve()
    manifest = default_manifest(
        repo_root=repo_root,
        usb_device=args.usb_device,
        ventoy_version=args.ventoy_version,
        dry_run=args.dry_run,
    )
    return manifest.to_dict()

def write_plan(
    repo_root: Path,
    usb_device: str,
    ventoy_version: str,
    dry_run: bool,
    out_path: Path,
) -> Dict:
    manifest = default_manifest(repo_root, usb_device, ventoy_version, dry_run)
    write_manifest(out_path, manifest)
    return manifest.to_dict()


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sonic Screwdriver planner")
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--usb-device", default="/dev/sdb")
    parser.add_argument("--ventoy-version", default="1.1.10")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--out", default="config/sonic-manifest.json")

    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    print(support_message())
    if not is_supported():
        print("ERROR Unsupported OS for build operations. Use Linux.")
        return 1

    out_path = Path(args.out)
    plan = write_plan(
        repo_root=Path(args.repo_root),
        usb_device=args.usb_device,
        ventoy_version=args.ventoy_version,
        dry_run=args.dry_run,
        out_path=out_path,
    )
    print(f"Plan written: {out_path}")
    if args.dry_run:
        print("Dry run enabled. No destructive operations should be executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
