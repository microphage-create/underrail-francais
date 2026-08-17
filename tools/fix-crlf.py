#!/usr/bin/env python3
"""Force CRLF on loc text files. Engine ignores LF-only dialogs and shows English."""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "packs/francais")
n = 0
for p in root.rglob("*.txt"):
    raw = p.read_bytes()
    if b"\r\n" in raw and b"\n" in raw.replace(b"\r\n", b""):
        # mixed: normalize
        text = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        p.write_bytes(text.replace(b"\n", b"\r\n"))
        n += 1
        print("mixed->CRLF", p.relative_to(root))
    elif b"\r\n" not in raw and b"\n" in raw:
        p.write_bytes(raw.replace(b"\n", b"\r\n"))
        n += 1
        print("LF->CRLF", p.relative_to(root))
print("converted", n)
