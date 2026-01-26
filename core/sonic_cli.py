"""Sonic Screwdriver CLI wrapper.

Usage:
  python3 core/sonic_cli.py plan --usb-device /dev/sdb --ventoy-version 1.1.10
"""

import argparse
import subprocess
from pathlib import Path

from os_limits import support_message, is_supported
from plan import write_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Sonic Screwdriver CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    plan_cmd = sub.add_parser("plan", help="Generate ops manifest")
    plan_cmd.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    plan_cmd.add_argument("--usb-device", default="/dev/sdb")
    plan_cmd.add_argument("--ventoy-version", default="1.1.10")
    plan_cmd.add_argument("--dry-run", action="store_true")
    plan_cmd.add_argument("--out", default="config/sonic-manifest.json")
    plan_cmd.add_argument("--layout-file", default="config/sonic-layout.json")
    plan_cmd.add_argument(
        "--format-mode",
        default=None,
        choices=["full", "skip"],
        help="Formatting mode for partitions (full|skip). Defaults to layout file or full.",
    )

    run_cmd = sub.add_parser("run", help="Execute bash entrypoint")
    run_cmd.add_argument("--manifest", default="config/sonic-manifest.json")
    run_cmd.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    if args.cmd == "plan":
        print(support_message())
        if not is_supported():
            print("ERROR Unsupported OS for build operations. Use Linux.")
            return 1
        try:
            write_plan(
                repo_root=Path(args.repo_root),
                usb_device=args.usb_device,
                ventoy_version=args.ventoy_version,
                dry_run=args.dry_run,
                layout_path=Path(args.layout_file) if args.layout_file else None,
                format_mode=args.format_mode,
                out_path=Path(args.out),
            )
        except ValueError as exc:
            print(f"ERROR {exc}")
            return 1
        print(f"Plan written: {args.out}")
        if args.dry_run:
            print("Dry run enabled. No destructive operations should be executed.")
        return 0

    print(support_message())
    if not is_supported():
        print("ERROR Unsupported OS for build operations. Use Linux.")
        return 1

    script = Path(__file__).resolve().parents[1] / "scripts" / "sonic-stick.sh"
    cmd = ["bash", str(script), "--manifest", args.manifest]
    if args.dry_run:
        cmd.append("--dry-run")
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
