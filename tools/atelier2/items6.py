"""Atelier 3 slides moches x 10 mises en page (11 Nov 2026). Each variant rebuilds the slide from its own data (read live on the slide),
so it works on every slide of the type. ITEMS=items6 python3 tools/atelier2/shoot.py decks/edtech-full <out>"""

KEYS = list('ABCDEFGHIJ')

# ---------------------------------------------------------------- shared helpers (prepended to every variant)
LIB = r'''
const N='#062A3C',N2='#0B3850',N3='#123F57',LN='#334D54',CR='#E7CDA8',PK='#FB0161',GR='#8FA3AB',W='#FFFFFF';
const T=A.texts(sl), clean=t=>t.el.innerText.replace(/\s+/g,' ').trim();
const stage=(html,keep)=>{sl.querySelectorAll('.raw > *').forEach(e=>{if(!(keep||[]).includes(e))e.style.visibility='hidden'});return A.div(sl,0,0,960,672,'font-family:Lexend,sans-serif;color:'+CR,html)};
const ic=(e,sz,col,st)=>{const s=e&&A.svg(e,st||'line',sz,col||CR,2);return s||''};
const up=s=>s.toUpperCase(), ttl=s=>s.split(' ').map(w=>/^(AI|K-12|HR|IT|US|EU)$/i.test(w)?w.toUpperCase():w.charAt(0)+w.slice(1).toLowerCase()).join(' ');
const box=(x,y,w,h,css,inner)=>`<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;${css||''}">${inner||''}</div>`;
const flexc='display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center';
'''

# who pays / who needs: 5 personas (name, description, emoji)
WHO = LIB + r'''
const sub=T.find(t=>t.y>140&&t.y<185&&t.w>500);
const heads=T.filter(t=>t.y>190&&t.h<60&&t.w<200&&/^[A-Z0-9\-&’' ]+$/.test(clean(t))).sort((a,b)=>a.x-b.x);
const descs=T.filter(t=>t.h>90&&/[a-z]/.test(t.text)).sort((a,b)=>a.x-b.x);
const emo=T.filter(t=>A.isEmoji(t.text));
const P=heads.map((h,i)=>({n:clean(h),d:descs[i]?clean(descs[i]):'',e:(emo.find(e=>Math.abs(e.cx-h.cx)<45)||{}).text}));
const SEG=sub?clean(sub):'';const keep=sub?[sub.el]:[];
const ini=n=>/\d/.test(n)?n.replace(/[^A-Z0-9]/g,'').replace(/^([A-Z])(\d+).*/,'$1$2').slice(0,3):n.split(/[ \-]/).filter(Boolean).map(w=>w[0]).join('').slice(0,2);
'''

# segment divider: section, name, description, position among the segments of the same section
DIV = LIB + r'''
const big=T.slice().sort((a,b)=>b.h-a.h)[0], desc=T.find(t=>/[a-z]/.test(t.text)&&t!==big), sec=T.find(t=>t!==big&&t!==desc&&/^[A-Z ]+$/.test(t.text));
const stage0=stage;const stageI=h=>{const d=stage0(h);d.style.top='40px';return d};
const NAME=clean(big), DESC=desc?clean(desc):'', SEC=sec?clean(sec):'';
const ALL=[...document.querySelectorAll('.slide')].filter(s=>!s.querySelector('h1.title')&&[...s.querySelectorAll('.raw > .rx-t')].some(e=>e.innerText.trim()===SEC)).map(s=>{const t=[...s.querySelectorAll('.raw > .rx-t')].sort((a,b)=>b.getBoundingClientRect().height-a.getBoundingClientRect().height)[0];return t.innerText.replace(/\s+/g,' ').trim()});
const IDX=Math.max(0,ALL.indexOf(NAME)), CNT=ALL.length||1, NEXT=ALL[IDX+1]||'', NUM=String(IDX+1).padStart(2,'0');
'''

# exceptional vs bad experience
EXP = LIB + r'''
const sub=T.find(t=>t.y>140&&t.y<185&&t.w>500);
const txt=T.filter(t=>t.h>80&&/[a-z]/.test(t.text)).sort((a,b)=>a.y-b.y);
const GOOD=clean(txt[0]), BAD=clean(txt[1]), SEG=sub?clean(sub):'', keep=sub?[sub.el]:[];
const sent=s=>s.match(/[^.!?]+[.!?]+/g).map(x=>x.trim());
const G=sent(GOOD), B=sent(BAD);
const chk=sz=>`<svg width="${sz}" height="${sz}" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const crs=(sz,c)=>`<svg width="${sz}" height="${sz}" viewBox="0 0 24 24"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" fill="none" stroke="${c||'#fff'}" stroke-width="3" stroke-linecap="round"/></svg>`;
'''

def V(name, desc, js):
    return dict(name=name, desc=desc, js=js)

