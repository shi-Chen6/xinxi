# -*- coding: utf-8 -*-
import json, importlib.util, os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

def load(name, var):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, name))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, var)

UNITS8 = load("units8.py", "UNITS8")
OUTLINE8 = load("outline8.py", "OUTLINE8")

def safe(s):
    return s.replace("</script>", "<\\/script>")

UNITS8 = json.loads(json.dumps(UNITS8, ensure_ascii=False))
for u in UNITS8:
    u["intro"] = safe(u["intro"]); u["objectives"] = safe(u["objectives"])
    for l in u["lessons"]:
        l["points"] = safe(l["points"]); l["reference"] = safe(l["reference"])
OUTLINE8 = safe(OUTLINE8)

units_json = json.dumps(UNITS8, ensure_ascii=False)
outline_json = json.dumps(OUTLINE8, ensure_ascii=False)

CSS = """
* { box-sizing: border-box; }
body { margin:0; font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
  background:#eef2f6; color:#2c3e50; line-height:1.78; }
.header { background: linear-gradient(135deg,#16a085,#138d75); color:#fff; padding:22px 18px 16px; }
.header h1 { margin:0 0 6px; font-size:22px; }
.header .meta { font-size:13px; opacity:.9; }
.link-bar { margin-top:10px; display:flex; gap:10px; flex-wrap:wrap; }
.link-bar a { color:#fff; text-decoration:none; background:rgba(255,255,255,.18);
  padding:6px 12px; border-radius:18px; font-size:13px; }
.link-bar a:hover { background:rgba(255,255,255,.34); }
.search-wrap { background:#fff; padding:12px 18px; position:sticky; top:0; z-index:40;
  box-shadow:0 2px 10px rgba(0,0,0,.08); display:flex; align-items:center; gap:10px; }
.search-wrap input { flex:1; padding:9px 14px; border:1px solid #d6dde6; border-radius:22px;
  font-size:15px; outline:none; }
.search-wrap input:focus { border-color:#16a085; }
#search-count { font-size:13px; color:#7f8c8d; white-space:nowrap; }
.btn-next { border:none; background:#16a085; color:#fff; padding:8px 14px; border-radius:20px;
  font-size:13px; cursor:pointer; flex:none; }
.layout { display:flex; align-items:flex-start; max-width:1120px; margin:0 auto; padding:18px; gap:18px; }
.sidebar { width:248px; flex:none; position:sticky; top:76px; background:#fff; border-radius:14px;
  padding:14px; box-shadow:0 2px 10px rgba(0,0,0,.05); max-height:calc(100vh - 100px); overflow:auto; }
.side-title { font-size:12px; color:#9aa7b2; margin-bottom:10px; font-weight:700; letter-spacing:2px; }
.nav-item { display:block; width:100%; text-align:left; border:none; background:transparent;
  color:#4a5b6b; padding:11px 12px; border-radius:10px; font-size:14px; cursor:pointer;
  margin-bottom:4px; transition:.18s; border-left:3px solid transparent; }
.nav-item:hover { background:#eef7f4; }
.nav-item.active { background:#eafaf6; color:#138d75; font-weight:600; border-left-color:#16a085; }
.content { flex:1; min-width:0; }
.panel { animation: fade .25s ease; }
@keyframes fade { from{opacity:0; transform:translateY(8px);} to{opacity:1; transform:none;} }
.outline-card { background:#fff; border-radius:16px; padding:24px 28px; box-shadow:0 2px 12px rgba(0,0,0,.05); }
.outline-card h2 { color:#138d75; font-size:22px; border-left:5px solid #16a085; padding-left:12px; margin:0 0 16px; }
.outline-card h3 { color:#2c3e50; margin:18px 0 8px; font-size:17px; }
.outline-card p, .outline-card li { font-size:14.5px; }
.unit-card { background:#fff; border-radius:16px; padding:22px 24px; box-shadow:0 2px 12px rgba(0,0,0,.05); }
.unit-banner { background:linear-gradient(135deg,#16a085,#1abc9c); color:#fff; border-radius:12px;
  padding:18px 20px; margin-bottom:18px; }
.unit-banner h2 { margin:0 0 8px; font-size:21px; }
.unit-banner .u-intro { font-size:14px; opacity:.96; line-height:1.7; }
.unit-obj { background:#f4fbf9; border-left:4px solid #16a085; border-radius:0 10px 10px 0;
  padding:12px 16px; margin:14px 0; }
.unit-obj h3 { margin:0 0 6px; color:#138d75; font-size:16px; }
.lesson { background:#fff; border:1px solid #e8eef3; border-left:4px solid #1abc9c; border-radius:12px;
  padding:16px 18px; margin:14px 0; transition:.18s; }
.lesson:hover { box-shadow:0 4px 14px rgba(22,160,133,.12); }
.lesson-h { margin:0 0 10px; font-size:18px; color:#1f3a4d; display:flex; align-items:center;
  justify-content:space-between; gap:10px; flex-wrap:wrap; }
.quiz-link { font-size:12px; background:#16a085; color:#fff; padding:4px 11px; border-radius:14px;
  text-decoration:none; white-space:nowrap; }
.section { margin-top:10px; border-radius:10px; padding:10px 14px; }
.section h4 { margin:0 0 6px; font-size:14px; }
.sec-points { background:#f7fbfe; }
.sec-points h4 { color:#2980b9; }
.sec-ref { background:#fffdf3; }
.sec-ref h4 { color:#e67e22; }
table.kb-table { width:100%; border-collapse:collapse; margin:12px 0; font-size:14px; }
table.kb-table th, table.kb-table td { border:1px solid #dfe6ec; padding:9px 12px; text-align:left; }
table.kb-table th { background:#f0f7f5; color:#138d75; }
mark { background:#ffe08a; padding:0 2px; border-radius:3px; }
@media (max-width:860px){
  .layout { flex-direction:column; padding:12px; gap:12px; }
  .sidebar { width:100%; position:static; max-height:none; display:flex; gap:8px; overflow-x:auto; padding:10px; }
  .side-title { display:none; }
  .nav-item { white-space:nowrap; margin-bottom:0; flex:none; border-left:none; border-bottom:3px solid transparent; }
  .nav-item.active { border-left:none; border-bottom-color:#16a085; }
}
@media (max-width:640px){
  .header h1{font-size:19px;} .unit-card,.outline-card{padding:16px;}
  .link-bar a{font-size:12px;padding:5px 10px;}
}
"""

