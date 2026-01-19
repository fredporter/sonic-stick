# Sonic Stick - Quick Start Guide

## ✅ What's Installed

Your USB stick is ready with:

- **5 Bootable ISOs** ready to use
- **Custom Ventoy Menu** with organized categories
- **All downloads complete** (12GB+ of OS images)

## 📋 Available Systems

### Ubuntu Desktop ISOs (Installers + Live Mode)
- **Ubuntu 22.04.5 LTS Desktop** (4.5GB) - Full-featured, recommended
- **Lubuntu 22.04.5 LTS** (2.9GB) - Lightweight, good for older hardware
- **Ubuntu MATE 22.04.5 LTS** (4.2GB) - Traditional desktop experience

### Minimal & Rescue
- **Alpine Linux 3.19.1** (207MB) - Minimal, security-focused
- **TinyCore Pure64 15.0** (20MB) - Ultra-minimal rescue system

### Raspberry Pi Images (for SD card creation)
- Raspberry Pi OS Lite
- DietPi
- Ubuntu Server 22.04

## 🚀 How to Boot

### Step 1: Insert USB
Plug in your Sonic Stick USB drive

### Step 2: Reboot & Enter Boot Menu
- **Dell**: Press `F12` during startup
- **HP**: Press `ESC` or `F9`
- **Lenovo**: Press `F12`
- **Generic**: Try `ESC`, `F12`, or `F2`

### Step 3: Select USB Boot
Look for:
- `USB: SONIC 3.2Gen1`
- `UEFI: SONIC`
- `USB HDD`

### Step 4: Navigate Ventoy Menu
- **Arrow keys**: Navigate
- **Enter**: Select/boot
- **ESC**: Go back

## 🎯 Usage Modes

### Mode 1: Try Live (No Installation)
Boot any Ubuntu ISO → Select "Try Ubuntu"
- Runs entirely from USB
- Nothing installed to your computer
- Changes are lost on reboot
- Perfect for testing

### Mode 2: Install to System
Boot any Ubuntu ISO → Select "Install"
- Installs to your internal hard drive/SSD
- Replaces or dual-boots with existing OS
- **⚠️ CAUTION**: This modifies your system disk!

### Mode 3: Rescue/Recovery
Boot Alpine or TinyCore
- Emergency troubleshooting
- Data recovery
- System repair

## 📖 Menu Items Explained

| Menu Item | Purpose | Installs? |
|-----------|---------|-----------|
| Ubuntu 22.04.5 LTS Desktop | Try or install full Ubuntu | Optional |
| Lubuntu 22.04.5 LTS | Try or install lightweight Ubuntu | Optional |
| Ubuntu MATE 22.04.5 LTS | Try or install MATE desktop | Optional |
| Alpine Linux 3.19.1 | Live system, run 'setup-alpine' to install | Optional |
| TinyCore Pure64 15.0 | Emergency recovery, runs from RAM | Never |

## ⚙️ Customization

### Change Menu Configuration
Edit the file on USB: `/ventoy/ventoy.json`

Configuration location on your computer:
```bash
/home/wizard/Code/sonic-stick/config/ventoy/ventoy.json
```

### Add More ISOs
1. Download new ISO files
2. Copy to USB: `/ISOS/Ubuntu/` or `/ISOS/Minimal/`
3. Reboot - Ventoy auto-detects new ISOs

### Update Ventoy
Run from project directory:
```bash
sudo bash scripts/install-ventoy.sh
```

## 🔧 Troubleshooting

### Problem: Empty Ventoy Menu
**Solution**: 
1. Mount USB: `ls /media/$USER/Ventoy/ISOS/`
2. Check ISOs are present
3. If missing, rerun: `sudo bash scripts/rebuild-from-scratch.sh`

### Problem: Boot Fails / Black Screen
**Solution**:
1. Check BIOS settings - disable Secure Boot
2. Try different boot option (UEFI vs Legacy)
3. Verify ISO integrity

### Problem: Can't Boot from USB
**Solution**:
1. Enter BIOS (usually F2 or DEL at startup)
2. Set USB as first boot device
3. Save and exit

### Problem: System Boots Normally (Ignores USB)
**Solution**:
- USB is probably not selected in boot menu
- Try holding F12 longer during startup
- Check if USB is plugged in before powering on

## 📁 USB Stick Structure

```
/dev/sdb
├── sdb1 (114GB) - Ventoy partition (exFAT)
│   ├── ISOS/
│   │   ├── Ubuntu/        (3 ISOs, ~11GB)
│   │   ├── Minimal/       (Alpine, ~207MB)
│   │   └── Rescue/        (TinyCore, ~20MB)
│   ├── RaspberryPi/       (3 images, ~1.5GB)
│   └── ventoy/
│       └── ventoy.json    (custom menu config)
└── sdb2 (32MB) - EFI boot partition

Total ISOs: 5
Total Size Used: ~13GB
Free Space: ~101GB
```

## 🔄 Rebuild from Scratch

If something goes wrong:

```bash
cd /home/wizard/Code/sonic-stick
sudo bash scripts/rebuild-from-scratch.sh
```

This will:
- Wipe USB completely
- Reinstall Ventoy
- Copy all ISOs
- Apply custom menu
- Takes ~5 minutes

## ⚡ Quick Commands

### Check what's on the USB
```bash
lsblk /dev/sdb
ls /media/$USER/Ventoy/ISOS/
```

### Scan library
```bash
bash scripts/scan-library.sh
```

### Add new ISOs
```bash
# Download ISOs first
bash scripts/download-payloads.sh

# Then rebuild
sudo bash scripts/rebuild-from-scratch.sh
```

## 🎓 Tips

1. **First time?** Try "Try Ubuntu" mode - it won't change anything
2. **Slow computer?** Use Lubuntu instead of Ubuntu
3. **Just testing?** Alpine boots in seconds
4. **Need rescue?** TinyCore is your friend
5. **Installing?** Make sure you have internet/WiFi access

## 🆘 Help

Project location: `/home/wizard/Code/sonic-stick`

View documentation:
- [README.md](../README.md)
- [Ventoy Usage](ventoy-usage.md)
- [Partition Scheme](partition-scheme.md)

---

**Your Sonic Stick is ready to boot! 🚀**

Just reboot, press F12, and select your USB drive.
