# Dry Run

Use dry-run to validate device selection and manifest values before any destructive action.

```bash
python3 core/sonic_cli.py plan --usb-device /dev/sdb --dry-run
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json --dry-run
```
