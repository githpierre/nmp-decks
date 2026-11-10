"""Atelier 100, 2e tour (Pierre, 10 Nov 2026 23h) : seulement les points qu'il a demandé de remontrer, avec de vrais designs différents.
Règle : jamais de trait ou texte rose fin sur le bleu nuit ; rose = aplat ou gras épais."""
ITEMS = []
def V(name, desc, js='', css=''): return dict(name=name, desc=desc, js=js, css=css)
def I(id, title, what, scope, shot, A, B, C, mine, why, clip=None, fam=''):
    ITEMS.append(dict(id=id, title=title, what=what, scope=scope, shot=shot, A=A, B=B, C=C, mine=mine, why=why, clip=clip, fam=fam))

# ---------- Prix (slide 13) ----------
PRICE = r"const T=A.texts(sl).filter(t=>/💰/.test(t.text));"
I('1', "Prix : niveau de prix sans sacs d'argent", "Tu as trouvé les $$$, la jauge vide et les pièces au trait moches : il fallait un vrai dessin.", [13], 13,
  V('Barres de niveau (comme le réseau)', "Trois barres pleines de hauteur croissante ; 1, 2 ou 3 sont roses, les autres ardoise. Ça se lit comme un niveau, sans symbole américain.",
    PRICE + r"T.forEach(t=>{const n=[...t.text].filter(c=>c==='💰').length;t.el.innerHTML=`<div style='display:flex;align-items:flex-end;justify-content:center;gap:5px;height:30px'>${[1,2,3].map(i=>`<span style='width:12px;height:${8+i*7}px;border-radius:3px;background:${i<=n?C.pink:'#2A4A58'}'></span>`).join('')}</div>`})"),
  V('Pile de pièces pleines', "Une petite pile de pièces dessinée en SVG plein (crème et rose), 1, 2 ou 3 pièces de haut.",
    PRICE + r"T.forEach(t=>{const n=[...t.text].filter(c=>c==='💰').length;let g='';for(let i=0;i<n;i++){const y=30-i*8;g+=`<ellipse cx='20' cy='${y+4}' rx='14' ry='5' fill='#B8325F'/><rect x='6' y='${y-2}' width='28' height='6' fill='${C.pink}'/><ellipse cx='20' cy='${y-2}' rx='14' ry='5' fill='#FF4D8D'/>`}t.el.innerHTML=`<div style='display:flex;justify-content:center'><svg width='40' height='40' viewBox='0 0 40 40'>${g}</svg></div>`})"),
  V('Étiquette de gamme', "Une étiquette rose pleine en gras : ENTRY, MID, PREMIUM. Le niveau est dit en un mot, lisible de loin.",
    PRICE + r"T.forEach(t=>{const n=[...t.text].filter(c=>c==='💰').length;t.el.innerHTML=`<div style='display:flex;justify-content:center;padding-top:6px'><span style='background:${n==3?C.pink:n==2?'#B8325F':'#6B2A4A'};color:#fff;font:700 8pt Lexend;letter-spacing:.14em;padding:5px 12px;border-radius:12px'>${['ENTRY','MID-RANGE','PREMIUM'][n-1]}</span></div>`})"),
  'A', "Les barres de niveau sont un code universel (réseau, batterie) ; ni dollars ni emoji.", clip=[130, 230, 700, 280], fam='Icônes')

# ---------- Pastilles dans les cartes : 3 placements ----------
for (iid, n, title, extra) in [('4', 22, "Ce qui est rare : pastilles (4 lignes)", ''), ('5', 31, "Pourquoi ça excite : pastilles", ''),
                               ('6', 136, "Ce qui freine : pastilles", ''), ('7', 186, "Moonshots : pastilles", ''),
                               ('8', 207, "Comment les leaders ont percé : pastilles", ''), ('11', 172, "Types de startups : pastilles", ''),
                               ('12', 142, "Scénarios catastrophe : pastilles", '')]:
    I(iid, title, "Tu aimes l'icône dans une pastille, mais le texte restait centré seul et la pastille l'écrasait en haut.", [n], n,
      V('Pastille + texte centrés ensemble', "La pastille et le texte forment un seul bloc, centré verticalement dans la carte.", r"A.cardPill(sl,'flow',{d:34,ic:18})"),
      V('Pastille posée sur le bord haut', "La pastille est posée à cheval sur le bord haut de la carte, le texte est centré dans toute la carte.", r"A.cardPill(sl,'top',{d:36,ic:18,bg:'#062A3C'})"),
      V('Pastille sur le coin', "La pastille est posée à cheval sur le coin haut gauche, le texte est centré dans la carte.", r"A.cardPill(sl,'corner',{d:34,ic:17,bg:'#062A3C'})"),
      'B', "Sur le bord, la pastille ne prend plus de place dans la carte : le texte respire et toutes les cartes restent alignées.", fam='Pastilles')

