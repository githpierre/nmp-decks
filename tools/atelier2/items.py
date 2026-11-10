"""Atelier "100 améliorations" : pour chaque point, l'actuel et 3 variantes (CSS/JS injectés sur le vrai deck).
Chaque item : id, title (ce qui est moche), scope (slides qui partagent ce format), shot (slide montrée), clip (zoom, coordonnées slide),
A/B/C = variantes {name, desc, css, js}, mine = mon choix, why = pourquoi."""
ITEMS = []
def V(name, desc, js='', css=''): return dict(name=name, desc=desc, js=js, css=css)
def I(id, title, what, scope, shot, A, B, C, mine, why, clip=None, fam=''):
    ITEMS.append(dict(id=id, title=title, what=what, scope=scope, shot=shot, A=A, B=B, C=C, mine=mine, why=why, clip=clip, fam=fam))

RING = "{bg:'#0E3A50',border:'1px solid rgba(231,205,168,.25)'}"
PRING = "{bg:'rgba(251,1,97,.12)',border:'1px solid rgba(251,1,97,.55)'}"
def emo3(sz=22, ring=15, duo=24):
    return (V('Icône au trait, crème', "Une icône fine (Lucide) dans la couleur du texte, à la place de l'emoji.",
              f"A.swap(sl,{{style:'line',color:C.cream,size:{sz}}})"),
            V('Icône dans une pastille', "La même icône, plus petite, dans un rond bleu nuit bordé de crème : un vrai pictogramme de rapport.",
              f"A.swap(sl,{{style:'line',color:C.cream,size:{ring},ring:{RING}}})"),
            V('Icône rose bicolore', "Icône pleine en deux tons de rose (Phosphor duotone) : plus de couleur, toujours dans la charte.",
              f"A.swap(sl,{{style:'duo',color:C.pink,size:{duo}}})"))

# ---------------- 1. Emojis -> vraies icônes ----------------
I(1, "Prix : les sacs d'argent 💰", "Les emojis 💰 font clipart, ils sont flous et jaunes hors charte.", [13], 13,
  V('$ / $$ / $$$ en rose', "Le nombre de dollars dit le niveau de prix, en typo de la charte, sans image.",
    "A.texts(sl).filter(t=>/💰/.test(t.text)).forEach(t=>{const n=[...t.text].filter(c=>c==='💰').length;t.el.innerHTML=`<p style=\"text-align:center;font:700 22pt Lexend;color:${C.pink};letter-spacing:2px;line-height:1\">${'$'.repeat(n)}</p>`;})"),
  V('Pièces au trait', "1, 2 ou 3 icônes de pièces au trait crème, posées sur la bordure.",
    "A.swap(sl,{style:'line',color:C.cream,scale:.85,ring:{bg:C.navy,border:'none',pad:.2},gap:2})"),
  V('Jauge de 3 points', "Trois points : 1, 2 ou 3 remplis en rose. Lecture immédiate du niveau, très sobre.",
    "A.texts(sl).filter(t=>/💰/.test(t.text)).forEach(t=>{const n=[...t.text].filter(c=>c==='💰').length;t.el.innerHTML=`<p style=\"display:flex;justify-content:center;gap:9px;padding-top:6px;background:none\">${[1,2,3].map(i=>`<span style=\"width:13px;height:13px;border-radius:50%;background:${i<=n?C.pink:C.navy};border:2px solid ${i<=n?C.pink:'#4A6470'}\"></span>`).join('')}</p>`;})"),
  'C', "La jauge garde l'idée « plus cher » sans image, et elle se lit même en noir et blanc.", clip=[130, 230, 700, 280], fam='Emojis')

for (i, n, t, w, clip) in [
    (2, 14, "Cartes « quand la valeur se crée »", "Les emojis en haut des cartes ne vont pas avec le reste.", None),
    (3, 18, "Catégories : emojis en coin", "Les emojis en haut à gauche des cases sont trop petits et de styles différents.", [150, 180, 560, 420]),
    (4, 22, "Ce qui est rare : emojis des cartes", "8 emojis de styles différents (bulle, cadenas, graphique…).", None),
    (5, 31, "Pourquoi ça excite : emojis des cartes", "Chronomètre, graphique, robot… en emoji couleur, ça fait app grand public.", None),
    (6, 136, "Ce qui freine : cartes numérotées", "Emojis d'argent qui vole, cadenas, chrono : hétéroclite.", None),
    (7, 186, "Moonshots : cartes numérotées", "Cerveau, école, fusée en emoji : fait enfantin pour un rapport payant.", None),
    (8, 207, "Comment les leaders ont percé : cartes", "Hibou, palette, télé… emojis sans lien de style.", None),
    (9, 109, "Flux d'argent : étapes en emoji", "Chaque étape a un emoji couleur différent ; le flux paraît désordonné.", None),
    (10, 60, "Méthode : 4 étapes en emoji", "Cible, étiquette, personnages, visage fâché.", None),
    (11, 172, "Types de startups : cartes", "Emojis école, livres, bulle, robot, valise…", None),
    (12, 142, "Scénarios catastrophe : cartes", "Robot, billets, cadenas, balance : ton trop léger pour des scénarios noirs.", None),
]:
    a, b, c = emo3(26, 17, 28) if n == 14 else emo3()
    I(i, t, w, [n], n, a, b, c, 'B', "La pastille donne un rythme régulier à la grille et l'icône au trait se lit sans dominer le texte.", clip=clip, fam='Emojis')

a, b, c = emo3()
I(13, "« Qui paie » : petits carrés roses avec emoji", "Les carrés roses contiennent un emoji minuscule et illisible.", [63, 67, 71, 75, 79, 83], 63,
  V('Icône crème dans le carré', "On garde le carré rose, l'emoji devient une icône au trait crème bien visible.", "A.swap(sl,{style:'line',color:C.cream,size:15})"),
  V('Carré plein rose + icône blanche', "Le carré devient rose plein avec l'icône blanche : plus franc, plus lisible.",
    "A.shapes(sl).filter(s=>s.stroke&&s.stroke.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>s.p.setAttribute('fill',C.pink));A.swap(sl,{style:'line',color:'#fff',size:15,sw:2})"),
  V('Icône seule, sans carré', "On enlève le carré : une icône rose bicolore au-dessus de chaque colonne.",
    "A.shapes(sl).filter(s=>s.stroke&&s.stroke.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>s.el.style.visibility='hidden');A.swap(sl,{style:'duo',color:C.pink,size:26})"),
  'B', "Le rond rose plein donne un vrai point d'ancrage à chaque colonne, l'icône blanche se lit de loin.", clip=[60, 290, 840, 300], fam='Emojis')

I(14, "Points de douleur : le même emoji 🤒 répété 7 fois", "Sept fois le même visage malade : ça n'apporte rien et ça fait enfantin.", [64, 68, 72, 76, 80, 84], 64,
  V('Petit numéro rose', "Chaque carte porte son numéro (1 à 7) dans un rond rose : on peut y faire référence à l'oral.",
    "let i=0;A.emojis(sl).sort((a,b)=>{const ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect();return (Math.round(ra.top/20)-Math.round(rb.top/20))||(ra.left-rb.left)}).forEach(sp=>{i++;sp.outerHTML=`<span style=\"display:inline-flex;width:24px;height:24px;border-radius:50%;background:${C.pink};color:#fff;font:700 11pt Lexend;align-items:center;justify-content:center\">${i}</span>`;})"),
  V('Icône « alerte » au trait', "Un seul pictogramme sobre (triangle d'alerte) en rose au trait, cohérent avec « douleur ».",
    "A.emojis(sl).forEach(sp=>{sp.innerHTML=A.svg('⚠️','line',22,C.pink,1.8);sp.style.display='inline-flex'})"),
  V('Rien, texte remonté', "On enlève l'icône : la carte ne garde que la phrase, centrée, avec un liseré rose en haut.",
    "A.emojis(sl).forEach(sp=>sp.closest('p').style.display='none');A.shapes(sl).filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#2A4A58')});A.texts(sl).filter(t=>/They /.test(t.text)).forEach(t=>t.el.style.borderTop='2px solid '+C.pink)"),
  'A', "Le numéro remplace un emoji inutile par une info utile (on peut dire « la douleur 3 »).", fam='Emojis')

I(15, "Mythes : l'emoji 🤥 qui ment", "L'emoji Pinocchio est flou, jaune, et ne se comprend pas tout de suite.", [15, 16], 15,
  V('Étiquette MYTHE', "Une petite étiquette rose « MYTH » sur le coin de la case : on comprend tout de suite.",
    "A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style=\"display:inline-block;background:${C.pink};color:#fff;font:700 6.5pt Lexend;letter-spacing:1.5px;padding:3px 7px;border-radius:3px\">MYTH</span>`;})"),
  V('Point d\'interrogation au trait', "Un rond avec un « ? » au trait crème, comme une question qu'on se pose.",
    f"A.swap(sl,{{style:'line',color:C.cream,scale:.7,ring:{RING}}})"),
  V('Croix rose « faux »', "Un petit rond rose avec une croix blanche : le mythe est faux, la réponse à droite est la vérité.",
    "A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style=\"display:inline-flex;width:22px;height:22px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center\">${A.svg('❌','line',16,'#fff',2.4).replace(/<circle[^>]*>/,'')}</span>`;})"),
  'A', "Le mot MYTH dit exactement ce qu'est la case de gauche ; aucun pictogramme ne le dit aussi vite.", clip=[150, 180, 650, 420], fam='Emojis')

I(16, "Grille de livres 📚 (14 inscriptions par minute)", "93 emojis livres empilés : lourd, flou, et on ne compte rien.", [37], 37,
  V('Grille de points', "Une grille de petits points crème, 14 en rose = une minute. Propre, on voit la proportion.",
    "const t=A.texts(sl).filter(t=>/📚/.test(t.text));const b=t.reduce((a,o)=>({x:Math.min(a.x,o.x),y:Math.min(a.y,o.y),r:Math.max(a.r,o.x+o.w),bo:Math.max(a.bo,o.y+o.h)}),{x:1e9,y:1e9,r:0,bo:0});A.hide(t);let h='';for(let i=0;i<98;i++)h+=`<span style=\"width:11px;height:11px;border-radius:50%;background:${i<14?C.pink:'#33525F'}\"></span>`;A.div(sl,b.x,b.y,b.r-b.x,b.bo-b.y,`display:grid;grid-template-columns:repeat(14,11px);gap:9px;align-content:center;justify-content:center`,h)"),
  V('Icônes livre au trait', "Les mêmes livres mais en icônes fines crème : la grille garde l'idée « cours », sans le flou.",
    "A.swap(sl,{style:'line',color:C.cream,scale:.95})"),
  V('Grand chiffre + 14 icônes', "On remplace la grille par « 14 » en très grand et une ligne de 14 petites icônes de personnes.",
    "const t=A.texts(sl).filter(t=>/📚/.test(t.text));const b=t.reduce((a,o)=>({x:Math.min(a.x,o.x),y:Math.min(a.y,o.y),r:Math.max(a.r,o.x+o.w),bo:Math.max(a.bo,o.y+o.h)}),{x:1e9,y:1e9,r:0,bo:0});A.hide(t);let ic='';for(let i=0;i<14;i++)ic+=A.svg('👥','line',18,C.pink,1.8);A.div(sl,b.x,b.y,b.r-b.x,b.bo-b.y,`display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:${C.cream}`,`<div style=\"font:700 72pt Lexend;color:#fff;line-height:1\">14</div><div style=\"font:500 9pt Lexend;letter-spacing:2px\">ENROLLMENTS EVERY MINUTE</div><div style=\"display:grid;grid-template-columns:repeat(7,18px);gap:6px\">${ic}</div>`)"),
  'C', "Le chiffre 14 est le message du slide ; en très grand il se lit en une seconde, la grille ne servait qu'à décorer.", fam='Emojis')

I(17, "Grille de sacs d'argent 💰 (où est la valeur)", "88 emojis 💰 jaunes : c'est la zone la plus lourde de la slide et elle ne dit rien de précis.", [90], 90,
  V('Grille de carrés (waffle)', "100 petits carrés : 80 en rose (la valeur), 20 en bleu ardoise. On voit enfin « 80 % ».",
    "const t=A.texts(sl).filter(t=>/💰/.test(t.text));const b=t.reduce((a,o)=>({x:Math.min(a.x,o.x),y:Math.min(a.y,o.y),r:Math.max(a.r,o.x+o.w),bo:Math.max(a.bo,o.y+o.h)}),{x:1e9,y:1e9,r:0,bo:0});A.hide(t);let h='';for(let i=0;i<100;i++)h+=`<span style=\"width:15px;height:15px;border-radius:3px;background:${i<80?C.pink:'#33525F'}\"></span>`;A.div(sl,b.x,b.y,b.r-b.x,b.bo-b.y,`display:grid;grid-template-columns:repeat(10,15px);gap:5px;align-content:center;justify-content:center`,h)"),
  V('Pièces au trait', "Les mêmes piles mais en icônes fines crème, plus légères.", "A.swap(sl,{style:'line',color:C.cream,scale:.9})"),
  V('Grand 80 % en anneau', "Un anneau rempli à 80 % en rose avec « 80 % » au centre.",
    "const t=A.texts(sl).filter(t=>/💰/.test(t.text));const b=t.reduce((a,o)=>({x:Math.min(a.x,o.x),y:Math.min(a.y,o.y),r:Math.max(a.r,o.x+o.w),bo:Math.max(a.bo,o.y+o.h)}),{x:1e9,y:1e9,r:0,bo:0});A.hide(t);const R=70,L=2*Math.PI*R;A.div(sl,b.x,b.y,b.r-b.x,b.bo-b.y,'display:flex;align-items:center;justify-content:center',`<svg width=\"190\" height=\"190\" viewBox=\"0 0 190 190\"><circle cx=\"95\" cy=\"95\" r=\"${R}\" fill=\"none\" stroke=\"#33525F\" stroke-width=\"18\"/><circle cx=\"95\" cy=\"95\" r=\"${R}\" fill=\"none\" stroke=\"${C.pink}\" stroke-width=\"18\" stroke-dasharray=\"${L*.8} ${L}\" transform=\"rotate(-90 95 95)\"/><text x=\"95\" y=\"105\" text-anchor=\"middle\" font-family=\"Lexend\" font-weight=\"700\" font-size=\"34\" fill=\"#fff\">80%</text></svg>`)"),
  'A', "Le waffle montre la proportion exacte (80 sur 100) tout en gardant l'effet « beaucoup de cases » de l'original.", fam='Emojis')

