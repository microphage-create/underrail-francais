#!/usr/bin/env python3
"""Patch Underrail.exe player-visible journal / combat-log strings EN -> FR.
FR must be <= EN character count (.NET user-string slot).
Quit the game first.
"""
from __future__ import annotations

from pathlib import Path

EXE = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Underrail\underrail.exe")
BACKUP_DIR = Path(r"C:\Users\Marcel\Documents\Underrail-FR\backups")

# Journal / combat log / HUD notices only. Identifiers excluded.
REPLACEMENTS: list[tuple[str, str]] = [
    # trade log (screenshot)
    ("Item sold: ", "Vendu : "),
    ("Item purchased: ", "Acheté : "),
    ("Item acquired: ", "Obtenu : "),
    ("Item lost: ", "Perdu : "),
    # stealth break (screenshot) — short, game-log, not a calque
    (
        "You" + "'" + "ve bumped into another character and stumbled out of stealth.",
        "Tu rentres dans quelqu'un. Plus de furtivité.",
    ),
    (
        "Tu as percuté quelqu'un et tu sors de furtivité.",
        "Tu rentres dans quelqu'un. Plus de furtivité.",
    ),
    # pickpocket
    ("You successfully pickpocketed an item.", "Vol à la tire réussi."),
    ("You have been caught pickpocketing!", "Pris la main dans le sac !"),
    ("Insufficient pickpocketing skill.", "Pickpocketing trop bas."),
    # xp / oddity
    ("Level Up!", "Niveau +!"),
    ("Experience: ", "XP : "),
    ("You discovered ", "Découvert : "),
    ("You discover ", "Tu trouves "),
    (
        "You fail to learn anything new from this oddity: {0}.",
        "Rien de neuf sur cette curiosité : {0}.",
    ),
    (
        "Player gains [prop]{0}[/prop] experience points",
        "Tu gagnes [prop]{0}[/prop] XP",
    ),
    (
        "Your character has earned enough experience to advance a level.",
        "Assez d'XP pour monter d'un niveau.",
    ),
    # combat / AP
    ("Not enough action points", "Pas assez de PA."),
    ("Out of ammo!", "Munitions: 0"),
    ("Out of bolts!", "Carreaux: 0 !"),
    ("Not enough energy!", "Plus d'énergie !"),
    ("Insufficient skill.", "Skill trop bas."),
    ("Insufficient skill", "Skill trop bas"),
    ("Critical failure!", "Échec critique !"),
    ("Your actions have provoked hostilities.", "Tu as provoqué des hostilités."),
    ("Cannot end combat at this time.", "Combat pas encore fini."),
    ("Cannot interact with this object during combat.", "Impossible en combat."),
    ("Cannot initiate dialog while in combat.", "Pas de dialogue en combat."),
    ("Cannot initiate turn based combat again manually so soon.", "Trop tôt pour relancer le tour par tour."),
    ("Cannot fire single shots, but only burst.", "Uniquement en rafale."),
    # vents / world
    ("You closed the ventilation shaft.", "Tu fermes la gaine."),
    ("You opened the ventilation shaft.", "Tu ouvres la gaine."),
    ("You forced the ventilation shaft open.", "Tu forces la gaine."),
    (
        "You were not strong enough to force the ventilation shaft open.",
        "Pas assez fort pour forcer la gaine.",
    ),
    ("You picked up a spear.", "Tu ramasses une lance."),
    ("You found something", "Tu trouves un truc"),
    ("You found nothing unusual", "Rien d'inhabituel."),
    ("Not enough room", "Pas la place"),
    ("Not enough room to disembark here.", "Pas la place pour débarquer."),
    ("Not enough room to dismount here.", "Pas la place pour descendre."),
    ("You are too far away from the charges.", "Trop loin des charges."),
    ("You can catch no signal here.", "Aucun signal ici."),
    ("The signal is coming from somewhere above.", "Signal : quelque part au-dessus."),
    ("The signal is coming from somewhere far below.", "Signal : bien plus bas."),
    ("The signal is coming from somewhere below.", "Signal : quelque part en bas."),
    ("The signal is coming from the northeast.", "Signal : nord-est."),
    ("The signal is coming from the north.", "Signal : nord."),
    ("The signal is coming from the northwest.", "Signal : nord-ouest."),
    ("The signal is coming from the west.", "Signal : ouest."),
    ("The signal is coming from the southwest.", "Signal : sud-ouest."),
    ("The signal is coming from nearby.", "Signal : tout près."),
    ("You catch a very strong signal from somewhere nearby.", "Signal très fort, tout près."),
    ("You catch a strong signal from somewhere below.", "Signal fort, en bas."),
    ("You catch a strong signal from somewhere above.", "Signal fort, en haut."),
    ("You cannot save the game at this time.", "Sauvegarde impossible."),
    ("The pull handle broke off!", "La poignée a cassé !"),
    ("The Juice had no effect on {0}", "Juice inefficace sur {0}"),
    ("Damaged Armor", "Armure abîmée"),
    ("Stealth Mode", "Mode furtif"),
    ("You are currently in ", "Tu es en "),
    (
        "You are carrying so much junk you cannot move. You are also potentially suffering action point penalties.",
        "Trop chargé : tu ne bouges plus. Pénalité de PA possible.",
    ),
    (
        "Your current weapon has degraded from extensive use and will suffer reduced precision until repaired.",
        "Arme usée : précision réduite jusqu'à réparation.",
    ),
    (
        "Your current weapon has heavily degraded from extensive use and will suffer greatly reduced precision until repaired.",
        "Arme très usée : précision fortement réduite jusqu'à réparation.",
    ),
    (
        "Your character is fully focused, which makes them more effective in ranged combat. Focus is lost when you move.",
        "Focus max : meilleur au tir à distance. Perdu si tu bouges.",
    ),
    ("You cannot pilot anything with those claws.", "Pas de pilotage avec ces griffes."),
    ("You cannot operate a fishing rod with those appendages.", "Pas de canne avec ces appendices."),
    ("Cannot jump the ramp while towing.", "Pas de rampe en tractant."),
    ("You do not have the key to the ignition", "Pas la clé de contact"),
    ("The ignition has already been hotwired.", "Contact déjà ponté."),
    ("The ignition has already been hotwired", "Contact déjà ponté"),
    ("The coal is ready to be burned", "Le charbon est prêt."),
    ("The fire is roaring.", "Le feu rugit."),
    ("The fire is getting low.", "Le feu baisse."),
    ("The fire has burnt out.", "Le feu est éteint."),
]