# ---------- Qui paie (carré rose + icône blanche plus grasse) ----------
SQ = "A.shapes(sl).filter(s=>s.stroke&&s.stroke.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>s.p.setAttribute('fill',C.pink));"
I('13', "Qui paie : carré rose plein, icône blanche plus grasse", "Tu as aimé le carré rose plein ; on teste des icônes plus épaisses.", [63, 67, 71, 75, 79, 83], 63,
  V('Trait épais', "Icône au trait blanc, trait 2,6 px.", SQ + r"A.swap(sl,{style:'line',color:'#fff',size:16,sw:2.6})"),
  V('Icône pleine', "Icône pleine blanche (Phosphor fill), plus graphique.", SQ + r"A.swap(sl,{style:'fill',color:'#fff',size:17})"),
  V('Icône pleine, carré arrondi plus grand', "Icône pleine blanche, carré rose aux coins arrondis un peu plus grand.", r"A.shapes(sl).filter(s=>s.stroke&&s.stroke.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>{A.hide([s]);const d=A.div(sl,s.cx-21,s.cy-21,42,42,'border-radius:10px;background:#FB0161;box-shadow:0 2px 6px rgba(0,0,0,.35)');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)});A.swap(sl,{style:'fill',color:'#fff',size:20})"),
  'B', "L'icône pleine se lit mieux sur le rose plein qu'un trait, même épais.", clip=[60, 290, 840, 300], fam='Pastilles')

# ---------- Bonne / mauvaise expérience ----------
EXP = r"const e=A.emojis(sl)[0];const im=A.imgs(sl).find(i=>i.y>300);"
def exp(top, bot):
    return EXP + r"if(e){const p=e.closest('p');p.style.textAlign='center';p.style.display='flex';p.style.justifyContent='center';e.outerHTML=`" + top + r"`;}if(im){im.el.style.visibility='hidden';A.div(sl,im.x,im.y,im.w,im.h,'display:flex;align-items:center;justify-content:center',`" + bot + r"`)}"
I('18', "Bonne / mauvaise expérience : pastilles", "La coche partait à droite, le pouce et la croix étaient moches.", [108, 113, 117, 121, 125, 129], 108,
  V('Coche rose / croix ardoise, bien centrées', "Rond rose plein avec coche blanche épaisse en haut, rond ardoise avec croix en bas, tous deux centrés sur le bord de leur cadre.",
    exp(r"<span style='display:inline-flex;width:34px;height:34px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center'>${A.svg('✓','line',20,'#fff',3.2)}</span>",
        r"<span style='display:inline-flex;width:30px;height:30px;border-radius:50%;background:#33525F;align-items:center;justify-content:center'>${A.svg('❌','line',26,'#DDE5E8',2.4).replace(/<circle[^>]*>/,'')}</span>")),
  V('Visages pleins', "Visage souriant plein blanc dans un rond rose, visage triste plein dans un rond ardoise : on garde l'émotion des emojis, dans la charte.",
    exp(r"<span style='display:inline-flex;width:34px;height:34px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center'>${A.svg('🤩','fill',24,'#fff')}</span>",
        r"<span style='display:inline-flex;width:30px;height:30px;border-radius:50%;background:#33525F;align-items:center;justify-content:center'>${A.svg('😣','fill',22,'#C9D4D8')}</span>")),
  V('Étiquettes pleines', "« GOOD » en étiquette rose pleine et « BAD » en étiquette ardoise, posées sur le bord gauche du cadre.",
    exp(r"<span style='display:inline-flex;background:${C.pink};color:#fff;font:700 8pt Lexend;letter-spacing:.12em;padding:6px 10px;border-radius:12px'>GOOD</span>",
        r"<span style='display:inline-flex;background:#33525F;color:#DDE5E8;font:700 8pt Lexend;letter-spacing:.12em;padding:6px 10px;border-radius:12px'>BAD</span>")),
  'A', "Coche et croix pleines disent bien / mal sans ambiguïté et restent nettes en petit.", clip=[100, 220, 760, 380], fam='Pastilles')

