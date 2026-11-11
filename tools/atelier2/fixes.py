"""Visual audit of 11 Nov 2026: the fixes applied after the atelier decisions (decisions.js runs F.all on every raw slide, then these).
Each fix: id, title (FR, for Pierre), why, slides (where it applies), shot/clip (before/after crop: slide, x, y, w, h), js (per slide, optional),
how ('règle générale' = fixlib rule on every raw slide of every deck, 'convertisseur' = tools/pptx2html.py, 'type' = all slides of the type)."""

PILL = 'F.pillText(sl)'
FIXES = [
    dict(id=1, title='« $ 192 B » → « $192B »', why='Espaces parasites dans les montants : le chiffre se lit en trois morceaux.',
         how='convertisseur', slides=[45, 159, 164, 165, 166, 167, 169], clip=(45, 220, 215, 520, 300)),
    dict(id=2, title='« ≈5 % » → « ≈5% »', why='Même règle pour les pourcentages : le signe colle au chiffre.',
         how='convertisseur', slides=[143], clip=(143, 90, 160, 420, 160)),
    dict(id=3, title='« ASIA - PACIFIC » → « ASIA-PACIFIC »', why='Le tiret avec espaces coupait le nom de la région en deux étiquettes.',
         how='convertisseur', slides=[183], clip=(183, 640, 300, 320, 160)),
    dict(id=4, title='En-têtes de colonnes invisibles', why='« FIRM / CAGR / COMMENTS » étaient écrits dans la couleur des traits (#334D54) : on ne les voyait pas.',
         how='règle générale', slides=[50, 77, 81, 85], clip=(50, 150, 170, 660, 150)),
    dict(id=5, title='Soulignement qui déborde sur l’espace', why='Le lien « Grand View EdTech_ » était souligné jusqu’après le dernier mot.',
         how='convertisseur', slides=[216, 217, 218, 219, 220], clip=(216, 40, 110, 480, 120)),
    dict(id=6, title='Texte collé en haut des cartes', why='Le texte était aligné en haut de la carte, avec un grand vide en bas : il est centré.',
         how='règle générale', slides=[10], clip=(10, 100, 375, 760, 165)),
    dict(id=11, title='Pastille collée au texte, bloc trop haut', why='La pastille numérotée touchait la 1re ligne et l’ensemble était décentré. Pastille + texte sont centrés ensemble, 8 px d’écart.',
         how='type', slides=[64, 68, 72, 76, 80, 84], js=PILL, clip=(64, 100, 230, 760, 320)),
    dict(id=12, title='Mini-jauges (ton choix 30 B) absentes des slides converties', why='Le choix 30 B ne s’appliquait qu’aux 3 slides refaites ; les 3 autres gardaient les « +++ ».',
         how='règle générale', slides=[77, 81, 85], clip=(77, 400, 215, 460, 350)),
    dict(id=13, title='Titres et cartes décalés', why='« DIGITAL TUTORING » et « CREDENTIALING » étaient 3 px à droite de leur carte, une carte 2 px plus haute.',
         how='type', slides=[61], clip=(61, 200, 190, 560, 370),
         js="A.cards(sl).forEach(c=>A.texts(sl).filter(t=>t.cy<c.y&&t.cy>c.y-70&&Math.abs(t.cx-c.cx)<25&&t.h<70).forEach(t=>{t.el.style.left=c.x+'px';t.el.style.width=c.w+'px'}))"),
    dict(id=14, title='2e ligne du parcours décalée de 3 px', why='Les cartes 5 à 8 (et leurs pastilles, flèches) étaient 3 px à gauche de la ligne du dessus.',
         how='règle générale', slides=[109, 114, 118, 122, 126, 130], clip=(109, 110, 240, 720, 300)),
    dict(id=15, title='Montants alignés sur les flèches', why='« $1B » était centré alors que les flèches partent toutes du même point : les montants sont calés à droite.',
         how='type', slides=[36], clip=(36, 280, 240, 460, 270),
         js="const Ls=F.lines(sl).filter(l=>l.horiz);A.texts(sl).filter(t=>/^\\$[\\d.]+[KMB]$/.test(t.text)).forEach(t=>{const l=Ls.find(l=>Math.abs(l.a.y-t.cy)<12);if(!l)return;const x0=Math.min(l.a.x,l.b.x);t.el.querySelector('p').style.textAlign='right';t.el.style.left=(x0-10-t.w)+'px'})"),
    dict(id=16, title='« 33% » écrit à la verticale', why='La boîte faisait 29 px de large : « 3 / 3 / % » sur trois lignes.',
         how='slide', slides=[187], clip=(187, 520, 200, 280, 110),
         js="const t=A.texts(sl).find(t=>t.text==='33%');if(t){const L=F.lines(sl).filter(l=>l.horiz).sort((a,b)=>Math.abs(a.a.y-t.cy)-Math.abs(b.a.y-t.cy))[0];t.el.style.left=(t.cx-24)+'px';t.el.style.width='48px';t.el.style.padding='0';t.el.style.background='#062A3C';if(L&&Math.abs(L.a.y-t.cy)<14)t.el.style.top=(L.a.y-t.h/2)+'px'}"),
    dict(id=17, title='« PEARSON market cap $9B » sur 3 lignes', why='Le libellé se cassait en « market / cap $9B » : nom sur une ligne, valeur sur la suivante.',
         how='slide', slides=[187], clip=(187, 600, 220, 240, 200),
         js="A.texts(sl).filter(t=>/^(PEARSON|ERUDITUS)/.test(t.text)).forEach(t=>{const p=t.el.querySelector('p'),sp=[...p.querySelectorAll(':scope > span')];if(sp.length<2)return;const a=sp[0].cloneNode(false),b=sp[1].cloneNode(false);a.textContent=sp[0].textContent.trim();b.textContent=sp.slice(1).map(x=>x.innerText).join(' ').replace(/\\s+/g,' ').trim();p.innerHTML='';p.append(a,document.createElement('br'),b);p.style.whiteSpace='nowrap';t.el.style.width='150px'})"),
    dict(id=18, title='Boucles : liaisons refaites', why='Les courbes coupaient les bulles et les pointes flottaient. Chaque passage d’une rangée à l’autre est maintenant une courte flèche verticale, dans la zone où les deux bulles se superposent.',
         how='type', slides=[154], js='const MK=(svg,id)=>{const d=document.createElementNS(\'http://www.w3.org/2000/svg\',\'defs\');d.innerHTML=`<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#FB0161"/></marker>`;svg.appendChild(d)};F.arrowheads(sl);const sh=A.shapes(sl),bx=sh.filter(s=>!s.dash&&s.w>200&&s.h<70&&s.h>40),cur=sh.filter(s=>s.dash&&s.h>60);A.hide(cur);const ns=\'http://www.w3.org/2000/svg\',svg=document.createElementNS(ns,\'svg\');svg.setAttribute(\'width\',\'960\');svg.setAttribute(\'height\',\'672\');svg.style.cssText=\'position:absolute;left:0;top:0;overflow:visible\';MK(svg,\'v154\');const Rr=sl.getBoundingClientRect(),near=(pt)=>bx.reduce((a,s)=>{const d=Math.hypot(Math.max(s.x-pt.x,0,pt.x-s.x-s.w),Math.max(s.y-pt.y,0,pt.y-s.y-s.h));return !a||d<a.d?{s,d}:a},null).s;cur.forEach(c=>{const L=c.p.getTotalLength(),M=c.p.getScreenCTM(),P=l=>{const q=c.p.getPointAtLength(l).matrixTransform(M);return {x:q.x-Rr.left,y:q.y-Rr.top}};let a=near(P(0)),b=near(P(L));if(!a||!b||a===b)return;const from=a.y<b.y?a:b,to=a.y<b.y?b:a;const x=(Math.max(from.x,to.x)+Math.min(from.x+from.w,to.x+to.w))/2;const p=document.createElementNS(ns,\'path\');p.setAttribute(\'d\',`M${x} ${from.y+from.h+3}L${x} ${to.y-3}`);p.setAttribute(\'stroke\',\'#4A6470\');p.setAttribute(\'stroke-width\',\'2\');p.setAttribute(\'stroke-dasharray\',\'4 4\');p.setAttribute(\'marker-end\',\'url(#v154)\');svg.appendChild(p)});sl.querySelector(\'.raw\').appendChild(svg)', clip=(154, 100, 200, 770, 340)),
    dict(id=19, title='Flèches du « MARKET » refaites', why='Les 5 liaisons partent toutes du bord du cercle et arrivent toutes au milieu du bord gauche de leur bulle, avec la même pointe rose.',
         how='type', slides=[151], js='const MK=(svg,id)=>{const d=document.createElementNS(\'http://www.w3.org/2000/svg\',\'defs\');d.innerHTML=`<marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#FB0161"/></marker>`;svg.appendChild(d)};const sh=A.shapes(sl),c0=sh.find(s=>s.fill&&s.fill.toUpperCase()===C.pink&&s.w>100),bx=sh.filter(s=>!s.dash&&s.w>200&&s.h<70),old=sh.filter(s=>s.dash||(s.fill&&s.fill.toUpperCase()===C.pink&&s.w<40));A.hide(old);if(!c0)return;const ns=\'http://www.w3.org/2000/svg\',svg=document.createElementNS(ns,\'svg\');svg.setAttribute(\'width\',\'960\');svg.setAttribute(\'height\',\'672\');svg.style.cssText=\'position:absolute;left:0;top:0;overflow:visible\';MK(svg,\'v151\');const r=c0.w/2;bx.sort((p,q)=>p.cy-q.cy).forEach((b,i,arr)=>{const ex=b.x-4,ey=b.cy,a=(-38+76*i/Math.max(1,arr.length-1))*Math.PI/180,sx=c0.cx+Math.cos(a)*(r+8),sy=c0.cy+Math.sin(a)*(r+8),k=(ex-sx)*.5;const p=document.createElementNS(ns,\'path\');p.setAttribute(\'d\',`M${sx} ${sy}C${sx+k} ${sy},${ex-k} ${ey},${ex} ${ey}`);p.setAttribute(\'fill\',\'none\');p.setAttribute(\'stroke\',\'#4A6470\');p.setAttribute(\'stroke-width\',\'2\');p.setAttribute(\'stroke-dasharray\',\'5 5\');p.setAttribute(\'marker-end\',\'url(#v151)\');svg.appendChild(p)});sl.querySelector(\'.raw\').insertBefore(svg,sl.querySelector(\'.raw\').firstChild)', clip=(151, 90, 190, 800, 390)),
    dict(id=20, title='Légendes des barres en colonne étroite', why='Les notes au-dessus des barres faisaient 86 px de large (4-5 lignes, en escalier) : elles sont élargies.',
         how='overrides', slides=[159, 165, 166], clip=(165, 190, 130, 560, 410)),
    dict(id=21, title='« BEST CASE - ≈ 14% »', why='Tiret + espace + ≈ : trois signes à la suite. Devient « BEST CASE ≈ 14% ».',
         how='overrides', slides=[51], clip=(51, 380, 250, 200, 180)),
    dict(id=22, title='Frises datées : la 2e page n’avait pas ton choix 34 A', why='Sur les pages « 2/2 », la barre rose épaisse avec flèche restait : même type de slide, même rail fin + points partout.',
         how='type', slides=[93, 134, 150, 157, 177, 184, 195, 205], js='F.rail(sl)', clip=(93, 110, 170, 420, 440)),
    dict(id=23, title='« ≠ » rose en trait fin', why='Le signe ≠ était en graisse 300 : rose fin sur navy, interdit. Passé en gras.',
         how='slide', slides=[8], clip=(8, 300, 265, 380, 70),
         js="sl.querySelectorAll('.raw > div').forEach(d=>{if(d.textContent.trim()==='\\u2260'){d.style.fontWeight='700'}})"),
    dict(id=24, title='Encadré « exclude » décalé de 3 px', why='Les deux encadrés de droite n’avaient ni le même bord gauche ni la même largeur.',
         how='slide', slides=[41], clip=(41, 300, 280, 580, 230),
         js="const cs=A.cards(sl).filter(c=>c.w>400).sort((a,b)=>a.y-b.y);if(cs.length===2){const [a,b]=cs;const sa=a.el,sb=b.el;sb.setAttribute('preserveAspectRatio','none');sb.style.left=sa.style.left;sb.style.width=sa.style.width;const t=A.texts(sl).find(t=>Math.abs(t.x-b.x)<3&&Math.abs(t.y-b.y)<3);if(t){t.el.style.left=a.x+'px';t.el.style.width=a.w+'px'}}"),
    dict(id=25, title='Cadre « AFTER » en rose fin', why='Bordure rose de 2 px sur navy (règle : rose seulement en aplat ou épais). Bordure 3 px + titre en aplat rose.',
         how='slide', slides=[162], clip=(162, 220, 250, 520, 260),
         js="const c=A.cards(sl).find(c=>c.stroke&&c.stroke.toUpperCase()==='#FB0161');if(c){c.p.setAttribute('stroke-width','5');const t=A.texts(sl).find(t=>Math.abs(t.x-c.x)<3);const s=t&&[...t.el.querySelectorAll('span')].find(x=>x.textContent.trim()==='AFTER');if(s){s.style.cssText+=';background:#FB0161;color:#fff;padding:2px 10px;border-radius:4px'}}"),
]