I(18, "Bonne / mauvaise expérience : 🤩 et 😱", "L'emoji 🤩 est énorme et l'emoji gris du bas est illisible.", [108, 113, 117, 121, 125, 129], 108,
  V('Pouce haut / pouce bas', "Deux icônes au trait : pouce levé rose pour la bonne expérience, pouce baissé gris pour la mauvaise.",
    "const e=A.emojis(sl);if(e[0]){e[0].innerHTML=`<svg width=\"30\" height=\"30\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"${C.pink}\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M7 10v12\"/><path d=\"M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z\"/></svg>`;}A.imgs(sl).forEach(i=>{if(i.y>300){i.el.style.visibility='hidden';A.div(sl,i.x,i.y,i.w,i.h,'display:flex;align-items:center;justify-content:center',`<svg width=\"26\" height=\"26\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#7E949E\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M17 14V2\"/><path d=\"M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22a3.13 3.13 0 0 1-3-3.88Z\"/></svg>`)}})"),
  V('Pastilles ✓ et ✕', "Un rond rose avec une coche blanche, un rond gris avec une croix : plus net que des visages.",
    "const e=A.emojis(sl);if(e[0]){e[0].outerHTML=`<span style=\"display:inline-flex;width:30px;height:30px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center\">${A.svg('✓','line',18,'#fff',3)}</span>`;}A.imgs(sl).forEach(i=>{if(i.y>300){i.el.style.visibility='hidden';A.div(sl,i.x,i.y,i.w,i.h,'display:flex;align-items:center;justify-content:center',`<span style=\"display:inline-flex;width:26px;height:26px;border-radius:50%;background:#33525F;align-items:center;justify-content:center\">${A.svg('❌','line',22,'#B9C6CC',2).replace(/<circle[^>]*>/,'')}</span>`)}})"),
  V('Étiquettes texte', "Pas d'icône : les titres « EXCEPTIONAL » et « BAD » deviennent des étiquettes colorées lisibles.",
    "A.emojis(sl).forEach(s=>s.style.visibility='hidden');A.imgs(sl).forEach(i=>{if(i.y>300)i.el.style.visibility='hidden'});A.texts(sl).forEach(t=>{if(/^EXCEPTIONAL/.test(t.text)){t.el.querySelectorAll('span').forEach(s=>{s.style.cssText+=`;background:${C.pink};color:#fff;padding:3px 8px;border-radius:3px;font-weight:700;letter-spacing:1px`});}if(/^BAD/.test(t.text)){t.el.querySelectorAll('span').forEach(s=>{s.style.cssText+=`;background:#33525F;color:#DDE5E8;padding:3px 8px;border-radius:3px;font-weight:700;letter-spacing:1px`});}})"),
  'B', "Coche et croix disent « bien / mal » sans ambiguïté, et l'emoji gris illisible disparaît.", clip=[100, 140, 790, 420], fam='Emojis')

# ---------------- 2. Sommaires, intercalaires, étiquettes ----------------
NUM = ".agenda{counter-reset:c}.agenda .it{counter-increment:c}"
BR = "sl.querySelectorAll('.agenda .it br, .est .firm br').forEach(b=>b.replaceWith(' '));"
I(19, "Sommaire : chevrons creux", "Les chevrons vides au trait gris font maquette ; les questions sont petites et pâles.", [4], 4,
  V('Numéros roses + filet', "Chaque chapitre a son numéro 01-12 en rose, un filet fin au-dessus, texte blanc un peu plus grand.", js=BR, css=NUM + "S .agenda .chev{display:none}S .agenda{row-gap:34px;column-gap:24px;grid-template-columns:repeat(4,140px)}S .agenda .it{border-top:1px solid #33525F;padding-top:12px;font-size:9pt;color:#fff;text-align:left}S .agenda .it::before{content:counter(c,decimal-leading-zero);display:block;font:700 15pt Lexend;color:#FB0161;margin-bottom:4px}"),
  V('Chevrons pleins numérotés', "Les chevrons deviennent pleins (bleu plus clair) avec le numéro dedans : on lit une progression.", js=BR, css=NUM + "S .agenda .chev{position:relative;height:24px}S .agenda .chev path{fill:#123F57;stroke:none}S .agenda .chev::after{content:counter(c,decimal-leading-zero);position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:700 9pt Lexend;color:#E7CDA8}S .agenda .it{font-size:8.5pt}"),
  V('Liste en deux colonnes', "Un vrai sommaire de rapport : deux colonnes, numéro rose à gauche, question sur une ligne.", js=BR, css=NUM + "S .agenda .chev{display:none}S .agenda{grid-template-columns:repeat(2,320px);row-gap:0;column-gap:56px;grid-auto-flow:column;grid-template-rows:repeat(6,auto)}S .agenda .it{text-align:left;display:flex;gap:14px;align-items:baseline;font-size:10pt;color:#fff;border-bottom:1px solid #1E4558;padding:11px 0}S .agenda .it::before{content:counter(c,decimal-leading-zero);font:700 10pt Lexend;color:#FB0161;width:22px}"),
  'C', "Un sommaire en liste se lit comme une table des matières : c'est ce qu'un lecteur de rapport attend.", fam='Sommaire')

I(20, "Rappel du sommaire à chaque chapitre", "Le cadre rose épais écrase tout et les 11 autres chapitres à 25 % sont illisibles.", [5, 26, 40, 53, 86, 100, 131, 146, 155, 170, 191, 203], 26,
  V('Sans cadre, autres à 45 %', "On enlève le cadre rose ; les autres chapitres restent lisibles (45 %), le chapitre en cours est en rose.", css="S .agenda-frame{border:none;box-shadow:none}S .agenda .it.off{opacity:.45}S .agenda .it.on{color:#fff;font-weight:700}"),
  V('Grand numéro de chapitre', "Une page de chapitre : « 02 » en très grand rose, la question en titre, et une barre de progression de 12 segments.",
    "const its=[...sl.querySelectorAll('.agenda .it')];const i=its.findIndex(e=>e.classList.contains('on'));const q=its[i].innerHTML.replace(/<br\\s*\\/?>/g,' ').replace(/<[^>]+>/g,'');const body=sl.querySelector('.body');body.innerHTML=`<div style=\"display:flex;flex-direction:column;align-items:center;gap:14px\"><div style=\"font:700 96pt Lexend;color:#FB0161;line-height:1\">${String(i+1).padStart(2,'0')}</div><div style=\"font:700 22pt Lexend;color:#E7CDA8;text-align:center;max-width:560px;text-wrap:balance\">${q}</div><div style=\"display:flex;gap:6px;margin-top:18px\">${its.map((e,j)=>`<span style=\"width:34px;height:5px;border-radius:3px;background:${j==i?'#FB0161':j<i?'#7E949E':'#1E4558'}\"></span>`).join('')}</div><div style=\"font:500 8pt Lexend;letter-spacing:3px;color:#7E949E\">CHAPTER ${i+1} OF ${its.length}</div></div>`"),
  V('Cadre fin et arrondi', "Le cadre devient un filet crème fin à coins arrondis ; les autres chapitres à 40 %.", css="S .agenda-frame{border:1px solid rgba(231,205,168,.35);border-radius:14px;box-shadow:none}S .agenda .it.off{opacity:.4}"),
  'B', "Une vraie page de chapitre marque la respiration du deck ; la grille de 12 chevrons répétée 12 fois lasse.", fam='Sommaire')

I(21, "Intercalaires de segment (Pain points…)", "Quatre flèches pointillées qui pointent vers le centre : décor sans sens, et beaucoup de vide.", [62, 66, 70, 74, 78, 82, 106, 110, 115, 119, 123, 127], 62,
  V('Sans flèches, filet rose', "On enlève les 4 flèches ; un petit filet rose sous le texte suffit à poser la page.",
    "A.hide(A.shapes(sl).filter(s=>s.dash));const t=A.texts(sl).filter(t=>t.y>150&&t.y<480).sort((a,b)=>b.y-a.y)[0];if(t){const r=document.createRange();r.selectNodeContents(t.el);const q=r.getBoundingClientRect(),R=sl.getBoundingClientRect();A.div(sl,480-28,q.bottom-R.top+18,56,3,'background:#FB0161;border-radius:2px');}"),
  V('Flèches pleines roses courtes', "On garde l'idée « on zoome sur un segment » mais avec 4 flèches roses pleines, courtes et nettes.",
    "A.shapes(sl).filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','2.5');s.el.querySelectorAll('marker path').forEach(m=>m.setAttribute('fill',C.pink));})"),
  V('Étiquette en pastille', "Sans flèches ; le petit mot « PAIN POINTS » devient une pastille rose au-dessus du titre.",
    "A.hide(A.shapes(sl).filter(s=>s.dash));A.texts(sl).filter(t=>/^(PAIN POINTS|VALUE CREATION)$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(s=>{s.style.cssText+=';background:#FB0161;color:#fff;padding:4px 12px;border-radius:3px;font-weight:700;letter-spacing:.25em'}))"),
  'A', "Le titre se suffit ; les flèches pointillées étaient le seul élément « bricolé » de la page.", fam='Sommaire')

I(22, "Pastille rose « SIGNAL »", "Le bloc rose plein sous le titre crie plus fort que le titre lui-même.", [33, 34, 35, 36, 37, 38, 39, 7], 33,
  V('Pastille au trait', "Même pastille, mais seulement le contour rose et le texte rose : plus élégant.", css="S .pill{background:none;border:1px solid #FB0161;color:#FB0161;padding:4px 0 4px .42em}"),
  V('Mot rose entre deux filets', "Le mot SIGNAL en rose, encadré de deux petits filets : un sur-titre de magazine.", css="S .pill{background:none;color:#FB0161;width:auto;padding:0 .42em 0 .84em;position:relative}S .pill::before,S .pill::after{content:'';position:absolute;top:50%;width:28px;height:1px;background:#FB0161}S .pill::before{right:100%}S .pill::after{left:100%}"),
  V('Pastille sombre + point rose', "Pastille bleu nuit claire, texte crème, avec un point rose devant : discret mais présent.", css="S .pill{background:#123F57;color:#E7CDA8;border-radius:20px}S .pill::before{content:'';display:inline-block;width:7px;height:7px;border-radius:50%;background:#FB0161;margin-right:10px;vertical-align:1px}"),
  'B', "Le sur-titre entre filets annonce la nature de la page sans voler la vedette au titre.", clip=[140, 15, 680, 175], fam='Sommaire')

# ---------------- 3. KPI, tableaux à gabarit ----------------
I(23, "KPI : grosses flèches roses", "Les flèches pleines roses font clipart et alourdissent les chiffres.", [33], 33,
  V('Petit triangle rose', "Un petit triangle ▲ rose à côté du chiffre : le sens se lit, le chiffre domine.", css="S .kpis .arr{width:14px;height:12px;clip-path:polygon(50% 0,100% 100%,0 100%)}"),
  V('Pastille de variation', "Une pastille rose pâle avec une flèche fine : comme dans un tableau de bord financier.", css="S .kpis .arr{width:30px;height:30px;border-radius:50%;background:rgba(251,1,97,.15);clip-path:none;position:relative}S .kpis .arr::after{content:'';position:absolute;left:9px;top:9px;border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:10px solid #FB0161}"),
  V('Flèche fine crème', "Une flèche au trait fin crème : sobre, cohérente avec les autres traits du deck.", css="S .kpis .arr{width:16px;height:34px;background:none;clip-path:none;position:relative}S .kpis .arr::after{content:'';position:absolute;left:7px;top:2px;bottom:0;width:2px;background:#E7CDA8}S .kpis .arr::before{content:'';position:absolute;left:2px;top:0;width:8px;height:8px;border-left:2px solid #E7CDA8;border-top:2px solid #E7CDA8;transform:rotate(45deg);transform-origin:center;margin-left:1px;margin-top:2px}"),
  'B', "La pastille de variation est le code visuel connu des investisseurs pour « en hausse ».", clip=[120, 180, 760, 380], fam='Graphiques')

I(24, "KPI : l'accolade grise", "L'accolade fine grise est vieillotte et sépare mal l'explication.", [33, 9, 19, 37, 45, 51, 90], 33,
  V('Simple filet vertical', "L'accolade devient un filet vertical fin : séparation nette, sans fioriture.", css="S .kpis .brace{width:1px;background:#33525F}S .kpis .brace path{display:none}"),
  V('Accolade rose fine', "On garde l'accolade mais en rose, un peu plus fine : elle devient un élément de la charte.", css="S .kpis .brace path{stroke:#FB0161;stroke-width:1.2}"),
  V('Explication en encart', "Plus d'accolade : l'explication passe dans un encart avec une bordure rose à gauche.", css="S .kpis .brace{display:none}S .kpis .why{background:#0B3850;border-left:3px solid #FB0161;padding:16px 18px;border-radius:0 8px 8px 0;text-align:left;color:#C9D4D8}"),
  'C', "L'encart rend l'explication lisible comme une note d'analyste, et l'accolade disparaît de tout le deck.", clip=[120, 180, 760, 380], fam='Graphiques')

I(25, "Tableau des estimations : en-têtes invisibles", "FIRM / MARKET SIZE / COMMENTS sont presque de la couleur du fond.", [42, 50], 42,
  V('En-têtes crème espacés', "En-têtes en crème, petites capitales espacées, filet fin dessous : le tableau a une tête.", css="S .est .h{color:#E7CDA8;letter-spacing:.18em;font-size:7.5pt;border-bottom-color:#33525F}"),
  V('En-têtes roses', "En-têtes en rose, sans filet : la structure se voit tout de suite.", css="S .est .h{color:#FB0161;font-weight:700;letter-spacing:.12em;border-bottom:none}"),
  V('Lignes séparées par des filets', "En-têtes crème et un filet fin sous chaque firme : on suit chaque ligne.", "const g=sl.querySelector('.est');const cells=[...g.children].filter(c=>!c.classList.contains('h'));for(let i=0;i<cells.length;i+=4){if((i/4)%2==0)cells.slice(i,i+4).forEach(c=>c.style.background='#0B3850')}", css="S .est .h{color:#E7CDA8;letter-spacing:.18em;font-size:7.5pt}S .est{row-gap:0}S .est>div:not(.h){padding-top:12px;padding-bottom:12px;align-self:stretch;display:flex;align-items:center}"),
  'A', "Le tableau redevient lisible sans ajouter de couleur.", clip=[60, 150, 840, 420], fam='Tableaux')

I(26, "Tableau des estimations : petites flèches grises", "Les flèches grises entre la firme et le chiffre ne servent à rien.", [42, 50], 42,
  V('Supprimées', "On enlève les flèches ; l'alignement suffit.", css="S .est .ar{visibility:hidden}"),
  V('Pointillés de liaison', "Une ligne de points fins, comme une table des matières : l'œil va de la firme au chiffre.", css="S .est .ar{height:0;background:none;border-top:2px dotted #33525F}S .est .ar::after{display:none}"),
  V('Point rose', "Un petit point rose à la place de la flèche : un repère discret par ligne.", css="S .est .ar{height:6px;width:6px;border-radius:50%;background:#FB0161;justify-self:center}S .est .ar::after{display:none}"),
  'B', "Les pointillés relient visuellement la firme à son chiffre, ce que la flèche essayait de faire.", clip=[60, 150, 840, 420], fam='Tableaux')

