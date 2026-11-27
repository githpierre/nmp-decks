import re, json, yaml
LIMITS = json.loads(r'''{"ed101": {"6": {"max": 78, "min": 66}, "7": {"caps": true, "max": 25, "wordmax": 9}, "8": {"max": 80, "min": 54}, "9": {"caps": true, "max": 22, "wordmax": 9}, "10": {"max": 73, "min": 60}, "11": {"max": 18, "wordmax": 9}, "12": {"max": 81, "min": 64}, "13": {"caps": true, "max": 20, "wordmax": 9}, "14": {"max": 81, "min": 62}, "15": {"caps": true, "max": 19, "wordmax": 9}, "16": {"max": 80, "min": 59}, "17": {"caps": true, "max": 20, "wordmax": 9}, "18": {"max": 87, "min": 62}, "19": {"caps": true, "max": 23, "wordmax": 9}, "20": {"max": 75, "min": 56}, "21": {"caps": true, "max": 18, "wordmax": 9}, "__icons__": 1}, "ed102": {"6": {"max": 80, "min": 60}, "7": {"caps": true, "max": 25, "wordmax": 9}, "8": {"max": 78, "min": 59}, "9": {"caps": true, "max": 22, "wordmax": 9}, "10": {"max": 77, "min": 63}, "11": {"max": 18, "wordmax": 9}, "12": {"max": 70, "min": 59}, "13": {"caps": true, "max": 20, "wordmax": 9}, "14": {"max": 81, "min": 62}, "15": {"caps": true, "max": 19, "wordmax": 9}, "16": {"max": 75, "min": 60}, "17": {"caps": true, "max": 20, "wordmax": 9}, "18": {"max": 71, "min": 57}, "19": {"caps": true, "max": 23, "wordmax": 9}, "20": {"max": 76, "min": 59}, "21": {"caps": true, "max": 18, "wordmax": 9}, "__icons__": 1}, "ed103": {"7": {"max": 99, "min": 60}, "9": {"caps": true, "max": 20, "wordmax": 9}, "10": {"max": 94, "min": 76}, "12": {"caps": true, "max": 27, "wordmax": 9}, "15": {"max": 101, "min": 53}, "17": {"caps": true, "max": 24, "wordmax": 15}, "__icons__": 1}, "ed104": {"7": {"max": 99, "min": 60}, "9": {"caps": true, "max": 20, "wordmax": 9}, "10": {"max": 94, "min": 76}, "12": {"caps": true, "max": 27, "wordmax": 9}, "15": {"max": 101, "min": 53}, "17": {"caps": true, "max": 24, "wordmax": 15}, "__icons__": 1}, "ed107": {"5": {"caps": true, "max": 27, "wordmax": 10}, "7": {"max": 133, "min": 94}, "8": {"caps": true, "max": 28, "wordmax": 12}, "10": {"max": 128, "min": 90}, "11": {"caps": true, "max": 27, "wordmax": 13}, "13": {"max": 122, "min": 81}, "14": {"caps": true, "max": 27, "wordmax": 9}, "16": {"max": 121, "min": 85}, "17": {"caps": true, "max": 28, "wordmax": 11}, "19": {"max": 127, "min": 80}, "21": {"caps": true, "max": 48, "wordmax": 14}}, "ed108": {"5": {"caps": true, "max": 48, "wordmax": 14}, "6": {"max": 266, "min": 175}, "7": {"max": 291, "min": 197}, "9": {"caps": true, "max": 30, "wordmax": 10}, "10": {"caps": true, "max": 40, "wordmax": 11}, "12": {"caps": true, "max": 4, "wordmax": 9}}, "ed109": {"6": {"max": 53, "wordmax": 13}, "7": {"max": 53, "wordmax": 12}, "8": {"max": 52, "wordmax": 10}, "9": {"max": 60, "wordmax": 11}, "10": {"max": 50, "wordmax": 13}, "11": {"max": 52, "wordmax": 11}, "12": {"max": 54, "wordmax": 12}, "13": {"max": 54, "wordmax": 12}, "14": {"caps": true, "max": 48, "wordmax": 14}, "22": {"max": 3, "wordmax": 9}, "23": {"max": 3, "wordmax": 9}, "24": {"max": 3, "wordmax": 9}, "25": {"max": 3, "wordmax": 9}, "26": {"max": 3, "wordmax": 9}, "27": {"max": 3, "wordmax": 9}, "28": {"max": 3, "wordmax": 9}, "29": {"max": 3, "wordmax": 9}}}''')
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