# ---------- Intercalaires de segment ----------
SEG = r"A.hide(A.shapes(sl).filter(s=>s.dash));const lab=A.texts(sl).find(t=>/^(PAIN POINTS|VALUE CREATION)$/.test(t.text));const all=[...document.querySelectorAll('.slide')].filter(x=>x.querySelector('.raw')&&[...x.querySelectorAll('.rx-t')].some(t=>lab&&t.textContent.trim()===lab.text)&&x.querySelectorAll('.raw svg.rx-s').length<=6&&!x.querySelector('.title'));const idx=all.indexOf(sl),N=all.length;const ti=A.texts(sl).filter(t=>t!==lab&&t.y>150&&t.y<480).sort((a,b)=>a.y-b.y);"
I('21', "Intercalaires de segment : vrais designs", "Les flèches pointillées vers le centre faisaient décor ; mes premières variantes n'étaient pas inspirées.", [62, 66, 70, 74, 78, 82, 106, 110, 115, 119, 123, 127], 62,
  V('Grand numéro en filigrane', "Un très grand numéro de segment (01, 02…) en bleu à peine plus clair derrière le titre, et une barre de progression des segments en bas.",
    SEG + r"const d=A.div(sl,0,150,960,330,'display:flex;align-items:center;justify-content:center;font:700 260pt Lexend;color:#0A3348;line-height:1;letter-spacing:-8px',String(idx+1).padStart(2,'0'));const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);A.div(sl,480-N*21,500,N*42,6,'display:flex;gap:6px',Array.from({length:N},(_,i)=>`<i style='flex:1;border-radius:3px;background:${i==idx?C.pink:'#1E4558'}'></i>`).join(''))"),
  V('Bandeau rose à gauche', "Une bande rose pleine sur toute la hauteur à gauche, titre aligné à gauche à côté, numéro du segment en gras.",
    SEG + r"A.div(sl,0,0,14,672,'background:#FB0161');ti.forEach(t=>{t.el.style.left='90px';t.el.style.width='620px';t.el.querySelectorAll('p').forEach(p=>p.style.textAlign='left')});if(lab){lab.el.style.left='90px';lab.el.style.width='620px';lab.el.querySelectorAll('p').forEach(p=>p.style.textAlign='left')}A.div(sl,90,ti.length?ti[0].y-70:200,200,40,'font:700 26pt Lexend;color:#FB0161',`${String(idx+1).padStart(2,'0')}<span style=\"font-size:12pt;color:#7E949E\"> / ${String(N).padStart(2,'0')}</span>`)"),
  V('Carte centrale', "Le titre et la phrase passent dans une grande carte bleu clair centrée ; l'étiquette PAIN POINTS devient une pastille rose pleine posée sur le bord haut.",
    SEG + r"if(ti.length){const y0=Math.min(...ti.map(t=>t.y))-36,y1=Math.max(...ti.map(t=>t.y+t.h))+30;const d=A.div(sl,170,y0,620,y1-y0,'background:#0B3850;border-radius:16px;box-shadow:0 8px 24px rgba(0,0,0,.3)');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);if(lab){lab.el.style.visibility='hidden';A.div(sl,480-70,y0-13,140,26,'background:#FB0161;border-radius:13px;color:#fff;font:700 8pt Lexend;letter-spacing:.22em;display:flex;align-items:center;justify-content:center',lab.text)}}"),
  'A', "Le numéro en filigrane donne de la profondeur et dit où on en est, sans rien ajouter de criard.", fam='Intercalaires')

# ---------- Comparaison de marchés ----------
I('28', "Comparaison de marchés : barres crème, plus soignées", "Tu as aimé les barres crème transparentes (C) ; on peut les rendre plus jolies.", [46], 46,
  V('Barres arrondies, chiffre au bout', "Barres crème à 25 % arrondies, montant en clair au bout ; EdTech crème plein avec son montant en pastille rose.", css="S .cmp .bw:not(.hl) .bar{background:rgba(231,205,168,.25);border:none;border-radius:0 6px 6px 0}S .cmp .bw:not(.hl) .tag{border:none;color:#C9D4D8}S .cmp .hl .bar{border-radius:0 8px 8px 0}S .cmp .hl .tag{border-radius:15px}S .cmp .ax{border-left:1px solid #1E4558}S .cmp .ax::after{display:none}"),
  V('Grille de fond', "Mêmes barres, plus une grille verticale très discrète tous les 100 B$ pour lire l'échelle.", js=r"const c=sl.querySelector('.cmp');for(let i=1;i<=3;i++)c.insertAdjacentHTML('afterbegin',`<i style='position:absolute;top:-14px;bottom:-14px;left:${200+i*130}px;border-left:1px solid #123F57;z-index:0'></i>`)", css="S .cmp .bw,S .cmp .n{position:relative;z-index:1}S .cmp .bw:not(.hl) .bar{background:#3A4E57!important;background:rgba(231,205,168,.25);border:none;border-radius:0 6px 6px 0}S .cmp .bw:not(.hl) .tag{border:none;color:#C9D4D8}S .cmp .hl .bar{border-radius:0 8px 8px 0}S .cmp .hl .tag{border-radius:15px}S .cmp .ax{display:none}"),
  V('Rangée EdTech surlignée', "Barres arrondies ; la rangée EdTech a un fond bleu clair sur toute la largeur.", js=r"const h=sl.querySelector('.cmp .bw.hl');const n=h.previousElementSibling;[n,h].forEach(e=>{e.style.background='#0B3850';e.style.padding='8px 0'});n.style.borderRadius='10px 0 0 10px';n.style.paddingLeft='14px';h.style.borderRadius='0 10px 10px 0'", css="S .cmp .bw:not(.hl) .bar{background:rgba(231,205,168,.25);border:none;border-radius:0 6px 6px 0}S .cmp .bw:not(.hl) .tag{border:none;color:#C9D4D8}S .cmp .hl .bar{border-radius:0 8px 8px 0}S .cmp .hl .tag{border-radius:15px}S .cmp .ax{display:none}"),
  'B', "La grille donne l'échelle sans alourdir, et les barres arrondies font plus fini.", clip=[60, 140, 840, 380], fam='Graphiques')