I(27, "Tableau des estimations : noms de firmes coupés", "« Grand View / Research » sur deux lignes, en crème, à côté de chiffres en blanc gras : déséquilibré.", [42, 50], 42,
  V('Nom sur une ligne, blanc', "Nom de la firme sur une seule ligne, en blanc : chaque ligne du tableau a la même hauteur.", js=BR, css="S .est .firm br{display:none}S .est .firm{white-space:nowrap;color:#fff;font-size:10.5pt}S .est{grid-template-columns:200px 30px 100px 250px}"),
  V('Nom en gras crème', "Nom sur une ligne, en gras crème : il répond au chiffre en gras.", js=BR, css="S .est .firm br{display:none}S .est .firm{white-space:nowrap;font-weight:700;font-size:10pt}S .est{grid-template-columns:200px 30px 100px 250px}"),
  V('Petites capitales', "Nom sur une ligne, en petites capitales espacées : style tableau financier.", js=BR, css="S .est .firm br{display:none}S .est .firm{white-space:nowrap;text-transform:uppercase;letter-spacing:.1em;font-size:8.5pt;color:#E7CDA8}S .est{grid-template-columns:200px 30px 100px 250px}"),
  'B', "Le gras crème donne du poids au nom sans concurrencer le chiffre.", clip=[60, 150, 840, 420], fam='Tableaux')

I(28, "Comparaison de marchés : barres creuses", "Les barres en simple contour gris font brouillon à côté de la barre EdTech pleine.", [46], 46,
  V('Barres pleines ardoise', "Les autres marchés en barres pleines bleu ardoise, EdTech en crème : comparaison franche.", css="S .cmp .bar{background:#33525F;border:none}S .cmp .tag{border:none;padding:0 4px}"),
  V('Bâtonnets à point', "Chaque marché = une ligne fine + un point au bout ; EdTech reste une barre pleine. Très épuré.", css="S .cmp .bw:not(.hl) .bar{height:2px;background:#4A6470;border:none;position:relative}S .cmp .bw:not(.hl) .bar::after{content:'';position:absolute;right:-5px;top:-4px;width:10px;height:10px;border-radius:50%;background:#7E949E}S .cmp .bw:not(.hl) .tag{border:none;margin-left:6px}"),
  V('Barres crème transparentes', "Toutes les barres pleines dans la même couleur crème, mais les autres à 25 % : EdTech ressort seul.", css="S .cmp .bw:not(.hl) .bar{background:rgba(231,205,168,.25);border:none}S .cmp .bw:not(.hl) .tag{border:none}"),
  'A', "Des barres pleines se comparent d'un coup d'œil ; le contour seul obligeait à deviner.", clip=[60, 140, 840, 380], fam='Graphiques')

I(29, "Catégories : barres dans des boîtes pointillées", "Les boîtes pointillées vides au-dessus des barres font maquette.", [47], 47,
  V('Boîtes pleines discrètes', "La boîte devient un fond bleu légèrement plus clair, sans pointillés : on voit le « reste » sans bruit.", css="S .catbars .box{border:none;background:#0B3850;border-radius:4px 4px 0 0}"),
  V('Sans boîte, ligne de base', "Juste les barres sur une ligne de base fine : un vrai histogramme.", css="S .catbars .box{border:none;border-bottom:1px solid #4A6470}"),
  V('Barres arrondies sans boîte', "Barres seules aux coins arrondis en haut, avec le pourcentage au-dessus.", css="S .catbars .box{border:none}S .catbars .fill{border-radius:6px 6px 0 0}"),
  'B', "L'histogramme simple est la forme la plus lisible pour comparer 5 montants.", clip=[150, 130, 660, 420], fam='Graphiques')

I(30, "Matrice de priorité : les « +++ »", "Les + en texte s'alignent mal et se lisent comme du code.", [65, 69, 73, 77, 81, 85], 65,
  V('Points de taille croissante', "+ = petit point, ++ = moyen, +++ = gros point rose : l'intensité se voit d'un coup.",
    "sl.querySelectorAll('.prio .sc').forEach(c=>{const v=c.textContent.length;const s=[0,7,11,16][v];c.innerHTML=`<span style=\"display:inline-block;width:${s}px;height:${s}px;border-radius:50%;background:${v==3?C.pink:v==2?'#7E949E':'#4A6470'}\"></span>`})"),
  V('Mini-jauges', "Trois petits segments par case, remplis selon le score (rose pour le max).",
    "sl.querySelectorAll('.prio .sc').forEach(c=>{const v=c.textContent.length;c.innerHTML=`<span style=\"display:inline-flex;gap:3px\">${[1,2,3].map(i=>`<i style=\"display:block;width:9px;height:9px;border-radius:2px;background:${i<=v?(v==3?C.pink:'#9FB0B7'):'#1E4558'}\"></i>`).join('')}</span>`})"),
  V('Cases de chaleur', "Chaque case est colorée selon le score : bleu, bleu clair, rose. Une vraie heatmap.",
    "sl.querySelectorAll('.prio .sc').forEach(c=>{const v=c.textContent.length;c.textContent='';c.style.cssText+=`;align-self:stretch;margin:3px;border-radius:4px;background:${['','#123F57','#2E5568','#FB0161'][v]}`})"),
  'A', "Les points de taille variable se lisent comme une intensité, sans compter les +.", clip=[100, 120, 760, 400], fam='Tableaux')

I(31, "Matrice de priorité : HIGH / CRITICAL / MAJOR", "Les niveaux de priorité sont tous du même blanc ; CRITICAL ne ressort pas.", [65, 69, 73, 77, 81, 85], 65,
  V('Pastilles graduées', "CRITICAL en rose plein, MAJOR en contour rose, HIGH en gris : la hiérarchie saute aux yeux.",
    "sl.querySelectorAll('.prio .pr').forEach(p=>{const t=p.textContent.trim();const st=t=='CRITICAL'?'background:#FB0161;color:#fff':t=='MAJOR'?'border:1px solid #FB0161;color:#FB0161':'background:#1E4558;color:#C9D4D8';p.innerHTML=`<span style=\"${st};padding:3px 9px;border-radius:10px;font-size:7pt;letter-spacing:.08em\">${t}</span>`})"),
  V('Seul CRITICAL en rose', "On garde le texte, sans flèche ; seul CRITICAL passe en rose.", "sl.querySelectorAll('.prio .pr').forEach(p=>{p.querySelector('i').style.display='none';if(p.textContent.trim()=='CRITICAL')p.style.color=C.pink})"),
  V('Point de couleur', "Un point coloré avant le mot (rose / rose pâle / gris), sans flèche.",
    "sl.querySelectorAll('.prio .pr').forEach(p=>{const t=p.textContent.trim();p.querySelector('i').outerHTML=`<i style=\"width:8px;height:8px;border-radius:50%;background:${t=='CRITICAL'?C.pink:t=='MAJOR'?'#F77FA8':'#7E949E'}\"></i>`})"),
  'A', "Trois niveaux, trois styles : on voit les urgences sans lire.", clip=[100, 120, 760, 400], fam='Tableaux')

a, b, c = emo3(16, 11, 18)
I(32, "Matrice de priorité : emojis en tête de colonnes", "Les têtes de colonnes sont des emojis minuscules et les mots PAIN POINT / PRIORITY sont invisibles.", [65, 69, 73, 77, 81, 85], 65,
  V(a['name'], a['desc'] + " Et les en-têtes passent en crème.", a['js'], "S .prio .h{color:#9FB0B7}"), V(b['name'], b['desc'] + " Et les en-têtes passent en crème.", b['js'], "S .prio .h{color:#9FB0B7}"),
  V(c['name'], c['desc'] + " Et les en-têtes passent en crème.", c['js'], "S .prio .h{color:#9FB0B7}"), 'B', "La pastille donne une vraie tête de colonne ; les en-têtes deviennent lisibles.", clip=[100, 120, 760, 160], fam='Tableaux')

I(33, "Avant / après d'une startup (Preply, Gizmo…)", "Dix cadres roses épais à droite : la colonne entière clignote.", [210, 211, 212, 213, 214], 210,
  V('Bordure rose à gauche seulement', "Chaque ligne de droite garde un trait rose à gauche, le reste du cadre disparaît.", css="S .contrast .b{border:none;border-left:3px solid #FB0161;border-radius:0;background:#0B3850}S .contrast .a{border:none;background:rgba(255,255,255,.03)}"),
  V('Fond rose très pâle', "Les lignes de droite ont un fond rose à 12 %, sans bordure ; celles de gauche, rien.", css="S .contrast .b{border:none;background:rgba(251,1,97,.13)}S .contrast .a{border:none;border-bottom:1px solid #1E4558;border-radius:0;box-shadow:none}"),
  V('Coche rose en début de ligne', "Plus de cadres : une coche rose devant chaque ligne de droite, une croix grise devant celles de gauche.", "sl.querySelectorAll('.contrast .b').forEach(b=>b.insertAdjacentHTML('afterbegin',`<span style=\"color:${C.pink};font-weight:700;margin-right:8px\">✓</span>`));sl.querySelectorAll('.contrast .a').forEach(b=>b.insertAdjacentHTML('afterbegin','<span style=\"color:#4A6470;margin-right:8px\">✕</span>'))", css="S .contrast .b,S .contrast .a{border:none;box-shadow:none;border-bottom:1px solid #1E4558;border-radius:0}"),
  'A', "Le trait rose garde l'idée « côté gagnant » sans dix rectangles qui vibrent.", clip=[40, 150, 880, 420], fam='Tableaux')

# ---------------- 4. Frises, flux, cartes ----------------
RAIL = "const sh=A.shapes(sl);const rail=sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<14);const ticks=sh.filter(s=>s.stroke==='#789096'&&s.h<22&&s.w>30&&s.w<50);const R=rail.sort((a,b)=>b.h-a.h)[0];if(!R)return;const cx=R.cx;A.hide(rail);const y0=ticks.length?Math.min(...ticks.map(t=>t.cy)):R.y,y1=ticks.length?Math.max(...ticks.map(t=>t.cy)):R.y+R.h;"
I(34, "Frises d'actualité : rail rose épais", "La barre rose de 11 px, avec ses petits carrés en haut et sa flèche, écrase les dates.", [92, 93, 134, 150, 156, 157, 176, 177, 184, 192, 195, 204, 205], 92,
  V('Rail fin + points roses', "Un trait rose de 2 px et un point rose à chaque date : la frise devient légère.",
    RAIL + "A.div(sl,cx-1,y0-14,2,y1-y0+28,'background:#FB0161');ticks.forEach(t=>{A.hide([t]);A.div(sl,cx-5,t.cy-5,10,10,'border-radius:50%;background:#FB0161;box-shadow:0 0 0 3px #062A3C')})"),
  V('Rail ardoise, dates roses', "Le rail devient ardoise fin avec des ronds creux ; ce sont les dates qui passent en rose.",
    RAIL + "A.div(sl,cx-1,y0-14,2,y1-y0+28,'background:#33525F');ticks.forEach(t=>{A.hide([t]);A.div(sl,cx-6,t.cy-6,12,12,'border-radius:50%;background:#062A3C;border:2px solid #FB0161;box-sizing:border-box')});A.texts(sl).filter(t=>/^\\d{4}/.test(t.text)&&t.x<300).forEach(t=>A.color(t,C.pink))"),
  V('Sans rail, dates en pastilles', "Plus de rail : chaque date devient une petite pastille rose, alignée avec son texte.",
    RAIL + "A.hide(ticks);A.texts(sl).filter(t=>/^\\d{4}/.test(t.text)&&t.x<300).forEach(t=>t.el.querySelectorAll('span').forEach(s=>s.style.cssText+=';background:#FB0161;color:#fff;padding:3px 9px;border-radius:10px'))"),
  'A', "Le rail fin garde l'idée de frise et laisse respirer les dates et les textes.", clip=[100, 150, 700, 440], fam='Frises')

I(35, "Frises de phases (1997-2007 … TODAY)", "Flèche rose épaisse au-dessus de cases au trait gris : beaucoup de traits pour peu d'info.", [54, 91, 133, 138, 147, 174], 54,
  V('Flèche fine, cases pleines', "Flèche rose de 3 px ; cases pleines bleu clair sans bord ; TODAY garde un bord rose.",
    "const sh=A.shapes(sl);const ar=sh.find(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<30&&s.w>300);if(ar){A.hide([ar]);A.div(sl,ar.x,ar.cy-1.5,ar.w-10,3,'background:#FB0161;border-radius:2px');A.div(sl,ar.x+ar.w-14,ar.cy-7,0,0,'border-left:14px solid #FB0161;border-top:7px solid transparent;border-bottom:7px solid transparent')}sh.filter(s=>s.h>150&&s.stroke).forEach(s=>{if(s.stroke.toUpperCase()==='#FB0161'){s.p.setAttribute('fill','#0B3850');s.p.setAttribute('stroke-width','2')}else{s.p.setAttribute('fill','#0B3850');s.p.setAttribute('stroke','none')}})"),
  V('Bandeau de couleur en haut', "Cases pleines sans bord, avec un bandeau en haut : ardoise pour le passé, rose pour TODAY.",
    "const sh=A.shapes(sl);sh.filter(s=>s.h>150&&s.stroke).forEach(s=>{const pk=s.stroke.toUpperCase()==='#FB0161';s.p.setAttribute('fill','#0B3850');s.p.setAttribute('stroke','none');A.div(sl,s.x+2,s.y,s.w-4,4,`background:${pk?C.pink:s.dash?'#1E4558':'#4A6470'};border-radius:3px 3px 0 0`)})"),
  V('Frise à jalons', "La flèche devient un trait fin avec un point au-dessus de chaque case ; les cases gardent un trait très fin.",
    "const sh=A.shapes(sl);const ar=sh.find(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<30&&s.w>300);const bx=sh.filter(s=>s.h>150&&s.stroke);if(ar){A.hide([ar]);A.div(sl,ar.x,ar.cy-1,ar.w,2,'background:#33525F');bx.forEach(s=>A.div(sl,s.cx-6,ar.cy-6,12,12,`border-radius:50%;background:${s.stroke.toUpperCase()==='#FB0161'?C.pink:'#7E949E'}`))}bx.forEach(s=>{if(s.stroke.toUpperCase()!=='#FB0161')s.p.setAttribute('stroke','#1E4558')})"),
  'B', "Le bandeau de couleur dit « passé / aujourd'hui » sans cadre ni flèche massive.", clip=[130, 200, 700, 300], fam='Frises')

