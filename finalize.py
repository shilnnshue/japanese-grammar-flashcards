import re, json, sys

BASE = r"C:\Users\27028\WorkBuddy\2026-08-21-15-28-37"
data_path = BASE + r"\grammar_data.json"
ex_path = BASE + r"\examples.json"
html_path = BASE + r"\日语语法闪卡.html"

# 1) load base data
with open(data_path, encoding="utf-8") as f:
    data = json.load(f)

# 2) load generated examples
with open(ex_path, encoding="utf-8") as f:
    ex = json.load(f)

# map by id (examples may be list or dict)
if isinstance(ex, list):
    exmap = {int(e["id"]): e for e in ex}
elif isinstance(ex, dict):
    exmap = {int(k): v for k, v in ex.items()}
else:
    print("examples.json format unknown:", type(ex)); sys.exit(1)

missing = []
for d in data:
    e = exmap.get(int(d["id"]))
    if e and (e.get("ex_jp") or e.get("ex_cn")):
        d["ex_jp"] = (e.get("ex_jp") or "").strip()
        d["ex_cn"] = (e.get("ex_cn") or "").strip()
    else:
        d.setdefault("ex_jp", "")
        d.setdefault("ex_cn", "")
        missing.append(d["id"])

print("Total cards:", len(data), "| examples found:", len(exmap), "| missing:", len(missing))
if missing:
    print("Missing ids:", missing[:20])

# 3) save updated data
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

# 4) re-inject into HTML
js = json.dumps(data, ensure_ascii=False)
js = js.replace("</", "<\\/")
with open(html_path, encoding="utf-8") as f:
    html = f.read()
new_block = "const DATA = " + js + ";"
html2, n = re.subn(r'const DATA = \[.*?\];', new_block, html, count=1, flags=re.S)
if n == 0:
    print("ERROR: could not find DATA block to replace"); sys.exit(1)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html2)

cards_with_ex = sum(1 for d in data if d.get("ex_jp"))
print("Injected. Cards with example sentence:", cards_with_ex, "/", len(data))
print("OK")