# ---------- Why it matters ----------
WHY = r"const lab=A.texts(sl).find(t=>/^(WHY|WHAT|THE STORY)/.test(t.text));const big=A.texts(sl).find(t=>lab&&Math.abs(t.x-lab.x)<6&&t.y<lab.y&&t.y>lab.y-90);const body=A.texts(sl).filter(t=>lab&&Math.abs(t.x-lab.x)<6&&t.y>lab.y);A.hide(A.shapes(sl).filter(s=>s.dash&&s.h>200));"
I('56', "Encadré « Why it matters » : mieux", "Le libellé rose fin était moche ; il faut une vraie mise en forme de l'explication.", [112, 135, 137, 139, 163, 179, 180, 181, 197, 202], 112,
  V('Chiffre géant blanc', "Le chiffre clé passe en très grand blanc, le libellé en petites capitales crème dessous, le séparateur pointillé disparaît.",
    WHY + r"if(big)big.el.querySelectorAll('span').forEach(s=>{s.style.fontSize='46pt';s.style.color='#fff'});if(big)big.el.style.top=(big.y-30)+'px';if(lab)lab.el.querySelectorAll('span').forEach(s=>s.style.color=C.cream)"),
  V('Chiffre en pastille rose pleine', "Le chiffre clé dans une grande pastille rose pleine (texte blanc gras), puis le libellé et le texte.",
    WHY + r"if(big)big.el.querySelectorAll('span').forEach(s=>s.style.cssText+=';background:#FB0161;color:#fff;padding:2px 14px;border-radius:10px')"),
  V('Carte avec barre rose épaisse', "Libellé, chiffre et texte dans une carte bleu clair, avec une barre rose pleine de 6 px en haut.",
    WHY + r"if(lab&&body.length){const ys=[big||lab,...body].map(t=>t.y),ye=Math.max(...body.map(t=>t.y+t.h));const x=lab.x-20,y=Math.min(...ys)-18;const d=A.div(sl,x,y,250,ye-y+16,'background:#0B3850;border-radius:10px;overflow:hidden');d.innerHTML='<i style=\"display:block;height:6px;background:#FB0161\"></i>';const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)}"),
  'C', "La carte regroupe l'explication en un bloc lisible ; la barre épaisse rappelle la barre rose du graphique.", fam='Graphiques')

# ---------- Classement des couches ----------
RK = r"const bx=A.shapes(sl).filter(s=>s.w>200&&s.h<40).sort((a,b)=>a.y-b.y);A.hide(A.shapes(sl).filter(s=>s.stroke==='#789096'));"
I('66', "Classement des couches : top 3 rose plein, en mieux", "Tu prends le top 3 en rose plein ; on peut le soigner.", [89], 89,
  V('Top 3 rose, reste ardoise, sans flèches', "Top 3 rose plein texte blanc, les 5 autres en aplat ardoise ; les petites flèches grises disparaissent.",
    RK + r"bx.forEach((s,i)=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill',i<3?C.pink:'#1E4558');s.el.style.borderRadius='6px'});A.texts(sl).filter(t=>t.w>200&&t.w<250).forEach(t=>A.color(t,'#fff'))"),
  V('Rang dans un rond + barres', "Rangs 1-3 dans des ronds roses pleins ; barres arrondies rose / ardoise ; description en blanc pour le top 3.",
    RK + r"bx.forEach((s,i)=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill',i<3?C.pink:'#1E4558')});A.texts(sl).filter(t=>t.w>200&&t.w<250).forEach(t=>A.color(t,'#fff'));A.texts(sl).filter(t=>/^[1-8]$/.test(t.text)).forEach(t=>{const n=+t.text;t.el.querySelector('p').innerHTML=`<span style='display:inline-flex;width:26px;height:26px;border-radius:50%;align-items:center;justify-content:center;font:700 11pt Lexend;${n<=3?'background:#FB0161;color:#fff':'background:#123F57;color:#9FB0B7'}'>${n}</span>`});A.texts(sl).filter(t=>t.w>400).slice(0,3).forEach(t=>A.color(t,'#fff'))"),
  V('Lignes entières en bandes', "Chaque couche devient une bande pleine qui va jusqu'au texte : rose pour le top 3, ardoise ensuite.",
    RK + r"bx.forEach((s,i)=>{A.hide([s]);const d=A.div(sl,s.x,s.y,760,s.h,`background:${i<3?'rgba(251,1,97,.18)':'#0A3044'};border-radius:6px;border-left:6px solid ${i<3?C.pink:'#33525F'}`);const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)})"),
  'B', "Les ronds roses donnent le rang d'un coup d'œil et le top 3 ressort sans cadre.", fam='Graphiques')

