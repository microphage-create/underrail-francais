# Contexte Underrail — base obligatoire avant toute traduction

Pack perso. Ce fichier **prime** sur l’instinct EN→FR générique.

## Ce que c’est
- CRPG **isométrique, tour par tour (ou temps réel selon mode)**, ultra punitif, craft / buildcrafting.
- Studio : **Stygian Software**. EN only officiel ; le jeu **expose un système de packs** (`data/localization/`) pour la communauté.
- DLC / couches de contenu visibles dans les clés : `xpbl` (Expedition / Black Sea), `xphw` (Heavy Duty), `full`, `_RT` (real-time variants des pouvoirs).
- Ton narratif : **post-apo souterrain, froid, cynique, bureaucratique et violent**. Pas d’héroïsme anime. Pas de blagues de traducteur.

## Monde (à ne pas inventer)
- **Underrail** : réseau de stations, tunnels, grottes sous la surface ; métro / stations verticales.
- **South Gate Station (SGS)** : hub de départ, compound vertical (niveaux 2–9 : armurerie, cantine, Tanner, logements, med/psi, ingénierie, biologie, caves/docks).
- Lieux fréquents dans les quêtes early : **Crossroad Caves**, **Mushroom Cove**, **GMS compound**, outposts nord, etc.
- Factions / orgs (ne pas renommer en “cool FR” sans raison) : conserver les **noms propres EN** (Tanner, Gorsky, Big Bret, Old Jonas, Abram, Core City, Free Drones, Protectorate, etc.) sauf si le jeu a déjà une forme établie — pour l’instant : **noms EN**.
- Créatures early : **cave hoppers**, eels, etc. → traduire **quand c’est un nom commun descriptif** ; garder la cohérence sur tout le pack (glossaire).

## Systèmes (vocabulaire de design)
| Concept | Sens in-game | FR cible |
|---|---|---|
| **Base abilities** | STR / DEX / AGI / CON / PER / WIL / INT | **Attributs** (pas “capacités de base” calqué) |
| **Skills** | Guns, Melee, Stealth, Hacking… | **Compétences** |
| **Feats** | Traits / techniques apprises | **Talents** |
| **Specialization** | Points post-feats | **Spécialisation** |
| **Psi** | Disciplines mentales (cryo, pyro, télékinésie…) | **Psi** (invariable) |
| **Innervate** | Brancher un pouvoir psi sur un “circuit” pour l’utiliser | **Innerver** (terme de jeu, assumé) |
| **Psionic circuit** | Slot de pouvoir | **Circuit psionique** |
| **Oddity** | Mode d’XP : étudier des objets “curiosité” | **Curiosité** + verbes “étudier” |
| **Classic XP** | XP classique | **Classique** |
| **AP / MP** | Action / Movement points | **PA / PM** |
| **Cooldown** | Recharge d’abilité | **Recharge** (UI courte) |
| **Stealth** | Mode furtif + skill | **Furtivité** |
| **Armor suit** | Armure corps entier (slot) | **Armure** (pas “combinaison d’armure”) |
| **Energy shield / emitter** | Bouclier énergétique équipable | **Bouclier énergétique / émetteur** |
| **Shielding** | Qualité de protection du bouclier | **Protection** (pas “blindage” tank) |
| **Fortitude** | Save physique (stun, etc.) | **Vigueur** |
| **Resolve** | Save mental / psi | **Sang-froid** (ou **Résolution** si UI trop long — garder **un** choix pack-wide) |
| **DOMINATING** | Difficulté extrême “vétérans” | **DOMINATING** (marque) |
| **Snipe / Aimed Shot / Dirty Kick…** | Noms de feats/attaques | Traduire le **sens** + garder reconnaissance ; cohérence feats ↔ tooltips |
| **Biological / living targets** | Cibles organiques vs robots | **Cibles biologiques / vivantes** vs machines |
| **Expedition / Heavy Duty** | Thèmes menu / DLC | **Expedition** / **Heavy Duty** (titres) |

## Dialogues (quand on y touche)
- Clés `q*` = PNJ / système ; `a*` = répliques joueur.
- Ne **jamais** modifier `*_original`.
- Garder balises `::wheeze::`, `::He coughs.::`, etc. — ce sont des **didascalies**, pas du texte à fusionner n’importe comment.
- Voix : un soldat SGS ≠ un dealer Core City ≠ un Tchortist ≠ un pirate. Le FR change de **registre**, pas seulement de langue. Table dans `CHARTE-TRADUCTION.md`.
- Institute of Tchort : *brother/sister* / `bro/sis` = **frère / sœur** (ordre), jamais *Bro*.
- Tutoiement/vouvoiement : **par personnage**. UI = vouvoiement sec ou nominal.

## Format fichiers (contraintes moteur)
- `knowledge/*.txt` : `::Key` puis valeur ; certaines clés s’**ajoutent** (itemnames, featnames, entitynames…), d’autres se **traduisent en place** seulement (readme officiel).
- Dialogues : traduire `q` / `a`, laisser `_original`.
- Placeholders `{0}` `{1}` : même **nombre** ; ordre stable sauf reformulation testée.
- Variantes `*-RT`, `*_xpbl`, `*_xphw` : **traduire chaque variante**, ce ne sont pas des doublons gratuits (modes / DLC).

## Processus “bien contextualisé” (obligatoire)
Pour **chaque** fichier ou lot :
1. Lire le **readme** + le type de fichier (add keys vs in-place).
2. Lire **5–10 clés voisines** et, si dialogue, le **fichier entier** du PNJ.
3. Croiser glossaire (`GLOSSAIRE.md`) : un terme = une forme partout.
4. Relire le FR **sans** l’EN : si ça sent le patch, réécrire.
5. Ne jamais “embellir” le lore (pas d’humour ajouté, pas de modernité Discord).

## Hors scope moteur (ne pas promettre)
- Cutscenes non localisables (readme).
- Texte hardcodé EN encore injecté parfois.
- `data/locale/*` = assets graphiques, **pas** de trad.

## État pack
- Racine travail : `Documents\Underrail-FR\`
- Pack jeu : `francais\` (à copier dans `Underrail\data\localization\`)
- UI : `knowledge\ui.txt` réécrit (anti-calque) — **à valider en jeu**
