# -*- coding: utf-8 -*-
"""
信息科技 · 七八年级汇总刷题页 —— 一键构建脚本
把 6 个源 HTML（七年级/八年级 × 刷题/笔记/教材）合并成一个单文件手机刷题页。

用法：双击运行，或 python build.py
源文件：../../七年级刷题练习.html 等（本脚本上一级目录）
输出：  ../信息科技_汇总刷题.html
"""
import os, re, json, sys, traceback
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT  = os.path.abspath(os.path.join(HERE, "..", "信息科技_汇总刷题.html"))
TPLD = os.path.join(HERE, "tpl")

SRC = {
    "quiz_g7": "七年级刷题练习.html",
    "quiz_g8": "八年级刷题练习.html",
    "note_g7": "七年级备考知识笔记.html",
    "note_g8": "八年级备考知识笔记.html",
    "book_g7": "七年级教材参考.html",
    "book_g8": "八年级教材参考.html",
}

LOG = []

# ---------------- 通用工具 ----------------
def extract_json_array(s, start_idx):
    """从 s[start_idx] 处的 '[' 开始做括号匹配"""
    depth, i, in_str, esc = 0, start_idx, False, False
    while i < len(s):
        ch = s[i]
        if in_str:
            if esc: esc = False
            elif ch == '\\': esc = True
            elif ch == '"': in_str = False
        else:
            if ch == '"': in_str = True
            elif ch == '[': depth += 1
            elif ch == ']':
                depth -= 1
                if depth == 0: return s[start_idx:i+1]
        i += 1
    raise ValueError("括号不匹配")

def extract_div_blocks(s):
    """提取 <div class="section..."> 的 (id, inner_html)"""
    out = []
    for m in re.finditer(r'<div\s+class="section[^"]*"[^>]*>', s):
        sid_m = re.search(r'id="([^"]+)"', m.group(0))
        if not sid_m: continue
        i, depth = m.end(), 1
        while i < len(s) and depth > 0:
            nm = re.search(r'<div\b|</div>', s[i:])
            if not nm: break
            pos = i + nm.start()
            if nm.group(0) == '</div>':
                depth -= 1
                if depth == 0:
                    out.append((sid_m.group(1), s[m.end():pos]))
                    break
            else:
                depth += 1
            i = pos + 4
    return out

def clean_html(x):
    return (" " if not x else x).replace("\u201c", "“").replace("\u201d", "”").strip()

def read(name):
    return open(os.path.join(BASE, name), encoding="utf-8-sig").read()

# ---------------- 1. 刷题数据 ----------------
def norm_single(ans, n):
    if isinstance(ans, bool): raise ValueError("bool")
    if isinstance(ans, int):
        if 0 <= ans < n: return ans
        raise ValueError("越界 %s/%s" % (ans, n))
    if isinstance(ans, str):
        s = ans.strip()
        if len(s) == 1 and s.upper() in "ABCDEF":
            v = ord(s.upper()) - 65
            if v < n: return v
        if re.fullmatch(r"\d+", s):
            v = int(s)
            if 0 <= v < n: return v
    raise ValueError("无法解析 %r/%d" % (ans, n))

def norm_multi(ans, n):
    if not isinstance(ans, list): raise ValueError("非list")
    idx = []
    for v in ans:
        if isinstance(v, int): idx.append(v)
        elif isinstance(v, str):
            s = v.strip()
            if len(s) == 1 and s.upper() in "ABCDEF": idx.append(ord(s.upper()) - 65)
            elif re.fullmatch(r"\d+", s): idx.append(int(s))
            else: raise ValueError("项无法解析 %r" % v)
        else: raise ValueError("项类型 %s" % type(v))
    if any(i >= n for i in idx): raise ValueError("越界 %s/%d" % (idx, n))
    return sorted(set(idx))

def build_quiz(items):
    res = OrderedDict()
    for it in items:
        lid = str(it["lesson"]).strip()
        if re.fullmatch(r"\d+", lid): lid = "L%02d" % int(lid)
        t = str(it["type"])
        opts = [clean_html(o) for o in (it.get("options") or [])]
        ans = it.get("answer")
        if t == "single":
            tk, a = "s", norm_single(ans, len(opts))
        elif t in ("multi", "multiple"):
            tk, a = "m", norm_multi(ans, len(opts))
        elif t in ("tf", "judge"):
            tk = "j"; opts = ["正确", "错误"]
            if not isinstance(ans, int) or ans not in (0, 1):
                raise ValueError("判断题答案非法 %r" % (ans,))
            a = 0 if ans == 1 else 1     # 1=正确 → 选项索引 0
        elif t == "short":
            tk, opts, a = "q", [], str(ans)
        else:
            raise ValueError("未知题型 " + t)
        q = {"t": tk, "q": clean_html(it["stem"]), "a": a, "an": clean_html(it.get("analysis", ""))}
        if opts: q["o"] = opts
        res.setdefault(lid, []).append(q)
    return res

