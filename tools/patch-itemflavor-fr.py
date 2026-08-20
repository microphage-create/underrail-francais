#!/usr/bin/env python3
"""Patch hardcoded crafted-weapon flavor sentences in underrail.exe."""
from __future__ import annotations
from datetime import datetime
from pathlib import Path

EXE = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Underrail\underrail.exe")
BACKUP_DIR = Path(r"C:\Users\Marcel\Documents\Underrail-FR\backups")

REPLACEMENTS = [
    (
        " It sports a circular wave amplifier that periodically amplifies energy output.",
        " Un amplificateur d'onde circulaire booste périodiquement la sortie d'énergie.",
    ),
    (
        " It sports a module that runs targeting assistance software which increases efficiency of precision shots.",
        " Un module d'aide à la visée pour des tirs de précision plus efficaces.",
    ),
    (
        " It sports an airburst capable scope that both increases precision and times grenades to explode before surface impact.",
        " Une lunette airburst augmente la précision et fait exploser les grenades avant l'impact.",
    ),
    (
        " It sports a scope with a range finder that allows for increased precision.",
        " Une lunette à télémètre pour plus de précision.",
    ),
    (
        " It sports a simple grenade launcher iron sight.",
        " Un cran de mire simple de lance-grenades.",
    ),
    (
        " It sports an extended magazine which stores a total of {0} rounds.",
        " Un chargeur étendu de {0} cartouches.",
    ),
    (
        " It sports a combat-ready headlight.",
        " Un phare de combat.",
    ),
    (
        " It is equipped with bipod attachment, allowing for better, although slower, aiming.",
        " Un bipied : visée meilleure, mais plus lente.",
    ),
    (
        " It is equipped with ammo belt that can house {0} rounds.",
        " Une bande de munitions de {0} cartouches.",
    ),
    (
        " It is equipped with {0} capacity box magazine.",
        " Un chargeur boîte de {0} coups.",
    ),
    (
        " It has a long barrel for increased range.",
        " Un canon long pour plus de portée.",
    ),
    (
        " It also comes with a {0} shield for extra protection against melee attacks.",
        " Un bouclier {0} contre la mêlée.",
    ),
    (
        " It also comes with a shield for extra protection against melee attacks.",
        " Un bouclier en plus contre la mêlée.",
    ),
    (
        " It is equipped with a laser sight, allowing for easier aiming.",
        " Un viseur laser, visée plus simple.",
    ),
    (
        " It is equipped with an especially strong string.",
        " Une corde particulièrement solide.",
    ),
    (
        "Damage of special {0} attacks increased by {1}% (this does not affect unconditional special attacks)",
        "Dégâts des attaques spéciales {0} +{1}% (hors spéciales inconditionnelles)",
    ),
    (
        "Damage of special {0} attacks decreased by {1}% (this does not affect unconditional special attacks)",
        "Dégâts des attaques spéciales {0} -{1}% (hors spéciales inconditionnelles)",
    ),
    (
        "Restores {0} to {1} action points. Can only occur once per turn.",
        "Restaure {0} à {1} PA. Une fois par tour.",
    ),
    (
        "{0}% chance to restore {1} to {2} action points. Can only occur once per turn.",
        "{0}% de chance de restaurer {1} à {2} PA. Une fois par tour.",
    ),
    (
        " The electromagnetic rail catapult completely neutralizes any backblast.",
        " Le rail électromagnétique annule le backblast.",
    ),
    (
        "An electroshock weapon used to harm and stun the target.",
        "Arme électrochoc : blesse et étourdit la cible.",
    ),
    (
        " The installed energy converter reduces the energy usage per shot.",
        " Le convertisseur réduit l'énergie par tir.",
    ),
    (
        " The silencer will make sure almost no noise is emitted when fired, but at the cost of power.",
        " Le silencieux coupe presque tout le bruit, au prix de la puissance.",
    ),
    (
        " The silencer will make sure almost no noise is emitted when fired.",
        " Le silencieux coupe presque tout le bruit du tir.",
    ),
    (
        " The mounted pneumatic barrel retractor makes it more wieldy when used in close quarters combat.",
        " Le rétracteur pneumatique rend l'arme plus maniable au corps à corps.",
    ),
    (
        " A barrel compensator is mounted on the end of the barrel to counter the vertical movement during bursts.",
        " Un compensateur en bout de canon contre le relèvement en rafale.",
    ),
    (
        " A muzzle brake is mounted on the end of the barrel to take some of the kick out of the gun, allowing for longer bursts.",
        " Un frein de bouche absorbe une partie du recul, pour des rafales plus longues.",
    ),
    (
        "Instantly restores {0} health points.",
        "Restaure tout de suite {0} PV.",
    ),
    (
        " Choke has been added to the end of the barrel to reduce pellet spread at the price of power.",
        " Un choke en bout de canon réduit la dispersion, au prix de la puissance.",
    ),
    (
        " Magazine capacity is increased throgh tube extension.",
        " Capacité du chargeur augmentée par le tube.",
    ),
    ("This item cannot be disassembled", "Objet non démontable"),
    ("This item has deteriorated too much to recycle.", "Trop abîmé pour être recyclé."),
    ("Incompatible barrel type.", "Canon incompatible."),
    ("Incompatible magazine type.", "Chargeur incompatible."),
    ("Could not attach the silencer to the barrel.", "Impossible de monter le silencieux."),
    (" Costs {0} energy.", " Coût {0} énergie"),
    ("Strange Medallion", "Médaillon étrange"),
    ("Show all feats", "Tout afficher"),
    ("Filter:", "Filtre:"),
    ("[none]", "[rien]"),
    ("Remaining feats", "Feats restants"),
    ("a controlled zone", "zone contrôlée"),
    ("an uncontrolled zone", "zone non contrôlée"),
    ("a partially controlled zone", "zone sous contrôle partiel"),
    ("Quick Invoker", "Invoc. rapide"),
    ("End Combat", "Fin combat"),
    ("Begin Combat", "Début combat"),
    ("Reload Weapon", "Recharger"),
    ("Material", "Matériau"),
    ("Component", "Composant"),
    ("Enhancement", "Renfort"),
    ("Frame", "Cadre"),
    ("Barrel", "Canon"),
    ("Magazine", "Chargeur"),
    ("Handle", "Manche"),
    ("Fabric", "Tissu"),
    ("Leather", "Cuir"),
    ("Padding", "Rembour"),
    ("Filler", "Charge"),
    ("Overcoat", "Finition"),
    ("Soles", "Sole"),
    ("Metal", "Métal"),
    ("Primary Explosive", "Charge principale"),
    ("Secondary Explosive", "Charge secondaire"),
    ("Primary modulator", "Modul. principal"),
    ("Secondary modulator", "Modul. secondaire"),
    ("Primary Micro Discharger", "Micro-déch. principal"),
    ("Secondary Micro Discharger", "Micro-déch. secondaire"),
    ("Primary Electromagnetic Discharger", "Déch. EM principal"),
    ("Secondary Electromagnetic Discharger", "Déch. EM secondaire"),
    ("Any Bullet Case", "Toutes douilles"),
    ("Any Launcher Grenade Case", "Toute douille grenade"),
    ("Grenade Case", "Étui grenade"),
    ("Explosive", "Explosif"),
    ("Incendiary", "Incend."),
    ("Crafting", "Atelier"),
    ("Strength", "Force"),
    ("Dexterity", "Dextérité"),
    ("Agility", "Agilité"),
    ("Will", "Vol."),
    ("Stealth", "Furtif"),
    ("Health", "PV"),
    ("Shield", "Boucl."),
    ("Focused", "Focus"),
    ("Frozen", "Gelé"),
    ("Stunned", "Étourdi"),
    ("Burning", "En feu"),
    ("Chilled", "Transi"),
    ("Dazed", "Sonné"),
]


