# Status pack FR Underrail

## Knowledge — **DONE**
Tout le `knowledge/` (UI, skills, attributs, rules, feats, psi, quests, maps, items, status effects, enums, tooltips…)  
Sauf `items.txt` vide (comme l’EN).

## Dialogs — **DONE** (couverture) / **voix en second-pass**
**1042 / 1042** fichiers loc. Inventaire nickel : 0 `mt`.

Passe mécanique 2026-08-19 (pack-wide) : Acorn, checks `::[Skill]::` remis EN, tokens genre, CTA, hypos, hopper≠trémie.

Passe voix : SGS early, JKK/Ola/Vivian, oligarques Acorn, Azif, Junkyard hub, Arena, Institute core, Expedition, Foundry/Drones/Edgar, HD, Mordre.

Second-pass 2026-08-21 (gros fichiers encore MT en queue) : **Phreak/forger** (fini : plus de croustilles, tu stable, run≠chips), Dude, Kokoschka, Cathcart, Ethan, Briggs, Marcus, Eidein, Georgis, Rista, Stavros.

Reste : knowledge noms EN (skip), Steam-mod **périmé** vs `francais/`. Pas de sync Steam cette session.

## Qualité
- Noms skills/attributs/feats : **EN**
- Descriptions / dialogues : **FR** gaming
- Grep live 2026-08-19 : 0 maïs, 0 Bro, 0 `Persuader`/`Frappe`, 0 hypoglycémie
- Docs : `CONTEXT-UNDERRAIL.md`, `GLOSSAIRE.md`, `CHARTE-TRADUCTION.md`, `KNOWLEDGE-BASE/`
- Tuto install : `TUTO-INSTALLATION.md`

## Install Steam — **DONE** (2026-07-31)
```
C:\Program Files (x86)\Steam\steamapps\common\Underrail\data\localization\francais\
```
- knowledge: 59 fichiers
- dialogs: 1042 fichiers
- info.txt: Français (UTF-8)
- backup éventuel: `francais.backup-*`

### À faire de ton côté
1. Lancer Underrail  
2. **Options → Language → Français**  
3. Quitter et relancer le jeu  

## Limites moteur
Cutscenes non localisables ; hardcode EN possible ; add-key names à enrichir en jouant.