# ---------------- 2. 笔记数据 ----------------
def build_notes(mods):
    out = []
    for m in mods:
        out.append({
            "id": m["id"], "title": m["title"], "subtitle": m.get("subtitle", ""),
            "intro": clean_html(m.get("intro", "")),
            "lessons": [{
                "id": l["id"], "title": l["title"],
                "knowledge": clean_html(l.get("knowledge", "")),
                "exam": clean_html(l.get("exam", "")),
                "difficulty": clean_html(l.get("difficulty", "")),
                "qa": l.get("qa") or "",
            } for l in m.get("lessons", [])],
        })
    return out

# ---------------- 3. 教材数据 ----------------
def build_book7(src):
    outline, units = "", []
    for sid, inner in extract_div_blocks(src):
        if sid == "front":
            outline = clean_html(inner); continue
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", inner, re.S)
        title = re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else sid
        page = ""
        pm = re.search(r"\((P[\d\-–]+)\)", title)
        if pm:
            page = pm.group(1); title = title.replace(pm.group(0), "").strip()
        no = ""
        nm = re.match(r"^([一二三四五六七八九十]+)\s*", title)
        if nm:
            no = nm.group(1); title = title[nm.end():].strip()
        marks = [(m.start(), m.end(), int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip())
                 for m in re.finditer(r'<h3[^>]*>\s*<span class="lesson-num"[^>]*>(\d+)</span>\s*(.*?)</h3>', inner, re.S)]
        head = inner[:marks[0][0]] if marks else inner
        lessons = []
        for k, (st, en, num, lname) in enumerate(marks):
            end = marks[k+1][0] if k + 1 < len(marks) else len(inner)
            lessons.append({"no": num,
                            "title": "第%d课 %s" % (num, re.sub(r"\s*核心概念\s*$", "", lname).strip()),
                            "html": clean_html(inner[en:end])})
        units.append({"id": sid, "no": no, "title": title, "page": page,
                      "head": clean_html(head), "lessons": lessons})
    return {"outline": outline, "units": units}

def build_book8(src, tb_units):
    om = re.search(r'var\s+TB_OUTLINE\s*=\s*("(?:[^"\\]|\\.)*")', src)
    outline = clean_html(json.loads(om.group(1))) if om else ""
    units = []
    for u in tb_units:
        nm = re.match(r"^第([一二三四五六七八九十]+)单元\s*(.*)$", u["name"])
        no, title = (nm.group(1), nm.group(2)) if nm else ("", u["name"])
        head = ""
        if u.get("intro"):
            head += '<div class="note-box"><div class="note-title">📌 单元引言</div>%s</div>' % u["intro"]
        if u.get("objectives"):
            head += "<h3>学习目标</h3>%s" % u["objectives"]
        lessons = []
        for l in u.get("lessons", []):
            seg = ""
            if l.get("points"): seg += "<h4>核心概念</h4>%s" % l["points"]
            if l.get("reference"):
                seg += '<div class="ref-box"><div class="ref-title">📝 教学参考</div>%s</div>' % l["reference"]
            lm = re.match(r"^第(\d+)课\s*(.*)$", l["title"])
            lessons.append({"no": int(lm.group(1)) if lm else 0, "title": l["title"], "html": clean_html(seg)})
        units.append({"id": u["id"], "no": no, "title": title, "page": "", "head": clean_html(head), "lessons": lessons})
    return {"outline": outline, "units": units}