# ---------- Avant / après Preply ----------
I('33', "Avant / après d'une startup : vraies alternatives", "Tes retours : tout était moche. Voici trois mises en page différentes.", [210, 211, 212, 213, 214], 210,
  V('Colonne startup en carte', "La colonne de droite devient une seule grande carte bleu clair (sans cadres par ligne) ; la colonne de gauche est atténuée, sans cadres.", css="S .contrast .a{border:none;box-shadow:none;color:#6E8590;background:none}S .contrast .b{border:none;box-shadow:none;background:#0B3850;border-radius:0}S .contrast{row-gap:0}S .contrast .a,S .contrast .b{padding:8px 10px}S .contrast .hd:last-child{background:#0B3850;border-radius:10px 10px 0 0;padding:8px 0;margin:0}"),
  V('Lignes séparées par des filets', "Ni cadres ni flèches : deux colonnes de texte, un filet fin sous chaque ligne, logo au milieu.", css="S .contrast .a,S .contrast .b{border:none;box-shadow:none;border-bottom:1px solid #1E4558;border-radius:0}S .contrast .b{color:#fff;font-weight:600}S .contrast .mid i{display:none}"),
  V('Pastille rose pleine à droite', "Chaque ligne de droite commence par une petite pastille rose pleine ; plus de cadres roses.", css="S .contrast .a,S .contrast .b{border:none;box-shadow:none}S .contrast .b{position:relative;padding-left:22px;color:#fff}S .contrast .b::before{content:'';position:absolute;left:6px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;background:#FB0161}S .contrast .a{color:#7E949E}"),
  'A', "La carte fait de la colonne startup un seul bloc « gagnant », sans dix rectangles.", clip=[40, 150, 880, 420], fam='Tableaux')

# ---------- Conflits ----------
CF = r"const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill==='#789096'||(s.fill&&s.fill.toUpperCase()==='#FB0161')));const ar=sh.filter(s=>s.fill==='#789096');"
I('40', "Conflits : bien placé cette fois", "La pastille VS était mal posée ; il faut un séparateur net entre les deux positions.", [140], 140,
  V('Pastille VS rose pleine', "Une pastille rose pleine « VS » en blanc gras, centrée pile entre les deux cartes.",
    CF + r"ar.forEach(s=>A.div(sl,s.cx-20,s.cy-14,40,28,'border-radius:14px;background:#FB0161;color:#fff;font:700 9pt Lexend;display:flex;align-items:center;justify-content:center;z-index:3','VS'))"),
  V('Éclair dans un rond rose', "Un rond rose plein avec un éclair blanc plein, centré entre les deux cartes.",
    CF + r"ar.forEach(s=>A.div(sl,s.cx-17,s.cy-17,34,34,'border-radius:50%;background:#FB0161;display:flex;align-items:center;justify-content:center;z-index:3',A.svg('💥','fill',20,'#fff')))"),
  V('Cartes jointes', "Les deux cartes se touchent en une seule paire ; la séparation est une barre rose pleine verticale avec VS.",
    CF + r"ar.forEach(s=>A.div(sl,s.cx-3,s.cy-30,6,60,'border-radius:3px;background:#FB0161;z-index:3'));ar.forEach(s=>A.div(sl,s.cx-15,s.cy-10,30,20,'border-radius:10px;background:#062A3C;color:#fff;font:700 8pt Lexend;display:flex;align-items:center;justify-content:center;z-index:4;border:2px solid #FB0161','VS'))"),
  'A', "« VS » est exactement la question de la slide ; en pastille pleine il se voit sans écraser les textes.", clip=[100, 190, 760, 380], fam='Cartes')

# ---------- Leaders (étoiles) ----------
ST = r"const st=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30);A.hide(st);const seg=A.shapes(sl).filter(s=>s.w>120&&s.w<150);"
I('55', "Leaders par segment : sans étoiles", "Les étoiles roses en coin ne servaient à rien ; propose mieux.", [178], 178,
  V('Segment en aplat rose', "La case du segment devient rose pleine (texte blanc gras), la case des leaders reste sobre.",
    ST + r"seg.forEach(s=>{s.p.setAttribute('fill',C.pink);s.p.setAttribute('stroke','none')});A.texts(sl).filter(t=>t.w<140&&t.w>120).forEach(t=>A.color(t,'#fff'))"),
  V('Couronne pleine en pastille', "Une couronne pleine blanche dans un rond rose posé sur le coin de la case segment.",
    ST + r"st.forEach(s=>A.div(sl,s.cx-13,s.cy-13,26,26,'border-radius:50%;background:#FB0161;display:flex;align-items:center;justify-content:center;z-index:3',`<svg width='14' height='14' viewBox='0 0 24 24' fill='#fff'><path d='M2 6l4.5 10h11L22 6l-5.5 4L12 3 7.5 10z'/><rect x='5' y='18' width='14' height='3' rx='1'/></svg>`))"),
  V('Cartes pleines liées', "Case segment et case leaders en aplats bleu clair, reliées par une petite barre rose pleine.",
    ST + r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>120).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.shapes(sl).filter(s=>s.w>40&&s.w<60&&s.h<24).forEach(s=>{A.hide([s]);A.div(sl,s.x+4,s.cy-2,s.w-8,4,'background:#FB0161;border-radius:2px')})"),
  'A', "Le segment en rose plein structure la grille : on lit « segment → leader » sans icône.", fam='Cartes')