# ================================================================= 1. Who pays / who needs it the most
W = dict(id='W', fam='Qui paie / Qui en a le plus besoin', title='« Qui paie ? » et « Qui en a le plus besoin ? » (arbre à 5 branches)',
         shot=63, mine='C', keys=KEYS,
         scope=[63, 67, 71, 75, 79, 83, 107, 111, 116, 120, 124, 128],
         what="Un arbre en râteau, cinq cartes étroites où le texte s'empile sur 6 lignes, des petits carrés roses à cheval sur le coin des cartes. Utilisé 12 fois.",
         why="Les fiches persona donnent un visage à chaque acheteur, se lisent d'un coup d'œil et gardent le texte sur 3-4 lignes.")
W['A'] = V('Tableau à deux colonnes', 'Une ligne par acheteur : qui (gras, avec icône) | ce qu’il veut. Filets fins, aucune carte.', WHO + r'''
let h='';P.forEach((p,i)=>{const y=212+i*72;h+=box(110,y,740,72,`border-top:1px solid ${LN};${i==P.length-1?'border-bottom:1px solid '+LN:''}`)
+box(118,y+14,44,44,`${flexc};border-radius:10px;background:${N3}`,ic(p.e,22)||`<b style="font-size:14px;color:${W}">${ini(p.n)}</b>`)
+box(180,y,230,72,'display:flex;align-items:center;font:700 13px Lexend;color:#fff;letter-spacing:.04em',p.n)
+box(420,y,430,72,`display:flex;align-items:center;font:400 12.5px/1.45 Lexend;color:${CR}`,p.d)});
h+=box(180,192,230,18,`font:600 9.5px Lexend;letter-spacing:.2em;color:${GR}`,'WHO')+box(420,192,300,18,`font:600 9.5px Lexend;letter-spacing:.2em;color:${GR}`,'WHAT THEY NEED');
stage(h,keep)''')
W['B'] = V('Roue autour du segment', 'Le segment au centre dans un disque, les 5 acheteurs en couronne, reliés par des rayons.', WHO + r'''
const cx=480,cy=395,R=168;let h=`<svg style="position:absolute;left:0;top:0" width="960" height="672">`;
const pos=P.map((p,i)=>{const a=-Math.PI/2+i*2*Math.PI/P.length;return [cx+Math.cos(a)*R*1.55,cy+Math.sin(a)*R*1.02]});
pos.forEach(([x,y])=>h+=`<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="${LN}" stroke-width="2"/>`);h+='</svg>';
h+=box(cx-66,cy-66,132,132,`${flexc};border-radius:50%;background:${PK};font:700 13px/1.25 Lexend;color:#fff;padding:12px;box-shadow:0 0 0 6px ${N}`,SEG||'');
P.forEach((p,i)=>{const [x,y]=pos[i];h+=box(x-105,y-38,210,76,`${flexc};background:${N3};border-radius:10px;padding:8px 12px;box-shadow:0 0 0 4px ${N}`,
`<div style="font:700 11.5px Lexend;color:#fff;letter-spacing:.04em">${p.n}</div><div style="font:400 9.5px/1.35 Lexend;color:${CR};margin-top:4px">${p.d}</div>`)});
stage(h,keep)''')
W['C'] = V('Fiches persona', 'Cinq fiches debout : grand médaillon (icône ou initiales) en haut, nom, puis le besoin. Pas de lignes.', WHO + r'''
let h='';const w=150,g=14,x0=(960-(P.length*w+(P.length-1)*g))/2;
P.forEach((p,i)=>{const x=x0+i*(w+g);h+=box(x,230,w,320,`border-radius:14px;background:${N2};border:1px solid ${LN}`)
+box(x+w/2-38,200,76,76,`${flexc};border-radius:50%;background:${N3};border:3px solid ${N};box-shadow:0 0 0 2px ${LN}`,ic(p.e,32)||`<b style="font:700 22px Lexend;color:${CR}">${ini(p.n)}</b>`)
+box(x+10,292,w-20,44,`${flexc};font:700 12px/1.3 Lexend;color:#fff;letter-spacing:.04em`,p.n)
+box(x+18,340,w-36,4,`background:${PK};border-radius:2px;width:28px;left:${x+w/2-14}px`)
+box(x+12,356,w-24,180,`display:flex;justify-content:center;text-align:center;font:400 11.5px/1.5 Lexend;color:${CR}`,p.d)});
stage(h,keep)''')
W['D'] = V('Liste numérotée en 2 colonnes', 'Grands numéros 01-05 crème, 3 à gauche et 2 à droite, texte libre à côté : une page de magazine.', WHO + r'''
let h='';P.forEach((p,i)=>{const col=i<3?0:1,row=i<3?i:i-3,x=col?500:110,y=215+row*118;
h+=box(x,y,80,70,`font:700 46px/1 Lexend;color:${N3};-webkit-text-stroke:1.5px ${CR}`,String(i+1).padStart(2,'0'))
+box(x+88,y+2,262,22,`font:700 13px Lexend;color:#fff;letter-spacing:.05em`,p.n)
+box(x+88,y+26,262,80,`font:400 12px/1.5 Lexend;color:${CR}`,p.d)});
h+=box(500,215+2*118,350,96,`${flexc};border:1.5px dashed ${LN};border-radius:12px;font:600 12px/1.4 Lexend;color:${GR};padding:14px`,'Five buyers, one market: '+(SEG?ttl(SEG):''));
stage(h,keep)''')
W['E'] = V('Bandes horizontales', 'Chaque acheteur est une bande pleine largeur : bloc navy clair à gauche (nom), texte à droite. Rythme régulier.', WHO + r'''
let h='';P.forEach((p,i)=>{const y=200+i*76;
h+=box(100,y,760,64,`border-radius:10px;background:${i%2?N2:'#0E3448'}`)
+box(100,y,230,64,`display:flex;align-items:center;gap:12px;padding:0 16px;border-radius:10px 0 0 10px;background:${N3};font:700 12.5px Lexend;color:#fff;letter-spacing:.04em`,(ic(p.e,22)?`<span style="flex:none;display:flex">${ic(p.e,22)}</span>`:'')+`<span>${p.n}</span>`)
+box(350,y,490,64,`display:flex;align-items:center;font:400 12.5px/1.45 Lexend;color:${CR}`,p.d)});
stage(h,keep)''')
W['F'] = V('Bulles de parole', 'Chaque besoin devient une bulle (comme un témoignage), le nom de l’acheteur dessous avec son médaillon.', WHO + r'''
let h='';const w=158,g=12,x0=(960-(P.length*w+(P.length-1)*g))/2;
P.forEach((p,i)=>{const x=x0+i*(w+g),hi=12;
h+=box(x,212+hi,w,210,`${flexc};border-radius:16px;background:${N3};padding:16px;font:400 11.5px/1.5 Lexend;color:#fff`,'“'+p.d+'”')
+`<svg style="position:absolute;left:${x+30}px;top:${421+hi}px" width="22" height="16"><path d="M0 0H22L4 16Z" fill="${N3}"/></svg>`
+box(x,446+hi,40,40,`${flexc};border-radius:50%;background:${PK};margin-left:24px`,ic(p.e,20,'#fff')||`<b style="font:700 13px Lexend;color:#fff">${ini(p.n)}</b>`)
+box(x+72,446+hi,w-70,40,`display:flex;align-items:center;font:700 10.5px/1.25 Lexend;color:#fff;letter-spacing:.04em`,p.n)});
stage(h,keep)''')
W['G'] = V('Tableau périodique', 'Une case carrée par acheteur, initiales en très grand comme un symbole chimique, nom et besoin dessous.', WHO + r'''
let h='';const w=150,g=14,x0=(960-(P.length*w+(P.length-1)*g))/2;
P.forEach((p,i)=>{const x=x0+i*(w+g);
h+=box(x,205,w,150,`border-radius:6px;background:${i===0?PK:N3};position:absolute`)
+box(x+10,212,40,16,`font:600 11px Lexend;color:${i===0?'#fff':GR}`,String(i+1))
+box(x,232,w,80,`${flexc};font:700 52px/1 Lexend;color:#fff`,ini(p.n))
+box(x+8,316,w-16,32,`${flexc};font:600 9.5px/1.2 Lexend;color:${i===0?'#fff':CR};letter-spacing:.06em`,p.n)
+box(x+6,372,w-12,180,`text-align:center;font:400 11.5px/1.5 Lexend;color:${CR}`,p.d)});
stage(h,keep)''')
W['H'] = V('Entonnoir vers le segment', 'Les 5 acheteurs à gauche, des flèches qui convergent vers le segment à droite : on voit d’où vient l’argent.', WHO + r'''
let h=`<svg style="position:absolute;left:0;top:0" width="960" height="672"><defs><marker id="fm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="${PK}"/></marker></defs>`;
const ty=392;P.forEach((p,i)=>{const y=208+i*76+32;h+=`<path d="M560 ${y} C 640 ${y}, 650 ${ty}, 716 ${ty}" fill="none" stroke="${PK}" stroke-width="3" marker-end="url(#fm)"/>`});h+='</svg>';
P.forEach((p,i)=>{const y=208+i*76;h+=box(90,y,470,64,`display:flex;align-items:center;gap:14px;padding:0 16px;border-radius:10px;background:${N2};border:1px solid ${LN}`,
`<div style="flex:none;width:150px;font:700 11.5px/1.3 Lexend;color:#fff;letter-spacing:.04em">${p.n}</div><div style="font:400 11px/1.4 Lexend;color:${CR}">${p.d}</div>`)});
h+=box(722,322,160,140,`${flexc};border-radius:14px;background:${PK};font:700 15px/1.3 Lexend;color:#fff;padding:14px`,`<div style="font:600 9px Lexend;letter-spacing:.2em;opacity:.85;margin-bottom:6px">PAID TO</div>${SEG}`);
stage(h,keep)''')
W['I'] = V('Un acheteur en vedette', 'Le 1er acheteur en grande carte à gauche (le plus important), les 4 autres en liste compacte à droite.', WHO + r'''
const [a,...r]=P;let h=box(100,205,330,350,`border-radius:16px;background:${N3};padding:28px`,
`<div style="width:64px;height:64px;border-radius:14px;background:${PK};display:flex;align-items:center;justify-content:center">${ic(a.e,32,'#fff')||`<b style="font:700 22px Lexend;color:#fff">${ini(a.n)}</b>`}</div>
<div style="font:600 10px Lexend;letter-spacing:.2em;color:${GR};margin-top:26px">FIRST BUYER</div><div style="font:700 22px/1.2 Lexend;color:#fff;margin-top:6px">${ttl(a.n)}</div>
<div style="font:400 14px/1.55 Lexend;color:${CR};margin-top:14px">${a.d}</div>`);
r.forEach((p,i)=>{const y=205+i*90;h+=box(460,y,400,80,`display:flex;gap:16px;align-items:flex-start;padding:14px 4px;border-bottom:1px solid ${LN}`,
`<div style="flex:none;width:34px;height:34px;border-radius:50%;background:${N3};display:flex;align-items:center;justify-content:center">${ic(p.e,18)||`<b style="font:700 11px Lexend;color:${CR}">${ini(p.n)}</b>`}</div>
<div><div style="font:700 12px Lexend;color:#fff;letter-spacing:.04em">${p.n}</div><div style="font:400 11.5px/1.45 Lexend;color:${CR};margin-top:3px">${p.d}</div></div>`)});
stage(h,keep)''')
W['J'] = V('Cercles alignés', 'Cinq grands cercles de même taille sur une ligne, le nom dedans, le besoin centré dessous. Simple et symétrique.', WHO + r'''
let h='';const d=136,g=26,x0=(960-(P.length*d+(P.length-1)*g))/2;
h+=box(x0+d/2,272,P.length*(d+g)-g-d,2,`background:${LN}`);
P.forEach((p,i)=>{const x=x0+i*(d+g);h+=box(x,206,d,d,`${flexc};border-radius:50%;background:${N3};border:3px solid ${i===0?PK:LN};padding:14px;gap:6px`,
(ic(p.e,24)?`<div>${ic(p.e,24)}</div>`:'')+`<div style="font:700 11px/1.25 Lexend;color:#fff;letter-spacing:.04em">${p.n}</div>`)
+box(x-6,360,d+12,190,`text-align:center;font:400 11.5px/1.5 Lexend;color:${CR}`,p.d)});
stage(h,keep)''')

