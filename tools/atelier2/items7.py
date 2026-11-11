"""11 Nov, 10h: slide 97 (bold bets) x 15 layouts, contrast logo x 6. ITEMS=items7 python3 tools/atelier2/shoot.py decks/edtech-full <out>"""
import importlib.util, pathlib
_s = importlib.util.spec_from_file_location('i6', pathlib.Path(__file__).parent / 'items6.py'); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
LIB = _m.LIB

# 8 bets read live from the slide (title, text, horizon), icons chosen per bet
BETS = LIB + r'''
const cards=A.cards(sl), tt=A.texts(sl);
const ICO={'AI TUTOR FOR ALL':'🤖','TWO-HOUR SCHOOL':'🏫','AI UNIVERSITIES':'🎓','SKILLS PASSPORTS':'📜','LIFELONG TUTORS':'🧭','VR CLASSROOMS':'🖥️','NEURO LEARNING':'🧠','INSTANT COURSES':'⏱️'};
const B=cards.map(c=>{const h=tt.find(t=>t.cy<c.y&&t.cy>c.y-70&&Math.abs(t.cx-c.cx)<20),d=tt.find(t=>Math.abs(t.x-c.x)<3&&Math.abs(t.y-c.y)<3);
  return {n:h?clean(h):'',d:d?clean(d):'',near:c.y<400,y:c.y,x:c.x}}).sort((a,b)=>a.y-b.y||a.x-b.x);
const NEAR=B.filter(b=>b.near), FAR=B.filter(b=>!b.near), SIX=[...NEAR.slice(0,3),...FAR.slice(0,3)];
const icn=(b,sz,col)=>A.svg(ICO[b.n]||'💡','line',sz||22,col||CR,1.8)||'';
const lab=(t,c)=>`<div style="font:700 10px Lexend;letter-spacing:.16em;color:${c||GR}">${t}</div>`;
'''
def V(name, desc, js): return dict(name=name, desc=desc, js=js)
K = [chr(65 + i) for i in range(15)]
X = dict(id='B', fam='Bold bets', title='Slide 97 « Which bold bets could reshape learning? » : 15 mises en page',
         shot=97, mine='C', keys=K, scope=[97],
         what="8 cartes identiques en deux rangées, et les horizons écrits en gris à gauche, sur l’accolade. On ne voit pas tout de suite ce qui est proche et ce qui est lointain.",
         why="Le proche en grand devant, le lointain petit et pâle derrière : la distance dans le temps se voit comme une distance dans l’espace, sans accolade ni étiquette sur le côté.")
