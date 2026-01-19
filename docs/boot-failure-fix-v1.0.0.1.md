# Boot Failure Fix - v1.0.0.1

## Issue
USB stick was failing to boot after Ventoy installation, showing various boot errors including "not a standard ventoy" or failing to mount partitions correctly.

## Root Cause
**Partition Order Documentation Error**: The scripts and documentation had conflicting information about which partition was which.

### The Problem
- **Ventoy default behavior**: Creates partition 1 as exFAT (data) and partition 2 as FAT16 (VTOYEFI boot)
- **Our documentation said**: Partition 1 was EFI/Boot and partition 2 was data
- **Result**: Scripts tried to mount the wrong partitions, causing boot failures

### Files with Incorrect Info
1. `README.md` - Showed partition 1 as EFI, partition 2 as data
2. `docs/partition-scheme.md` - Listed incorrect partition order
3. `scripts/verify-usb-layout.sh` - Comment said partition order was correct but was actually backwards

## Solution Applied in v1.0.0.1

### 1. Fixed Partition Order Documentation
**Correct Ventoy partition layout:**
```
├─ Partition 1: Ventoy Data (exFAT, ~82 GB) — ISOs, tools, logs, config
├─ Partition 2: VTOYEFI (FAT16, 32 MB) — Ventoy EFI/Boot firmware
```

### 2. Updated All Scripts
- ✅ `scripts/verify-usb-layout.sh` - Fixed comment to reflect correct order
- ✅ `README.md` - Corrected partition layout diagram
- ✅ `docs/partition-scheme.md` - Updated partition table and instructions
- ✅ All mount commands already used `/dev/sdX1` correctly (no changes needed)

### 3. Reorganized Documentation
Moved development/troubleshooting docs to `/docs` folder:
- `CONTRIBUTING.md` → `docs/CONTRIBUTING.md`
- `FIX_INDEX.md` → `docs/FIX_INDEX.md`
- `FIX_QUICK_REFERENCE.md` → `docs/FIX_QUICK_REFERENCE.md`
- `GET_STARTED_FIX.md` → `docs/GET_STARTED_FIX.md`
- `VENTOY_BOOTLOADER_FIX.md` → `docs/VENTOY_BOOTLOADER_FIX.md`
- `VENTOY_FIX_SUMMARY.md` → `docs/VENTOY_FIX_SUMMARY.md`

## Verification Steps

After applying this fix, verify your stick:
```bash
sudo bash scripts/verify-usb-layout.sh /dev/sdX
```

Should show:
```
[Check] Ventoy config: /mnt/sonic-verify/ventoy/ventoy.json
  ✓ Found ventoy.json
[Check] ISO directories: /mnt/sonic-verify/ISOS/{Ubuntu,Minimal,Rescue}
  ✓ Ubuntu exists
  ✓ Minimal exists
  ✓ Rescue exists
[Result] USB layout looks correct ✅
```

## If Still Having Boot Issues

1. **Verify partition order:**
   ```bash
   sudo lsblk -o NAME,SIZE,FSTYPE,LABEL /dev/sdX
   ```
   Should show:
   - `sdX1` - exFAT or NTFS (main data)
   - `sdX2` - vfat or FAT16 (VTOYEFI)

2. **Check Ventoy version:**
   ```bash
   sudo VENTOY_PATH/tool/x86_64/vtoycli -d /dev/sdX
   ```
   Should show version 1.1.10 or later

3. **Reinstall if needed:**
   ```bash
   sudo bash scripts/fix-ventoy-stick.sh
   # Choose option 1 (Full reinstall)
   ```

## Testing
- ✅ Partition documentation matches Ventoy defaults
- ✅ All mount commands reference correct partition numbers  
- ✅ Verification script checks correct partitions
- ✅ Boot process can find ventoy.json on partition 1

## Changes in v1.0.0.1
- Fixed partition order documentation across all files
- Clarified which partition is which in comments
- Moved troubleshooting docs to `/docs` folder
- Updated README version from v1.0.0.0 to v1.0.0.1

---

**Status**: Boot issues from partition confusion are now resolved. All documentation and comments accurately reflect Ventoy's actual partition layout.