# ---- 2nd audit round (11 Nov, 4h): shown to Pierre on their own
FIXES += [
    dict(id=26, title='Matrices de priorité : même rendu sur les 4 segments', why='Les slides 77, 81 et 85 étaient restées en version convertie (+ / ++ / +++, colonnes décalées) alors que 65, 69 et 73 avaient le modèle propre. Les 4 ont maintenant le même modèle.',
         how='convertisseur', slides=[77, 81, 85], clip=(77, 60, 140, 840, 440)),
    dict(id=27, title='« $ 187 B » restait dans les slides modèles', why='La règle des chiffres ne touchait que les slides converties : « $ 123 B », « $ 67 B », « $ 189 M » restaient sur les barres. Elle s’applique maintenant à tout le deck.',
         how='convertisseur', slides=[42, 46, 47, 52, 158], clip=(46, 80, 160, 560, 260)),
    dict(id=29, title='« CREDENTIALING » partout → « DIGITAL CREDENTIALING »', why='Suite de ton OK sur le 13 : un même segment doit porter le même nom sur toutes les slides (intercalaire, sous-titres, tableaux, cartes).',
         how='règle générale', slides=[82, 83, 84, 85, 168, 173, 178, 200, 206], clip=(200, 90, 400, 780, 110)),
    dict(id=30, title='Petits 📉 à cheval sur le coin des cartes', why='Un emoji minuscule posé sur l’angle bas-gauche de chaque carte, à moitié dehors. Devient une pastille ronde propre (icône au trait) centrée sur le bord bas de la carte (en haut il y a déjà les titres). Le texte passe à 4 lignes, centré dans l’espace au-dessus de la pastille.',
         how='type', slides=[101, 102], clip=(101, 150, 180, 660, 370),
         js="const cs=A.cards(sl);A.texts(sl).filter(t=>t.text==='\U0001F4C9').forEach(t=>{const c=cs.find(c=>Math.abs(c.x-t.cx)<20&&Math.abs(c.y+c.h-t.cy)<20);t.el.style.visibility='hidden';if(!c)return;A.div(sl,c.x+c.w/2-13,c.y+c.h-13,26,26,'display:flex;align-items:center;justify-content:center;border-radius:50%;background:#123F57;box-shadow:0 0 0 3px #062A3C',A.svg('\U0001F4C9','line',14,'#E7CDA8',2))});A.cards(sl).forEach(c=>A.texts(sl).filter(t=>Math.abs(t.x-c.x)<3&&Math.abs(t.y-c.y)<3).forEach(t=>{t.el.style.justifyContent='center';t.el.style.paddingBottom='22px';t.el.style.paddingTop='4px'}))"),
    dict(id=32, title='« MEDIUM / HIGH » collés à la barre rose', why='Les étiquettes touchaient le bord de la barre verticale, on lisait « █MEDIUM ». Décalées pour avoir le même écart de 12 px que sur la slide 143 (règle générale : toute étiquette collée à une barre rose verticale).',
         how='règle générale', slides=[144], clip=(144, 80, 170, 520, 200)),
    dict(id=34, title='Colonne de droite en traits roses fins', why='Les 10 lignes « PREPLY / GIZMO / … » étaient encadrées de rose 2 px sur navy (règle : jamais de rose fin). Elles deviennent des aplats navy clair avec un bord gauche rose épais ; les logos ont leur marge blanche.',
         how='type', slides=[210, 211, 212, 213, 214], clip=(210, 380, 140, 580, 280)),
]

