"""Prix (slide 13) : 30 variations de gradation, propres et ordonnées (Pierre, 10 Nov 23h56)."""
H = r"""A.texts(sl).filter(t=>/💰/.test(t.text)).forEach(t=>t.el.style.visibility='hidden');
const cs=A.shapes(sl).filter(s=>s.dash&&s.w>150).sort((a,b)=>a.x-b.x);
cs.forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#2A4A58');s.p.setAttribute('stroke-width','1')});
const ar=A.shapes(sl).find(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w>600);
const tb=A.texts(sl).filter(t=>/^\$/.test(t.text)).sort((a,b)=>a.x-b.x);
const hd=tb.map(t=>t.el.querySelector('p span'));
const PK='#FB0161',SL='#33525F',MID='#9A2F5E',CR='#E7CDA8';
const G=[SL,MID,PK],LV=['ENTRY','MID-RANGE','PREMIUM'];
const mk=(x,y,w,h,css,inner)=>A.div(sl,x,y,w,h,css,inner||'');
const under=(d)=>{const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);return d};
const grad='linear-gradient(90deg,#33525F,#9A2F5E 55%,#FB0161)';
const hideAr=()=>{if(ar)ar.el.style.visibility='hidden'};
"""
V = []
def v(name, desc, js): V.append(dict(name=name, desc=desc, js=H + js, css=''))
v("Barre d'accent qui s'allonge", "Une barre rose de 4 px en haut de chaque carte : un tiers, deux tiers, toute la largeur.",
  "cs.forEach((s,i)=>mk(s.x+14,s.y,(s.w-28)*(i+1)/3,4,'background:#FB0161;border-radius:0 0 3px 3px'))")
v("Barre d'accent qui s'intensifie", "Même barre pleine largeur en haut de chaque carte, du gris ardoise au rose.",
  "cs.forEach((s,i)=>mk(s.x+14,s.y,s.w-28,4,`background:${G[i]};border-radius:0 0 3px 3px`))")
v("Prix qui grossit", "Seule la typographie change : le prix grandit et s'éclaircit d'une carte à l'autre (12, 15, 18 pt).",
  "hd.forEach((h,i)=>{h.style.fontSize=(12+i*3)+'pt';h.style.color=['#C9D4D8',CR,'#fff'][i]})")
v("Flèche en dégradé", "La flèche du haut passe du gris ardoise au rose : la gradation est portée par un seul élément.",
  "if(ar){hideAr();mk(ar.x,ar.cy-4,ar.w-14,8,`background:${grad};border-radius:4px`);mk(ar.x+ar.w-16,ar.cy-10,0,0,'border-left:16px solid #FB0161;border-top:10px solid transparent;border-bottom:10px solid transparent')}")
v("Flèche en dégradé + repères", "Flèche en dégradé, avec un repère rond au-dessus de chaque carte dans la couleur de la flèche à cet endroit.",
  "if(ar){hideAr();mk(ar.x,ar.cy-3,ar.w-14,6,`background:${grad};border-radius:3px`);mk(ar.x+ar.w-14,ar.cy-8,0,0,'border-left:14px solid #FB0161;border-top:8px solid transparent;border-bottom:8px solid transparent');cs.forEach((s,i)=>mk(s.cx-7,ar.cy-7,14,14,`border-radius:50%;background:${G[i]};box-shadow:0 0 0 4px #062A3C`))}")
v("Bord gauche coloré", "Un trait de 3 px sur le bord gauche de chaque carte : ardoise, framboise, rose.",
  "cs.forEach((s,i)=>mk(s.x,s.y+14,3,s.h-28,`background:${G[i]};border-radius:2px`))")
v("Socle coloré", "Une barre pleine de 4 px en bas de chaque carte, du gris au rose.",
  "cs.forEach((s,i)=>mk(s.x+14,s.y+s.h-4,s.w-28,4,`background:${G[i]};border-radius:3px 3px 0 0`))")
v("Teinte très légère", "Le fond des cartes se teinte à peine de rose : 0 %, 6 %, 12 %.",
  "cs.forEach((s,i)=>s.p.setAttribute('fill',['#082F43','#1A2D46','#2B2A48'][i]))")
v("Prix en couleur", "Le prix passe du crème au rose clair puis au rose, en gras ; le reste ne bouge pas.",
  "hd.forEach((h,i)=>{h.style.color=[CR,'#FF8FB5',PK][i];h.style.fontWeight='700'})")
v("Jauge sous le prix", "Sous chaque prix, trois petits segments alignés : 1, 2 ou 3 remplis en rose.",
  "tb.forEach((t,i)=>{const p=t.el.querySelector('p');p.insertAdjacentHTML('afterend',`<div style='display:flex;justify-content:center;gap:4px;margin:4px 0 2px'>${[0,1,2].map(j=>`<i style='width:16px;height:4px;border-radius:2px;background:${j<=i?PK:'#1E4558'}'></i>`).join('')}</div>`)})")
