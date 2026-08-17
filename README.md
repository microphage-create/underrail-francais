# Underrail — pack français (v2)

Localisation française **communautaire** pour [Underrail](https://store.steampowered.com/app/250520/Underrail/) (base + Expedition + Heavy Duty).

Le jeu est © Stygian Software. Ce dépôt ne contient **que** le pack `data/localization/` prévu par le studio. Pas d’exe, pas de maps, pas d’assets.

## État

**v2 = reprise voix par voix.** Le v1 était une couverture MT (tout le jeu en FR, qualité machine). Ici chaque fichier est revu à la charte avant d’être marqué `nickel`.

Le pack reste **jouable** à tout moment : les fichiers pas encore repris sont du FR de couverture, pas de l’anglais.

Voir `STATUS.md`.

## Installer

1. Underrail installé (Steam).
2. PowerShell :

```powershell
cd $env:USERPROFILE\Documents\Underrail-FR-v2
.\INSTALL-PACK.ps1
```

3. Jeu **fermé**. Puis **Options → Language → Français**. Quitter le process. Relancer.

Copie manuelle : coller le dossier `francais\` dans  
`Steam\steamapps\common\Underrail\data\localization\`

## Règles (lire avant de toucher une ligne)

- `CHARTE-TRADUCTION.md` — voix par faction, tokens genre, barre nickel
- `GLOSSAIRE.md` — un terme = une forme
- Skills / feats / attributs / checks `::[Persuasion]::` : **EN**
- Ne **jamais** éditer `*_original`
- Placeholders `{0}` et `$(…)` intacts

## Contribuer

Voir `CONTRIBUTING.md`. Un fichier à la fois. Pas de dump MT.

## Licence

- Texte et univers du jeu : © Stygian Software
- Traduction FR de ce dépôt : voir `LICENSE.md`