# ---- 4th round (11 Nov, 4h20): 10 new obvious defects
FIXES += [
    dict(id=35, title='Étiquettes « $1.3M / $2M » posées sur les points', why='Les médianes s’écrivaient par-dessus les points du nuage. Elles ont maintenant un fond navy, comme une pastille.',
         how='slide', slides=[163], clip=(163, 170, 240, 420, 200),
         js="A.texts(sl).filter(t=>/^\\$[\\d.]+M$/.test(t.text)).forEach(t=>{const s=t.el.querySelector('p > span')||t.el;s.style.cssText+=';background:#062A3C;padding:1px 5px;border-radius:4px;white-space:nowrap';t.el.style.width='auto';t.el.style.overflow='visible';t.el.style.zIndex=5})"),
    dict(id=36, title='Cartes carrées à bord clair', why='Ces deux slides avaient des cadres carrés à bord clair, alors que toutes les autres grilles du deck ont des cartes arrondies au trait gris-bleu. Harmonisées.',
         how='type', slides=[160, 188], clip=(160, 140, 220, 680, 330), js="const rr=(s,r)=>{const b=s.p.getBBox();s.p.setAttribute('d',`M${b.x+r} ${b.y}H${b.x+b.width-r}A${r} ${r} 0 0 1 ${b.x+b.width} ${b.y+r}V${b.y+b.height-r}A${r} ${r} 0 0 1 ${b.x+b.width-r} ${b.y+b.height}H${b.x+r}A${r} ${r} 0 0 1 ${b.x} ${b.y+b.height-r}V${b.y+r}A${r} ${r} 0 0 1 ${b.x+r} ${b.y}Z`)};A.shapes(sl).filter(s=>s.p&&!s.line&&(s.stroke||'').match(/#(D0E1E5|789096)/i)&&s.w>150&&s.h>100).forEach(s=>{s.p.setAttribute('stroke','#334D54');s.p.setAttribute('stroke-width','1.2');rr(s,10)})"),
    dict(id=37, title='Points du radar reliés à rien', why='Les 5 points roses ne disaient pas quelle startup ils représentent. Chaque point est relié à sa carte par un trait pointillé.',
         how='slide', slides=[175], clip=(175, 50, 170, 860, 420), js="const sh=A.shapes(sl),dots=sh.filter(s=>s.fill&&s.fill.toUpperCase()===C.pink&&s.w<24&&s.h<24),cards=sh.filter(s=>(s.fill||'').toUpperCase()==='#123F57'&&s.w>150).map(h=>{const left=h.x+h.w/2<480;return {x:left?h.x+h.w:h.x,y:h.y+45}});const perm=a=>a.length<2?[a]:a.flatMap((x,i)=>perm(a.filter((_,j)=>j!==i)).map(p=>[x,...p]));let best=null;perm([...dots.keys()]).forEach(p=>{const d=p.reduce((s,di,ci)=>s+(cards[ci]?Math.hypot(dots[di].cx-cards[ci].x,dots[di].cy-cards[ci].y):0),0);if(!best||d<best.d)best={d,p}});if(!best)return;const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('width','960');svg.setAttribute('height','672');svg.style.cssText='position:absolute;left:0;top:0;overflow:visible;pointer-events:none';best.p.forEach((di,ci)=>{const c=cards[ci];if(!c)return;const d=dots[di],a=Math.atan2(c.y-d.cy,c.x-d.cx),sx=d.cx+Math.cos(a)*9,sy=d.cy+Math.sin(a)*9;const l=document.createElementNS(ns,'path');l.setAttribute('d',`M${sx} ${sy}L${c.x+(c.x<d.cx?6:-6)} ${c.y}`);l.setAttribute('stroke','#5E7E8E');l.setAttribute('stroke-width','1.5');l.setAttribute('stroke-dasharray','4 4');svg.appendChild(l)});sl.querySelector('.raw').appendChild(svg)"),
    dict(id=38, title='« Users quit » écrit en tout petit', why='Une seule bulle avait un texte de 6 pt, illisible à côté des autres. Même taille que « Tool sprawl ».',
         how='slide', slides=[59], clip=(59, 90, 170, 380, 420),
         js="const t=A.texts(sl).find(t=>/Users\\s*quit/.test(t.el.innerText));const r=A.texts(sl).find(t=>/Tool\\s*sprawl/.test(t.el.innerText));if(t&&r){const fs=getComputedStyle(r.el.querySelector('span')).fontSize;t.el.querySelectorAll('span,p').forEach(s=>s.style.fontSize=fs)}"),
    dict(id=39, title='« ≈ 35% » → « ≈35% »', why='Même règle que le 2 : le signe ≈ colle au chiffre. Restait un espace sur les catégories, les taux de croissance, le scénario et le poids du top deal.',
         how='convertisseur', slides=[47, 50, 51, 164], clip=(47, 170, 455, 620, 75)),
    dict(id=40, title='Point manquant entre deux phrases des notes', why='« …historical phases These phases are… » : deux phrases collées sans point dans les notes de bas de slide. Le point est ajouté.',
         how='convertisseur', slides=[91, 94, 133, 138, 147, 7], clip=(91, 0, 600, 560, 50)),
    dict(id=41, title='Années « 2024 / 2025 » en haut du graphique', why='Sur ce graphique, les années étaient au-dessus des courbes ; partout ailleurs elles sont sous l’axe. Descendues sous les traits verticaux.',
         how='slide', slides=[197], clip=(197, 200, 210, 360, 380),
         js="const V=A.shapes(sl).filter(s=>s.line&&s.h>200&&s.w<30);const yb=Math.max(...V.map(s=>s.y+s.h));A.texts(sl).filter(t=>/^20\\d\\d$/.test(t.text)&&t.y<300).forEach(t=>{t.el.style.top=(yb+4)+'px'})"),
]