X['A'] = V('Frise du temps', 'Une flèche « Today → 10 years » ; les 4 paris proches au-dessus, les 4 lointains dessous, chacun épinglé à sa période.', BETS + r'''
let h=box(90,372,780,6,`background:linear-gradient(90deg,${PK},#2E5568);border-radius:3px`)+box(70,364,22,22,`border-radius:50%;background:${PK};box-shadow:0 0 0 5px ${N}`)
+box(40,392,90,16,`text-align:center;font:700 10px Lexend;color:#fff`,'TODAY')+box(800,392,100,16,`text-align:right;font:700 10px Lexend;color:${GR}`,'10 YEARS')
+box(470,392,40,16,`text-align:center;font:600 10px Lexend;color:${GR}`,'5 Y')+box(487,366,3,18,`background:${GR}`);
const col=(b,i,up)=>{const x=120+i*190;return box(x,up?190:420,170,up?160:150,`border-radius:10px;background:${up?N3:'transparent'};border:${up?'0':'1px dashed '+LN};padding:12px 14px`,
`<div style="display:flex;align-items:center;gap:8px">${icn(b,18,up?CR:GR)}<span style="font:700 10.5px Lexend;color:${up?'#fff':CR};letter-spacing:.05em">${b.n}</span></div><div style="font:400 10.5px/1.45 Lexend;color:${up?CR:GR};margin-top:8px">${b.d}</div>`)
+box(x+84,up?350:384,2,up?22:36,`background:${up?PK:LN}`)};
NEAR.forEach((b,i)=>h+=col(b,i,1));FAR.forEach((b,i)=>h+=col(b,i,0));stage(h)''')
X['B'] = V('Deux colonnes « bientôt / plus tard »', 'Deux colonnes titrées « Next 5 years » et « 5 to 10 years », 4 paris chacune, icône à gauche : on lit comme une liste.', BETS + r'''
let h='';[[NEAR,'NEXT 5 YEARS',110,1],[FAR,'5 TO 10 YEARS',500,0]].forEach(([L,t,x,hot])=>{h+=box(x,180,350,26,`font:700 13px Lexend;letter-spacing:.14em;color:${hot?'#fff':GR};border-bottom:${hot?4:2}px solid ${hot?PK:LN};padding-bottom:6px`,t);
L.forEach((b,i)=>{const y=224+i*86;h+=box(x,y,46,46,`${flexc};border-radius:12px;background:${hot?N3:'transparent'};border:${hot?0:1.5}px solid ${LN}`,icn(b,22,hot?CR:GR))
+box(x+60,y,290,80,'',`<div style="font:700 11.5px Lexend;color:${hot?'#fff':CR};letter-spacing:.05em">${b.n}</div><div style="font:400 11px/1.45 Lexend;color:${hot?CR:GR};margin-top:4px">${b.d}</div>`)})});stage(h)''')
X['C'] = V('Perspective : le proche devant, le lointain derrière', 'Les 4 paris proches en grandes cartes au premier plan, les 4 lointains en petites cartes plus pâles au fond, comme vus de loin.', BETS + r'''
let h=box(170,178,620,16,`text-align:center;font:700 9px Lexend;letter-spacing:.16em;color:${GR}`,'FURTHER AWAY · 5 TO 10 YEARS');
FAR.forEach((b,i)=>{h+=box(170+i*158,198,146,118,`border-radius:10px;border:1px dashed ${LN};padding:10px;opacity:.85`,`<div style="display:flex;gap:6px;align-items:center">${icn(b,14,GR)}<span style="font:700 8.5px Lexend;color:${CR};letter-spacing:.04em">${b.n}</span></div><div style="font:400 8.5px/1.4 Lexend;color:${GR};margin-top:5px">${b.d}</div>`)});
h+=box(90,338,780,16,`text-align:center;font:700 10px Lexend;letter-spacing:.16em;color:#fff`,'UP CLOSE · NEXT 5 YEARS');
NEAR.forEach((b,i)=>{h+=box(90+i*198,362,184,210,`border-radius:14px;background:${N3};padding:18px;box-shadow:0 10px 24px #0005`,`<div style="width:44px;height:44px;border-radius:12px;background:${PK};display:flex;align-items:center;justify-content:center">${icn(b,22,'#fff')}</div><div style="font:700 13px Lexend;color:#fff;margin-top:14px;letter-spacing:.04em">${b.n}</div><div style="font:400 12px/1.5 Lexend;color:${CR};margin-top:6px">${b.d}</div>`)});stage(h)''')
X['D'] = V('Six cartes à étiquette d’horizon', 'Passage à 6 paris (les 3 premiers de chaque horizon), cartes 3×2 plus grandes, une pastille « 0-5 Y » rose ou « 5-10 Y » grise en haut de chaque carte.', BETS + r'''
let h='';SIX.forEach((b,i)=>{const x=110+(i%3)*255,y=190+Math.floor(i/3)*195,hot=b.near;
h+=box(x,y,235,175,`border-radius:14px;background:${hot?N3:N2};border:1px solid ${LN};padding:18px`,`<div style="display:flex;justify-content:space-between;align-items:center">${icn(b,26,hot?CR:GR)}<span style="font:700 9px Lexend;letter-spacing:.12em;padding:4px 9px;border-radius:20px;background:${hot?PK:'transparent'};border:${hot?0:1.5}px solid ${GR};color:${hot?'#fff':GR}">${hot?'0-5 YEARS':'5-10 YEARS'}</span></div>
<div style="font:700 13px Lexend;color:#fff;margin-top:16px;letter-spacing:.04em">${b.n}</div><div style="font:400 11.5px/1.5 Lexend;color:${CR};margin-top:6px">${b.d}</div>`)});stage(h)''')
X['E'] = V('Gantt sur 10 ans', 'Une règle 2026 → 2036 ; chaque pari est une barre sur sa fenêtre (proche : 2026-2031 en rose, lointain : 2031-2036 en navy), son texte à gauche.', BETS + r'''
const x0=410,w=460;let h='';for(let k=0;k<=10;k+=5)h+=box(x0+w*k/10-20,180,40,14,`text-align:center;font:600 10px Lexend;color:${GR}`,String(2026+k))+box(x0+w*k/10,198,1,390,`background:${LN}`);
B.forEach((b,i)=>{const y=210+i*47,s=b.near?0:.5;h+=box(90,y,300,42,'display:flex;flex-direction:column;justify-content:center',`<div style="font:700 10.5px Lexend;color:#fff;letter-spacing:.05em">${b.n}</div><div style="font:400 9px/1.3 Lexend;color:${GR}">${b.d}</div>`)
+box(x0+w*s+4,y+10,w/2-8,22,`border-radius:11px;background:${b.near?PK:'#2E5568'}`)});stage(h)''')
X['F'] = V('Un pari en vedette', 'Le premier pari (AI tutor for all) en grande carte à gauche, les 7 autres en liste compacte à droite, rangés par horizon.', BETS + r'''
const [a,...r]=B;let h=box(90,190,330,380,`border-radius:16px;background:${N3};padding:30px`,`<div style="width:60px;height:60px;border-radius:14px;background:${PK};display:flex;align-items:center;justify-content:center">${icn(a,30,'#fff')}</div>${'<div style="height:24px"></div>'+lab('THE BIGGEST BET · 0-5 YEARS')}<div style="font:700 26px/1.15 Lexend;color:#fff;margin-top:8px">${ttl(a.n)}</div><div style="font:400 15px/1.55 Lexend;color:${CR};margin-top:14px">${a.d}</div>`);
r.forEach((b,i)=>{const y=190+i*55;h+=box(450,y,420,52,`display:flex;gap:12px;align-items:center;border-bottom:1px solid ${LN}`,`<span style="flex:none;font:700 8.5px Lexend;letter-spacing:.1em;width:62px;color:${b.near?PK:GR}">${b.near?'0-5 Y':'5-10 Y'}</span><div><div style="font:700 11px Lexend;color:#fff;letter-spacing:.04em">${b.n}</div><div style="font:400 10px/1.35 Lexend;color:${CR}">${b.d}</div></div>`)});stage(h)''')
X['G'] = V('Unes de journal du futur', 'Chaque pari en « une » de journal : grand titre, horizon en date, phrase en chapeau. 6 paris, cartes claires sur navy.', BETS + r'''
let h='';SIX.forEach((b,i)=>{const x=100+(i%3)*260,y=185+Math.floor(i/3)*200;h+=box(x,y,240,184,`border-radius:6px;background:#E9E2D6;padding:14px 16px;box-shadow:0 6px 18px #0006`,
`<div style="display:flex;justify-content:space-between;border-bottom:2px solid #062A3C;padding-bottom:5px;font:700 8px Lexend;letter-spacing:.14em;color:#062A3C"><span>THE LEARNING TIMES</span><span>${b.near?'BY 2031':'BY 2036'}</span></div>
<div style="font:700 21px/1.15 Georgia,serif;color:#062A3C;margin-top:12px">${ttl(b.n)}</div><div style="font:400 13px/1.45 Georgia,serif;color:#33444C;margin-top:8px">${b.d}</div>`)});stage(h)''')
X['H'] = V('Matrice horizon × public', 'Deux axes : horizon (proche → lointain) et public (école → adultes et travail). Chaque pari est posé dans sa case.', BETS + r'''
const AUD={'AI TUTOR FOR ALL':0,'TWO-HOUR SCHOOL':0,'VR CLASSROOMS':0,'NEURO LEARNING':0,'AI UNIVERSITIES':1,'SKILLS PASSPORTS':1,'LIFELONG TUTORS':1,'INSTANT COURSES':1};
let h=box(150,203,730,2,`background:${LN}`)+box(150,398,730,1,`background:${LN}`)+box(515,203,1,390,`background:${LN}`)
+box(150,178,365,18,`text-align:center;font:700 10px Lexend;letter-spacing:.16em;color:#fff`,'NEXT 5 YEARS')+box(515,178,365,18,`text-align:center;font:700 10px Lexend;letter-spacing:.16em;color:${GR}`,'5 TO 10 YEARS')
+box(40,278,100,40,`text-align:right;font:700 9.5px/1.3 Lexend;letter-spacing:.12em;color:${GR}`,'SCHOOLS &<br>CHILDREN')+box(40,473,100,40,`text-align:right;font:700 9.5px/1.3 Lexend;letter-spacing:.12em;color:${GR}`,'ADULTS &<br>WORK');
const cnt={};B.forEach(b=>{const c=(b.near?0:1)+'-'+AUD[b.n],k=cnt[c]=(cnt[c]||0)+1,x=(b.near?160:525),y=(AUD[b.n]?410:215)+(k-1)*92;
h+=box(x,y,345,84,`display:flex;gap:12px;align-items:center;padding:10px 14px;border-radius:10px;background:${b.near?N3:'transparent'};border:1px solid ${LN}`,`<span style="flex:none">${icn(b,22,b.near?CR:GR)}</span><div><div style="font:700 11px Lexend;color:#fff;letter-spacing:.04em">${b.n}</div><div style="font:400 10px/1.4 Lexend;color:${CR};margin-top:2px">${b.d}</div></div>`)});stage(h)''')
X['I'] = V('Liste magazine numérotée', 'Grands numéros 01-08 en contour crème, deux colonnes, l’horizon écrit à côté du numéro. Très éditorial, aucune boîte.', BETS + r'''
let h='';B.forEach((b,i)=>{const x=i<4?100:500,y=185+(i%4)*96;h+=box(x,y,70,60,`font:700 42px/1 Lexend;color:transparent;-webkit-text-stroke:1.3px ${b.near?PK:GR}`,String(i+1).padStart(2,'0'))
+box(x+80,y,300,90,'',`<div style="font:700 8.5px Lexend;letter-spacing:.14em;color:${b.near?PK:GR}">${b.near?'NEXT 5 YEARS':'5 TO 10 YEARS'}</div><div style="font:700 12px Lexend;color:#fff;letter-spacing:.04em;margin-top:3px">${b.n}</div><div style="font:400 11px/1.45 Lexend;color:${CR};margin-top:3px">${b.d}</div>`)});stage(h)''')
X['J'] = V('Écran coupé en deux', 'Moitié gauche pleine (navy clair) pour les 4 paris proches, moitié droite sombre et pointillée pour les 4 lointains. Le contraste dit « plus sûr / plus spéculatif ».', BETS + r'''
let h=box(70,175,410,410,`border-radius:16px 0 0 16px;background:${N3};padding:24px`,lab('NEXT 5 YEARS','#fff'))+box(480,175,410,410,`border-radius:0 16px 16px 0;border:1.5px dashed ${LN};padding:24px`,lab('5 TO 10 YEARS'));
[[NEAR,94,1],[FAR,504,0]].forEach(([L,x,hot])=>L.forEach((b,i)=>{h+=box(x,215+i*90,370,84,'display:flex;gap:12px',`<span style="flex:none;margin-top:2px">${icn(b,22,hot?CR:GR)}</span><div><div style="font:700 11.5px Lexend;color:${hot?'#fff':CR};letter-spacing:.04em">${b.n}</div><div style="font:400 11px/1.45 Lexend;color:${hot?CR:GR};margin-top:3px">${b.d}</div></div>`)}));stage(h)''')
X['K'] = V('Vague du temps', 'Une ligne ondulée de « Today » à « 10 years » ; les 8 paris posés dessus à intervalles réguliers, textes alternés au-dessus et en dessous. La ligne est rose sur les 5 premières années.', BETS + r'''
const Y=x=>392+7*Math.sin((x-90)/780*Math.PI*4);let d='',d2='';for(let x=90;x<=870;x+=6){d+=(x===90?'M':'L')+x+' '+Y(x);if(x<=480)d2+=(x===90?'M':'L')+x+' '+Y(x)}
let h=`<svg style="position:absolute;left:0;top:0" width="960" height="672"><path d="${d}" fill="none" stroke="${LN}" stroke-width="3"/><path d="${d2}" fill="none" stroke="${PK}" stroke-width="5"/></svg>`;
B.forEach((b,i)=>{const x=125+i*101,y=Y(x),up=i%2===0;h+=box(x-15,y-15,30,30,`${flexc};border-radius:50%;background:${b.near?PK:N};border:${b.near?0:2}px solid ${GR}`,icn(b,14,b.near?'#fff':GR))
+box(x-92,up?y-190:y+28,184,160,`text-align:center;display:flex;flex-direction:column;justify-content:${up?'flex-end':'flex-start'}`,`<div style="font:700 10px Lexend;color:#fff;letter-spacing:.04em">${b.n}</div><div style="font:400 9.5px/1.4 Lexend;color:${CR};margin-top:3px">${b.d}</div>`)
+box(x-1,up?y-22:y+15,2,8,`background:${LN}`)});
h+=box(60,Y(90)+18,80,14,`font:700 9px Lexend;color:#fff;letter-spacing:.12em`,'TODAY')+box(800,Y(870)-34,90,14,`text-align:right;font:700 9px Lexend;color:${GR};letter-spacing:.12em`,'10 YEARS');stage(h)''')
X['L'] = V('Tableau avec jauge d’horizon', 'Une ligne par pari : nom, ce que c’est, et une petite jauge à 2 segments (le premier rose = 0-5 ans, le second = 5-10 ans).', BETS + r'''
let h=box(100,180,760,18,`display:flex;font:700 9px Lexend;letter-spacing:.16em;color:${GR}`,'<span style="width:220px">BET</span><span style="width:430px">WHAT IT IS</span><span>WHEN</span>');
B.forEach((b,i)=>{const y=204+i*47;h+=box(100,y,760,46,`display:flex;align-items:center;border-top:1px solid ${LN}`,`<span style="width:220px;display:flex;gap:10px;align-items:center;font:700 11px Lexend;color:#fff;letter-spacing:.04em">${icn(b,18)}${b.n}</span><span style="width:430px;font:400 10.5px/1.35 Lexend;color:${CR}">${b.d}</span><span style="display:flex;gap:4px"><i style="width:44px;height:10px;border-radius:5px;background:${b.near?PK:N3}"></i><i style="width:44px;height:10px;border-radius:5px;background:${b.near?N3:'#8FA3AB'}"></i></span>`)});stage(h)''')
X['M'] = V('Cartes à retourner', 'Grandes icônes rondes en grille 4×2, le nom dessous, le texte en petit ; les paris lointains en contour seulement (plus « flous »).', BETS + r'''
let h='';B.forEach((b,i)=>{const x=110+(i%4)*190,y=185+Math.floor(i/4)*205,hot=b.near;h+=box(x+50,y,70,70,`${flexc};border-radius:50%;background:${hot?N3:'transparent'};border:${hot?'3px solid '+PK:'2px dashed '+GR}`,icn(b,30,hot?CR:GR))
+box(x,y+80,170,20,`text-align:center;font:700 11px Lexend;color:${hot?'#fff':CR};letter-spacing:.04em`,b.n)+box(x+5,y+104,160,80,`text-align:center;font:400 10.5px/1.45 Lexend;color:${hot?CR:GR}`,b.d)});
h+=box(100,590,760,14,`text-align:center;font:600 9px Lexend;letter-spacing:.14em;color:${GR}`,'TOP ROW · NEXT 5 YEARS &nbsp;&nbsp;·&nbsp;&nbsp; BOTTOM ROW · 5 TO 10 YEARS');stage(h)''')
X['N'] = V('Rangées sans accolade', 'On garde les 8 cartes actuelles, mais l’horizon devient un bandeau horizontal au-dessus de chaque rangée (« NEXT 5 YEARS » plein, « 5 TO 10 YEARS » contour) : plus d’accolade ni de texte sur le côté.', LIB + r'''
const tt=A.texts(sl);tt.filter(t=>/HORIZON/.test(t.text)).forEach(t=>t.el.style.visibility='hidden');A.hide(A.shapes(sl).filter(s=>s.w<20&&s.h>150));
A.div(sl,156,152,702,22,`display:flex;align-items:center;gap:10px;font:700 10px Lexend;letter-spacing:.16em;color:#fff`,`<span style="background:${PK};padding:4px 10px;border-radius:4px">NEXT 5 YEARS</span><i style="flex:1;height:2px;background:${PK}"></i>`);
A.div(sl,156,370,702,22,`display:flex;align-items:center;gap:10px;font:700 10px Lexend;letter-spacing:.16em;color:${GR}`,`<span style="border:1.5px solid ${GR};padding:3px 9px;border-radius:4px">5 TO 10 YEARS</span><i style="flex:1;height:0;border-top:2px dashed ${LN}"></i>`);''')
X['O'] = V('Correctif minimal', 'Ta slide telle quelle, seules les étiquettes d’horizon sont corrigées : sur 3 lignes, collées à gauche, elles ne touchent plus l’accolade.', LIB + r'''
A.texts(sl).filter(t=>/HORIZON/.test(t.text)).forEach(t=>{t.el.style.left='18px';t.el.style.width='92px';t.el.querySelectorAll('span').forEach(s=>s.style.whiteSpace='normal')})''')