JS = """
var TB_UNITS = __UNITS__;
var TB_OUTLINE = __OUTLINE__;
var searchMarks = [];
var curMark = -1;
var NAV = [{label:'📋 课程纲要', idx:-1}].concat(TB_UNITS.map(function(u,i){return {label:u.name, idx:i};}));
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function buildNav(){
  var nav=document.getElementById('side-nav'); nav.innerHTML='';
  NAV.forEach(function(n){
    var b=document.createElement('button');
    b.className='nav-item'+(n.idx===-1?' active':'');
    b.dataset.idx=n.idx; b.textContent=n.label;
    b.onclick=function(){switchPanel(n.idx);};
    nav.appendChild(b);
  });
}
function switchPanel(idx){
  document.querySelectorAll('.nav-item').forEach(function(b){
    b.classList.toggle('active', parseInt(b.dataset.idx,10)===idx);
  });
  clearMarks();
  var panel=document.getElementById('panel');
  if(idx===-1){
    panel.innerHTML='<div class="outline-card panel">'+TB_OUTLINE+'</div>';
  } else {
    var u=TB_UNITS[idx], html='<div class="unit-card panel">';
    html+='<div class="unit-banner"><h2>'+esc(u.name)+'</h2><div class="u-intro">'+u.intro+'</div></div>';
    html+='<div class="unit-obj"><h3>学习目标</h3>'+u.objectives+'</div>';
    u.lessons.forEach(function(l){
      html+='<div class="lesson" id="'+l.id+'">';
      html+='<h3 class="lesson-h"><span>'+esc(l.title)+'</span><a class="quiz-link" href="八年级刷题练习.html#lesson='+l.id+'" onclick="event.stopPropagation()">📝 刷题</a></h3>';
      html+='<div class="section sec-points"><h4>教学要点</h4>'+l.points+'</div>';
      html+='<div class="section sec-ref"><h4>教学参考</h4>'+l.reference+'</div>';
      html+='</div>';
    });
    html+='</div>';
    panel.innerHTML=html;
  }
  if(window.scrollTo) window.scrollTo({top:0,behavior:'smooth'});
}
function clearMarks(){
  document.querySelectorAll('mark').forEach(function(m){
    var p=m.parentNode; if(p){ p.replaceChild(document.createTextNode(m.textContent),m); if(p.normalize)p.normalize(); }
  });
}
function searchText(q){
  q=(q||'').trim(); clearMarks(); searchMarks=[]; curMark=-1;
  var cnt=document.getElementById('search-count');
  if(q.length<1){ cnt.textContent=''; return; }
  var root=document.getElementById('main');
  var walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null,false);
  var nodes=[],t; while(t=walker.nextNode()) nodes.push(t);
  var low=q.toLowerCase(), total=0;
  nodes.forEach(function(node){
    var txt=node.nodeValue; if(!txt||txt.trim()==='') return;
    var lowt=txt.toLowerCase(), i=lowt.indexOf(low);
    if(i<0) return;
    var html='',last=0,k=lowt.indexOf(low);
    while(k>=0){
      html+=esc(txt.substring(last,k))+'<mark>'+esc(txt.substring(k,k+q.length))+'</mark>';
      last=k+q.length; k=lowt.indexOf(low,last);
    }
    html+=esc(txt.substring(last));
    var wrap=document.createElement('span'); wrap.innerHTML=html;
    node.parentNode.replaceChild(wrap,node); total++;
  });
  cnt.textContent=total+' 处匹配';
  searchMarks=Array.prototype.slice.call(root.querySelectorAll('mark'));
  if(searchMarks.length) jumpMark(0);
}
function jumpMark(d){
  if(!searchMarks.length) return;
  if(curMark>=0) searchMarks[curMark].style.background='#ffe08a';
  curMark=(curMark+d+searchMarks.length)%searchMarks.length;
  var m=searchMarks[curMark];
  m.style.background='#ff9f43';
  if(m.scrollIntoView) m.scrollIntoView({block:'center'});
  document.getElementById('search-count').textContent=(curMark+1)+'/'+searchMarks.length+' 处匹配';
}
document.addEventListener('DOMContentLoaded',function(){ buildNav(); switchPanel(-1); });
"""

