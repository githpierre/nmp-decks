"""Emoji -> SVG icons (Lucide line, Phosphor duotone / fill). Writes icons.json for the atelier pages."""
import json, pathlib, re
NM = pathlib.Path('/home/claude/icons/node_modules')
M = {  # emoji: (lucide, phosphor)
 '📚': ('library-big', 'books'), '💰': ('coins', 'coins'), '🤒': ('frown', 'smiley-sad'), '📉': ('trending-down', 'trend-down'),
 '🎓': ('graduation-cap', 'graduation-cap'), '🔒': ('lock', 'lock'), '🟢': ('circle-check', 'check-circle'), '🗣️': ('speech', 'chat-teardrop-text'),
 '📈': ('trending-up', 'trend-up'), '✓': ('check', 'check'), '🚀': ('rocket', 'rocket-launch'), '🏫': ('school', 'chalkboard-teacher'),
 '🤥': ('circle-help', 'question'), '💼': ('briefcase', 'briefcase'), '🏢': ('building-2', 'building-office'), '📝': ('notebook-pen', 'note-pencil'),
 '🏆': ('trophy', 'trophy'), '🔁': ('repeat', 'repeat'), '📊': ('chart-column', 'chart-bar'), '💎': ('gem', 'diamond'), '🤩': ('laugh', 'smiley'),
 '⛔': ('circle-minus', 'minus-circle'), '💀': ('skull', 'skull'), '🏛️': ('landmark', 'bank'), '🧩': ('puzzle', 'puzzle-piece'), '🤖': ('bot', 'robot'),
 '🔍': ('search', 'magnifying-glass'), '🎯': ('target', 'target'), '📜': ('scroll-text', 'scroll'), '🧪': ('flask-conical', 'flask'), '🏅': ('medal', 'medal'),
 '🎒': ('backpack', 'backpack'), '🤝': ('handshake', 'handshake'), '💸': ('banknote', 'money'), '🏠': ('house', 'house'), '🔥': ('flame', 'fire'),
 '📋': ('clipboard-list', 'clipboard-text'), '🍎': ('apple', 'apple-logo'), '✅': ('circle-check', 'check-circle'), '🧭': ('compass', 'compass'),
 '🖥️': ('monitor', 'desktop'), '📺': ('tv', 'television'), '🧠': ('brain', 'brain'), '⚠️': ('triangle-alert', 'warning'), '🛠️': ('wrench', 'wrench'),
 '📞': ('phone', 'phone'), '👔': ('id-card', 'identification-card'), '💻': ('laptop', 'laptop'), '🔎': ('search', 'magnifying-glass'),
 '💳': ('credit-card', 'credit-card'), '⚖️': ('scale', 'scales'), '🔗': ('link', 'link'), '🧸': ('baby', 'baby'), '📖': ('book-open', 'book-open'),
 '🙋': ('hand', 'hand-waving'), '🏦': ('landmark', 'bank'), '🌱': ('sprout', 'plant'), '❌': ('circle-x', 'x-circle'), '😤': ('angry', 'smiley-angry'),
 '😖': ('frown', 'smiley-x-eyes'), '☠️': ('skull', 'skull'), '💥': ('zap', 'lightning'), '🏷️': ('tag', 'tag'), '🧑‍🤝‍🧑': ('users', 'users'),
 '😣': ('frown', 'smiley-sad'), '🔄': ('refresh-cw', 'arrows-clockwise'), '🎥': ('video', 'video-camera'), '👥': ('users', 'users'), '🆓': ('gift', 'gift'),
 '📱': ('smartphone', 'device-mobile'), '🛡️': ('shield', 'shield'), '📅': ('calendar', 'calendar'), '🏃': ('footprints', 'person-simple-run'),
 '🔓': ('lock-open', 'lock-open'), '📵': ('phone-off', 'phone-x'), '🌍': ('globe', 'globe'), '🦉': ('bird', 'bird'), '📘': ('book', 'book'),
 '🎨': ('palette', 'palette'), '✨': ('sparkles', 'sparkle'), '🎭': ('drama', 'mask-happy'), '🎮': ('gamepad-2', 'game-controller'),
 '⏱️': ('timer', 'timer'), '⏱': ('timer', 'timer'), '🌎': ('globe', 'globe'), '📍': ('map-pin', 'map-pin'), '💡': ('lightbulb', 'lightbulb'),
 '🧑‍🏫': ('presentation', 'chalkboard-teacher'), '👩‍🏫': ('presentation', 'chalkboard-teacher'), '🔐': ('lock', 'lock'),
 '🌐': ('globe', 'globe'), '🛒': ('shopping-cart', 'shopping-cart'), '🎤': ('mic', 'microphone'), '✍️': ('pen-line', 'pen-nib'),
 '🗂️': ('folders', 'folders'), '📦': ('package', 'package'), '⭐': ('star', 'star'), '❓': ('circle-help', 'question'), '🤔': ('circle-help', 'question'),
 '🏗️': ('construction', 'crane'), '🧾': ('receipt', 'receipt'), '📣': ('megaphone', 'megaphone'), '💬': ('message-circle', 'chat-circle'),
 '🧬': ('dna', 'dna'), '🏥': ('hospital', 'hospital'), '💉': ('syringe', 'syringe'), '🩺': ('stethoscope', 'stethoscope'), '🩸': ('droplet', 'drop'),
 '✂️': ('scissors', 'scissors'), '🧫': ('flask-round', 'test-tube'), '🔀': ('shuffle', 'shuffle'), '🧑': ('user', 'user'), '🦠': ('bug', 'virus'),
 '⏳': ('hourglass', 'hourglass'), '🎗️': ('ribbon', 'heart'), '🏭': ('factory', 'factory'), '💧': ('droplet', 'drop'), '⭕': ('circle', 'circle'),
 '♾️': ('infinity', 'infinity'), '🐒': ('paw-print', 'paw-print'), '🔬': ('microscope', 'microscope'), '⚡': ('zap', 'lightning'), '🫧': ('droplets', 'drop-half'),
 '❔': ('circle-help', 'question'), '🦴': ('bone', 'bone'), '🦋': ('heart-pulse', 'butterfly'), '💊': ('pill', 'pill'), '🧲': ('magnet', 'magnet'),
 '🚑': ('ambulance', 'ambulance'), '🧯': ('fire-extinguisher', 'fire-extinguisher'), '🛰️': ('satellite', 'planet'), '🔋': ('battery-charging', 'battery-charging'), '⚙️': ('settings', 'gear'),
 '🚚': ('truck', 'truck'), '🌡️': ('thermometer', 'thermometer'), '🧱': ('brick-wall', 'wall'), '🪙': ('coins', 'coin'), '🔧': ('wrench', 'wrench'), '👁️': ('eye', 'eye'),
 '✖️': ('x', 'x'), '⏰': ('alarm-clock', 'alarm'), '🚧': ('construction', 'barricade'), '📡': ('radio-tower', 'broadcast'), '🧮': ('calculator', 'calculator'),
 '👐': ('hand', 'hand-palm'), '🦾': ('grab', 'hand-grabbing'), '📏': ('ruler', 'ruler'), '🦿': ('footprints', 'footprints'), '🛞': ('disc', 'tire'),
 '🚗': ('car', 'car'), '🧰': ('toolbox', 'toolbox'), '✋': ('hand', 'hand'), '🚶': ('footprints', 'person-simple-walk'),
 '🧑‍💻': ('laptop', 'laptop'), '🏗️': ('construction', 'crane'),
 '__default__': ('circle-dot', 'circle'),
}
def clean(s): return re.sub(r'<!--.*?-->', '', s).strip()
out = {}; miss = []
for e, (lu, ph) in M.items():
    a = NM / f'lucide-static/icons/{lu}.svg'; b = NM / f'@phosphor-icons/core/assets/duotone/{ph}-duotone.svg'; c = NM / f'@phosphor-icons/core/assets/fill/{ph}-fill.svg'
    for f in (a, b, c):
        if not f.exists(): miss.append(str(f))
    if a.exists() and b.exists() and c.exists():
        out[e] = {'line': clean(a.read_text()), 'duo': clean(b.read_text()), 'fill': clean(c.read_text())}
pathlib.Path(__file__).with_name('icons.json').write_text(json.dumps(out, ensure_ascii=False))
print(len(out), 'icons;', 'missing:', miss)
