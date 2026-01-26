# Dry Run

Use dry-run to validate device selection and manifest values before any destructive action.

```bash
python3 core/sonic_cli.py plan --usb-device /dev/sdb --dry-run --layout-file config/sonic-layout.json
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --dry-run

# V2 partitioning dry-run
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --v2 --dry-run

# V2 payload-only dry-run
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --v2 --payloads-only --dry-run

# V2 payloads dir override dry-run
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --v2 --payloads-dir /path/to/payloads --payloads-only --dry-run

# V2 payloads without validation (dry-run)
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --v2 --no-validate-payloads --payloads-only --dry-run
```
