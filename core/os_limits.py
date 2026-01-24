"""OS detection and limitations for Sonic Screwdriver."""

import platform
from typing import Dict


def detect_platform() -> str:
    system = platform.system().lower()
    if system == "linux":
        distro = platform.release().lower()
        if "alpine" in distro:
            return "alpine"
        return "linux"
    if system == "darwin":
        return "macos"
    if system == "windows":
        return "windows"
    return system


def os_capabilities() -> Dict[str, bool]:
    os_name = detect_platform()
    return {
        "linux": os_name in {"linux", "alpine"},
        "alpine": os_name == "alpine",
        "macos": os_name == "macos",
        "windows": os_name == "windows",
    }


def is_supported() -> bool:
    caps = os_capabilities()
    return caps.get("linux", False)


def support_message() -> str:
    if is_supported():
        return "OK Linux-based OS detected."
    return "WARN Sonic Screwdriver build requires Linux (Ubuntu/Debian/Alpine)."