# ---------- Six chiffres du financement ----------
SIX = r"const bx=A.shapes(sl).filter(s=>s.stroke==='#D0E1E5');bx.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});const hl=t=>t.el.querySelectorAll('span').forEach(s=>{s.innerHTML=s.innerHTML.replace(/(\$?\d[\d,.]*\s?(%|M|B|\$M|\$B)?(\s(to|of)\s\$?\d[\d,.]*(M|B)?)?)/,'<b style=\"display:block;font:700 20pt Lexend;color:#fff;margin-bottom:4px\">$1</b>')});"
I('59', "Six chiffres du financement : plus de relief", "Les cadres clairs étaient moches ; l'aplat seul est un peu plat.", [160], 160,
  V('Chiffre clé en grand', "Aplat sans bord ; le premier chiffre de chaque case sort en grand blanc gras au-dessus de la phrase.",
    SIX + r"A.texts(sl).filter(t=>t.w>150&&t.w<220).forEach(hl)"),
  V('Chiffre clé + barre rose épaisse', "Même chose, avec une barre rose pleine de 5 px en haut de chaque case.",
    SIX + r"A.texts(sl).filter(t=>t.w>150&&t.w<220).forEach(hl);bx.forEach(s=>A.div(sl,s.x,s.y,s.w,5,'background:#FB0161;border-radius:3px 3px 0 0'))"),
  V('Une case vedette', "Chiffres en grand ; la première case (la plus importante) en rose plein, les autres en aplat.",
    SIX + r"A.texts(sl).filter(t=>t.w>150&&t.w<220).forEach(hl);const f=bx.sort((a,b)=>(a.y-b.y)||(a.x-b.x))[0];f.p.setAttribute('fill',C.pink)"),
  'A', "Le chiffre en grand donne à chaque case un point d'entrée ; la phrase complète reste dessous.", fam='Cartes')

# ---------- Chaîne de valeur ----------
CH = r"const b=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<20).sort((a,b)=>a.x-b.x);A.hide(b);const tt=A.texts(sl).filter(t=>t.h<40&&t.y<320&&t.y>250).sort((a,b)=>a.x-b.x);"
I('64', "Chaîne de valeur : vraies alternatives", "Les bandes roses écrasaient les leaders ; il faut un vrai schéma de chaîne.", [182, 185], 182,
  V('Chevrons pleins avec le titre dedans', "Les titres passent dans des chevrons pleins, du bleu ardoise vers le rose : on lit la chaîne de gauche à droite.",
    CH + r"b.forEach((s,i)=>{const c=['#1E4558','#33525F','#6B2A4A','#B8325F','#FB0161'][i]||C.pink;A.div(sl,s.x,s.y-24,s.w+6,40,`background:${c};clip-path:polygon(0 0,calc(100% - 14px) 0,100% 50%,calc(100% - 14px) 100%,0 100%,14px 50%);display:flex;align-items:center;justify-content:center;color:#fff;font:700 8.5pt Lexend;letter-spacing:.06em`,tt[i]?tt[i].text:'')});A.hide(tt)"),
  V('Étapes numérotées reliées', "Un rond rose plein numéroté par maillon, relié par une barre ardoise épaisse ; titre dessous.",
    CH + r"const y=b[0].cy,x0=b[0].cx,x1=b[b.length-1].cx;A.div(sl,x0,y-2,x1-x0,4,'background:#33525F;border-radius:2px');b.forEach((s,i)=>A.div(sl,s.cx-15,y-15,30,30,'border-radius:50%;background:#FB0161;color:#fff;font:700 10pt Lexend;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 5px #062A3C',String(i+1)))"),
  V('Colonnes en cartes', "Chaque maillon devient une carte bleu clair (titre en haut sur un bandeau rose plein, texte des leaders dessous).",
    CH + r"b.forEach((s,i)=>{const d=A.div(sl,s.x+3,s.y-30,s.w-6,250,'background:#0B3850;border-radius:10px;overflow:hidden');d.innerHTML='<i style=\"display:block;height:40px;background:#FB0161\"></i>';const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)});tt.forEach(t=>{A.color(t,'#fff');t.el.style.top=(t.y-24)+'px'})"),
  'A', "Les chevrons dégradés montrent le sens de la chaîne et portent les titres : plus besoin de bandes séparées.", fam='Schémas')

# ---------- Paris audacieux ----------
BB = r"A.hide(A.shapes(sl).filter(s=>(s.w<14&&s.h>150)||(s.w<24&&s.h<50&&s.h>40)));const hz=A.texts(sl).filter(t=>/HORIZON/.test(t.text));const cards=A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>150);"
I('68', "Paris audacieux : nouvelle mise en page", "Tu détestes cette slide : accolades, petites flèches, libellés de biais.", [97], 97,
  V('Deux couloirs', "Chaque horizon devient un couloir bleu clair arrondi, avec une étiquette rose pleine « 0-5 YEARS » en haut à gauche ; cartes en aplat, petites flèches retirées.",
    BB + r"cards.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});[[170,210],[383,210]].forEach(([y,h],i)=>{const d=A.div(sl,140,y,730,h,'background:#082F43;border-radius:14px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);A.div(sl,156,y-11,120,22,'background:#FB0161;border-radius:11px;color:#fff;font:700 7.5pt Lexend;letter-spacing:.1em;display:flex;align-items:center;justify-content:center',i?'5-10 YEARS':'0-5 YEARS')});A.hide(hz)"),
  V('Bandes d\u2019horizon roses', "Cartes en aplat, petites flèches et accolades retirées ; l'horizon devient une bande rose pleine verticale à gauche de chaque rangée.",
    BB + r"cards.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.hide(hz);[[184,'0-5 YEARS'],[397,'5-10 YEARS']].forEach(([y,l])=>A.div(sl,118,y,26,182,'background:#FB0161;border-radius:6px;color:#fff;font:700 7pt Lexend;letter-spacing:.14em;writing-mode:vertical-rl;transform:rotate(180deg);display:flex;align-items:center;justify-content:center',l))"),
  V('Frise d’horizon', "Une frise horizontale pleine entre les deux rangées (0 → 5 → 10 ans) avec des jalons roses ; cartes en aplat.",
    BB + r"cards.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.hide(hz);A.div(sl,156,378,702,4,'background:#33525F;border-radius:2px');[['TODAY',156],['5 YEARS',507],['10 YEARS',858]].forEach(([l,x])=>{A.div(sl,x-7,373,14,14,'border-radius:50%;background:#FB0161;box-shadow:0 0 0 4px #062A3C');A.div(sl,x-50,354,100,16,'text-align:center;font:700 7pt Lexend;letter-spacing:.12em;color:#E7CDA8',l)})"),
  'A', "Les couloirs disent l'horizon d'un coup d'œil et remplacent accolades et libellés de biais.", fam='Schémas')