# ================================================================= 2. Segment dividers
I = dict(id='I', fam='Intercalaires de segment', title='Intercalaires de segment (« SCHOOL PLATFORMS », « AI TUTORS »…)',
         shot=66, mine='A', keys=KEYS,
         scope=[62, 66, 70, 74, 78, 82, 106, 110, 115, 119, 123, 127],
         what="Une page presque vide : un titre, une phrase, et quatre flèches pointillées qui ne pointent sur rien. Elle ne dit pas où on en est. Utilisée 12 fois.",
         why="Le fil d'Ariane dit où on est et ce qui vient ensuite : l'intercalaire sert enfin à se repérer.")
I['A'] = V('Fil d’Ariane + suivant', 'En haut « Pain points › School platforms », le nom en très grand calé à gauche, et en bas à droite « Next: Online courses → ».', DIV + r'''
let h=box(110,150,740,20,`font:600 11px Lexend;letter-spacing:.18em;color:${GR}`,`${SEC} <span style="color:${LN}">›</span> <span style="color:${CR}">${up(NAME)}</span>`)
+box(110,170,740,2,`background:${LN}`)+box(110,170,Math.round(740*(IDX+1)/CNT),2,`background:${PK};height:4px;margin-top:-1px`)
+box(110,250,740,90,`font:700 54px/1.05 Lexend;color:${CR}`,ttl(NAME))
+box(110,350,560,70,`font:400 17px/1.5 Lexend;color:#fff`,DESC)
+(NEXT?box(560,520,290,40,`display:flex;align-items:center;justify-content:flex-end;gap:10px;font:600 13px Lexend;color:${GR}`,`Next: <b style="color:#fff">${ttl(NEXT)}</b><span style="display:inline-flex;width:28px;height:28px;border-radius:50%;background:${PK};align-items:center;justify-content:center;color:#fff;font-size:15px">→</span>`):'');
stageI(h)''')
I['B'] = V('Grand numéro', 'Le numéro du segment (02) en chiffres géants à gauche, nom et phrase à droite, séparés par une barre rose épaisse.', DIV + r'''
let h=box(100,180,330,300,`display:flex;align-items:center;justify-content:flex-end;font:700 230px/1 Lexend;color:${N3}`,NUM)
+box(452,240,6,180,`background:${PK};border-radius:3px`)
+box(484,236,400,20,`font:600 11px Lexend;letter-spacing:.2em;color:${GR}`,`${SEC} · ${IDX+1} / ${CNT}`)
+box(484,262,400,100,`font:700 40px/1.1 Lexend;color:${CR}`,ttl(NAME))
+box(484,350,380,80,`font:400 15px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['C'] = V('Barre de progression segmentée', 'Les 6 segments sur une barre en haut (celui-ci en rose plein, les autres en navy), nom et phrase centrés dessous.', DIV + r'''
const w=(760-(CNT-1)*8)/CNT;let h='';ALL.forEach((n,i)=>{const x=100+i*(w+8);h+=box(x,200,w,10,`border-radius:5px;background:${i<IDX?'#2E5568':i===IDX?PK:N3}`)
+box(x,218,w,34,`text-align:center;font:${i===IDX?700:500} 9.5px/1.3 Lexend;letter-spacing:.06em;color:${i===IDX?'#fff':GR}`,up(n))});
h+=box(100,170,760,18,`text-align:center;font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(100,300,760,80,`${flexc};font:700 50px/1.1 Lexend;color:${CR}`,up(NAME))
+box(220,392,520,70,`text-align:center;font:400 16px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['D'] = V('Page partagée', 'Moitié gauche en navy clair avec le chapitre et le numéro, moitié droite le nom et la phrase. Comme une page de livre.', DIV + r'''
let h=box(0,-40,400,712,`background:${N2}`)
+box(70,200,280,20,`font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(70,230,280,120,`font:700 96px/1 Lexend;color:${PK}`,NUM)
+box(70,350,280,20,`font:500 12px Lexend;color:${GR}`,`Segment ${IDX+1} of ${CNT}`)
+box(460,250,420,110,`font:700 42px/1.1 Lexend;color:${CR}`,ttl(NAME))
+box(460,370,400,90,`font:400 15px/1.55 Lexend;color:#fff`,DESC);
stageI(h)''')
I['E'] = V('Onglets de classeur', 'Les 6 segments en onglets au-dessus d’une grande fiche : l’onglet actif est relié à la fiche qui porte le nom et la phrase.', DIV + r'''
const w=(760-(CNT-1)*6)/CNT;let h='';ALL.forEach((n,i)=>{const x=100+i*(w+6),a=i===IDX;h+=box(x,a?186:196,w,a?52:40,`${flexc};border-radius:10px 10px 0 0;background:${a?N3:N2};font:${a?700:500} 9.5px/1.25 Lexend;letter-spacing:.05em;color:${a?'#fff':GR};padding:0 6px;${a?'border-top:4px solid '+PK:''}`,up(n))});
h+=box(100,236,760,300,`border-radius:0 0 16px 16px;background:${N3}`)
+box(140,276,680,20,`font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(140,306,680,100,`font:700 46px/1.1 Lexend;color:${CR}`,ttl(NAME))
+box(140,410,560,80,`font:400 16px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['F'] = V('Anneau de progression', 'Un anneau en 6 arcs à gauche (l’arc du segment en rose, « 2/6 » au centre), le nom et la phrase à droite.', DIV + r'''
const cx=260,cy=360,r=110;let s=`<svg style="position:absolute;left:0;top:0" width="960" height="672">`;
for(let i=0;i<CNT;i++){const a0=-Math.PI/2+i*2*Math.PI/CNT+.06,a1=-Math.PI/2+(i+1)*2*Math.PI/CNT-.06;s+=`<path d="M${cx+r*Math.cos(a0)} ${cy+r*Math.sin(a0)}A${r} ${r} 0 0 1 ${cx+r*Math.cos(a1)} ${cy+r*Math.sin(a1)}" fill="none" stroke="${i===IDX?PK:i<IDX?'#2E5568':N3}" stroke-width="22"/>`}
s+='</svg>';let h=s+box(cx-70,cy-40,140,80,`${flexc};font:700 40px/1 Lexend;color:#fff`,`${IDX+1}<span style="font:500 14px Lexend;color:${GR};margin-top:6px">of ${CNT}</span>`)
+box(440,250,420,20,`font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(440,278,420,100,`font:700 44px/1.1 Lexend;color:${CR}`,ttl(NAME))
+box(440,384,400,90,`font:400 16px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['G'] = V('Couverture éditoriale', 'Le nom en capitales énormes sur toute la largeur, une règle fine, puis la phrase en petit avec « Chapitre 2 / 6 ». Style magazine.', DIV + r'''
let h=box(70,170,820,20,`display:flex;justify-content:space-between;font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,`<span>${SEC}</span><span>${NUM} / ${String(CNT).padStart(2,'0')}</span>`)
+box(70,196,820,1,`background:${CR};opacity:.5`)
+box(70,220,820,220,`display:flex;align-items:center;font:700 ${NAME.length>16?70:84}px/0.98 Lexend;color:${CR};letter-spacing:-.01em`,up(NAME))
+box(70,460,820,6,`background:${PK};width:90px`)
+box(70,486,520,70,`font:400 16px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['H'] = V('Frise de pastilles', 'Les 6 segments en pastilles reliées par une ligne ; la pastille active est grande, rose, numérotée ; nom et phrase dessous.', DIV + r'''
const sp=760/(CNT-1||1);let h=box(100,234,760,3,`background:${LN}`);
ALL.forEach((n,i)=>{const x=100+i*sp,a=i===IDX,d=a?56:18;h+=box(x-d/2,235-d/2,d,d,`${flexc};border-radius:50%;background:${a?PK:i<IDX?'#2E5568':N3};${a?'box-shadow:0 0 0 6px '+N:''};font:700 18px Lexend;color:#fff`,a?String(IDX+1):'')
+box(x-60,a?270:252,120,32,`text-align:center;font:${a?700:500} 9.5px/1.3 Lexend;letter-spacing:.05em;color:${a?'#fff':GR}`,a?'':up(n))});
h+=box(100,180,760,18,`text-align:center;font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(100,320,760,80,`${flexc};font:700 48px/1.1 Lexend;color:${CR}`,up(NAME))
+box(220,410,520,70,`text-align:center;font:400 16px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')
I['I'] = V('Mosaïque des 6 segments', 'Les 6 segments en tuiles 3×2 ; la tuile du segment est pleine (navy clair, bord rose épais) et contient la phrase, les autres sont éteintes.', DIV + r'''
let h=box(100,170,760,18,`text-align:center;font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC);
const w=240,g=20,hh=150;ALL.forEach((n,i)=>{const c=i%3,r=Math.floor(i/3),x=100+c*(w+g),y=205+r*(hh+g),a=i===IDX;
h+=box(x,y,w,hh,`display:flex;flex-direction:column;justify-content:center;padding:18px;border-radius:12px;background:${a?N3:'transparent'};border:${a?'4px solid '+PK:'1.5px solid '+LN}`,
`<div style="font:600 10px Lexend;color:${a?PK:LN};letter-spacing:.1em">${String(i+1).padStart(2,'0')}</div><div style="font:700 ${a?17:13}px/1.2 Lexend;color:${a?'#fff':'#46616C'};margin-top:4px">${up(n)}</div>${a?`<div style="font:400 11.5px/1.45 Lexend;color:${CR};margin-top:8px">${DESC}</div>`:''}`)});
stageI(h)''')
I['J'] = V('Plan de métro', 'Une ligne verticale à gauche avec les 6 stations ; la station du segment est grosse et rose, son nom et sa phrase s’affichent à côté.', DIV + r'''
const y0=190,sp=360/(CNT-1||1);let h=box(160,y0,6,360,`background:${N3};border-radius:3px`);
ALL.forEach((n,i)=>{const y=y0+i*sp,a=i===IDX,d=a?34:16;h+=box(163-d/2,y-d/2,d,d,`border-radius:50%;background:${a?PK:N};border:${a?0:4}px solid ${i<IDX?'#2E5568':N3}`)
+box(200,y-9,260,18,`font:${a?700:500} 11px Lexend;letter-spacing:.06em;color:${a?'#fff':GR}`,up(n))});
const ya=y0+IDX*sp;h+=box(470,ya-60,1,120,`background:${LN}`)
+box(500,ya-70,380,20,`font:600 11px Lexend;letter-spacing:.22em;color:${GR}`,SEC)
+box(500,ya-46,380,60,`font:700 36px/1.1 Lexend;color:${CR}`,ttl(NAME))
+box(500,ya+20,360,70,`font:400 14px/1.5 Lexend;color:#fff`,DESC);
stageI(h)''')

# ================================================================= 3. Exceptional vs bad experience
X = dict(id='X', fam='Expérience client', title='« Maximum customer value » : expérience exceptionnelle vs mauvaise',
         shot=108, mine='F', keys=KEYS,
         scope=[108, 113, 117, 121, 125, 129],
         what="Deux paragraphes empilés dans des cadres, un 🤩 et un pouce à cheval sur le bord, un cadre rose fin, un « VS » perdu au milieu. On lit deux pavés, on ne voit pas la différence.",
         why="Le récit en étapes montre ce qui se passe vraiment pour le client, et l'échec se lit en face, étape par étape.")
X['A'] = V('Côte à côte', 'Deux colonnes : la mauvaise expérience à gauche (grise, croix), l’exceptionnelle à droite (navy clair, coche rose pleine), une flèche entre les deux.', EXP + r'''
let h=box(90,215,340,320,`border-radius:14px;border:1.5px dashed ${LN};padding:26px`,`<div style="display:flex;align-items:center;gap:10px;font:700 11px Lexend;letter-spacing:.16em;color:${GR}"><span style="display:inline-flex;width:30px;height:30px;border-radius:8px;background:${N3};align-items:center;justify-content:center">${crs(18,GR)}</span>BAD</div><div style="font:400 14px/1.6 Lexend;color:${GR};margin-top:20px">${BAD}</div>`)
+box(446,350,68,40,`${flexc};font:700 26px Lexend;color:${PK}`,'→')
+box(530,215,340,320,`border-radius:14px;background:${N3};padding:26px`,`<div style="display:flex;align-items:center;gap:10px;font:700 11px Lexend;letter-spacing:.16em;color:#fff"><span style="display:inline-flex;width:30px;height:30px;border-radius:8px;background:${PK};align-items:center;justify-content:center">${chk(18)}</span>EXCEPTIONAL</div><div style="font:400 14px/1.6 Lexend;color:#fff;margin-top:20px">${GOOD}</div>`);
stage(h,keep)''')
X['B'] = V('Curseur de satisfaction', 'Une règle de « Bad » à « Exceptional » ; chaque histoire est épinglée à son bout de la règle.', EXP + r'''
let h=box(110,300,740,10,`border-radius:5px;background:linear-gradient(90deg,${N3},#2E5568 55%,${PK})`)
+box(104,294,22,22,`border-radius:50%;background:${N};border:4px solid ${GR}`)+box(834,290,30,30,`border-radius:50%;background:${PK};box-shadow:0 0 0 5px ${N}`)
+box(100,262,200,20,`font:700 11px Lexend;letter-spacing:.16em;color:${GR}`,'BAD')+box(660,262,200,20,`text-align:right;font:700 11px Lexend;letter-spacing:.16em;color:#fff`,'EXCEPTIONAL')
+box(100,322,2,40,`background:${LN}`)+box(857,328,3,34,`background:${PK}`)
+box(100,362,360,180,`border-radius:12px;border:1.5px dashed ${LN};padding:20px;font:400 13px/1.55 Lexend;color:${GR}`,BAD)
+box(500,362,360,180,`border-radius:12px;background:${N3};padding:20px;font:400 13px/1.55 Lexend;color:#fff`,GOOD);
stage(h,keep)''')
X['C'] = V('Conversation', 'Les deux histoires en bulles de discussion : la mauvaise à gauche en gris, l’exceptionnelle à droite en navy clair, avec leurs avatars.', EXP + r'''
let h=box(110,215,46,46,`${flexc};border-radius:50%;background:${N3}`,crs(22,GR))
+box(170,215,470,140,`border-radius:4px 18px 18px 18px;background:#0E3448;padding:20px 22px;font:400 13.5px/1.55 Lexend;color:${GR}`,`<div style="font:700 10px Lexend;letter-spacing:.16em;margin-bottom:8px">BAD EXPERIENCE</div>${BAD}`)
+box(804,388,46,46,`${flexc};border-radius:50%;background:${PK}`,chk(22))
+box(320,388,470,150,`border-radius:18px 4px 18px 18px;background:${N3};padding:20px 22px;font:400 13.5px/1.55 Lexend;color:#fff`,`<div style="font:700 10px Lexend;letter-spacing:.16em;margin-bottom:8px;color:${CR}">EXCEPTIONAL EXPERIENCE</div>${GOOD}`);
stage(h,keep)''')
X['D'] = V('Écran coupé en deux', 'La zone de contenu coupée en deux panneaux pleine hauteur : gauche sombre (bad), droite claire (exceptional), grands titres.', EXP + r'''
let h=box(60,200,420,370,`background:#04202E;border-radius:16px 0 0 16px;padding:34px`,`<div style="font:700 30px Lexend;color:${LN}">Bad</div><div style="width:40px;height:4px;background:${LN};margin:14px 0 20px"></div><div style="font:400 15px/1.6 Lexend;color:${GR}">${BAD}</div>`)
+box(480,200,420,370,`background:${N3};border-radius:0 16px 16px 0;padding:34px`,`<div style="font:700 30px Lexend;color:#fff">Exceptional</div><div style="width:40px;height:4px;background:${PK};margin:14px 0 20px"></div><div style="font:400 15px/1.6 Lexend;color:#fff">${GOOD}</div>`);
stage(h,keep)''')
X['E'] = V('Avis notés', 'Chaque histoire présentée comme un avis client : 5 étoiles roses pleines pour l’exceptionnelle, 1 étoile pour la mauvaise.', EXP + r'''
const star=(c)=>`<svg width="20" height="20" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.2 6.6.7-5 4.5 1.4 6.6L12 17.3 6.1 20.5l1.4-6.6-5-4.5 6.6-.7z" fill="${c}"/></svg>`;
const card=(y,good)=>box(130,y,700,150,`border-radius:14px;${good?'background:'+N3:'border:1.5px solid '+LN};padding:20px 26px;display:flex;gap:26px`,
`<div style="flex:none;width:130px"><div style="display:flex;gap:3px">${[0,1,2,3,4].map(i=>star(good?PK:(i<1?GR:N3))).join('')}</div><div style="font:700 10.5px Lexend;letter-spacing:.14em;color:${good?'#fff':GR};margin-top:10px">${good?'EXCEPTIONAL':'BAD'}</div></div><div style="font:400 14px/1.55 Lexend;color:${good?'#fff':GR}">${good?GOOD:BAD}</div>`);
stage(card(215,1)+card(390,0),keep)''')
X['F'] = V('Récit en étapes', 'L’histoire exceptionnelle découpée en 3 étapes numérotées sur une ligne rose épaisse ; l’échec en face, étape par étape, en gris.', EXP + r'''
const n=Math.min(3,G.length),w=(760-(n-1)*20)/n;let h=box(100,200,300,18,`font:700 10.5px Lexend;letter-spacing:.16em;color:#fff`,'EXCEPTIONAL')+box(100,386,300,18,`font:700 10.5px Lexend;letter-spacing:.16em;color:${GR}`,'BAD');
const g3=[G[0],G[1],G.slice(2).join(' ')].slice(0,n), b3=[B[0],B[1],B.slice(2).join(' ')].filter(Boolean);
h+=box(100,240,760,6,`background:${PK};border-radius:3px`)+box(100,426,760,3,`background:repeating-linear-gradient(90deg,${LN} 0 10px,transparent 10px 18px)`);
g3.forEach((s,i)=>{const x=100+i*(w+20);h+=box(x,228,30,30,`${flexc};border-radius:50%;background:${PK};font:700 13px Lexend;color:#fff;box-shadow:0 0 0 5px ${N}`,String(i+1))+box(x,268,w,100,`font:400 13px/1.5 Lexend;color:#fff`,s)});
b3.forEach((s,i)=>{const x=100+i*(w+20);h+=box(x,416,22,22,`${flexc};border-radius:50%;background:${N};border:2px solid ${LN}`,crs(12,GR))+box(x,450,w,100,`font:400 12.5px/1.5 Lexend;color:${GR}`,s)});
stage(h,keep)''')
X['G'] = V('Citation magazine', 'L’expérience exceptionnelle en grande citation avec guillemets géants ; la mauvaise en petit dessous, introduite par « Instead of ».', EXP + r'''
let h=box(100,180,120,120,`font:700 150px/1 Georgia,serif;color:${PK}`,'“')
+box(190,220,640,190,`display:flex;align-items:center;font:500 21px/1.45 Lexend;color:#fff`,GOOD)
+box(190,430,90,4,`background:${PK}`)
+box(190,452,640,110,`font:400 13px/1.55 Lexend;color:${GR}`,`<b style="color:${CR};letter-spacing:.14em;font-size:10.5px">INSTEAD OF</b><br>${BAD}`);
stage(h,keep)''')
X['H'] = V('La conséquence en titre', 'Pour chaque histoire, la dernière phrase (ce qui arrive au client) en gros titre, le contexte en petit dessous.', EXP + r'''
const blk=(y,good)=>{const S=good?G:B,last=S[S.length-1],ctx=S.slice(0,-1).join(' ');return box(110,y,740,165,`border-left:6px solid ${good?PK:LN};padding:6px 0 6px 28px`,
`<div style="font:700 10.5px Lexend;letter-spacing:.16em;color:${good?CR:GR}">${good?'EXCEPTIONAL · OUTCOME':'BAD · OUTCOME'}</div><div style="font:700 22px/1.3 Lexend;color:${good?'#fff':GR};margin-top:8px">${last}</div><div style="font:400 12.5px/1.5 Lexend;color:${GR};margin-top:10px">${ctx}</div>`)};
stage(blk(210,1)+blk(400,0),keep)''')
X['I'] = V('Deux cercles', 'L’exceptionnelle dans un grand disque navy clair cerclé de rose épais, la mauvaise dans un petit cercle pointillé gris : la taille dit l’écart.', EXP + r'''
let h=box(450,186,390,390,`${flexc};border-radius:50%;background:${N3};border:8px solid ${PK};padding:58px`,`<div style="font:700 11px Lexend;letter-spacing:.16em;color:${CR};margin-bottom:12px">EXCEPTIONAL</div><div style="font:400 14px/1.55 Lexend;color:#fff">${GOOD}</div>`)
+box(110,256,290,290,`${flexc};border-radius:50%;border:2px dashed ${LN};padding:44px`,`<div style="font:700 10.5px Lexend;letter-spacing:.16em;color:${GR};margin-bottom:10px">BAD</div><div style="font:400 12px/1.5 Lexend;color:${GR}">${BAD}</div>`);
stage(h,keep)''')
X['J'] = V('Chemin qui bifurque', 'Un point de départ commun (« Same need »), puis deux branches : la rose épaisse monte vers l’expérience exceptionnelle, la grise pointillée descend vers l’échec.', EXP + r'''
let h=`<svg style="position:absolute;left:0;top:0" width="960" height="672"><path d="M190 390 C 280 390, 290 290, 380 290" fill="none" stroke="${PK}" stroke-width="6" stroke-linecap="round"/><path d="M190 390 C 280 390, 290 490, 380 490" fill="none" stroke="${LN}" stroke-width="3" stroke-dasharray="8 7"/></svg>`;
h+=box(80,350,120,80,`${flexc};border-radius:14px;background:${N3};font:700 11px/1.3 Lexend;color:#fff;letter-spacing:.1em`,'SAME<br>NEED')
+box(380,215,480,150,`border-radius:14px;background:${N3};padding:20px 24px;border-left:6px solid ${PK}`,`<div style="font:700 10.5px Lexend;letter-spacing:.16em;color:${CR}">EXCEPTIONAL</div><div style="font:400 13.5px/1.55 Lexend;color:#fff;margin-top:8px">${GOOD}</div>`)
+box(380,425,480,140,`border-radius:14px;border:1.5px dashed ${LN};padding:20px 24px`,`<div style="font:700 10.5px Lexend;letter-spacing:.16em;color:${GR}">BAD</div><div style="font:400 13px/1.55 Lexend;color:${GR};margin-top:8px">${BAD}</div>`);
stage(h,keep)''')

ITEMS = [W, I, X]