v("Libellé de gamme", "Un petit libellé crème espacé sous le prix (ENTRY, MID-RANGE, PREMIUM), souligné d'un trait rose qui s'allonge.",
  "tb.forEach((t,i)=>{const p=t.el.querySelector('p');p.insertAdjacentHTML('afterend',`<div style='text-align:center;font:600 6.5pt Lexend;letter-spacing:.2em;color:#E7CDA8;margin-top:2px'>${LV[i]}<div style='margin:4px auto 0;height:3px;border-radius:2px;background:#FB0161;width:${14+i*14}px'></div></div>`)})")
v("Bordure qui se colore", "Le contour des cartes passe de l'ardoise au rose : même trait, couleur qui monte.",
  "cs.forEach((s,i)=>{s.p.setAttribute('stroke',G[i]);s.p.setAttribute('stroke-width','1.5')})")
v("Bandeau d'en-tête sombre → rose foncé", "Le prix est dans un bandeau en haut de chaque carte ; le bandeau passe de l'ardoise au framboise foncé.",
  "cs.forEach((s,i)=>under(mk(s.x+1,s.y+1,s.w-2,34,`background:${['#1E4558','#4A2A50','#7A2450'][i]};border-radius:13px 13px 0 0`)));hd.forEach(h=>h.style.color='#fff')")
v("Bandeau continu en dégradé", "Un seul dégradé traverse les trois en-têtes de cartes, de l'ardoise au rose : la gradation se lit d'un bloc.",
  "const x0=cs[0].x,x1=cs[2].x+cs[2].w;cs.forEach(s=>{const d=under(mk(s.x+1,s.y+1,s.w-2,34,`background:${grad};background-size:${x1-x0}px 100%;background-position:${x0-s.x}px 0;border-radius:13px 13px 0 0;opacity:.9`))});hd.forEach(h=>h.style.color='#fff')")
v("Halo intérieur", "Chaque carte a un léger halo rose en haut, de plus en plus marqué.",
  "cs.forEach((s,i)=>under(mk(s.x+1,s.y+1,s.w-2,s.h-2,`border-radius:13px;background:linear-gradient(180deg,rgba(251,1,97,${[0,.10,.2][i]}),rgba(251,1,97,0) 60%)`)))")
v("Rail en trois segments", "La flèche devient trois segments arrondis alignés sur les cartes : ardoise, framboise, rose.",
  "if(ar){hideAr();cs.forEach((s,i)=>mk(s.x,ar.cy-4,s.w,8,`background:${G[i]};border-radius:4px`))}")
v("Trois chevrons", "La flèche devient trois chevrons pleins, un par carte, du gris au rose.",
  "if(ar){hideAr();cs.forEach((s,i)=>mk(s.x,ar.cy-11,s.w,22,`background:${G[i]};clip-path:polygon(0 0,calc(100% - 12px) 0,100% 50%,calc(100% - 12px) 100%,0 100%,12px 50%)`))}")
v("Barre de progression en bas", "En bas de chaque carte, une barre fine ardoise remplie de rose : 33 %, 66 %, 100 %.",
  "cs.forEach((s,i)=>{mk(s.x+20,s.y+s.h-16,s.w-40,5,'background:#1E4558;border-radius:3px');mk(s.x+20,s.y+s.h-16,(s.w-40)*(i+1)/3,5,'background:#FB0161;border-radius:3px')})")
v("Anneau de niveau", "Un petit anneau dans le coin haut droit de chaque carte, rempli au tiers, aux deux tiers, en entier.",
  "cs.forEach((s,i)=>{const r=8,L=2*Math.PI*r;mk(s.x+s.w-30,s.y+10,20,20,'',`<svg width='20' height='20' viewBox='0 0 20 20'><circle cx='10' cy='10' r='${r}' fill='none' stroke='#1E4558' stroke-width='3.5'/><circle cx='10' cy='10' r='${r}' fill='none' stroke='#FB0161' stroke-width='3.5' stroke-dasharray='${L*(i+1)/3} ${L}' transform='rotate(-90 10 10)'/></svg>`)})")
v("Prix en pastille", "Le prix passe dans une pastille arrondie : ardoise, framboise, rose.",
  "hd.forEach((h,i)=>h.style.cssText+=`;background:${G[i]};color:#fff;padding:3px 12px;border-radius:12px`)")
v("Lueur croissante", "Les cartes gagnent une lueur rose douce de plus en plus visible.",
  "cs.forEach((s,i)=>under(mk(s.x+2,s.y+2,s.w-4,s.h-4,`border-radius:12px;box-shadow:${['none','0 0 14px 2px rgba(251,1,97,.28)','0 0 24px 5px rgba(251,1,97,.5)'][i]}`)))")
v("Contour qui s'épaissit", "Contour rose de plus en plus épais : 1, 2, 3 px.",
  "cs.forEach((s,i)=>{s.p.setAttribute('stroke',i?PK:SL);s.p.setAttribute('stroke-width',String(1+i))})")
