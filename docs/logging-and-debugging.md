# Logging and Debugging

This project now ships with a small logging toolkit to capture build-time activity and USB stick state for troubleshooting boot issues.

## Where logs go
- **On the stick (preferred):** `/media/$USER/SONIC/LOGS` if the Ventoy partition is mounted and writable.
- **Data partition:** `/media/$USER/SONIC_DATA/logs` if you log from within a live session (TinyCore hook writes here when available).
- **Host fallback:** `LOGS/` in this repository if the stick is not mounted.

## Enabling script logging
- All major scripts (`install-ventoy.sh`, `reflash-complete.sh`, `rebuild-from-scratch.sh`, `create-data-partition.sh`, `setup-data-partition-guided.sh`, `scan-library.sh`) now tee their output to a timestamped log.
- Set `DEBUG=1` to enable verbose `set -x` tracing inside any script:
  ```bash
  DEBUG=1 sudo bash scripts/reflash-complete.sh
  ```
- Override the log destination if needed:
  ```bash
  LOG_ROOT=/media/$USER/SONIC/LOGS sudo bash scripts/rebuild-from-scratch.sh
  ```

## Collecting a support bundle
Use the collector after a failed boot to gather state without copying ISOs:
```bash
sudo bash scripts/collect-logs.sh /dev/sdX   # example: /dev/sdb
```
What you get in `LOGS/collect-<timestamp>/`:
- `lsblk.txt`, `blkid.txt`, and `dmesg-tail.txt`
- `iso-list.txt` (names of ISOs on the stick)
- Ventoy config/version (`ventoy.json`, `ventoy-version.txt` when present)
- Data partition config, catalog, and any `logs/` content (without ISOs)

## Boot-time logs (TinyCore)
- `scripts/tinycore-bootlog.sh` appends hardware, dmesg tail, and network state to `LOGS/boot.log` on the stick. It prefers the `SONIC_DATA` mount when present and falls back to the Ventoy partition.
- To enable in TinyCore, add to `/opt/bootlocal.sh`:
  ```bash
  /mnt/sda1/tinycore-bootlog.sh
  ```
  Adjust the path if your stick shows up as another device.

## What to attach when reporting issues
1. The latest directory under `LOGS/collect-*` from `scripts/collect-logs.sh`.
2. Any `boot.log` produced by `scripts/tinycore-bootlog.sh` during the failing boot.
3. The exact ISO name and boot mode (UEFI vs legacy) you used.