# ---------------- 4. 合并 ----------------
TITLE_DIFF = []
def unit_index(notes_g, book_g, gname):
    """课名以笔记为准（与教材配套 PPT 文件名一致），仅记录与教材的差异"""
    units = []
    for i, m in enumerate(notes_g):
        bm = book_g["units"][i] if i < len(book_g["units"]) else None
        book_titles = {}
        if bm:
            for l in bm["lessons"]: book_titles[l["no"]] = l["title"]
        lessons = []
        for l in m["lessons"]:
            no = int(l["id"].replace("L", ""))
            bt = book_titles.get(no)
            if bt and bt != l["title"]:
                TITLE_DIFF.append("%s %s：笔记「%s」≠ 教材「%s」→ 统一用笔记" % (gname, l["id"], l["title"], bt))
            lessons.append({"id": l["id"], "title": l["title"]})
        units.append({"id": "u%d" % (i+1), "no": bm["no"] if bm else "",
                      "title": bm["title"] if bm else m["title"],
                      "page": bm["page"] if bm else "", "lessons": lessons})
    return units

def sync_book_titles(book, units):
    """把教材里的课名对齐到统一课名，避免同一课两种叫法"""
    for u, bu in zip(units, book["units"]):
        tmap = {}
        for l in bu["lessons"]: tmap[l["no"]] = l
        for l in u["lessons"]:
            no = int(l["id"].replace("L", ""))
            if no in tmap: tmap[no]["title"] = l["title"]

def build_db():
    src = {k: read(v) for k, v in SRC.items()}

    quiz = {}
    for g in ("g7", "g8"):
        m = re.search(r"var\s+DATA\s*=\s*\[", src["quiz_" + g])
        if not m: raise ValueError("未找到 DATA：" + SRC["quiz_" + g])
        items = json.loads(extract_json_array(src["quiz_" + g], m.end() - 1))
        quiz[g] = build_quiz(items)
        LOG.append("%s 刷题：%d 课 %d 题" % (g, len(quiz[g]), sum(len(v) for v in quiz[g].values())))

    notes = {}
    for g in ("g7", "g8"):
        m = re.search(r"const\s+MODULES\s*=\s*\[", src["note_" + g])
        if not m: raise ValueError("未找到 MODULES：" + SRC["note_" + g])
        notes[g] = build_notes(json.loads(extract_json_array(src["note_" + g], m.end() - 1)))
        LOG.append("%s 笔记：%d 模块 %d 课" % (g, len(notes[g]), sum(len(x["lessons"]) for x in notes[g])))

    book7 = build_book7(src["book_g7"])
    m = re.search(r"var\s+TB_UNITS\s*=\s*\[", src["book_g8"])
    book8 = build_book8(src["book_g8"], json.loads(extract_json_array(src["book_g8"], m.end() - 1)))
    LOG.append("教材：七年级 %d 单元 / 八年级 %d 单元" % (len(book7["units"]), len(book8["units"])))

    units7 = unit_index(notes["g7"], book7, "七年级")
    units8 = unit_index(notes["g8"], book8, "八年级")
    sync_book_titles(book7, units7)
    sync_book_titles(book8, units8)
    for d in TITLE_DIFF: LOG.append("课名差异 → " + d)

    return {
        "meta": {"g7": {"name": "七年级", "book": "互联网应用与创新"},
                 "g8": {"name": "八年级", "book": "物联网实践与探索"}},
        "units": {"g7": units7, "g8": units8},
        "quiz": quiz, "notes": notes,
        "book": {"g7": book7, "g8": book8},
    }

def render(db):
    css = open(os.path.join(TPLD, "style.css"), encoding="utf-8").read()
    js = open(os.path.join(TPLD, "app.js"), encoding="utf-8").read()
    shell = open(os.path.join(TPLD, "shell.html"), encoding="utf-8").read()
    dbjson = json.dumps(db, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return shell.replace("__CSS__", css).replace("__JS__", js).replace("/*@@DBJSON@@*/", dbjson)

def main():
    db = build_db()
    html = render(db)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    # 自检
    probs = []
    for g in ("g7", "g8"):
        for u in db["units"][g]:
            for l in u["lessons"]:
                if not db["quiz"][g].get(l["id"]): probs.append("%s %s 无题" % (g, l["id"]))
    LOG.append("完整性：%d 个问题" % len(probs))
    LOG.append("输出：%s" % OUT)
    LOG.append("体积：%.2f MB" % (os.path.getsize(OUT) / 1024 / 1024))
    LOG.append("总题数：%d" % sum(len(v) for g in ("g7", "g8") for v in db["quiz"][g].values()))
    txt = "\n".join(LOG)
    open(os.path.join(HERE, "_build_log.txt"), "w", encoding="utf-8").write(txt)
    try:
        print(txt)
    except Exception:
        pass

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
        sys.exit(1)
