"""Pierre's decisions on atelier 100 (10 Nov 2026, 23h). id: (variant, extra js run after it, extra css, scope override)
Built into decks/<slug>/decisions.js by make_decisions.py; run at build after rawfit."""
D = {
 3:  ('B', "A.toCorner(sl)", '', [18, 19, 20]),
 14: ('A', "A.centerCards(sl)", '', None),
 15: ('C', '', '', None),
 17: ('A', r"const g=[...sl.querySelectorAll('.raw > div:not(.rx-t)')].pop();const tx=A.texts(sl).filter(t=>t.x>500&&t.text.length>60);if(g&&tx.length){const y0=Math.min(...tx.map(t=>t.y)),y1=Math.max(...tx.map(t=>t.y+t.h));const gh=parseFloat(g.style.height);g.style.top=((y0+y1)/2-gh/2)+'px'}", '', None),
 20: ('A', '', "S .agenda .it.off{opacity:.4}", None),
 30: ('B', '', '', None),
 34: ('A', '', '', None),
 39: ('C', '', '', None),
 43: ('C', r"A.texts(sl).filter(t=>/^[A-Z][A-Z0-9 ]+$/.test(t.text)&&t.h<34).forEach(t=>t.el.querySelectorAll('span').forEach(s=>s.style.fontWeight='700'))", '', None),
 44: ('B', "A.toCorner(sl)", '', None),
 45: ('B', "A.toCorner(sl)", '', None),
 46: ('B', "A.toCorner(sl)", '', None),
 47: ('B', "A.toCorner(sl)", '', None),
 48: ('B', '', '', None),
 52: ('A', '', '', None),
 54: ('C', '', '', None),
 57: ('C', '', '', None),
 61: ('B', '', '', None),
 63: ('B', '', '', None),
 65: ('B', '', '', None),
 69: ('C', '', '', None),
 70: ('C', '', '', [105]),
 72: ('B', '', '', None),
 76: ('B', '', '', None),
 84: ('C', '', '', None),
 85: ('A', '', "S .defbox .ico{box-shadow:0 1px 3px rgba(0,0,0,.22)}", None),
 86: ('A', '', '', None),
 89: ('A', '', '', None),
 91: ('C', '', '', None),
 92: ('C', '', '', None),
 95: ('C', '', '', None),
 96: ('A', '', '', None),
 97: ('B', '', '', None),
 99: ('A', '', '', None),
}
# 2nd round (10 Nov 23h50): card grids with emojis -> pastilles; numbered grids = A (flow), plain grids = B (top edge, rows spaced)
CARDS = [22, 31, 136, 142, 172, 186, 207]
# variants from other atelier rounds: (module, item id, variant key, slides)
EXTRA = [('items5', 'Q', 'ZB', [13]), ('items7', 'B', 'B', [97])]   # prix : quadrillage de fond (11 Nov 00h08)
# item 47: smaller trophies
SIZE = {47: ("size:14", "size:11")}
