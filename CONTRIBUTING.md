# Contribute

## New language
Read [`docs/ADDING-A-LANGUAGE.md`](docs/ADDING-A-LANGUAGE.md).  
`python tools/new-pack.py --id deutsch --name "Deutsch"` then translate live keys.

## Existing pack (e.g. French)
One file per PR. Read `CHARTE-TRADUCTION.md` + `GLOSSAIRE.md` for French.

## Every PR
- [ ] `*_original` untouched
- [ ] `{0}` / `$(context…)` / `$(#a/b)` intact (both sides of `#` in **your** language)
- [ ] Dialog checks: keep `::[Persuasion]::` unless your pack documents otherwise
- [ ] CRLF line endings, never `\r\r\n`
- [ ] No whole-game machine dump

## French voice (this pack only)
Tchort: frère / sœur, not Bro.  
Ola / street: gars / sœurette.  
Oldfield: warm professor, vous.