I(36, "Flux d'argent : numéros dans des ronds gris", "Les numéros des étapes sont dans de petits ronds gris quasi invisibles.", [109, 114, 118, 122, 126, 130], 109,
  V('Ronds roses pleins', "Les ronds deviennent roses pleins, numéros blancs en gras : on suit l'ordre 1 → 8.",
    "A.shapes(sl).filter(s=>s.w<32&&s.h<32&&s.fill==='#062A3C').forEach(s=>{s.p.setAttribute('fill',C.pink);s.p.setAttribute('stroke','none')});A.texts(sl).filter(t=>/^\\d$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(x=>{x.style.color='#fff';x.style.fontWeight='700'}))"),
  V('Ronds au trait rose', "Ronds bleu nuit bordés de rose, numéros roses ; les flèches passent aussi en rose.",
    "A.shapes(sl).filter(s=>s.w<32&&s.h<32&&s.fill==='#062A3C').forEach(s=>s.p.setAttribute('stroke',C.pink));A.shapes(sl).filter(s=>s.stroke==='#789096').forEach(s=>{s.p.setAttribute('stroke',C.pink);s.el.querySelectorAll('marker path').forEach(m=>m.setAttribute('fill',C.pink))});A.texts(sl).filter(t=>/^\\d$/.test(t.text)).forEach(t=>A.color(t,C.pink))"),
  V('Gros numéros sans rond', "Plus de rond : un « 01 » rose en gras dans le coin de chaque carte.",
    "A.hide(A.shapes(sl).filter(s=>s.w<32&&s.h<32&&s.fill==='#062A3C'));A.texts(sl).filter(t=>/^\\d$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(x=>{x.textContent='0'+x.textContent;x.style.whiteSpace='nowrap';x.closest('.rx-t').style.width='40px';x.style.color=C.pink;x.style.fontWeight='700';x.style.fontSize='11pt'}))"),
  'A', "Le rond rose plein guide l'œil dans la boucle ; c'est le seul repère d'ordre de la slide.", clip=[100, 220, 740, 330], fam='Frises')

CARDS = "const bx=A.shapes(sl).filter(s=>s.stroke==='#334D54'&&!s.line&&s.w>90&&s.h>40);"
I(37, "Toutes les cartes : bord gris fin", "Les cartes au trait gris 1 px paraissent ternes et mal finies sur le fond bleu.", [22, 31, 56, 57, 109, 136, 142, 153, 172, 186, 207, 208], 22,
  V('Cartes pleines, sans bord', "Les cartes deviennent un aplat bleu un peu plus clair, sans contour : plus moderne.", CARDS + "bx.forEach(s=>{s.p.setAttribute('fill','#0E3D55');s.p.setAttribute('stroke','none')})"),
  V('Bord crème très léger', "Bord crème à 20 % et fond très légèrement éclairci : les cartes ont du relief sans peser.", CARDS + "bx.forEach(s=>{s.p.setAttribute('fill','#08314A');s.p.setAttribute('stroke','rgba(231,205,168,.22)')})"),
  V('Liseré rose en haut', "Carte pleine sans bord, avec un fin liseré rose en haut : un rappel de la charte sur chaque carte.", CARDS + "bx.forEach(s=>{s.p.setAttribute('fill','#0B3850');s.p.setAttribute('stroke','none');A.div(sl,s.x+12,s.y,s.w-24,2,'background:#FB0161;border-radius:2px')})"),
  'A', "L'aplat sans bord est plus net et laisse le contenu respirer ; c'est le style des rapports modernes.", fam='Cartes')

I(38, "Bulles en pointillés", "Les contours pointillés font « brouillon » sur les douleurs, les prix et les frises.", [13, 29, 30, 54, 64, 68, 72, 76, 80, 84, 91, 133], 64,
  V('Aplat sans bord', "Les bulles deviennent des aplats bleu clair, sans pointillés.", "A.shapes(sl).filter(s=>s.dash&&!s.line).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0B3850')})"),
  V('Trait plein fin', "Les pointillés deviennent un trait plein fin : même dessin, propre.", "A.shapes(sl).filter(s=>s.dash&&!s.line).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#2A4A58')})"),
  V('Aplat + bord gauche rose', "Aplat bleu clair et un trait rose à gauche : la douleur est « marquée ».", "A.shapes(sl).filter(s=>s.dash&&!s.line).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0B3850');A.div(sl,s.x,s.y+10,3,s.h-20,'background:#FB0161;border-radius:2px')})"),
  'A', "L'aplat garde la forme de la bulle sans le côté inachevé des pointillés.", fam='Cartes')

XS = "const xs=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<32&&s.h<32&&s.w>18);"
I(39, "Grosses croix roses en coin", "Les croix roses épaisses en haut à gauche des cases attirent l'œil plus que le texte.", [56, 57, 94, 95, 96], 56,
  V('Petite croix dans un rond', "Une petite croix rose dans un rond au trait : on garde le sens « problème », en discret.",
    XS + "A.hide(xs);xs.forEach(s=>A.div(sl,s.cx-10,s.cy-10,20,20,'border-radius:50%;border:1.5px solid #FB0161;background:#062A3C;display:flex;align-items:center;justify-content:center;color:#FB0161;font:700 10px Lexend','✕'))"),
  V('Barre rose à gauche', "Plus de croix : la case « problème » porte un trait rose vertical à gauche.",
    XS + "A.hide(xs);const bx=A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>100);xs.forEach(x=>{const b=bx.filter(b=>b.x>x.x-5&&Math.abs(b.y-x.y)<30).sort((a,c)=>a.x-c.x)[0];if(b)A.div(sl,b.x,b.y+6,3,b.h-12,'background:#FB0161;border-radius:2px')})"),
  V("Croix plus petite, sur l'angle", "La croix fait 55 % de sa taille et se pose pile sur l'angle de la case.",
    XS + "xs.forEach(s=>{s.el.style.transform='scale(.55)';s.el.style.transformOrigin='center'})"),
  'B', "Le trait rose marque les cases problème sans les dix croix qui dominent la slide.", fam='Cartes')

I(40, "Conflits : flèches doubles + croix rose", "Les flèches grises doubles barrées d'une croix rose énorme sont confuses.", [140], 140,
  V('Pastille « VS »', "On remplace flèches et croix par une petite pastille « VS » au trait rose.",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill==='#789096'||(s.fill&&s.fill.toUpperCase()==='#FB0161')));sh.filter(s=>s.fill==='#789096').forEach(s=>A.div(sl,s.cx-17,s.cy-11,34,22,'border:1.5px solid #FB0161;border-radius:11px;background:#062A3C;color:#FB0161;font:700 8pt Lexend;display:flex;align-items:center;justify-content:center','VS'))"),
  V('Trait fin + éclair', "Un trait fin ardoise entre les deux cases avec un petit éclair rose au milieu : le conflit.",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill==='#789096'||(s.fill&&s.fill.toUpperCase()==='#FB0161')));sh.filter(s=>s.fill==='#789096').forEach(s=>{A.div(sl,s.x,s.cy-.5,s.w,1,'background:#4A6470');A.div(sl,s.cx-11,s.cy-11,22,22,'border-radius:50%;background:#062A3C;display:flex;align-items:center;justify-content:center',A.svg('💥','line',18,C.pink,2))})"),
  V('Signe ≠ rose', "Un simple signe ≠ rose entre les deux positions : « ils ne veulent pas la même chose ».",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill==='#789096'||(s.fill&&s.fill.toUpperCase()==='#FB0161')));sh.filter(s=>s.fill==='#789096').forEach(s=>A.div(sl,s.cx-12,s.cy-14,24,28,'color:#FB0161;font:700 20pt Lexend;display:flex;align-items:center;justify-content:center;line-height:1','≠'))"),
  'A', "« VS » est le mot exact de la question (où ils s'affrontent), lisible à toute taille.", clip=[100, 190, 760, 380], fam='Cartes')

UNDER = "const mk=(x,y,w,h,css,inner)=>{const d=A.div(sl,x,y,w,h,css,inner||'');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild);return d};"
I(41, "Pastilles numérotées carrées", "Les numéros dans des carrés roses pleins font « post-it ».", [32], 32,
  V('Ronds roses', "Les carrés deviennent des ronds roses de même taille.",
    UNDER + "A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>{A.hide([s]);mk(s.cx-14,s.cy-14,28,28,'border-radius:50%;background:#FB0161')})"),
  V('Ronds au trait rose', "Ronds bleu nuit bordés de rose, chiffre rose.",
    UNDER + "A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40).forEach(s=>{A.hide([s]);mk(s.cx-14,s.cy-14,28,28,'border-radius:50%;background:#062A3C;border:1.5px solid #FB0161;box-sizing:border-box')});A.texts(sl).filter(t=>/^\\d$/.test(t.text)).forEach(t=>A.color(t,C.pink))"),
  V('Chiffre seul en grand', "Plus de pastille : un grand chiffre rose posé sur le bord de la carte.",
    "A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40));A.texts(sl).filter(t=>/^\\d$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(x=>{x.style.color=C.pink;x.style.fontSize='18pt';x.style.fontWeight='700';x.style.background='#062A3C';x.style.padding='0 4px'}))"),
  'A', "Le rond est la forme standard d'une pastille numérotée ; même couleur, plus doux.", clip=[90, 200, 780, 320], fam='Cartes')

I(42, "Forces du marché : cercle MARKET et flèches", "Le gros cercle rose, les flèches roses éparpillées et les courbes pointillées font désordre.", [151], 151,
  V('Courbes pleines, sans flèches', "Les courbes deviennent pleines et fines, les petites flèches roses disparaissent.",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40));sh.filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#4A6470');s.p.setAttribute('stroke-width','1.2')})"),
  V('Cercle au trait', "Le cercle MARKET devient un anneau rose (fond bleu), courbes pleines ardoise, sans flèches.",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40));sh.filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#4A6470')});sh.filter(s=>s.w>120&&s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>{s.p.setAttribute('fill','#0B3850');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','4')})"),
  V('Courbes roses fines', "Courbes pleines roses fines qui partent du cercle vers chaque force, sans petites flèches.",
    "const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40));sh.filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','1.3')})"),
  'C', "Les courbes roses relient vraiment le marché à chaque force ; les flèches isolées ne reliaient rien.", fam='Schémas')

# ---------------- 5. Pictos restants, cadres, schémas ----------------
PINKB = "const pb=A.shapes(sl).filter(s=>s.stroke&&s.stroke.toUpperCase()==='#FB0161'&&s.h<34&&s.w>80);"
I(43, "Noms de startups dans des cadres roses", "Les noms (YOODLI, GIZMO…) sont dans des cadres roses épais qui vibrent.", [175, 188], 175,
  V('Étiquette rose pleine', "Le cadre devient une étiquette rose pleine, nom en blanc.", PINKB + r"pb.forEach(s=>{s.p.setAttribute('fill',C.pink);s.p.setAttribute('stroke-width','1')});A.texts(sl).filter(t=>/^[A-Z][A-Z0-9 ]+$/.test(t.text)&&t.h<34).forEach(t=>A.color(t,'#fff'))"),
  V('Nom rose, sans cadre', "Plus de cadre : le nom en rose, en gras, aligné sur la carte.", PINKB + r"A.hide(pb);A.texts(sl).filter(t=>/^[A-Z][A-Z0-9 ]+$/.test(t.text)&&t.h<34).forEach(t=>A.color(t,C.pink))"),
  V('Pastille bleu clair', "Le nom dans une pastille bleu clair arrondie, texte crème : intégré à la carte.", PINKB + r"pb.forEach(s=>{s.p.setAttribute('fill','#123F57');s.p.setAttribute('stroke','none')})"),
  'A', "L'étiquette pleine se lit comme un nom de marque ; le cadre épais faisait bouton cliquable.", fam='Cartes')

for (i, n, scope, t, w, mine, why) in [
    (44, 98, [98], "Fusées 🚀 sur chaque startup", "Huit fusées emoji identiques : décor sans info.", 'B', "La pastille discrète garde le rythme sans le côté emoji."),
    (45, 103, [103, 104], "Diamants 💎 devant chaque source de valeur", "Le diamant emoji bleu clair détonne dans la charte.", 'B', "La pastille au trait est sobre et cohérente avec les autres slides."),
    (46, 200, [200], "Têtes de mort 💀", "Les têtes de mort emoji font gadget sur une slide sérieuse sur les échecs.", 'C', "L'icône rose bicolore reste parlante sans le côté cartoon."),
    (47, 206, [206], "Trophées 🏆", "Les trophées emoji jaunes sortent de la charte.", 'C', "En rose bicolore, le trophée devient un picto de la charte."),
    (48, 141, [141], "Cadenas 🔒 sur les lignes pointillées", "Dix cadenas emoji jaunes posés sur des pointillés : très chargé.", 'A', "Le cadenas au trait crème garde l'idée « bloqué » en discret."),
    (49, 186, [186], "Cartes moonshots", "Emojis cerveau, école, fusée : enfantin.", 'B', "Même logique que les autres grilles de cartes."),
    (50, 153, [153], "Cartes « ce qui se cumule »", "Graphique, bulle, école, flamme en emoji.", 'B', "Même logique que les autres grilles de cartes."),
    (51, 208, [208], "Cartes « comment ils ont percé » 2/2", "Pomme, bulle, étincelles, manette en emoji.", 'B', "Même logique que les autres grilles de cartes."),
]:
    a, b, c = emo3(20, 14, 22)
    I(i, t, w, scope, n, a, b, c, mine, why, fam='Emojis')

