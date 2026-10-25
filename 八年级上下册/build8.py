# -*- coding: utf-8 -*-
import json, re, importlib.util, os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)  # 信息科技

def load_mod(name, var):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, name))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)

# ---- 载入数据 ----
NOTES_A = load_mod("notes_a.py", "NOTES_A")
NOTES_B = load_mod("notes_b.py", "NOTES_B")
NOTES_C = load_mod("notes_c.py", "NOTES_C")
Q12 = load_mod("q12.py", "Q12")
Q34 = load_mod("q34.py", "Q34")
Q56 = load_mod("q56.py", "Q56")

all_notes = NOTES_A + NOTES_B + NOTES_C
all_quiz = Q12 + Q34 + Q56

# 安全：把内容中的 </script> 替换为 <\/script> 防止破坏 script 块
def safe(s):
    return s.replace("</script>", "<\\/script>")

for u in all_notes:
    for l in u["lessons"]:
        for k in ("knowledge", "exam", "difficulty", "qa"):
            l[k] = safe(l[k])
for q in all_quiz:
    q["analysis"] = safe(q["analysis"])
    # 选项也可能是字符串列表
    if isinstance(q.get("options"), list):
        q["options"] = [safe(o) for o in q["options"]]

# ---- 构造 MODULES（笔记页格式）----
def build_modules(notes):
    mods = []
    for i, u in enumerate(notes):
        lessons = u["lessons"]
        first = int(lessons[0]["id"][1:])
        last = int(lessons[-1]["id"][1:])
        short = u["module"].split("：", 1)[-1] if "：" in u["module"] else u["module"]
        mods.append({
            "id": "m" + str(i + 1),
            "title": u["module"],
            "subtitle": "第%d-%d课 · %s" % (first, last, short),
            "intro": "<p>" + u["desc"] + "</p>",
            "lessons": lessons,
        })
    return mods

MODULES = build_modules(all_notes)
MODULES_JSON = json.dumps(MODULES, ensure_ascii=False)

# ---- 工具：替换脚本中某个数组变量 ----
def replace_array(html, var_decl, new_json):
    # var_decl 形如 'const MODULES = ' 或 'var DATA = '
    start = html.find(var_decl)
    if start < 0:
        raise RuntimeError("未找到 " + var_decl)
    # 从声明后的 '[' 开始括号计数，找到匹配的 ']'
    b = html.find("[", start)
    depth = 0
    end = -1
    for i in range(b, len(html)):
        c = html[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                end = i
                break
    if end < 0:
        raise RuntimeError("未找到数组结尾")
    # 替换 [ ... ] 为新的 json
    new_html = html[:b] + new_json + html[end + 1:]
    return new_html

def repl_links(html):
    return (html
            .replace("七年级备考知识笔记.html", "八年级备考知识笔记.html")
            .replace("七年级教材参考.html", "八年级教材参考.html")
            .replace("七年级刷题练习.html", "八年级刷题练习.html"))

# ---- 1. 笔记页 ----
notes_tpl = open(os.path.join(ROOT, "七年级备考知识笔记.html"), encoding="utf-8").read()
notes_tpl = replace_array(notes_tpl, "const MODULES = ", MODULES_JSON)
notes_tpl = repl_links(notes_tpl)
open(os.path.join(ROOT, "八年级备考知识笔记.html"), "w", encoding="utf-8").write(notes_tpl)
print("笔记页写入完成, MODULES单元数:", len(MODULES), " 课程:", sum(len(m['lessons']) for m in MODULES))

# ---- 2. 刷题页 ----
quiz_tpl = open(os.path.join(ROOT, "七年级刷题练习.html"), encoding="utf-8").read()
quiz_data_json = json.dumps(all_quiz, ensure_ascii=False)
# 刷题页是 var DATA=[...];var ALL=DATA; 用更精准替换
marker = "var DATA="
start = quiz_tpl.find(marker)
if start < 0:
    raise RuntimeError("未找到 var DATA=")
b = quiz_tpl.find("[", start)
depth = 0
end = -1
for i in range(b, len(quiz_tpl)):
    c = quiz_tpl[i]
    if c == "[":
        depth += 1
    elif c == "]":
        depth -= 1
        if depth == 0:
            end = i
            break
# 找到 ';var ALL=DATA;' 结束位置
tail = quiz_tpl.find(";var ALL=DATA;", end)
if tail < 0:
    raise RuntimeError("未找到 ;var ALL=DATA;")
new_quiz = quiz_tpl[:b] + quiz_data_json + quiz_tpl[tail:]
new_quiz = repl_links(new_quiz)
open(os.path.join(ROOT, "八年级刷题练习.html"), "w", encoding="utf-8").write(new_quiz)
print("刷题页写入完成, 题目数:", len(all_quiz))

print("DONE")