JS = JS.replace("__UNITS__", units_json).replace("__OUTLINE__", outline_json)

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>八年级物联网实践与探索 · 教材参考</title>
<style>__CSS__</style>
</head>
<body>
<div class="header">
  <h1>八年级 · 物联网实践与探索 · 教材参考</h1>
  <div class="meta">课程纲要 + 6单元教学要点与参考 · 侧栏切换 · 全文检索</div>
  <div class="link-bar">
    <a href="八年级备考知识笔记.html">📖 打开备考知识笔记</a>
    <a href="八年级刷题练习.html">📝 打开刷题练习</a>
  </div>
</div>
<div class="search-wrap">
  <input id="search-input" type="text" placeholder="搜索教材内容（如：传感器、MQTT、自主可控…）" oninput="searchText(this.value)">
  <span id="search-count"></span>
  <button class="btn-next" onclick="jumpMark(1)">下一个 ▶</button>
</div>
<div class="layout">
  <aside class="sidebar">
    <div class="side-title">教材导航</div>
    <nav id="side-nav"></nav>
  </aside>
  <main class="content" id="main">
    <div id="panel"></div>
  </main>
</div>
<script>__JS__</script>
</body>
</html>
"""

HTML = HTML.replace("__CSS__", CSS).replace("__JS__", JS)
open(os.path.join(ROOT, "八年级教材参考.html"), "w", encoding="utf-8").write(HTML)
print("教材参考页（优化版）生成完成, 导航项:", 1+len(UNITS8), " 单元:", len(UNITS8), " 课程:", sum(len(u['lessons']) for u in UNITS8))