# ---------- Qui paie : liens ----------
QP = r"A.hide(A.shapes(sl).filter(s=>s.dash==='1 3'||(s.sw===3&&s.w<30)));const col=A.shapes(sl).filter(s=>s.sw===3&&s.w<30);"
I('71', "Qui paie : liens vers les segments", "La ligne pointillée et les flèches grises n'apportaient rien.", [63, 67, 71, 75, 79, 83, 107, 111, 116, 120, 124, 128], 63,
  V('Organigramme plein', "Un vrai organigramme : barre ardoise pleine en haut et une descente pleine vers chaque colonne.",
    QP + r"if(col.length){const x0=col[0].cx,x1=col[col.length-1].cx,y=col[0].y;A.div(sl,x0,y,x1-x0,3,'background:#33525F');col.forEach(s=>A.div(sl,s.cx-1.5,y,3,s.h-6,'background:#33525F'));A.div(sl,480-1.5,y-22,3,22,'background:#33525F')}"),
  V('Racine rose pleine', "Même organigramme, avec en haut une pastille rose pleine qui porte le nom du segment.",
    QP + r"const ss0=sl.querySelector('.subtitle');const sub0=A.texts(sl).find(t=>t.y>140&&t.y<190&&/^[A-Z][A-Z0-9 &-]+$/.test(t.text));const sub=ss0?ss0:(sub0?{textContent:sub0.text,style:sub0.el.style}:null);if(col.length){const x0=col[0].cx,x1=col[col.length-1].cx,y=col[0].y+12;A.div(sl,x0,y,x1-x0,3,'background:#33525F');col.forEach(s=>A.div(sl,s.cx-1.5,y,3,s.h-18,'background:#33525F'));A.div(sl,480-90,y-14,180,28,'border-radius:14px;background:#FB0161;color:#fff;font:700 8pt Lexend;letter-spacing:.12em;display:flex;align-items:center;justify-content:center;z-index:3',sub?sub.textContent:'')}if(sub)sub.style.visibility='hidden';const ss=sl.querySelector('.subtitle');if(ss)ss.style.visibility='hidden'"),
  V('Sans liens, cartes pleines', "Plus aucun trait : les cinq colonnes deviennent des cartes bleu clair, titre compris.",
    QP + r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>100).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55');s.el.style.transform='scaleY(1.32)';s.el.style.transformOrigin='bottom'})"),
  'B', "La racine rose dit « ce segment se répartit entre ces clients », c'est le sens de la slide.", fam='Schémas')

