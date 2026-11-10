"""Présentation de variantes : le bouton NEWMARKETPITCH.COM des couvertures (6 variantes x 4 couvertures)."""
import json, pathlib, yaml, shutil
ROOT = pathlib.Path(__file__).resolve().parent.parent
ED = yaml.safe_load((ROOT / 'decks/edtech/deck.yaml').read_text())['slides'][0]
covers = [('wearable_technology.jpg', 'Wearable\ntechnology'), ('nuclear_fusion.jpg', 'Nuclear\nfusion'), ('biotechnology.jpg', 'Biotechnology'), ('edtech.jpg', 'EdTech\nmarket')]
V = [('a', 'Actuel', 'cadre sable, sans fond'),
     ('b', 'Fond bleu marine seulement si la photo est chargée', 'détecté automatiquement sous le bouton ; sinon rien ne change'),
     ('c', 'Fond bleu marine plein, toujours', 'le bouton devient une étiquette pleine sur toutes les couvertures'),
     ('d', 'Fond flou + bleu marine léger, toujours', 'la photo se devine derrière, floutée'),
     ('e', 'Fond bleu marine semi-opaque, toujours', '80 % d’opacité, sur toutes les couvertures'),
     ('f', 'Bouton déplacé en bas à gauche', 'sous le titre, toujours sur la partie sombre ; la photo reste libre')]
d = ROOT / 'decks/atelier7'; (d / 'media').mkdir(parents=True, exist_ok=True)
for img, _ in covers:
    src = ROOT / 'decks/examples/media' / img
    shutil.copy(src if src.exists() else ROOT / 'decks/edtech/media/cover.jpg', d / 'media' / img)
slides, vs = [], []
for k, name, desc in V:
    ns = []
    for img, big in covers:
        slides.append(dict(type='cover', image=f'media/{img}', big=big, disclaimer=ED['disclaimer'], btn=k)); ns.append(len(slides))
    vs.append(dict(key=k, name=name, desc=desc, n=ns))
sec = dict(kind='variantes', id='B', title='Couverture : le bouton NEWMARKETPITCH.COM', short='Bouton', zoom='button', grid=2,
    what='6 traitements du bouton, chacun sur 4 couvertures. La détection automatique trouve une photo chargée sous le bouton pour Wearable, Nuclear fusion et EdTech (la tablette rose) ; Biotechnology est propre. Sous chaque variante, un zoom ×2 sur le coin du bouton.',
    mine='b', why='Le bouton ne change que là où il en a besoin : il devient lisible sur Wearable, Nuclear fusion et EdTech, et Biotechnology reste exactement comme avant. Pas de nouvel élément sur les couvertures qui n’en ont pas besoin.',
    variants=vs)
(d / 'deck.yaml').write_text(yaml.dump(dict(market='Workshop 7', label='EdTech market', quarter='judge', year=2026, slug='atelier7', chapters=[], slides=slides), allow_unicode=True, sort_keys=False, width=1000))
(d / 'manifest.json').write_text(json.dumps(dict(sections=[sec]), ensure_ascii=False, indent=1))
print(len(slides))