def find_slots(data: bytes, text: str) -> list[int]:
    needle = text.encode("utf-16le")
    hits: list[int] = []
    start = 0
    expected = len(text) * 2 + 1
    while True:
        i = data.find(needle, start)
        if i < 0:
            break
        if i >= 1 and data[i - 1] == expected and i + len(needle) < len(data) and data[i + len(needle)] == 0:
            hits.append(i)
        start = i + 2
    return hits


def write_slot(buf: bytearray, off: int, en: str, fr: str) -> None:
    if len(fr) > len(en):
        raise ValueError(f"FR trop long: {len(fr)}>{len(en)} {fr!r} / {en!r}")
    old_payload = len(en) * 2
    for k in range(old_payload):
        buf[off + k] = 0
    raw = fr.encode("utf-16le")
    buf[off : off + len(raw)] = raw
    buf[off + len(raw)] = 0
    buf[off - 1] = len(fr) * 2 + 1


def main() -> int:
    for en, fr in REPLACEMENTS:
        if len(fr) > len(en):
            raise SystemExit(f"LEN FAIL {len(fr)}>{len(en)}\n EN {en!r}\n FR {fr!r}")
    if not EXE.exists():
        raise SystemExit(f"missing {EXE}")
    try:
        data = bytearray(EXE.read_bytes())
    except PermissionError:
        raise SystemExit("Exe verrouillé : quitte Underrail.")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    from datetime import datetime

    bak = BACKUP_DIR / f"underrail.exe.bak-journal-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    bak.write_bytes(bytes(data))
    print("backup", bak)
    n = 0
    for en, fr in REPLACEMENTS:
        hits = find_slots(data, en)
        if not hits:
            print("MISS ", en[:60])
            continue
        if len(hits) > 4:
            print("SKIP many", len(hits), en[:50])
            continue
        for h in hits:
            write_slot(data, h, en, fr)
            n += 1
            print("OK   ", fr[:50], "@", h)
    EXE.write_bytes(data)
    print("patched", n, "slots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