L = dict(id='L', fam='Contraste', title='Slides « How Preply… / Gizmo… / MagicSchool… » : place du logo (5 slides, même modèle)',
         shot=210, mine='A', keys=list('ABCDEF'), scope=[210, 211, 212, 213, 214], clip=(60, 170, 840, 330),
         what="Le logo est collé au bloc de gauche, avec la flèche, alors qu’il appartient à la colonne de droite.",
         why="Centré entre les deux blocs, il ne penche d’aucun côté et la flèche se lit « regular → Preply ».")
L['A'] = V('Logo centré', 'Flèche retirée, logo exactement à mi-distance des deux blocs.', '', )
L['A']['css'] = 'S .contrast .mid{justify-content:center}S .contrast .mid i{display:none}'
L['B'] = V('Sans logo, flèche centrée', 'Plus de logo par ligne : une petite flèche rose centrée entre les blocs.', '')
L['B']['css'] = 'S .contrast .mid{justify-content:center}S .contrast .mid .lt{display:none}S .contrast .mid i{width:22px;height:2px;background:#FB0161}S .contrast .mid i::after{border-left-color:#FB0161;top:-3px}'
L['C'] = V('Logo une seule fois, dans l’en-tête', 'Le logo passe à côté du titre « PREPLY » en haut de la colonne ; entre les blocs, une simple flèche centrée.', 'const h=sl.querySelectorAll(".contrast .hd")[1],lt=sl.querySelector(".contrast .mid .lt");if(h&&lt){const c=lt.cloneNode(true);c.style.cssText="display:inline-block;vertical-align:middle;margin-right:8px;width:24px;height:24px";h.prepend(c)}')
L['C']['css'] = L['B']['css']
L['D'] = V('Logo dans le bloc de droite', 'Le logo est le début du bloc de droite (petite tuile à gauche du texte), plus rien entre les blocs.', 'sl.querySelectorAll(".contrast .mid").forEach(m=>{const lt=m.querySelector(".lt"),b=m.nextElementSibling;if(lt&&b){lt.style.cssText="display:inline-block;vertical-align:middle;width:16px;height:16px;margin-right:8px;border-radius:4px";b.prepend(lt)}})')
L['D']['css'] = 'S .contrast .mid i{display:none}'
L['E'] = V('Logo centré sur une ligne verticale', 'Logos centrés, reliés par un fin trait vertical qui sépare les deux colonnes (effet « colonne vertébrale »).', '')
L['E']['css'] = 'S .contrast .mid{justify-content:center;position:relative}S .contrast .mid i{display:none}S .contrast .mid::before{content:"";position:absolute;left:50%;top:-8px;bottom:-8px;border-left:1px solid #334D54;z-index:0}S .contrast .mid .lt{position:relative;z-index:1}'
L['F'] = V('Gros logo unique au centre', 'Plus de logo par ligne ; un seul grand logo (48 px) centré au-dessus des deux colonnes, entre les deux titres.', 'const lt=sl.querySelector(".contrast .mid .lt"),hd=sl.querySelector(".contrast .hd");if(lt&&hd){const c=lt.cloneNode(true);const r=hd.getBoundingClientRect(),R=sl.getBoundingClientRect();c.style.cssText=`position:absolute;width:44px;height:44px;left:${480-22}px;top:${r.top-R.top-12}px;border-radius:10px`;sl.appendChild(c)}')
L['F']['css'] = 'S .contrast .mid{justify-content:center}S .contrast .mid .lt{display:none}S .contrast .mid i{display:none}'
ITEMS = [X, L]