I(52, "Pastilles vertes 🟢 « problème réglé »", "Le vert n'existe nulle part ailleurs dans la charte.", [55, 145], 55,
  V('Coche rose dans un rond', "Une coche blanche dans un rond rose.", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex;width:20px;height:20px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center'>${A.svg('✓','line',13,'#fff',3)}</span>`})"),
  V('Coche crème au trait', "Une coche fine crème, sans rond.", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex'>${A.svg('✓','line',20,C.cream,2.5)}</span>`})"),
  V('Rond au trait rose + coche', "Rond bleu nuit bordé de rose, coche rose.", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex;width:20px;height:20px;border-radius:50%;border:1.5px solid ${C.pink};box-sizing:border-box;align-items:center;justify-content:center'>${A.svg('✓','line',12,C.pink,3)}</span>`})"),
  'A', "La coche rose dit « réglé » dans la couleur de la charte.", fam='Emojis')

I(53, "Panneaux « sens interdit » ⛔", "Les sens interdits emoji rouges font panneau routier.", [149], 149,
  V('Rond rose « moins »', "Un rond rose avec un trait blanc : « ce moteur s'est arrêté ».", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex;width:20px;height:20px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center'><i style='width:9px;height:2px;background:#fff;display:block'></i></span>`})"),
  V('Flèche descendante', "Une petite flèche descendante rose au trait : la croissance s'essouffle.", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex'>${A.svg('📉','line',20,C.pink,2)}</span>`})"),
  V('Croix grise', "Une petite croix grise : discret, le texte porte le message.", r"A.emojis(sl).forEach(sp=>{sp.outerHTML=`<span style='display:inline-flex'>${A.svg('❌','line',18,'#7E949E',2)}</span>`})"),
  'B', "La flèche descendante dit exactement « moteur à bout de souffle », le titre de la slide.", fam='Emojis')

I(54, "Tableau OUI / NON en texte", "Des YES roses et NO crème en toutes lettres : il faut lire chaque case.", [173], 173,
  V('Point rose / tiret', "YES = point rose plein, NO = petit tiret gris.", r"A.texts(sl).filter(t=>/^(YES|NO)$/.test(t.text)).forEach(t=>{const y=t.text=='YES';t.el.querySelector('p').innerHTML=`<span style='display:inline-block;${y?`width:12px;height:12px;border-radius:50%;background:${C.pink}`:'width:10px;height:2px;background:#4A6470;vertical-align:3px'}'></span>`})"),
  V('Coche rose / rien', "YES = coche rose au trait, NO = case vide.", r"A.texts(sl).filter(t=>/^(YES|NO)$/.test(t.text)).forEach(t=>{t.el.querySelector('p').innerHTML=t.text=='YES'?`<span style='display:inline-flex'>${A.svg('✓','line',16,C.pink,3)}</span>`:'&nbsp;'})"),
  V('Cases pleines', "YES = petite case rose pleine, NO = case vide au trait.", r"A.texts(sl).filter(t=>/^(YES|NO)$/.test(t.text)).forEach(t=>{const y=t.text=='YES';t.el.querySelector('p').innerHTML=`<span style='display:inline-block;width:13px;height:13px;border-radius:3px;${y?`background:${C.pink}`:'border:1px solid #33525F'}'></span>`})"),
  'A', "Le point rose se lit en une seconde sur 30 cases, sans lire un mot.", clip=[100, 180, 760, 330], fam='Tableaux')

I(55, "Étoiles roses devant les leaders", "Les étoiles roses en coin n'ajoutent rien et alourdissent.", [178], 178,
  V('Supprimées', "On enlève les étoiles : les cartes suffisent.", r"A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30))"),
  V('Trait rose à gauche', "L'étoile devient un trait rose vertical sur la case du segment.", r"const st=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30);A.hide(st);st.forEach(s=>A.div(sl,s.x-3,s.y+10,3,79,'background:#FB0161;border-radius:2px'))"),
  V('Petite couronne au trait', "Une petite couronne au trait rose : « leader ».", r"const st=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30);A.hide(st);st.forEach(s=>A.div(sl,s.x-2,s.y-2,24,24,'background:#062A3C;border-radius:50%;display:flex;align-items:center;justify-content:center',`<svg width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='#FB0161' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M2 4l3 12h14l3-12-6 7-4-7-4 7-6-7z'/><path d='M5 20h14'/></svg>`))"),
  'B', "Le trait rose relie la case au segment sans pictogramme inutile.", fam='Cartes')

WHY = r"const lab=A.texts(sl).find(t=>/^(WHY|WHAT|THE STORY)/.test(t.text));const body=A.texts(sl).filter(t=>lab&&Math.abs(t.x-lab.x)<6&&t.y>lab.y);const big=A.texts(sl).find(t=>lab&&Math.abs(t.x-lab.x)<6&&t.y<lab.y&&t.y>lab.y-90);"
I(56, "Encadré « Why it matters » des slides chiffre", "Le libellé espacé et le texte gris flottent à droite, séparés par un pointillé.", [112, 135, 137, 139, 163, 179, 180, 181, 197, 202], 112,
  V('Libellé rose', "Le libellé « WHY IT MATTERS » passe en rose : on comprend que c'est l'explication.", WHY + r"if(lab)A.color(lab,C.pink)"),
  V('Encart avec trait rose', "Libellé, chiffre et texte dans un encart bleu clair avec un trait rose à gauche ; le pointillé disparaît.", WHY + r"A.hide(A.shapes(sl).filter(s=>s.dash&&s.h>200));if(lab){const ys=[big||lab,...body].map(t=>t.y),ye=Math.max(...body.map(t=>t.y+t.h));A.add(sl,`<div style='position:absolute;left:${lab.x-18}px;top:${Math.min(...ys)-14}px;width:250px;height:${ye-Math.min(...ys)+20}px;background:#0B3850;border-left:3px solid #FB0161;border-radius:0 8px 8px 0'></div>`);const r=sl.querySelector('.raw');r.insertBefore(r.lastChild,r.firstChild)}"),
  V('Grand chiffre rose', "Le grand chiffre (2x, 3 %…) passe en rose, le libellé en crème : un vrai point d'accroche.", WHY + r"if(big)A.color(big,C.pink);if(lab)A.color(lab,C.cream)"),
  'C', "Le chiffre rose est le message de la slide ; il répond à la barre rose du graphique.", fam='Graphiques')

I(57, "Tête de profil géante", "La silhouette beige énorme mange la moitié de la slide et n'explique rien.", [152], 152,
  V('Tête retirée, cases centrées', "On enlève la tête, les flèches roses aussi ; les cinq cases se centrent en quinconce.", r"const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill==='#E7CDA8'||(s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<40)));const raw=sl.querySelector('.raw');[...raw.children].forEach(e=>{const b=A.box(e,sl);if(b.x<560&&b.y>180)e.style.transform='translateX(160px)'})"),
  V('Tête en contour fin', "La tête devient un simple contour crème fin à 40 % : présente mais légère.", r"A.shapes(sl).filter(s=>s.fill==='#E7CDA8').forEach(s=>{s.p.setAttribute('fill','none');s.p.setAttribute('stroke','rgba(231,205,168,.4)');s.p.setAttribute('stroke-width','2')})"),
  V('Tête bleu clair en fond', "La tête passe en bleu légèrement plus clair que le fond : un décor, plus un sujet.", r"A.shapes(sl).filter(s=>s.fill==='#E7CDA8').forEach(s=>s.p.setAttribute('fill','#0E3D55'))"),
  'C', "On garde l'idée « ce qui ferait grandir le marché » en image, sans que la tête vole la vedette.", fam='Schémas')

I(58, "Boucles qui s'auto-alimentent : 📈 et petites flèches roses", "Les emojis graphiques et les petits traits roses perdus rendent les boucles illisibles.", [154], 154,
  V('Icônes au trait + flèches pleines', "Icône « courbe » au trait crème, pointillés pleins ardoise, sans petits traits roses.", r"A.swap(sl,{style:'line',color:C.cream,size:22});const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'));sh.filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#4A6470')})"),
  V('Icône rose dans une pastille', "Pastille rose avec icône « boucle » blanche entre les deux cases de chaque cycle.", r"A.emojis(sl).forEach(sp=>sp.outerHTML=`<span style='display:inline-flex;width:30px;height:30px;border-radius:50%;background:${C.pink};align-items:center;justify-content:center'>${A.svg('🔁','line',16,'#fff',2.2)}</span>`);A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'))"),
  V('Boucles roses fines', "Les liaisons pointillées deviennent des courbes roses fines, emojis remplacés par de petites flèches.", r"A.emojis(sl).forEach(sp=>sp.outerHTML=`<span style='display:inline-flex'>${A.svg('🔄','line',20,C.pink,2)}</span>`);const sh=A.shapes(sl);A.hide(sh.filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'));sh.filter(s=>s.dash).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','1.2')})"),
  'B', "Le picto « boucle » dit exactement ce que montre la slide : un cercle vertueux.", fam='Schémas')

I(59, "Six cases de chiffres aux bords crème épais", "Les cadres clairs épais donnent un tableau Excel.", [160], 160,
  V('Aplats sans bord', "Six aplats bleu clair, sans contour.", r"A.shapes(sl).filter(s=>s.stroke==='#D0E1E5').forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Aplats + trait rose en haut', "Aplats sans bord avec un petit trait rose en haut de chaque case.", r"A.shapes(sl).filter(s=>s.stroke==='#D0E1E5').forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55');A.div(sl,s.x+16,s.y,40,3,'background:#FB0161;border-radius:2px')})"),
  V('Bord ardoise fin', "On garde le cadre mais en ardoise fin, plus doux.", r"A.shapes(sl).filter(s=>s.stroke==='#D0E1E5').forEach(s=>s.p.setAttribute('stroke','#33525F'))"),
  'B', "Le petit trait rose rythme la grille et donne un point d'entrée à chaque chiffre.", fam='Cartes')

I(60, "Barres dans des colonnes pointillées", "Les grandes colonnes pointillées vides au-dessus des petites barres font maquette.", [164, 187], 164,
  V('Colonnes en aplat discret', "Le « reste » devient un aplat bleu à peine plus clair.", r"A.shapes(sl).filter(s=>s.dash&&s.h>100).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0B3850')})"),
  V('Sans colonne', "On enlève les colonnes : il reste les barres sur la ligne de base.", r"A.hide(A.shapes(sl).filter(s=>s.dash&&s.h>100))"),
  V('Contour plein fin', "Les colonnes gardent leur contour, mais plein et très fin.", r"A.shapes(sl).filter(s=>s.dash&&s.h>100).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#33525F');s.p.setAttribute('stroke-width','1')})"),
  'A', "L'aplat montre toujours « la part sur le total » sans le côté brouillon.", fam='Graphiques')

I(61, "Annotations au-dessus des barres : longues flèches", "Chaque barre a une flèche blanche au-dessus d'un petit paragraphe : la slide paraît hachée.", [165, 166], 165,
  V('Sans flèche', "On enlève les flèches : chaque note se pose juste au-dessus de son montant.", r"A.hide(A.shapes(sl).filter(s=>s.stroke==='#D0E1E5'&&s.w<30))"),
  V('Filet pointillé court', "Les flèches deviennent un court filet pointillé ardoise.", r"A.shapes(sl).filter(s=>s.stroke==='#D0E1E5'&&s.w<30).forEach(s=>{s.p.setAttribute('stroke','#4A6470');s.p.setAttribute('stroke-dasharray','2 3');s.el.querySelectorAll('marker').forEach(m=>m.remove());s.p.removeAttribute('marker-end');s.p.removeAttribute('marker-start')})"),
  V('Point rose', "Un petit point rose remplace la flèche, entre la note et le montant.", r"const ar=A.shapes(sl).filter(s=>s.stroke==='#D0E1E5'&&s.w<30);A.hide(ar);ar.forEach(s=>A.div(sl,s.cx-3,s.cy-3,6,6,'border-radius:50%;background:#FB0161'))"),
  'B', "Le filet garde le lien note → barre, plus léger qu'une flèche.", fam='Graphiques')

I(62, "Tableaux : séparateurs en pointillés", "Les lignes en petits points rendent les tableaux flous.", [167, 169, 173], 167,
  V('Filets pleins fins', "Les pointillés deviennent des filets pleins très fins.", r"A.shapes(sl).filter(s=>s.dash==='1 3').forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#1E4558');s.p.setAttribute('stroke-width','1')})"),
  V('Lignes en bandes', "Plus de séparateur : une ligne sur deux a un fond légèrement plus clair.", r"const L=A.shapes(sl).filter(s=>s.dash==='1 3');A.hide(L);L.forEach((s,i)=>{if(i%2==0){const d=A.div(sl,s.x,s.cy,s.w,74,'background:#0A3044;border-radius:6px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)}})"),
  V('Filets + chiffres blancs', "Filets pleins fins, et les montants roses passent en blanc gras (le rose reste pour l'essentiel).", r"A.shapes(sl).filter(s=>s.dash==='1 3').forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#1E4558')});A.texts(sl).filter(t=>/^\$ ?\d/.test(t.text)).forEach(t=>A.color(t,'#fff'))"),
  'A', "Des filets nets structurent le tableau sans bruit.", fam='Tableaux')

I(63, "Radar à cercles épais", "Six cercles gris épais (jusqu'à 8 px) : la cible écrase les startups.", [175], 175,
  V('Cercles fins', "Cercles de 1 px, du plus clair au plus foncé : un vrai radar.", r"A.shapes(sl).filter(s=>s.w>40&&s.w===s.h&&s.stroke==='#334D54').forEach((s,i)=>{s.p.setAttribute('stroke-width','1');s.p.setAttribute('stroke',i%2?'#1E4558':'#33525F')})"),
  V('Disques dégradés', "Les cercles deviennent des disques pleins, plus clairs vers le centre.", r"A.shapes(sl).filter(s=>s.w>40&&s.w===s.h&&s.stroke==='#334D54').forEach((s,i)=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill',['#082F43','#0A344A','#0C3951','#0E3E58','#11435F','#144866'][i]||'#144866')})"),
  V('Trois cercles pointillés', "On garde trois cercles fins pointillés : plus d'air pour les points roses.", r"A.shapes(sl).filter(s=>s.w>40&&s.w===s.h&&s.stroke==='#334D54').forEach((s,i)=>{if(i%2){A.hide([s])}else{s.p.setAttribute('stroke-width','1');s.p.setAttribute('stroke-dasharray','3 4')}})"),
  'B', "Les disques dégradés donnent un vrai effet radar et font ressortir les points roses.", fam='Schémas')

I(64, "Chaîne de valeur : bandes roses", "Cinq bandes roses pleines comme des flèches : plus visibles que les leaders.", [182, 185], 182,
  V('Ligne fine + points', "Une ligne fine ardoise avec un point rose par maillon.", r"const b=A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<20);A.hide(b);const y=b[0].cy,x0=Math.min(...b.map(s=>s.x)),x1=Math.max(...b.map(s=>s.x+s.w));A.div(sl,x0,y-1,x1-x0,2,'background:#33525F');b.forEach(s=>A.div(sl,s.cx-6,y-6,12,12,'border-radius:50%;background:#FB0161;box-shadow:0 0 0 4px #062A3C'))"),
  V('Chevrons ardoise numérotés', "Les bandes deviennent ardoise avec un numéro, seule la première reste rose.", r"A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<20).sort((a,b)=>a.x-b.x).forEach((s,i)=>{if(i){s.p.setAttribute('fill','#1E4558')}A.div(sl,s.x,s.y,s.w,s.h,'display:flex;align-items:center;justify-content:center;color:#fff;font:700 7.5pt Lexend',`0${i+1}`)})"),
  V('Bandes plus fines', "Les bandes passent de 14 à 4 px de haut, collées aux titres.", r"A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.h<20).forEach(s=>{s.el.style.transform='scaleY(.3)'})"),
  'A', "Une ligne à points montre la chaîne sans écraser les textes des leaders.", fam='Schémas')

I(65, "Couches tech : cadres crème", "Les cadres crème épais sur fond bleu font boutons de formulaire.", [87, 88], 87,
  V('Aplats bleus sans bord', "Chaque couche devient un aplat bleu clair, texte crème.", r"A.shapes(sl).filter(s=>s.stroke==='#E7CDA8'&&!s.dash).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#123F57')})"),
  V('Empilement dégradé', "Les couches deviennent un empilement du plus clair (haut) au plus foncé (bas).", r"A.shapes(sl).filter(s=>s.stroke==='#E7CDA8'&&!s.dash).sort((a,b)=>a.y-b.y).forEach((s,i)=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill',['#2A5A72','#1F4D64','#164157','#10364A'][i]||'#10364A')})"),
  V('Bord ardoise + trait rose', "Bord ardoise fin et un trait rose à gauche de chaque couche.", r"A.shapes(sl).filter(s=>s.stroke==='#E7CDA8'&&!s.dash).forEach(s=>{s.p.setAttribute('stroke','#33525F');A.div(sl,s.x,s.y,3,s.h,'background:#FB0161')})"),
  'B', "Le dégradé fait sentir l'empilement des couches, c'est le sens de la slide.", fam='Schémas')

I(66, "Classement des couches : cadres roses vs crème", "Le top 3 en cadres roses épais et le reste en crème : beaucoup de cadres.", [89], 89,
  V('Top 3 en rose plein', "Le top 3 devient rose plein (texte blanc), le reste aplat bleu sans bord.", r"A.shapes(sl).filter(s=>s.w>200&&s.h<40).forEach(s=>{const pk=s.stroke.toUpperCase()==='#FB0161';s.p.setAttribute('stroke','none');s.p.setAttribute('fill',pk?C.pink:'#123F57')});A.texts(sl).filter(t=>t.w>200&&t.w<250).forEach(t=>A.color(t,'#fff'))"),
  V('Barres de longueur décroissante', "Chaque couche devient une barre dont la longueur baisse avec le rang.", r"A.shapes(sl).filter(s=>s.w>200&&s.h<40).sort((a,b)=>a.y-b.y).forEach((s,i)=>{const pk=s.stroke.toUpperCase()==='#FB0161';s.p.setAttribute('stroke','none');s.p.setAttribute('fill',pk?C.pink:'#2A4F63');s.el.style.transformOrigin='left';s.el.style.transform=`scaleX(${1-i*.08})`})"),
  V('Rangs dans des ronds', "Les cadres disparaissent ; le rang passe dans un rond (rose pour le top 3).", r"A.hide(A.shapes(sl).filter(s=>s.w>200&&s.h<40));A.texts(sl).filter(t=>/^[1-8]$/.test(t.text)).forEach(t=>{const n=+t.text;t.el.querySelector('p').innerHTML=`<span style='display:inline-flex;width:24px;height:24px;border-radius:50%;align-items:center;justify-content:center;font:700 10pt Lexend;${n<=3?`background:${C.pink};color:#fff`:'border:1px solid #4A6470;color:#C9D4D8'}'>${n}</span>`})"),
  'B', "Les barres décroissantes montrent le classement d'un coup d'œil, ce que des cadres identiques ne font pas.", fam='Graphiques')

I(67, "Matrice douleur × client : points sur des lignes", "Les lignes horizontales derrière les points et les en-têtes coupés rendent la grille confuse.", [58], 58,
  V('Lignes retirées', "Sans les lignes : les points tiennent seuls en grille, plus aérés.", r"A.hide(A.shapes(sl).filter(s=>s.stroke==='#1C4153'))"),
  V('Bandes alternées', "Lignes retirées, une ligne sur deux en bande légèrement plus claire.", r"const L=A.shapes(sl).filter(s=>s.stroke==='#1C4153');A.hide(L);L.forEach((s,i)=>{if(i%2==0){const d=A.div(sl,130,s.cy-22,660,44,'background:#0A3044;border-radius:6px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)}})"),
  V('Cases de chaleur', "Chaque point devient une case colorée : rose (fort), ardoise (moyen), vide (faible).", r"A.hide(A.shapes(sl).filter(s=>s.stroke==='#1C4153'));A.shapes(sl).filter(s=>s.w<24&&s.stroke==='none').forEach(s=>{A.hide([s]);const c=s.fill.toUpperCase()==='#FB0161'?C.pink:s.fill==='#5E7E8E'?'#2E5568':'#0E3A50';A.div(sl,s.cx-40,s.cy-18,80,36,`background:${c};border-radius:4px`)})"),
  'C', "La heatmap rend la matrice lisible en un regard ; c'est la forme standard pour ce croisement.", fam='Tableaux')

I(68, "Paris audacieux : accolades d'horizon", "Les accolades grises et les libellés « NEAR-TERM HORIZON » sur le côté se lisent mal.", [97], 97,
  V('Libellés roses, sans accolade', "Accolades retirées, libellés d'horizon en rose.", r"A.hide(A.shapes(sl).filter(s=>s.w<14&&s.h>150));A.texts(sl).filter(t=>/HORIZON/.test(t.text)).forEach(t=>A.color(t,C.pink))"),
  V('Filet vertical rose', "L'accolade devient un filet vertical rose ; libellés en crème.", r"A.shapes(sl).filter(s=>s.w<14&&s.h>150).forEach(s=>{A.hide([s]);A.div(sl,s.cx,s.y,2,s.h,'background:#FB0161')});A.texts(sl).filter(t=>/HORIZON/.test(t.text)).forEach(t=>A.color(t,C.cream))"),
  V('Fond de rangée', "Chaque rangée d'horizon a un fond bleu légèrement plus clair, accolades retirées.", r"A.hide(A.shapes(sl).filter(s=>s.w<14&&s.h>150));[[178,195],[390,195]].forEach(([y,h])=>{const d=A.div(sl,8,y,860,h,'background:#0A3044;border-radius:10px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)})"),
  'B', "Le filet rose relie les deux paris d'un même horizon et dit l'horizon sans accolade.", fam='Schémas')

I(69, "Matrice des fonctions (Duolingo vs autres)", "Le cadre pointillé autour de Duolingo et les minuscules points gris font brouillon.", [99], 99,
  V('Ligne Duolingo en aplat', "La ligne de Duolingo passe en aplat bleu clair sans pointillés.", r"A.shapes(sl).filter(s=>s.dash&&s.w>600).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Cadre rose fin', "La ligne de Duolingo garde un cadre, mais plein, rose et fin.", r"A.shapes(sl).filter(s=>s.dash&&s.w>600).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('fill','none')})"),
  V('Aplat + tirets à la place des points gris', "Aplat sur Duolingo ; les petits points gris (« non ») deviennent des tirets courts.", r"A.shapes(sl).filter(s=>s.dash&&s.w>600).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.shapes(sl).filter(s=>s.fill==='#3E6E86').forEach(s=>{A.hide([s]);A.div(sl,s.cx-5,s.cy-1,10,2,'background:#33525F')})"),
  'C', "Un tiret dit « non » plus clairement qu'un point minuscule, et Duolingo ressort sans cadre.", fam='Tableaux')

I(70, "Quadrant des modèles économiques : axes épais", "Les axes gris de 4 px sont plus lourds que les logos.", [105, 12], 105,
  V('Axes fins + flèches', "Axes de 1,5 px avec une petite flèche au bout.", r"A.shapes(sl).filter(s=>s.sw>=4&&(s.w>500||s.h>250)).forEach(s=>s.p.setAttribute('stroke-width','1.5'))"),
  V('Axes roses fins', "Axes fins roses : ils deviennent un élément de la charte.", r"A.shapes(sl).filter(s=>s.sw>=4&&(s.w>500||s.h>250)).forEach(s=>{s.p.setAttribute('stroke-width','1.5');s.p.setAttribute('stroke',C.pink);s.el.querySelectorAll('marker path').forEach(m=>m.setAttribute('fill',C.pink))})"),
  V('Grille en quatre zones', "Plus d'axes : quatre zones très légèrement teintées délimitent les quadrants.", r"const ax=A.shapes(sl).filter(s=>s.sw>=4&&(s.w>500||s.h>250));A.hide(ax);[[205,245,300,140,'#0A3044'],[508,245,300,140,'#0B3850'],[205,388,300,140,'#0B3850'],[508,388,300,140,'#0A3044']].forEach(([x,y,w,h,c])=>{const d=A.div(sl,x,y,w,h,`background:${c};border-radius:8px`);const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)})"),
  'A', "Des axes fins laissent les logos au premier plan.", fam='Graphiques')

I(71, "Qui paie : ligne pointillée et flèches grises", "La ligne pointillée en haut et les flèches grises qui descendent n'apportent rien.", [63, 67, 71, 75, 79, 83, 107, 111, 116, 120, 124, 128, 10], 63,
  V('Supprimées', "On enlève ligne et flèches : les colonnes suffisent.", r"A.hide(A.shapes(sl).filter(s=>s.dash==='1 3'||(s.sw===3&&s.w<30)))"),
  V('Ligne pleine + points', "Une ligne pleine fine en haut et un petit point rose au-dessus de chaque colonne.", r"A.hide(A.shapes(sl).filter(s=>s.sw===3&&s.w<30));A.shapes(sl).filter(s=>s.dash==='1 3').forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#33525F');s.p.setAttribute('stroke-width','1')});A.shapes(sl).filter(s=>s.sw===3&&s.w<30).forEach(s=>A.div(sl,s.cx-4,s.y-4,8,8,'border-radius:50%;background:#FB0161'))"),
  V('Flèches fines roses', "On garde la ligne et les flèches, mais fines et roses.", r"A.shapes(sl).filter(s=>s.dash==='1 3'||(s.sw===3&&s.w<30)).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','1');s.el.querySelectorAll('marker path').forEach(m=>m.setAttribute('fill',C.pink))})"),
  'B', "La ligne à points relie les segments comme un arbre, sans les flèches lourdes.", fam='Schémas')

I(72, "Intro : grand cadre pointillé", "Le texte d'intro dans un grand cadre pointillé gris fait brouillon.", [2, 3, 221], 2,
  V('Cadre plein fin', "Le cadre devient plein, fin et arrondi.", r"A.shapes(sl).filter(s=>s.dash&&s.w>500).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#33525F')})"),
  V('Sans cadre, trait rose', "Plus de cadre : un trait rose vertical à gauche du texte.", r"A.shapes(sl).filter(s=>s.dash&&s.w>500).forEach(s=>{A.hide([s]);A.div(sl,s.x,s.y+30,3,s.h-60,'background:#FB0161;border-radius:2px')})"),
  V('Carte pleine', "Le texte passe sur une carte bleu clair sans bord.", r"A.shapes(sl).filter(s=>s.dash&&s.w>500).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0B3850')})"),
  'B', "Le trait rose fait éditorial : c'est un texte à lire, pas une case.", fam='Cartes')

I(73, "Intercalaire SOURCES : grand cadre rose", "Le cadre rose épais vide ne ressemble à aucun autre intercalaire.", [215], 215,
  V('Comme les autres intercalaires', "Plus de cadre : titre centré avec un petit trait rose dessous.", r"A.hide(A.shapes(sl).filter(s=>s.w>500));A.div(sl,452,345,56,3,'background:#FB0161;border-radius:2px')"),
  V('Cadre fin crème', "Le cadre devient un filet crème fin arrondi.", r"A.shapes(sl).filter(s=>s.w>500).forEach(s=>{s.p.setAttribute('stroke','rgba(231,205,168,.35)');s.p.setAttribute('stroke-width','1')})"),
  V('Grand numéro de chapitre', "Comme une page de chapitre : « 13 » en grand rose au-dessus de SOURCES.", r"A.hide(A.shapes(sl).filter(s=>s.w>500));A.div(sl,330,170,300,110,'display:flex;align-items:flex-end;justify-content:center;font:700 80pt Lexend;color:#FB0161;line-height:1','13')"),
  'A', "La page des sources reprend le code des autres intercalaires.", fam='Sommaire')

I(74, "Sources : liens soulignés", "Les liens soulignés et coupés sur deux lignes font page web de 2005.", [216, 217, 218, 219, 220], 216,
  V('Crème gras, sans soulignement', "Nom de la source en crème gras, sans soulignement.", r"sl.querySelectorAll('span').forEach(s=>{if(/underline/.test(s.style.textDecoration)){s.style.textDecoration='none';s.style.color=C.cream;s.style.fontWeight='700'}})"),
  V('Rose + flèche ↗', "Nom en rose, sans soulignement, avec une petite flèche ↗ qui dit « lien ».", r"sl.querySelectorAll('span').forEach(s=>{if(/underline/.test(s.style.textDecoration)){s.style.textDecoration='none';s.style.color=C.pink}});A.texts(sl).filter(t=>t.el.querySelector('span[style*=\"color: rgb(251, 1, 97)\"],span[style*=\"#FB0161\"]')).forEach(t=>{const p=t.el.querySelector('p:last-child');p&&p.insertAdjacentHTML('beforeend',' <span style=\"color:#FB0161\">↗</span>')})"),
  V('Blanc + soulignement fin rose', "Nom en blanc, soulignement fin rose décalé.", r"sl.querySelectorAll('span').forEach(s=>{if(/underline/.test(s.style.textDecoration)){s.style.color='#fff';s.style.textDecorationColor=C.pink;s.style.textUnderlineOffset='3px';s.style.textDecorationThickness='1px'}})"),
  'B', "Le rose + ↗ dit « cliquable » dans la charte, sans le soulignement daté.", clip=[30, 20, 900, 300], fam='Tableaux')

I(75, "Étapes de la méthode : marqueurs gris", "Les petits marqueurs gris à gauche des 11 étapes ne disent rien de l'ordre.", [43, 44], 43,
  V('Numéros roses', "Chaque étape a son numéro rose (1 à 11) à la place du marqueur.", r"const m=A.shapes(sl).filter(s=>s.fill==='#789096'&&s.w<20).sort((a,b)=>a.y-b.y);A.hide(m);m.forEach((s,i)=>A.div(sl,s.x-18,s.cy-10,28,20,'display:flex;align-items:center;justify-content:flex-end;font:700 9pt Lexend;color:#FB0161',String(i+1).padStart(2,'0')))"),
  V('Ligne verticale + points', "Une ligne verticale fine relie des points : on lit un parcours de haut en bas.", r"const m=A.shapes(sl).filter(s=>s.fill==='#789096'&&s.w<20).sort((a,b)=>a.y-b.y);A.hide(m);A.div(sl,m[0].cx-1,m[0].cy,2,m[m.length-1].cy-m[0].cy,'background:#33525F');m.forEach((s,i)=>A.div(sl,s.cx-5,s.cy-5,10,10,`border-radius:50%;background:${i==m.length-1?C.pink:'#7E949E'};box-shadow:0 0 0 3px #062A3C`))"),
  V('Cadres retirés', "On garde les marqueurs mais on enlève les cadres de chaque ligne : liste plus légère.", r"A.hide(A.shapes(sl).filter(s=>s.w>600))"),
  'B', "Le fil vertical montre que les étapes s'enchaînent jusqu'au résultat (point rose).", fam='Frises')

I(76, "Signes ≠ roses entre les marchés", "Les gros signes ≠ roses ressemblent à des boutons.", [8], 8,
  V('« vs » en petit', "Les signes deviennent « vs » en petites lettres crème.", r"A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30).forEach(s=>{A.hide([s]);A.div(sl,s.cx-14,s.cy-10,28,20,'display:flex;align-items:center;justify-content:center;font:500 9pt Lexend;color:#E7CDA8','vs')})"),
  V('≠ fin', "Le ≠ reste, mais en trait fin rose.", r"A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30).forEach(s=>{A.hide([s]);A.div(sl,s.cx-12,s.cy-14,24,28,'display:flex;align-items:center;justify-content:center;font:300 22pt Lexend;color:#FB0161;line-height:1','≠')})"),
  V('Rien', "On enlève les signes : les trois colonnes se comparent seules.", r"A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<30))"),
  'B', "Le ≠ fin garde l'idée « différent de » sans peser.", clip=[100, 240, 760, 300], fam='Cartes')

# ---------------- 6. Chrome du deck (toutes les slides) ----------------
ALL = 'toutes les slides'
I(77, "Bouton NEWMARKETPITCH.COM en bas à droite", "Le cadre crème épais avec ombre ressemble à un bouton de 2010 et pèse sur chaque slide.", [ALL], 33,
  V('Cadre fin', "Même bouton, cadre de 1 px, texte plus petit et plus espacé.", css="S .foot-brand{border-width:1px;font-size:9.5pt;letter-spacing:.2em;line-height:21px;box-shadow:none}"),
  V('Texte seul, point rose', "Plus de cadre : NEWMARKETPITCH.COM en crème espacé, précédé d'un point rose.", css="S .foot-brand{border:none;box-shadow:none;font-size:9pt;letter-spacing:.24em;text-align:right}S .foot-brand::before{content:'';display:inline-block;width:6px;height:6px;border-radius:50%;background:#FB0161;margin-right:10px;vertical-align:2px}"),
  V('Pastille pleine crème', "Une pastille pleine crème arrondie, texte bleu nuit : un vrai logo de marque.", css="S .foot-brand{border:none;background:#E7CDA8;color:#062A3C;border-radius:12px;font-size:9.5pt;letter-spacing:.14em;line-height:23px;box-shadow:none}"),
  'B', "La marque reste visible sans le bouton qui attire l'œil sur chaque page.", clip=[480, 560, 480, 112], fam='Chrome')

I(78, "Sur-titre de section en haut", "Le petit sur-titre crème très espacé est discret au point d'être ignoré.", [ALL], 33,
  V('Sur-titre rose', "Le sur-titre passe en rose : on sait toujours dans quel chapitre on est.", css="S .section{color:#FB0161}"),
  V('Numéro de chapitre + nom', "« 02 · MARKET OPPORTUNITY » : le numéro du chapitre en rose devant.", js=r"const s=sl.querySelector('.section');if(s)s.innerHTML=`<b style='color:#FB0161'>02</b> &nbsp;·&nbsp; ${s.textContent}`"),
  V('Entre deux filets', "Le sur-titre entre deux petits filets crème.", css="S .section{display:flex;align-items:center;justify-content:center;gap:14px}S .section::before,S .section::after{content:'';width:30px;height:1px;background:#E7CDA8;opacity:.6}"),
  'B', "Le numéro de chapitre aide à se repérer dans 221 slides, en lecture comme à l'oral.", clip=[180, 0, 600, 140], fam='Chrome')

I(79, "Notes de bas de page", "Les notes en gris clair de 7 pt sont presque illisibles sur le bleu.", [ALL], 64,
  V('Un ton plus clair', "Même taille, gris plus clair : lisibles sans attirer l'œil.", css="S .note{color:#9FB0B7}"),
  V('Trait rose devant', "Gris plus clair et un petit trait rose à gauche : la note est identifiée comme « méthode ».", css="S .note{color:#9FB0B7;padding-left:12px;border-left:2px solid #FB0161}"),
  V('Italique crème', "Note en italique crème à 70 % : style « source » de presse.", css="S .note{color:rgba(231,205,168,.7);font-style:italic}"),
  'A', "Le texte reste en retrait mais se lit enfin ; rien d'autre à ajouter.", clip=[0, 560, 720, 112], fam='Chrome')

I(80, "Triangle rose dans le coin", "Le triangle rose en haut à gauche n'a pas de rôle et semble coupé.", [ALL], 33,
  V('Barre rose fine en haut', "Une fine barre rose sur toute la largeur du haut de slide.", css="S .tri{width:100%;height:4px;clip-path:none}"),
  V('Petit carré rose', "Un petit carré rose de 10 px dans le coin, comme un sceau.", css="S .tri{width:10px;height:10px;left:20px;top:20px;clip-path:none}"),
  V('Supprimé', "Plus rien dans le coin : le titre se suffit.", css="S .tri{display:none}"),
  'C', "Le triangle n'apporte rien ; sans lui la slide est plus calme.", clip=[0, 0, 480, 160], fam='Chrome')

I(81, "Sous-titre (segment, 1/2…)", "Le sous-titre gris sous le titre (SCHOOL PLATFORMS, 1/2) se perd.", [ALL], 65,
  V('Pastille ardoise', "Le sous-titre dans une petite pastille ardoise arrondie.", css="S .subtitle{left:50%;width:auto;transform:translateX(-50%);background:#123F57;color:#E7CDA8;padding:2px 12px;border-radius:10px;font-size:8pt;letter-spacing:.14em}"),
  V('Rose espacé', "Sous-titre en rose, petites capitales espacées.", css="S .subtitle{color:#FB0161;letter-spacing:.24em;font-size:8pt;font-weight:700}"),
  V('Crème + filets', "Sous-titre crème entre deux filets courts.", css="S .subtitle{display:flex;align-items:center;justify-content:center;gap:12px;color:#E7CDA8;letter-spacing:.16em;font-size:8pt}S .subtitle::before,S .subtitle::after{content:'';width:24px;height:1px;background:#E7CDA8;opacity:.5}"),
  'A', "La pastille dit « vous êtes dans ce segment » sans concurrencer le titre.", clip=[180, 20, 600, 160], fam='Chrome')

# ---------------- 7. Graphiques à gabarit ----------------
I(82, "Levées par trimestre : barres et flèches", "Barres roses brutes et flèches grises sous des notes longues : lourd.", [158, 159], 158,
  V('Barres arrondies', "Barres aux coins arrondis en haut, sans ombre ; flèches fines.", css="S .vbars .bar{border-radius:6px 6px 0 0;box-shadow:none}S .vbars .down{opacity:.5}"),
  V('Barres + ligne de base', "Barres arrondies posées sur une ligne de base fine, flèches retirées.", css="S .vbars{border-bottom:1px solid #4A6470;padding-bottom:0}S .vbars .bar{border-radius:6px 6px 0 0;box-shadow:none}S .vbars .down{visibility:hidden;height:8px}"),
  V('Montant en pastille', "Le montant de chaque barre dans une pastille rose, flèches retirées.", css="S .vbars .v{background:#FB0161;color:#fff;padding:2px 8px;border-radius:9px}S .vbars .down{visibility:hidden;height:8px}S .vbars .bar{border-radius:4px 4px 0 0}"),
  'B', "La ligne de base donne une vraie échelle ; les flèches doublaient les notes.", fam='Graphiques')

I(83, "Projection du marché", "Barres serrées, toutes roses, et la flèche d'axe grise : la dernière année ne ressort pas.", [52], 52,
  V('Passé ardoise, futur rose', "Les années passées en ardoise, les projections en rose.", r"const c=[...sl.querySelectorAll('.vbars .col')];c.forEach((e,i)=>{if(i<c.length/2)e.querySelector('.bar').style.background='#4A6470'})"),
  V('Barres arrondies', "Toutes les barres arrondies en haut, sans ombre, la dernière plus large.", css="S .vbars .bar{border-radius:6px 6px 0 0;box-shadow:none}S .vbars .col.last .bar{width:56px!important}"),
  V('Dégradé vers le rose', "Les barres passent progressivement de l'ardoise au rose.", r"const c=[...sl.querySelectorAll('.vbars .col')];c.forEach((e,i)=>{const t=i/(c.length-1);e.querySelector('.bar').style.background=`color-mix(in srgb, #FB0161 ${Math.round(t*100)}%, #4A6470)`})"),
  'A', "On sépare le mesuré du projeté, ce que le lecteur se demande en premier.", clip=[100, 150, 760, 440], fam='Graphiques')

I(84, "Maturité du marché : jauge", "Une barre crème avec une double flèche rose posée dessus : on ne voit pas d'échelle.", [17], 17,
  V('Jauge en 5 segments', "La barre devient 5 segments ; ceux atteints en rose.", css="S .maturity .axis{background:repeating-linear-gradient(90deg,#FB0161 0 calc(20% - 4px),transparent calc(20% - 4px) 20%);height:10px;border-radius:5px}S .maturity .axis::after{display:none}S .maturity .mark{clip-path:none;width:4px;margin-left:-2px;height:28px;top:244px;background:#fff;border-radius:2px}"),
  V('Dégradé + curseur', "Barre en dégradé ardoise → rose, curseur rond blanc à la position.", css="S .maturity .axis{background:linear-gradient(90deg,#33525F,#FB0161);height:8px;border-radius:4px}S .maturity .axis::after{display:none}S .maturity .mark{clip-path:none;width:22px;height:22px;margin-left:-11px;top:248px;border-radius:50%;background:#fff;box-shadow:0 0 0 4px #062A3C}"),
  V('Barre de progression', "Une barre fine ardoise remplie en rose jusqu'au score.", js=r"const m=sl.querySelector('.maturity');const sc=+m.querySelector('.score').textContent;m.querySelector('.axis').style.background=`linear-gradient(90deg,#FB0161 ${sc}%,#1E4558 ${sc}%)`", css="S .maturity .axis{height:8px;border-radius:4px}S .maturity .axis::after{display:none}S .maturity .mark{display:none}"),
  'C', "La barre de progression se lit comme un score sur 100, sans légende.", fam='Graphiques')

I(85, "Définition : icônes dans les coins", "Les deux emojis (toque, coche verte) dans leurs carrés détonnent.", [6], 6,
  V('Icônes au trait crème', "Les emojis deviennent des icônes fines crème dans les mêmes carrés.", r"A.swap(sl,{style:'line',color:C.cream,size:20})"),
  V('Icônes roses', "Icônes au trait rose, carrés à bord rose fin.", r"A.swap(sl,{style:'line',color:C.pink,size:20});sl.querySelectorAll('.defbox .ico').forEach(e=>e.style.borderColor=C.pink)"),
  V('Pastilles rondes', "Les carrés deviennent des ronds bleu clair, icônes crème.", r"A.swap(sl,{style:'line',color:C.cream,size:18});sl.querySelectorAll('.defbox .ico').forEach(e=>{e.style.borderRadius='50%';e.style.background='#123F57';e.style.borderColor='transparent'})"),
  'A', "Même design que Pierre a validé, seul l'emoji devient une icône de la charte.", fam='Emojis')

I(86, "Carte des logos : grille", "Les lignes de la grille des logos sont lourdes et pointillées.", [171], 171,
  V('Grille très fine', "Lignes pleines très fines, couleur ardoise.", css="S .lgrid svg.gl *{stroke:#1E4558!important;stroke-dasharray:none!important;stroke-width:1!important}"),
  V('Bandes de fond', "Plus de lignes : trois bandes horizontales alternées.", js=r"const g=sl.querySelector('.lgrid svg.gl');if(g)g.style.display='none';const L=sl.querySelector('.lgrid');[0,1,2].forEach(i=>{if(i%2==0)L.insertAdjacentHTML('afterbegin',`<div style='position:absolute;left:0;right:0;top:${40+i*117}px;height:117px;background:#0A3044;border-radius:8px'></div>`)})"),
  V('Colonnes en aplat', "Les trois stades deviennent des colonnes légèrement teintées.", js=r"const g=sl.querySelector('.lgrid svg.gl');if(g)g.style.display='none';const L=sl.querySelector('.lgrid');[0,2].forEach(i=>L.insertAdjacentHTML('afterbegin',`<div style='position:absolute;top:0;bottom:0;left:${140+i*240}px;width:240px;background:#0A3044;border-radius:8px'></div>`))"),
  'A', "Une grille fine structure sans voler la vedette aux logos.", fam='Graphiques')

# ---------------- 8. Slides raw restantes ----------------
I(87, "Glossaire : cases des sigles", "Les cases des sigles et des définitions ont le même trait gris : on ne distingue pas le terme.", [11], 11,
  V('Sigle en rose', "Le sigle (LMS, MOOC…) passe en rose gras.", r"A.texts(sl).filter(t=>/^[A-Z0-9-]{2,6}$/.test(t.text)).forEach(t=>A.color(t,C.pink))"),
  V('Cartes pleines', "Les cases deviennent des aplats bleu clair sans bord.", r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>150).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Aplat + sigle rose', "Aplats sans bord et sigle en rose.", r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>150).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.texts(sl).filter(t=>/^[A-Z0-9-]{2,6}$/.test(t.text)).forEach(t=>A.color(t,C.pink))"),
  'C', "Le sigle rose est ce qu'on cherche dans un glossaire ; l'aplat rend la grille calme.", fam='Cartes')

I(88, "Grand choc de 2020 : bloc rose", "Le gros bloc rose et la barre rose sous le texte se disputent l'attention.", [28, 27], 28,
  V('Barre seule', "On garde la barre rose de la frise, le bloc rose devient un contour fin.", r"A.shapes(sl).filter(s=>s.w>100&&s.h>80&&s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>{s.p.setAttribute('fill','none');s.p.setAttribute('stroke-width','2')})"),
  V('Bloc ardoise', "Le bloc passe en ardoise, la barre reste rose.", r"A.shapes(sl).filter(s=>s.w>100&&s.h>80&&s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>{s.p.setAttribute('fill','#33525F');s.p.setAttribute('stroke','none')})"),
  V('Barre fine', "Bloc en contour fin et barre de frise affinée à 4 px.", r"A.shapes(sl).filter(s=>s.w>100&&s.h>80&&s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>{s.p.setAttribute('fill','none');s.p.setAttribute('stroke-width','2')});A.shapes(sl).filter(s=>s.w>400&&s.h<14).forEach(s=>s.el.style.transform='scaleY(.4)')"),
  'A', "Un seul élément rose plein (la frise) : l'œil sait où regarder.", fam='Frises')

I(89, "Problèmes que visent les startups : bulles", "Bulles de tailles diverses au trait gris avec des mini emojis : on ne sait pas quoi lire.", [59], 59,
  V('Bulles pleines', "Les bulles deviennent des disques bleu clair sans trait, emojis retirés.", r"A.shapes(sl).filter(s=>s.w===s.h||Math.abs(s.w-s.h)<4).forEach(s=>{if(s.w<300){s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')}});A.emojis(sl).forEach(e=>e.style.visibility='hidden')"),
  V('Taille = rose plus intense', "Les plus grosses bulles en rose, les moyennes en ardoise, petites en bleu.", r"A.shapes(sl).filter(s=>Math.abs(s.w-s.h)<4&&s.w<300&&s.w>60).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill',s.w>105?C.pink:s.w>85?'#2E5568':'#123F57')});A.emojis(sl).forEach(e=>e.style.visibility='hidden')"),
  V('Icônes au trait', "On garde les bulles, emojis remplacés par des icônes fines crème.", r"A.swap(sl,{style:'line',color:C.cream,size:14})"),
  'B', "La couleur dit la taille du problème ; on lit d'abord le plus gros.", fam='Schémas')

I(90, "Points Europe / Amérique / monde", "Trois couleurs de points (rose, blanc, gris bordé) : la légende est nécessaire pour tout lire.", [161], 161,
  V('Rose / crème / ardoise', "Europe rose, Amérique du Nord crème, reste ardoise sans bord.", r"A.shapes(sl).filter(s=>s.w<14).forEach(s=>{if(s.fill==='#FFFFFF')s.p.setAttribute('fill',C.cream);if(s.fill==='#334D54'){s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#1E4558')}})"),
  V('Seule l\'Europe en couleur', "Europe rose, tout le reste en ardoise : le message (42 %) saute aux yeux.", r"A.shapes(sl).filter(s=>s.w<14).forEach(s=>{if(s.fill!=='#FB0161'&&s.fill.toUpperCase()!=='#FB0161'){s.p.setAttribute('fill','#2A4A58');s.p.setAttribute('stroke','none')}})"),
  V('Carrés', "Les points deviennent de petits carrés arrondis (style waffle).", r"A.shapes(sl).filter(s=>s.w<14).forEach(s=>{A.hide([s]);A.div(sl,s.x,s.y,s.w,s.h,`border-radius:2px;background:${s.fill==='#334D54'?'#1E4558':s.fill}`)})"),
  'B', "Le titre parle de l'Europe : une seule couleur suffit et la légende devient inutile.", fam='Graphiques')

I(91, "Barres horizontales + logos par catégorie", "Les rails de fond des barres et les petits points roses en bout chargent la ligne.", [168], 168,
  V('Sans rail de fond', "On enlève les rails ; il reste les barres roses.", r"A.hide(A.shapes(sl).filter(s=>s.fill==='#0E4561'&&s.h<14))"),
  V('Barres arrondies sans point', "Barres arrondies, points de bout retirés.", r"A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<24&&s.h<24));A.shapes(sl).filter(s=>s.h<14&&s.w>20).forEach(s=>s.el.style.borderRadius='6px')"),
  V('Rail fin', "Le rail devient une ligne fine, la barre rose reste épaisse.", r"A.shapes(sl).filter(s=>s.fill==='#0E4561'&&s.h<14).forEach(s=>s.el.style.transform='scaleY(.25)')"),
  'C', "Le rail fin garde l'échelle (sur 100 %) sans doubler la barre.", fam='Graphiques')

I(92, "Temps pour devenir licorne : flèches", "Flèches roses et pointillés gris à hauteurs différentes : on compare mal les durées.", [189], 189,
  V('Flèches affinées', "Les flèches roses deviennent deux fois plus fines, pointillés retirés.", r"A.hide(A.shapes(sl).filter(s=>s.dash));A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>s.el.style.transform='scaleY(.5)')"),
  V('Points de début et fin', "Un point au début et à la fin de chaque durée, reliés par un trait (style « haltère »).", r"A.hide(A.shapes(sl).filter(s=>s.dash));A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>{A.hide([s]);A.div(sl,s.x,s.cy-1,s.w,2,'background:#FB0161');A.div(sl,s.x-5,s.cy-5,10,10,'border-radius:50%;background:#7E949E');A.div(sl,s.x+s.w-6,s.cy-6,12,12,'border-radius:50%;background:#FB0161')})"),
  V('Grille d\'années', "Barres conservées, avec des repères verticaux fins tous les 2 ans.", r"for(let i=0;i<=7;i++){const d=A.div(sl,259+i*63,230,1,300,'background:#123F57');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)}A.hide(A.shapes(sl).filter(s=>s.dash))"),
  'B', "L'haltère montre début et fin : on lit la durée et l'époque.", fam='Graphiques')

I(93, "Courbes de valorisation : encart d'explication", "L'encart pointillé posé sur la courbe cache une partie du graphique.", [193, 194, 196, 198, 190], 193,
  V('Encart plein', "Encart bleu clair plein, sans pointillés.", r"A.shapes(sl).filter(s=>s.dash==='1 3'&&s.h>40).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Trait rose à gauche', "Encart sans cadre avec un trait rose à gauche.", r"A.shapes(sl).filter(s=>s.dash==='1 3'&&s.h>40).forEach(s=>{s.p.setAttribute('stroke','none');A.div(sl,s.x,s.y,3,s.h,'background:#FB0161')})"),
  V('Texte seul', "On enlève l'encart : la note flotte sur le graphique, comme une annotation.", r"A.hide(A.shapes(sl).filter(s=>s.dash==='1 3'&&s.h>40))"),
  'A', "L'aplat sépare la note de la courbe sans le pointillé.", fam='Graphiques')

I(94, "Signaux d'alerte : petits carrés de risque", "Les carrés de risque (rose, jaune, bleu) en minuscule et la couleur jaune hors charte.", [199], 199,
  V('Jauge 3 points', "Le risque devient 3 points : roses pour élevé, jaune → crème pour moyen.", r"A.shapes(sl).filter(s=>s.fill==='#F2A93B').forEach(s=>s.p.setAttribute('fill',C.cream))"),
  V('Pastille de risque', "Carrés retirés ; « High risk » en pastille rose, « Medium » en pastille ardoise.", r"A.hide(A.shapes(sl).filter(s=>s.w<14&&s.h<14));A.texts(sl).filter(t=>/risk$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(x=>{const h=/High/.test(t.text);x.style.cssText+=`;background:${h?C.pink:'#33525F'};color:#fff;padding:2px 7px;border-radius:8px;font-style:normal`}))"),
  V('Barres verticales', "Les filets roses verticaux devant chaque cellule passent en ardoise ; seuls les risques élevés restent roses.", r"A.shapes(sl).filter(s=>s.w<4&&s.fill&&s.fill.toUpperCase()==='#FB0161').forEach(s=>s.p.setAttribute('fill','#4A6470'));A.shapes(sl).filter(s=>s.fill==='#F2A93B').forEach(s=>s.p.setAttribute('fill',C.cream))"),
  'B', "La pastille dit le niveau en un mot, sans légende de couleurs.", fam='Tableaux')

I(95, "Matrice de fonctions Duolingo : cases cochées", "Cases roses cochées ✓ et minuscules points gris : la grille paraît vide.", [209], 209,
  V('Coches sans case', "La coche rose seule, sans case ; le « non » devient un tiret.", r"A.hide(A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<26&&s.h<26));A.texts(sl).filter(t=>t.text==='✓').forEach(t=>A.color(t,C.pink));A.shapes(sl).filter(s=>s.fill==='#3E6E86').forEach(s=>{A.hide([s]);A.div(sl,s.cx-5,s.cy-1,10,2,'background:#33525F')})"),
  V('Ronds pleins', "Oui = rond rose plein, non = rond vide au trait.", r"A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<26&&s.h<26).forEach(s=>{A.hide([s]);A.div(sl,s.cx-7,s.cy-7,14,14,'border-radius:50%;background:#FB0161')});A.texts(sl).filter(t=>t.text==='✓').forEach(t=>t.el.style.visibility='hidden');A.shapes(sl).filter(s=>s.fill==='#3E6E86').forEach(s=>{A.hide([s]);A.div(sl,s.cx-6,s.cy-6,12,12,'border-radius:50%;border:1.5px solid #33525F;box-sizing:border-box')})"),
  V('Colonne Duolingo seule', "Seule la colonne Duolingo garde ses coches roses ; les autres passent en crème.", r"const col=A.shapes(sl).find(s=>s.fill==='#0C3A50');A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&s.w<26&&s.h<26).forEach(s=>{if(col&&(s.cx<col.x||s.cx>col.x+col.w))s.p.setAttribute('fill','#4A6470')})"),
  'C', "Le titre parle de Duolingo : sa colonne seule en rose fait le constat d'un coup d'œil.", fam='Tableaux')

I(96, "Startups qui ont cassé : points + statut", "Points roses dans une grille de petits points gris, statut en fin de ligne : on lit mal la cause.", [201], 201,
  V('Tirets à la place des points gris', "Les points gris deviennent des tirets ; les causes restent en rose.", r"A.shapes(sl).filter(s=>s.fill==='#5E7E8E'&&s.w<6).forEach(s=>{A.hide([s]);A.div(sl,s.cx-4,s.cy-.5,8,1,'background:#33525F')})"),
  V('Lignes en bandes', "Points gris retirés, une ligne sur deux en bande légèrement plus claire.", r"A.hide(A.shapes(sl).filter(s=>s.fill==='#5E7E8E'&&s.w<6));A.shapes(sl).filter(s=>s.stroke==='#1C4153').forEach((s,i)=>{A.hide([s]);if(i%2==0){const d=A.div(sl,s.x,s.cy,s.w,18,'background:#0A3044;border-radius:4px');const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)}})"),
  V('Statut en pastille', "Le statut de fin (Shut down, Sold cheap…) passe en pastille ardoise.", r"A.texts(sl).filter(t=>/^(Shut down|Sold cheap|Administration|Big layoffs)$/.test(t.text)).forEach(t=>t.el.querySelectorAll('span').forEach(x=>x.style.cssText+=';background:#1E4558;padding:2px 7px;border-radius:8px;white-space:nowrap'))"),
  'A', "Le tiret dit « non » sans ajouter de bruit, les causes roses ressortent.", clip=[180, 140, 700, 340], fam='Tableaux')

I(97, "Bulles « un concept = une question » (intro)", "Le texte d'intro en colonne étroite et les grands blancs donnent une page vide.", [3], 3,
  V('Cadre plein fin', "Cadre plein fin arrondi à la place du pointillé.", r"A.shapes(sl).filter(s=>s.dash&&s.w>400).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#33525F')})"),
  V('Trait rose', "Plus de cadre, un trait rose à gauche.", r"A.shapes(sl).filter(s=>s.dash&&s.w>400).forEach(s=>{A.hide([s]);A.div(sl,s.x,s.y+30,3,s.h-60,'background:#FB0161')})"),
  V('Carte pleine', "Le texte sur une carte bleu clair sans bord.", r"A.shapes(sl).filter(s=>s.dash&&s.w>400).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0B3850')})"),
  'B', "Même traitement que la page d'intro : un texte à lire, pas une case.", fam='Cartes')

I(98, "Arbre du marché (EdTech → 5 segments)", "La ligne pointillée et le mot EDTECH gris en haut de l'arbre manquent de présence.", [10], 10,
  V('EDTECH en pastille rose', "EDTECH dans une pastille rose, ligne pleine fine.", r"A.shapes(sl).filter(s=>s.dash==='1 3').forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#4A6470');s.p.setAttribute('stroke-width','1')});A.texts(sl).filter(t=>t.text==='EDTECH').forEach(t=>t.el.querySelectorAll('span').forEach(x=>x.style.cssText+=';background:#FB0161;color:#fff;padding:3px 16px;border-radius:12px'))"),
  V('EDTECH crème gras', "EDTECH en crème gras plus grand, ligne pleine.", r"A.shapes(sl).filter(s=>s.dash==='1 3').forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke','#4A6470')});A.texts(sl).filter(t=>t.text==='EDTECH').forEach(t=>t.el.querySelectorAll('span').forEach(x=>{x.style.color=C.cream;x.style.fontWeight='700';x.style.fontSize='16pt'}))"),
  V('Ligne rose', "La ligne de l'arbre et les branches passent en rose fin.", r"A.shapes(sl).filter(s=>s.dash==='1 3'||(s.sw===3&&s.w<30)).forEach(s=>{s.p.removeAttribute('stroke-dasharray');s.p.setAttribute('stroke',C.pink);s.p.setAttribute('stroke-width','1.2');s.el.querySelectorAll('marker path').forEach(m=>m.setAttribute('fill',C.pink))})"),
  'A', "La racine de l'arbre devient un vrai titre, comme les nœuds d'un organigramme.", clip=[90, 200, 780, 350], fam='Schémas')

I(99, "Produits par quadrant : petites cases", "24 petites cases grises au trait identiques : la grille est monotone.", [12], 12,
  V('Pastilles pleines', "Les cases deviennent des pastilles bleu clair arrondies sans bord.", r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>120&&s.h<45).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')})"),
  V('Quadrants teintés', "Cases retirées ; chaque quadrant a un fond légèrement teinté.", r"A.hide(A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>120&&s.h<45));[[170,240,290,145],[490,240,290,145],[170,405,290,145],[490,405,290,145]].forEach(([x,y,w,h],i)=>{const d=A.div(sl,x,y,w,h,`background:${i%3?'#0B3850':'#0A3044'};border-radius:10px`);const r=sl.querySelector('.raw');r.insertBefore(d,r.firstChild)})"),
  V('Axes ardoise', "Cases en pastilles et axes en ardoise : la croix ne domine plus.", r"A.shapes(sl).filter(s=>s.stroke==='#334D54'&&s.w>120&&s.h<45).forEach(s=>{s.p.setAttribute('stroke','none');s.p.setAttribute('fill','#0E3D55')});A.shapes(sl).filter(s=>s.fill&&s.fill.toUpperCase()==='#FB0161'&&(s.w>500||s.h>300)).forEach(s=>{s.p.setAttribute('fill','#4A6470');s.p.setAttribute('stroke','#4A6470')})"),
  'C', "Axes ardoise + pastilles : la croix ne domine plus et les produits se lisent.", fam='Graphiques')

I(100, "Écart Coursera / Udemy : lignes de pente", "La ligne grise de Udemy et l'encadré à droite séparé par un pointillé : on cherche le message.", [197], 197,
  V('Libellé et chiffre roses', "Le « -10.2¢ » et le libellé passent en rose, comme la ligne Coursera.", WHY + r"if(big)A.color(big,C.pink);if(lab)A.color(lab,C.pink)"),
  V('Pointillé retiré', "Le séparateur pointillé disparaît, l'explication s'aligne sur le graphique.", r"A.hide(A.shapes(sl).filter(s=>s.dash&&s.h>200))"),
  V('Encart', "L'explication passe dans un encart avec un trait rose à gauche.", WHY + r"A.hide(A.shapes(sl).filter(s=>s.dash&&s.h>200));if(lab){const ys=[big||lab,...body].map(t=>t.y),ye=Math.max(...body.map(t=>t.y+t.h));A.add(sl,`<div style='position:absolute;left:${lab.x-18}px;top:${Math.min(...ys)-14}px;width:250px;height:${ye-Math.min(...ys)+20}px;background:#0B3850;border-left:3px solid #FB0161;border-radius:0 8px 8px 0'></div>`);const r=sl.querySelector('.raw');r.insertBefore(r.lastChild,r.firstChild)}"),
  'A', "Même logique que les autres slides chiffre : le chiffre rose répond à la ligne rose.", fam='Graphiques')
