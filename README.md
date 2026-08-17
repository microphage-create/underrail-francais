# Underrail community localizations

Unofficial **language packs** for [Underrail](https://store.steampowered.com/app/250520/Underrail/) (base game + Expedition + Heavy Duty).

The game is © Stygian Software. This repo only holds `data/localization/` packs — the format the studio already supports. No exe, no maps, no art.

**Any language can live here.** French is the first pack. German, Spanish, Polish, etc. are the same shape: one folder, one `info.txt`, drop it into Steam.

---

## Packs

| Folder | Menu name | Status |
|---|---|---|
| [`packs/francais/`](packs/francais/) | Français | Playable coverage. Voice pass in progress (`STATUS.md`) |

Want another language? → [`docs/ADDING-A-LANGUAGE.md`](docs/ADDING-A-LANGUAGE.md)

---

## Install (any pack)

Game **closed**. PowerShell (admin if Windows blocks Program Files):

```powershell
cd path\to\underrail-francais
.\INSTALL-PACK.ps1 -Pack francais
# .\INSTALL-PACK.ps1 -Pack deutsch
```

Or copy `packs/<id>\` into:

`Steam\steamapps\common\Underrail\data\localization\`

Then **Options → Language → (your pack name)**. Quit the process. Relaunch.

---

## Rules that apply to every language

- Never edit `*_original` (English reference).
- Keep `{0}` `{1}` and `$(…)` placeholders.
- Dialog player/NPC keys are `q*` / `a*`.
- Line endings: CRLF (`\r\n`). Never `\r\r\n` (the engine falls back to English).
- Gender tokens `$(#he/she)` display **literally**. Translate both sides for *your* language.

French-specific voice/glossary: `CHARTE-TRADUCTION.md`, `GLOSSAIRE.md`.  
Other languages: write your own `packs/<id>/CHARTE.md` if you need it.

---

## Contribute

See `CONTRIBUTING.md`. One file per PR. No machine-dump of the whole game.

## License

- Game text and setting: © Stygian Software
- Translations in this repo: `LICENSE.md` (CC BY-NC-SA 4.0)
