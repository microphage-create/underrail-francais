# Add a language

Underrail loads **every folder** under `data/localization/` that contains `info.txt`. The first line of that file is the name in the Options menu.

## 1. Create the pack

From the repo root:

```powershell
python tools/new-pack.py --id deutsch --name "Deutsch"
```

This copies the French pack’s **file tree**, sets every live dialog line to the English `*_original`, writes `info.txt`, and leaves knowledge files for you to fill.

`--id` = folder name (ascii, no spaces): `deutsch`, `espanol`, `polski`, `portugues`, `italiano`…

`--name` = what players see: `Deutsch`, `Español`, `Polski`…

## 2. Translate

| Kind | How |
|---|---|
| Dialogs | Change the **live** key (`=>q12`, `=>a3`). Leave `=>q12_original` alone. |
| Knowledge (in-place) | Translate the text under `::Key`. Do not rename the key. |
| Knowledge (add-keys) | `itemnames`, `entitynames`, `featnames`, `abilitynames`… add `::EnglishName` then your line. |

Official file list: the game’s `data/localization/readme.txt`.

## 3. Gender and tone

`$(#he/she)` prints the side the player picked.  
English `he/she` on screen is a bug. Example:

| EN | FR | DE |
|---|---|---|
| `$(#he/she)` | `$(#il/elle)` | `$(#er/sie)` |
| `$(#bro/sis)` | depends on speaker (see French charte) | your call |

A Tchortist is not a pirate. Match the character, not a single slang.

## 4. Install and test

```powershell
.\INSTALL-PACK.ps1 -Pack deutsch
```

Quit Underrail completely. Language menu → your name. Relaunch.

If you still see English on a dialog, check that file for `\r\r\n` (broken line endings).

## 5. Open a PR

- Branch: `pack/<id>`
- Do not commit Steam backups
- First PR can be `info.txt` + 1–2 NPCs. Do not dump an unreviewed MT of 1000 files.

## Optional: start from the official template

Instead of `new-pack.py`, copy the game’s `data/localization/template\` into `packs/<id>\` and rename `info.txt`. Same result, empty English live keys from Stygian.
