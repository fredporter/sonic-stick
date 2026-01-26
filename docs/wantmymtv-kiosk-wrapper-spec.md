# WantMyMTV – Full‑Screen / Kiosk Wrapper Spec (Windows)

Target URL  
https://wantmymtv.vercel.app/player.html

---

## 1) Goals

- Instant full‑screen playback
- Remote‑only control
- No visible browser chrome
- Clean return to Kodi

---

## 2) Recommended Implementation — Edge Fullscreen / Kiosk

**Behaviour**
- Launches directly into WantMyMTV
- Full‑screen display
- Single‑site browsing

**Exit strategy**
- Remote‑mapped key closes window (Alt+F4 or custom)
- Kodi regains focus immediately

---

## 3) Alternative — Chrome App Mode

- Launch with `--app=<url>`
- Borderless window
- Optional fullscreen flag

Trade‑off: slightly less locked‑down than Edge kiosk.

---

## 4) Kodi Integration

- Kodi menu item launches kiosk command
- Browser runs on top of Kodi
- Closing browser returns user to Kodi UI

---

## 5) Remote Control Mapping (Minimum)

Recommended key mappings:
- Back / Exit → Close browser window
- Home → Close browser / return to Kodi
- Play / Pause → Space
- Volume → System volume

FLIRC or Bluetooth remotes recommended.

---

## 6) Resilience

- Kodi remains running if browser crashes
- WantMyMTV can always be relaunched
- No multi‑tab or general browsing allowed

---

## 7) Nice‑to‑Haves

- Party Mode (launch + set volume + disable notifications)
- Screensaver suppression
- Sonic Stick branded tile/icon