# ---- 5th round (11 Nov, 8h40): final audit before showing the whole deck
FIXES += [
    dict(id=44, title='Titres trop loin de leur carte', why='Quand le titre tient sur une ligne, il flottait au milieu de sa boîte, loin de la carte. Il est maintenant posé 8 px au-dessus (règle générale).',
         how='règle générale', slides=[101, 102], clip=(101, 150, 175, 660, 200)),
    dict(id=47, title='Mauvais chapitre en haut de la slide', why='La slide Eruditus / Pearson affichait « EDTECH MARKET » au lieu de son chapitre « TOP PLAYERS ». Corrigé dans le convertisseur pour tous les decks.',
         how='convertisseur', slides=[187], clip=(187, 280, 0, 400, 80)),
]

# ---- 6th round (11 Nov, 10h)
FIXES += [
    dict(id=49, title='Flèches de droite qui n’entrent pas dans les bulles', why='À gauche, les flèches ↔ entrent dans les deux bulles ; à droite elles s’arrêtaient avant la bulle de droite. Elles ont maintenant la même longueur relative, et la croix est recentrée.',
         how='slide', slides=[140], clip=(140, 480, 200, 400, 360),
         js="const sh=A.shapes(sl),cs=A.cards(sl),R=sl.getBoundingClientRect();sh.filter(s=>(s.fill||'').toUpperCase()==='#789096'&&s.h<25&&s.x>480).forEach(a=>{const L=cs.find(c=>c.x<a.x&&c.x+c.w>a.x-5&&Math.abs(c.cy-a.cy)<40),Rt=cs.find(c=>c.x>a.x&&Math.abs(c.cy-a.cy)<40);if(!L||!Rt)return;const x0=L.x+L.w-15,x1=Rt.x+14;a.el.setAttribute('preserveAspectRatio','none');a.el.style.left=x0+'px';a.el.style.width=(x1-x0)+'px';const xs=sh.find(s=>s.fill&&s.fill.toUpperCase()===C.pink&&Math.abs(s.cy-a.cy)<20&&s.x>480);if(xs)xs.el.style.left=(parseFloat(xs.el.style.left)+((x0+x1)/2-xs.cx))+'px'})"),
    dict(id=50, title='Grille trop proche du titre', why='Les 8 cartes des scénarios commençaient juste sous le titre. Tout le bloc descend de 22 px.',
         how='slide', slides=[142], clip=(142, 100, 100, 760, 500),
         js="sl.querySelectorAll('.raw > *').forEach(e=>{const t=parseFloat(e.style.top);if(t>150&&t<570)e.style.top=(t+22)+'px'})"),
    dict(id=51, title='« How did the leaders… 2/2 » : icônes comme sur la 1/2', why='La page 2/2 gardait ses emojis alors que la 1/2 avait les icônes au trait. Les pages d’une même série ont maintenant automatiquement les mêmes décisions (contrôle ajouté au générateur).',
         how='règle générale', slides=[208], clip=(208, 100, 170, 760, 420)),
]
