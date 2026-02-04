# Sonic Screwdriver Roadmap

**Scope:** Standalone USB builder + device database + uDOS compatibility

## Now (v1.3.0)
- Document standalone contract + decoupleable packaging
- Specify Ventoy-free partition layout
- Add Windows 10 install/WTG modes
- Define uDOS TUI minimal image target
- Expand device database schema (windows/media flags)

## Next (v1.2.x)
- Implement custom partitioning scripts
- Create bootloader profiles + reboot routing
- Add uDOS Windows launcher + mode selector
- Establish dataset validation + build scripts

## Later (v1.3+)
- Device profile auto-detection + recommendations
- Media console workflows (Kodi + WantMyMTV)
- Windows gaming profile automation
- Public standalone releases + install guide

## Gaps & Targets
- USB flashing + multi-boot builder still lacks Windows-side tooling (current scripts run only on Linux), so the roadmap needs desktop-friendly UI/CLI wrappers before Wizard bolt-ons can advertise cross-platform installers.
- Device database syncing is defined in the schema but the synchronized service/daemon that ships with Wizard is still missing; prioritize a `devices.db` importer plus metadata sync hooks so the TUI/Portal can surface the latest entries.
- Windows games/media-player integrations are roadmapped but currently have no runtime surface; document the codec/launcher requirements so a future Wizard/Sonic media console can be scoped before coding begins.

## Notes
- Sonic remains compatible with uDOS but must run independently.
- Build operations remain Linux-only (Alpine/Ubuntu).
