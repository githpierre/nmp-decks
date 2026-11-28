import re, json, yaml
LIMITS = json.loads(r'''{"ed054": {"6": {"max": 137, "min": 114}, "7": {"max": 140, "min": 115}, "8": {"max": 148, "min": 111}, "9": {"max": 140, "min": 110}, "10": {"max": 139, "min": 106}}, "ed055": {"5": {"max": 80, "min": 59}, "7": {"max": 119, "min": 49}, "8": {"max": 76, "min": 51}, "10": {"max": 114, "min": 45}, "11": {"max": 78, "min": 61}, "13": {"max": 119, "min": 50}, "14": {"max": 74, "min": 57}, "16": {"max": 108, "min": 54}, "17": {"max": 74, "min": 54}, "19": {"max": 117, "min": 46}, "20": {"max": 67, "min": 53}, "22": {"max": 118, "min": 49}, "__icons__": 1}, "ed056": {"6": {"max": 39, "wordmax": 11}, "8": {"max": 44, "wordmax": 11}, "10": {"max": 39, "wordmax": 10}, "12": {"max": 43, "wordmax": 9}, "14": {"max": 38, "wordmax": 9}, "16": {"max": 44, "wordmax": 10}, "18": {"max": 42, "wordmax": 13}, "20": {"max": 39, "wordmax": 9}, "23": {"max": 44, "wordmax": 15}, "25": {"max": 49, "wordmax": 10}, "27": {"max": 44, "wordmax": 10}, "29": {"max": 37, "wordmax": 9}, "31": {"max": 40, "wordmax": 9}, "33": {"max": 42, "wordmax": 11}, "35": {"max": 39, "wordmax": 9}, "37": {"max": 43, "wordmax": 10}}, "ed057": {"6": {"max": 39, "wordmax": 11}, "8": {"max": 44, "wordmax": 11}, "10": {"max": 39, "wordmax": 10}, "12": {"max": 43, "wordmax": 9}, "14": {"max": 38, "wordmax": 9}, "16": {"max": 44, "wordmax": 10}, "18": {"max": 42, "wordmax": 13}, "20": {"max": 39, "wordmax": 9}, "23": {"max": 44, "wordmax": 15}, "25": {"max": 49, "wordmax": 10}, "27": {"max": 44, "wordmax": 10}, "29": {"max": 37, "wordmax": 9}, "31": {"max": 40, "wordmax": 9}, "33": {"max": 42, "wordmax": 11}, "35": {"max": 39, "wordmax": 9}, "37": {"max": 43, "wordmax": 10}}, "ed059": {"11": {"max": 15, "wordmax": 9}, "12": {"max": 20, "wordmax": 9}, "13": {"max": 20, "wordmax": 11}, "14": {"max": 17, "wordmax": 9}, "15": {"max": 19, "wordmax": 9}, "16": {"max": 15, "wordmax": 9}, "18": {"max": 19, "wordmax": 9}, "19": {"max": 20, "wordmax": 9}, "21": {"max": 188, "min": 153}, "__icons__": 1}, "ed060": {"6": {"max": 86, "min": 64}, "7": {"max": 90, "min": 65}, "8": {"max": 91, "min": 62}, "9": {"max": 76, "min": 59}}, "ed061": {"6": {"max": 87, "min": 62}, "7": {"max": 38, "wordmax": 11}, "8": {"max": 89, "min": 60}, "9": {"max": 40, "wordmax": 12}, "10": {"max": 100, "min": 60}, "11": {"max": 28, "wordmax": 10}, "12": {"max": 95, "min": 61}, "13": {"max": 30, "wordmax": 11}}, "ed063": {"5": {"caps": true, "max": 32, "wordmax": 10}, "7": {"max": 114, "min": 85}, "8": {"caps": true, "max": 30, "wordmax": 11}, "10": {"max": 105, "min": 85}, "11": {"caps": true, "max": 30, "wordmax": 12}, "13": {"max": 102, "min": 78}, "14": {"caps": true, "max": 29, "wordmax": 11}, "16": {"max": 111, "min": 82}, "17": {"caps": true, "max": 29, "wordmax": 10}, "19": {"max": 104, "min": 81}, "27": {"caps": true, "max": 40, "wordmax": 12}}, "ed064": {"13": {"caps": true, "max": 40, "wordmax": 12}, "14": {"max": 61, "min": 46}, "15": {"max": 69, "min": 46}, "16": {"max": 61, "min": 44}, "17": {"max": 66, "min": 43}, "18": {"max": 59, "min": 42}, "19": {"max": 65, "min": 45}, "20": {"max": 64, "min": 43}, "__icons__": 1}, "ed065": {"subtitle": {"max": 40, "wordmax": 12}, "rows.*.pain": {"max": 69, "min": 44}, "rows.*.p": {"caps": true, "max": 12, "wordmax": 9}, "note_line": {"max": 138}}}''')
ICONS = set(json.loads(r'''["⏰", "⏱", "⏱️", "⏳", "☠️", "♨️", "♻️", "♾️", "⚖️", "⚗️", "⚙️", "⚛️", "⚠️", "⚡", "⛔", "⛽", "✂️", "✅", "✋", "✍️", "✓", "✖️", "✨", "❌", "❓", "❔", "⭐", "⭕", "🆓", "🌍", "🌎", "🌏", "🌐", "🌡️", "🌱", "🍎", "🎒", "🎓", "🎗️", "🎙", "🎙️", "🎤", "🎥", "🎨", "🎭", "🎮", "🎯", "🏃", "🏅", "🏆", "🏗️", "🏛️", "🏠", "🏢", "🏥", "🏦", "🏫", "🏭", "🏷️", "🐒", "👁️", "👐", "👔", "👥", "👩‍🏫", "👷", "💀", "💉", "💊", "💎", "💡", "💥", "💧", "💬", "💰", "💳", "💵", "💸", "💻", "💼", "📄", "📅", "📈", "📉", "📊", "📋", "📍", "📏", "📖", "📘", "📚", "📜", "📝", "📞", "📡", "📣", "📦", "📱", "📵", "📺", "🔀", "🔁", "🔄", "🔋", "🔌", "🔍", "🔎", "🔐", "🔒", "🔓", "🔗", "🔥", "🔧", "🔩", "🔬", "🕳️", "🖥️", "🗂️", "🗣️", "😖", "😣", "😤", "🙋", "🚀", "🚑", "🚗", "🚚", "🚛", "🚧", "🚶", "🛒", "🛞", "🛠️", "🛡️", "🛰️", "🟢", "🤒", "🤔", "🤖", "🤝", "🤥", "🤩", "🦉", "🦋", "🦠", "🦴", "🦾", "🦿", "🧂", "🧑", "🧑‍🏫", "🧑‍💻", "🧑‍🤝‍🧑", "🧠", "🧩", "🧪", "🧫", "🧬", "🧭", "🧮", "🧯", "🧰", "🧱", "🧲", "🧸", "🧾", "🩸", "🩺", "🩻", "🪙", "🫧"]'''))
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF][\uFE0F\u200D\U0001F000-\U0001FAFF]*")
md = open(__import__("sys").argv[1], encoding="utf-8").read(); n = 0
F = chr(96) * 3
SKIP = {"id", "type", "section", "title", "note", "src", "logo", "url", "page", "sources", "logos", "status", "comment"}
def leaves(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in SKIP: yield from leaves(v, (path + "." if path else "") + str(k))
    elif isinstance(x, list):
        for v in x: yield from leaves(v, path + ".*")
    elif isinstance(x, str): yield path, x
plain = lambda v: re.sub(r"\s+", " ", re.sub(r"\{\d\|([^}]*)\}", r"\1", v)).strip()
for sid, body in re.findall(r"### (\S+)\s+" + F + r"yaml\n(.*?)" + F, md, re.S):
    d = yaml.safe_load(body) or {}
    if d.get("status") != "ok": continue
    flat = json.dumps(d, ensure_ascii=False)
    for bad, why in ((chr(8212), "em dash"), (chr(8211), "en dash"), ("; ", "semicolon: write two sentences")):
        if bad in flat.replace("&amp; ", ""): print(sid, "|", why); n += 1
    for m in re.findall(r"\$\d+\.\d{2,}[BMK]|\$\d{2,}\.\d[B]|\$\d+\.0[BMK]|\d+\.\d{2,}%", flat): print(sid, "| amount format:", m, "(write $56B, $2.1B, $1B, 39.7%)"); n += 1
    L = LIMITS.get(sid) or LIMITS.get(re.sub(r"-s\d+$", "", sid)) or {}
    for p, v in leaves(d):
        k = p[2:] if p.startswith("t.") else p
        e = L.get(k)
        if not e or re.fullmatch(r"\s*[^\w\s]{1,4}\s*", v): continue
        t = plain(v); n0 = n
        if len(t) > e["max"]: print(sid, k, "| too long:", len(t), "for max", e["max"], "|", t[:60]); n += 1
        elif e.get("min") and len(t) < e["min"]: print(sid, k, "| too short:", len(t), "for min", e["min"], "(add one concrete fact) |", t[:60]); n += 1
        if e.get("words") and len(t.split()) != e["words"]: print(sid, k, "| must have exactly", e["words"], "words |", t[:40]); n += 1
        if e.get("wordmax") and max(map(len, re.split(r"[\s/-]+|\\n", t))) > e["wordmax"]: print(sid, k, "| a word longer than", e["wordmax"], "letters is cut in two on the slide: use shorter words |", t[:40]); n += 1
    for p, v in (leaves(d) if L.get("__icons__") else []):
        for m in {re.sub(r'(.)\1+', r'\1', x) for x in EMOJI.findall(v)}:
            if m not in ICONS and m.replace(chr(0xFE0F), "") not in ICONS and m + chr(0xFE0F) not in ICONS: print(sid, "| icon", m, "is not drawn: use one from ICONS"); n += 1
    nt = d.get("note"); nl = (L.get("note_line") or {}).get("max", 120)
    if isinstance(nt, list) and len(nt) > 1:
        Ls = [len(str(x)) for x in nt]
        if max(Ls) > nl: print(sid, "note | a line has", max(Ls), "characters for max", nl); n += 1
        if min(Ls) < 0.82 * max(Ls): print(sid, "note | lines of unequal length:", min(Ls), "and", max(Ls), "(rebalance)"); n += 1
print(n, "problems")