v("Bande de dégradé sous les cartes", "Une seule bande en dégradé ardoise → rose court sous les trois cartes, coupée à chaque carte.",
  "const y=cs[0].y+cs[0].h+14,x0=cs[0].x,x1=cs[2].x+cs[2].w;cs.forEach(s=>mk(s.x,y,s.w,6,`background:${grad};background-size:${x1-x0}px 100%;background-position:${x0-s.x}px 0;border-radius:3px`))")
v("Prix qui grossit + barre", "Le prix grandit (12, 15, 18 pt) et la barre d'accent en haut s'allonge en même temps.",
  "hd.forEach((h,i)=>{h.style.fontSize=(12+i*3)+'pt';h.style.color=['#C9D4D8',CR,'#fff'][i]});cs.forEach((s,i)=>mk(s.x+14,s.y,(s.w-28)*(i+1)/3,4,'background:#FB0161;border-radius:0 0 3px 3px'))")
v("Libellés sous la flèche", "La flèche passe en dégradé et porte, sous elle, ENTRY / MID-RANGE / PREMIUM en petites capitales crème.",
  "if(ar){hideAr();mk(ar.x,ar.cy-4,ar.w-14,8,`background:${grad};border-radius:4px`);mk(ar.x+ar.w-16,ar.cy-10,0,0,'border-left:16px solid #FB0161;border-top:10px solid transparent;border-bottom:10px solid transparent');cs.forEach((s,i)=>mk(s.x,ar.cy+10,s.w,14,'text-align:center;font:600 6.5pt Lexend;letter-spacing:.24em;color:#E7CDA8',LV[i]))}")
v("Rampe de fond continue", "Un fond très légèrement teinté va de gauche à droite sous les trois cartes, du bleu au rose sourd.",
  "const x0=cs[0].x,x1=cs[2].x+cs[2].w;cs.forEach(s=>{s.p.setAttribute('fill','none');under(mk(s.x+1,s.y+1,s.w-2,s.h-2,`border-radius:13px;background:linear-gradient(90deg,#0B3850,#3A2548);background-size:${x1-x0}px 100%;background-position:${x0-s.x}px 0`))})")
v("Grille de points", "Dans le coin haut droit, trois petits points en ligne : 1, 2 ou 3 sont pleins.",
  "cs.forEach((s,i)=>mk(s.x+s.w-44,s.y+14,34,8,'display:flex;gap:5px;justify-content:flex-end',[0,1,2].map(j=>`<i style='width:8px;height:8px;border-radius:50%;background:${j<=i?PK:'#1E4558'}'></i>`).join('')))")
v("Ligne de séparation colorée", "Un trait sous le prix sépare le prix du texte ; il passe de l'ardoise au rose et s'allonge.",
  "tb.forEach((t,i)=>{t.el.querySelector('p').insertAdjacentHTML('afterend',`<div style='margin:3px auto 4px;height:3px;border-radius:2px;background:${G[i]};width:${30+i*25}px'></div>`)})")
v("Niveau en toutes lettres", "Sous le prix, un niveau écrit en crème : « Level 1 », « Level 2 », « Level 3 », avec le chiffre en rose gras.",
  "tb.forEach((t,i)=>t.el.querySelector('p').insertAdjacentHTML('afterend',`<div style='text-align:center;font:500 7pt Lexend;letter-spacing:.18em;color:#9FB0B7;margin-top:2px'>LEVEL <b style='color:#FB0161;font-size:9pt'>${i+1}</b></div>`))")
v("Flèche dégradé + bandeaux sombres", "Combinaison : flèche en dégradé en haut et bandeaux d'en-tête de l'ardoise au framboise foncé.",
  "if(ar){hideAr();mk(ar.x,ar.cy-4,ar.w-14,8,`background:${grad};border-radius:4px`);mk(ar.x+ar.w-16,ar.cy-10,0,0,'border-left:16px solid #FB0161;border-top:10px solid transparent;border-bottom:10px solid transparent')}cs.forEach((s,i)=>under(mk(s.x+1,s.y+1,s.w-2,34,`background:${['#1E4558','#4A2A50','#7A2450'][i]};border-radius:13px 13px 0 0`)));hd.forEach(h=>h.style.color='#fff')")
assert len(V) == 30, len(V)
L = [chr(65 + i) if i < 26 else 'Z' + chr(65 + i - 26) for i in range(30)]
item = dict(id='P', title="Prix : 30 façons de montrer une gradation", what="Toutes propres et alignées : rien ne bouge, seule la couleur, la taille ou la longueur monte d'une carte à l'autre. Les sacs d'argent disparaissent.",
            scope=[13], shot=13, fam='Prix', clip=[130, 230, 700, 280], mine='A', why="La barre d'accent qui s'allonge est la plus sobre : un seul élément, toujours au même endroit, qui grandit avec le prix.")
for l, x in zip(L, V): item[l] = x
item['keys'] = L
ITEMS = [item]
