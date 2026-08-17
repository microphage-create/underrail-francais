# Charte de traduction — Underrail (FR, usage personnel)

**Lire d’abord** : `CONTEXT-UNDERRAIL.md` + `GLOSSAIRE.md`.  
Sans ça = traduction hors-sol, même “jolie”.

## Noms de base = **ANGLAIS** (non négociable)
Skills, attributs, écoles psi, noms de feats/abilities/status, checks `::[Skill]::` → **toujours EN**.  
Sinon le glossaire, les guides et le matching moteur deviennent un enfer.  
On traduit les **phrases** (descriptions, dialogues, aide), pas les **labels canoniques**.

## Anti-calque (priorité absolue)
On ne traduit **pas** mot à mot. On écrit ce qu’un joueur FR attend dans un CRPG.

| Interdit (calque) | Préférer |
|---|---|
| « Chances de coup critique » sur un label court | « Taux de critique » / « Crit. » |
| « Temps de recharge restant » | « Recharge restante » |
| « Voulez-vous vraiment… » | « Supprimer ? » / « Écraser ? » |
| « Consultez les… de votre personnage » | Forme nominale courte : « Attributs, compétences et talents. » |
| « Arme de poing » pour *fist weapon* | « Arme de poings » (gants/poings) |
| « Combinaison d’armure » | « Armure » |
| « Hors intrigue » | « Divers » / « Quête » selon filtre |
| « Provocation de combat » | « Répliques de combat » |
| « effectuez une innervation pour le rendre invocable » | « innervez-le pour pouvoir l’utiliser » |
| Anglais syntaxique (« Allows to displaying ») | Phrase FR correcte, pas le calque de la faute EN |

**Test** : relire la chaîne **sans** l’anglais. Si ça sonne traduit, réécrire.

## Registre = **voix par lieu / PNJ** (pas un FR unique)

Le HUD reste **gaming FR** (PA, PM, crit, CD). Les **dialogues** ne sont pas du HUD. Un Tchortist qui dit *Bro* = fail, même si le token EN est `bro/sis`.

Barre vault (L10N / MSG056) : phrases courtes en UI, pas d’argot EN calqué, *ça* ambigu à éviter. Collision : on **garde** PA/PM/crit (HUD). On **n’aplatit pas** l’argot d’un pirate en descriptif plat.

**Test voix** : relire le FR **sans** l’EN, à voix haute, dans la bouche du PNJ. Si Rista (Institute) sonne comme Ola (JKK), réécrire.

| Hub / faction | Voix | Adresse au joueur | Interdit |
|---|---|---|---|
| **Institute of Tchort** | Culte + labo. Solennel, vouvoiement, formules (*Tchort est l’évolution*). *Brother/sister* = **frère / sœur** (ordre), jamais *Bro*. | `$(#frère/sœur)` `$(#Frère/Sœur)` | Bro, mec, gars, slang Discord |
| **SGS** | Militaire-bureaucrate, sec. Tanner = froid. Gorsky = soldat. | Vous / grade | Potache, *Bro* |
| **Junkyard / Hathor** | Sale, oral, parfois tutoiement | gars / fille, vous selon âge | Académique |
| **Core City street / JKK (Ola)** | Relâché, vendeur. EN *bro* = **gars / sœurette** ou **mec / nana**, pas frère religieux | `$(#gars/sœurette)` selon phrase | *frère* Tchort, Bro EN à l’écran |
| **Oligarques / Arena / Protectorate** | Formel, vous, titres | monsieur / madame | Tutoiement pote |
| **Free Drones** | Militant, direct | vous / camarade selon PNJ | Langue de bois Tchort |
| **Pirates (Grim Jetters)** | Argot marin FR, pas *yer/Imma* EN | gars / fille | Calque pirate US |
| **Aegis / Briggs** | Officier, vous, sec | monsieur | Southerner potache sauf CTA joueur Sudiste |
| **Ethan** | Dandy, un peu précieux | vous (sauf drague) | MT *Avant que tu ne sois vieux* |