def find_slots(data: bytes, text: str) -> list[int]:
    needle = text.encode("utf-16le")
    hits = []
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
        raise ValueError(f"FR trop long {len(fr)}>{len(en)}")
    for k in range(len(en) * 2):
        buf[off + k] = 0
    raw = fr.encode("utf-16le")
    buf[off : off + len(raw)] = raw
    buf[off + len(raw)] = 0
    buf[off - 1] = len(fr) * 2 + 1


def main() -> int:
    for en, fr in REPLACEMENTS:
        if len(fr) > len(en):
            raise SystemExit(f"LEN FAIL {len(fr)}>{len(en)}\n{en}\n{fr}")
    try:
        data = bytearray(EXE.read_bytes())
    except PermissionError:
        raise SystemExit("Exe verrouillé : quitte Underrail.")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    bak = BACKUP_DIR / f"underrail.exe.bak-itemflavor-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    bak.write_bytes(bytes(data))
    print("backup", bak)
    n = 0
    for en, fr in REPLACEMENTS:
        hits = find_slots(data, en)
        if not hits:
            print("MISS", en[:60])
            continue
        if len(hits) > 4:
            print("SKIP many", len(hits), en[:40])
            continue
        for h in hits:
            write_slot(data, h, en, fr)
            n += 1
            print("OK", fr[:55], "@", h)
    EXE.write_bytes(data)
    print("patched", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
