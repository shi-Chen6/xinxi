base = r"C:\Users\shi\Desktop\信息科技"
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
# 唯一锚点：打印样式块结尾紧接 </style>
anchor = "block!important}}</style>"
assert quiz.count(anchor) == 1, ("anchor count", quiz.count(anchor))
quiz = quiz.replace(anchor, "block!important}}" + quiz_mq + "</style>", 1)
open(quiz_path, "w", encoding="utf-8").write(quiz)
print("刷题页: 已插入手机端 @media")