UI : **nominal / impératif court**. Confirmations *Écraser ?* / *Supprimer ?*.  
**Interdit partout** : *skill check* en plein FR ; Bro/Sis/man/woman **laissés en EN** dans un token live.

## Tokens genre : la branche s’affiche **telle quelle**

Le moteur lit `$(#avant/après)` au pied de la lettre. Le mot FR doit coller au **registre du locuteur**, pas à un mapping unique.

| EN (source) | Défaut | Tchort / culte | Street / Ola / pirate |
|---|---|---|---|
| `$(#he/she)` | `$(#il/elle)` | idem | idem |
| `$(#him/her)` | `$(#le/la)` ou `$(#lui/elle)` | idem | idem |
| `$(#his/her)` | `$(#son/sa)` | idem | idem |
| `$(#fellow/girl)` `$(#guy/girl)` | `$(#gars/fille)` | `$(#frère/sœur)` si adresse | `$(#gars/fille)` |
| `$(#bro/sis)` `$(#Bro/Sis)` | **selon PNJ** | **`$(#frère/sœur)`** | **`$(#gars/sœurette)`** ou *mec/nana* |
| `$(#man/woman)` (adresse) | selon phrase | frère/sœur ou homme/femme | gars/fille |
| `$(#man/woman)` (un/une X) | `$(#homme/femme)` | idem | idem |
| `$(#sir/ma'am)` | `$(#monsieur/madame)` | idem | rare |
| `$(#'im/'er)` | **reformuler** (pas de token moche) | — | — |

Reformuler si le token casse l’élision. Ne **jamais** laisser l’EN dans le live.

## Termes figés (glossaire v1)
| EN | FR | Notes |
|---|---|---|
| Psi | Psi | Invariable |
| Innervate | Innerver | Terme de jeu, assumé |
| Feat | Talent | Pas « don » |
| Oddity | Curiosité | Mode XP |
| AP / MP | PA / PM | |
| Stealth | Furtivité | |
| Shielding | Protection | Boucliers énergie (pas « blindage » militaire) |
| Blueprint | Plan | |
| Crafting | Artisanat | |
| DOMINATING | DOMINATING | Nom de difficulté |
| Critical chance | Taux de critique | Pas « chances de » en UI |
| Cooldown | Recharge | |
| Fist weapon | Arme de poings | ≠ pistolet |
| SMG | Mitraillette | Pas « PM » ambigu avec points de mouvement |

## Règles techniques
- Ne pas toucher les clés `::Key` ni les `*_original`.
- Garder `{0}` `{1}` `{2}` (même nombre).
- Garder balises dialogue `::wheeze::` etc.
- Labels courts = scannables ; phrases longues seulement pour tooltips / aides.

## Barre « ultra nickel »
1. Relire **sans** l’EN. Si ça sonne patch → réécrire.
2. Relire **dans la voix** du PNJ (table ci-dessus).
3. Tokens live : zéro EN affiché (`Bro`, `man`, `'im`).
4. Placeholders `{0}` / `$(context…)` intacts (pas d’espaces cassés).
5. Checks `::[Persuasion]::` **EN**.
6. Item de quête : jamais *Acorn* → *maïs*.

## CTA dialogues (choix joueur)
Forme **infinitif** courte : `Continuer`, `Passer l'intro`, `Accepter`, `Refuser`.  
Pas d’impératif poli long ni de point inutile sur un bouton d’une ligne.

## Priorité des lots
1. **UI** (`knowledge/ui.txt`) — fait (phase 1)
2. Skills / feats / base abilities / rules / enums
3. Item names / entity names / ability names
4. Quests + messages
5. Dialogues personnages (par hub)

## Légalité
Pack **personnel uniquement**. Ne pas redistribuer le pack FR ni le dump EN du jeu.
