# Build USB (Linux)

1) Generate manifest:
```bash
python3 core/sonic_cli.py plan --usb-device /dev/sdb --ventoy-version 1.1.10
```

2) Run launcher:
```bash
bash scripts/sonic-stick.sh --manifest config/sonic-manifest.json
```

3) Follow prompts and confirm destructive steps.
