import io, sys

base = r"C:\Users\shi\Desktop\信息科技"

# ---------- 知识笔记 ----------
notes_path = base + r"\七年级备考知识笔记.html"
notes = open(notes_path, encoding="utf-8").read()

notes_mq = """
/* ===== 手机端适配（≤640px） ===== */
@media (max-width:640px){
  .header{padding:24px 16px 18px}
  .header h1{font-size:21px;letter-spacing:1px}
  .header .subtitle,.header .meta{font-size:12px}
  .search-bar{padding:0 12px;margin-top:12px}
  .search-box{padding:6px 12px}
  .tab-nav{padding:12px 10px;gap:4px}
  .tab-btn{padding:7px 12px;font-size:12px}
  .container{padding:16px 12px 50px}
  .module-intro{padding:16px;margin-bottom:16px}
  .module-intro h2{font-size:19px}
  .lesson-header{padding:14px 16px}
  .lesson-header h3{font-size:15px}
  .lesson-header .arrow{margin-left:8px}
  .lesson-body{padding:16px}
  .section-tabs{gap:6px}
  .section-tab{padding:6px 11px;font-size:12px}
  .section-content h3{font-size:15px}
  .section-content p,.section-content li{font-size:14px}
  .kb-table{font-size:12px}
  .kb-table th,.kb-table td{padding:6px 9px}
  .quiz-link{font-size:11px;padding:2px 8px;margin-left:6px}
}
"""
assert notes.count("@media print {") == 1, "notes anchor not unique"
notes = notes.replace("@media print {", notes_mq + "@media print {", 1)
open(notes_path, "w", encoding="utf-8").write(notes)
print("知识笔记: 已插入手机端 @media")

# ---------- 刷题页 ----------
quiz_path = base + r"\七年级刷题练习.html"
quiz = open(quiz_path, encoding="utf-8").read()

quiz_mq = """
/* ===== 手机端适配（≤640px） ===== */
@media (max-width:640px){
  .header{padding:18px 14px}
  .header h1{font-size:20px}
  .header .sub{font-size:12px}
  .header .links{font-size:12px}
  .tab-nav{padding:10px 12px;gap:4px}
  .tab-nav button{padding:6px 11px;font-size:12px}
  .container{padding:12px 10px}
  .lesson-nav{margin-bottom:12px}
  .lesson-nav button{padding:5px 10px;font-size:11px}
  .progress{padding:10px 12px}
  .quiz-card{padding:16px 14px}
  .quiz-card .q-stem{font-size:15px}
  .option-item{padding:12px 14px;font-size:14px}
  .btn{padding:9px 18px;font-size:13px}
  .btn-row{gap:6px}
  .nav-bar{padding:10px 0}
  .nav-bar .btn-nav{padding:8px 12px;font-size:12px}
  .answer-sheet{padding:12px}
  .as-cell{width:30px;height:30px;font-size:11px}
  .as-legend{gap:12px;font-size:11px}
  .analysis-box{padding:14px;font-size:13px}
}
"""
assert quiz.count("</style>") == 1, "quiz style anchor not unique"
quiz = quiz.replace("</style>", quiz_mq + "</style>", 1)
open(quiz_path, "w", encoding="utf-8").write(quiz)
print("刷题页: 已插入手机端 @media")
