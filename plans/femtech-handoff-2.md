# FemTech deck : passation n° 2 (26 nov 2026, 16 h)

Cette conversation n'avait pas le droit de pousser sur nmp-decks : tout est dans le patch
`femtech-2026-11-26.patch`, à appliquer sur `main` de nmp-decks.
nmp-logos est DÉJÀ poussé (commits 6819b2c et suivant : 24 logos de startups femtech, domaine de Flo Health corrigé).
Avant d'appliquer : `git -C ../nmp-logos pull`, puis `git am femtech-2026-11-26.patch` (ou `git apply --3way`), puis
`python3 ../nmp-logos/tools/decks_sync.py` (et remettre avec `git checkout` les fichiers des AUTRES decks que le sync réécrit),
puis `tools/rebuild.sh femtech --png`.

## Fait (étapes 1 à 8 de la première note)
- Le build est à « 200 slides, 0 issues » et « 0 layout issues », sans avertissement en capitales.
- Libellé du pied de page : « FemTech market » (ligne 17 de market_labels.txt).
- Dans les textes, « femtech » est écrit en minuscules en milieu de phrase, comme sur la page en ligne. L'import utilise `--name "femtech"`.
- Radar S01 : Progyny sort du coin bas gauche et est remplacé par Calm. Progyny finance la fertilité, il est donc DANS la définition, et il est cité sur 13 slides. Le texte OCR des coins a été corrigé.
  → La slide S01 en ligne doit être remplacée.
- ed047p (donut S03-02), sur les 6 segments :
  - fertilité 35, grossesse 22, hormonal 18, midlife 12, pelvien 7, cancers 6 ;
  - les « 13 % other women's care » de la page en ligne sont répartis selon l'argent levé depuis 2024, ce que dit la note.
  - → La slide S03-02 en ligne doit être remplacée.
- ed048 est sur 6 cartes (1/2), plus ed048-2 dans extras.yaml.
- ed039p (Trends) : coupure au 2025-07-27, titre « more than doubled ». La slide affiche ×2.5 : c'est le rapport du pic à une semaine typique.
  → Image S02 à remplacer.
- ed052p : taille de 10 milliards de dollars et CAGR de 15 % (c'était 14 %), pour suivre ed051. Dans la note, Mordor remplace Precedence.
  → Image S03-01 à remplacer.
- ed171p (S10) : les libellés de lignes passent au-dessus des lignes (`rows_above`, nouvelle option de `pp_grid.j2` et de `css/nmp.css`). Le libellé « Software self-management » sortait de la slide.
- ed099p (S05) : « Nat. Cycles » devient « Natural Cycles ».
  → L'image en ligne garde l'abréviation, à remplacer aussi.
- Slides base faites (`make_db_slides`), ainsi que S09 ed168p (`s09_from_base`, au 2026-11-26).
  - La base va jusqu'au 19/11.
  - db_text ed162 réécrit : « midlife care has gained share since 2025 ». Vérifié dans la base : 10 % de l'argent en 2024, 19 % en 2025 et 2026.
  - → Image S09 à remplacer.
- Slide `xs_survivors` placée après ed199p : FemTec Health, Kindbody, Elvie, Apricity Fertility, Premom.
- Sources :
  - `sources_key.yaml` contient 20 lignes ;
  - les éditeurs femtech sont ajoutés au PUB de `build_sources.py` ;
  - `build_sources.py` a tourné : 142 sources, 5 slides.
- Liens des extras : `pp_s06` a son `link`, sur la note de ed104, réécrite pour amener la slide.
- Couverture : titre en 66 pt au lieu de 80, disclaimer large de 470 px. Sinon, les deux mordaient sur le téléphone (COVER_TEXT_ON_SUBJECT).
- Passe visuelle des 200 slides faite, sur des planches de 6. Corrections faites :
  - contrastes ed211, ed213 et ed214 (FILL) ;
  - titre ed211, qui disait « $1.7B business » pour une valorisation ;
  - Allara : 30 M$ en octobre 2026 (la base a les deux tours, 26 M$ en 2025 et 30 M$ en 2026) ;
  - « VIDEO VISITS » ;
  - mots coupés de ed059 ;
  - « PATCHY ACCESS » ;
  - « WOMEN AGED OVER 40 » ;
  - ed174 ;
  - carte ed049 ;
  - graphique ed190 : la boîte de texte est déplacée, le point de Kindbody était caché dessous.
- RULES.md : nouvelle section « FemTech first build (26 Nov 2026) ».

## Reste à faire, dans l'ordre
1. `tools/diff_slides.py femtech --snap` après le build `--png`.
2. Étape 5 : les slides complémentaires (SIGNAL d'abord) sur UNE page de revue. Pierre valide.
   - ed032 liste déjà 7 signaux : Progyny Q3, Pomelo, Hologic, Midi, Evvy, Alife, Teal.
   - Candidats dans 11 signals : Ferring-Gameto, labels de l'hormonothérapie, Flo 80 M d'utilisateurs, Maven 475 plans.
3. Étape 6 : page de revue du deck entier. Étape 7 : PDF « FemTech - Q4 2026 - newmarketpitch.com ©.pdf ».
4. Images de la page produit à remplacer :
   - liste : S01 (radar), S02 (Trends), S03-01 (taille et CAGR), S03-02 (donut), S05 (Natural Cycles), S09, et S10 si on veut les libellés au-dessus ;
   - outils : `tools/pp/export_twins.py`, puis alpha_guard, stagedUpload et fileUpdate ;
   - mettre à jour `?v` dans `custom.v1_sections` et dans `custom.encarts`, puis le manifest et le journal.

## Points à trancher ou à signaler
- Logos de FemTec Health et d'Apricity Fertility : faits à partir des captures de Pierre (patch 2), poussés sur nmp-logos.
- ed010 « smaller markets » : 5 cases pour 6 segments, Pelvic health absent. Pierre a validé (26/11).
- Sur la carte ed183, le trait de l'Australie finit dans le texte. Problème connu, ajouté à RULES.md, à corriger dans le gabarit de la carte.
- S04 en ligne (ed058) : il garde la colonne « Health plans ». Les segments de douleur ont « Women in midlife ». La slide n'est pas contradictoire, donc la jumelle copie la slide en ligne.
- Bizarreries de la première note, réglées :
  - Allara : deux tours réels ;
  - Flo et Google Health : communiqué du 12/10/2026, la donnée est sourcée ;
  - KFF 27 % contre Mercer 54 % : les deux enquêtes portent sur des populations d'employeurs différentes, chaque slide le dit.