# ---------- Arbre EdTech (slide 10) ----------
TR = r"A.hide(A.shapes(sl).filter(s=>s.dash==='1 3'||(s.sw===3&&s.w<30)));const col=A.shapes(sl).filter(s=>s.sw===3&&s.w<30);const root=A.texts(sl).find(t=>t.text==='EDTECH');"
I('98', "Arbre EdTech → 5 segments : nouveaux designs", "Tout était moche ; la racine EDTECH grise manquait de présence.", [10], 10,
  V('Racine rose + organigramme plein', "EDTECH dans une pastille rose pleine, organigramme ardoise plein vers les cinq segments, cartes en aplat.",
    TR + r"if(root){root.el.style.visibility='hidden';A.div(sl,480-80,root.y+4,160,36,'border-radius:18px;background:#FB0161;color:#fff;font:700 13pt Lexend;letter-spacing:.08em;display:flex;align-items:center;justify-content:center;z-index:3','EDTECH')}if(col.length){const x0=col[0].cx,x1=col[col.length-1].cx,y=col[0].y+6;A.div(sl,x0,y,x1-x0,3,'background:#33525F');col.forEach(s=>A.div(sl,s.cx-1.5,y,3,s.h-12,'background:#33525F'));A.div(sl,478.5,root?root.y+40:y-20,3,root?y-root.y-40:20,'background:#33525F')}A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>100).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Racine crème pleine', "EDTECH en pastille crème pleine (texte bleu nuit), même organigramme plein.",
    TR + r"if(root){root.el.style.visibility='hidden';A.div(sl,480-80,root.y+4,160,36,'border-radius:18px;background:#E7CDA8;color:#062A3C;font:700 13pt Lexend;letter-spacing:.08em;display:flex;align-items:center;justify-content:center;z-index:3','EDTECH')}if(col.length){const x0=col[0].cx,x1=col[col.length-1].cx,y=col[0].y+6;A.div(sl,x0,y,x1-x0,3,'background:#33525F');col.forEach(s=>A.div(sl,s.cx-1.5,y,3,s.h-12,'background:#33525F'));A.div(sl,478.5,root?root.y+40:y-20,3,root?y-root.y-40:20,'background:#33525F')}"),
  V('Cartes à bandeau rose', "Plus de traits : EDTECH en grand titre crème, et chaque segment devient une carte avec son nom sur un bandeau rose plein.",
    TR + r"if(root)root.el.querySelectorAll('span').forEach(s=>{s.style.color=C.cream;s.style.fontSize='20pt';s.style.fontWeight='700'});A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>100&&!s.dash&&s.h>40).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55');const d=A.div(sl,s.x,s.y-50,s.w,46,'background:#FB0161;border-radius:10px 10px 0 0');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)});A.texts(sl).filter(t=>t.h<50&&t.y>320&&t.y<380).forEach(t=>{A.color(t,'#fff');t.el.style.top=(t.y+4)+'px'})"),
  'A', "La racine rose pleine et l'organigramme plein font un vrai arbre lisible, sans pointillés.", fam='Schémas')

# ---------- Boucles qui s'auto-alimentent (slide 154) ----------
LP = r"const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'));A.hide(sh.filter(s=>s.dash));A.emojis(sl).forEach(e=>e.closest('.rx-t').style.visibility='hidden');const bx=sh.filter(s=>s.stroke==='#334D54'&&!s.dash&&s.w>200).sort((a,b)=>(a.y-b.y)||(a.x-b.x));"
LPAIRS = r"const pairs=[];const L=bx.filter(s=>s.x<300),R=bx.filter(s=>s.x>=300);"
I('58', "Boucles qui s'auto-alimentent : redessinées", "Le schéma était mal tracé (traits qui dépassent, flèches roses perdues, emojis) ; je le redessine proprement.", [154], 154,
  V('Paires reliées par un rond « boucle »', "Chaque boucle = deux cartes en aplat ; entre elles, un rond rose plein avec une icône boucle blanche. Plus aucun pointillé.",
    LP + r"bx.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});for(let i=0;i<bx.length;i+=2){const a=bx[i],b=bx[i+1];if(!b)break;const x=(a.cx+b.cx)/2,y=(a.y+a.h+b.y)/2;A.div(sl,x-16,y-16,32,32,'border-radius:50%;background:#FB0161;display:flex;align-items:center;justify-content:center;z-index:3;box-shadow:0 0 0 4px #062A3C',A.svg('🔁','line',17,'#fff',2.4))}"),
  V('Quatre boucles en panneaux', "Chaque boucle (deux cartes) est regroupée dans un panneau bleu clair avec un numéro rose plein.",
    LP + r"bx.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#123F57')});for(let i=0;i<bx.length;i+=2){const a=bx[i],b=bx[i+1];if(!b)break;const x0=Math.min(a.x,b.x)-10,y0=a.y-10,x1=Math.max(a.x+a.w,b.x+b.w)+10,y1=b.y+b.h+10;const d=A.div(sl,x0,y0,x1-x0,y1-y0,'background:#082F43;border-radius:14px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);A.div(sl,x0-12,y0-12,26,26,'border-radius:50%;background:#FB0161;color:#fff;font:700 10pt Lexend;display:flex;align-items:center;justify-content:center;z-index:3',String(i/2+1))}"),
  V('Cercle vertueux dessiné', "Entre les deux cartes de chaque boucle, deux flèches courbes pleines ardoise qui forment un cercle ; cartes en aplat.",
    LP + r"bx.forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});for(let i=0;i<bx.length;i+=2){const a=bx[i],b=bx[i+1];if(!b)break;const x=(a.cx+b.cx)/2,y=(a.y+a.h+b.y)/2;A.div(sl,x-18,y-18,36,36,'z-index:3',`<svg width='36' height='36' viewBox='0 0 36 36'><circle cx='18' cy='18' r='17' fill='#062A3C'/><path d='M8 18a10 10 0 0 1 17-7' fill='none' stroke='#7E949E' stroke-width='3' stroke-linecap='round'/><path d='M28 18a10 10 0 0 1-17 7' fill='none' stroke='#FB0161' stroke-width='3' stroke-linecap='round'/><path d='M22 7l4 4-5 1z' fill='#7E949E'/><path d='M14 29l-4-4 5-1z' fill='#FB0161'/></svg>`)}"),
  'B', "Les panneaux montrent qu'il y a quatre boucles distinctes ; avant, on ne savait pas quelle carte allait avec laquelle.", fam='Schémas')
