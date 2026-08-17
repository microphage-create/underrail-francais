#!/usr/bin/env python3
"""Create packs/<id> from the French tree. Live dialog keys = English *_original."""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "packs" / "francais"
KEY_RE = re.compile(r"^=>(\S+)\s*$")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Create packs/<id> for a new language.")
    p.add_argument("--id", required=True, help="folder id, e.g. deutsch")
    p.add_argument("--name", required=True, help="Options menu name, e.g. Deutsch")
    p.add_argument("--force", action="store_true")
    return p.parse_args()


def parse_blocks(text: str) -> list[tuple[str, str]]:
    """Return (key, body) in file order. body has no trailing <end>."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    ordered: list[tuple[str, str]] = []
    key: str | None = None
    buf: list[str] = []
    for line in text.split("\n"):
        m = KEY_RE.match(line)
        if m and key is None:
            key = m.group(1)
            buf = []
            continue
        if key is None:
            continue
        if line.strip() == "<end>" or line.rstrip().endswith("<end>"):
            if line.strip() != "<end>":
                buf.append(re.sub(r"<end>\s*$", "", line).rstrip())
            ordered.append((key, "\n".join(buf).rstrip("\n")))
            key = None
            buf = []
        else:
            buf.append(line)
    return ordered


def reset_dialog(src: Path, dst: Path) -> None:
    blocks = parse_blocks(src.read_text(encoding="utf-8"))
    by_key = {k: v for k, v in blocks}
    out: list[str] = []
    for key, body in blocks:
        if key.endswith("_original"):
            live = body
        else:
            live = by_key.get(key + "_original", body)
        out.append("=>" + key)
        if live:
            out.append(live)
        out.append("<end>")
        out.append("")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(("\r\n".join(out).rstrip() + "\r\n").encode("utf-8"))


def main() -> int:
    args = parse_args()
    pack_id = args.id.strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9_-]{1,32}", pack_id):
        print("id: ascii letters, digits, _- only", file=sys.stderr)
        return 2
    if not SRC.is_dir():
        print("missing", SRC, file=sys.stderr)
        return 2
    dest = ROOT / "packs" / pack_id
    if dest.exists() and not args.force:
        print("exists:", dest, "(use --force)", file=sys.stderr)
        return 2
    if dest.exists():
        shutil.rmtree(dest)

    n_dlg = n_oth = 0
    for src in SRC.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(SRC)
        dst = dest / rel
        if rel.name.lower() == "info.txt":
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes((args.name.strip() + "\n").encode("utf-8"))
        elif rel.parts[:1] == ("dialogs",) and src.suffix.lower() == ".txt":
            reset_dialog(src, dst)
            n_dlg += 1
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            n_oth += 1

    print(f"created {dest}")
    print(f"  dialogs (live = EN original): {n_dlg}")
    print(f"  other files copied: {n_oth}")
    print(f"  info.txt -> {args.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
