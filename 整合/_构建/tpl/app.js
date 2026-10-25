/* 信息科技 · 七八年级汇总刷题 —— 应用逻辑 */
(function () {
  'use strict';

  var DB = window.__DB__;
  var LS = 'xxkj_union_v1';
  var TYPES = { s: { n: '单选题', c: 's' }, m: { n: '多选题', c: 'm' }, j: { n: '判断题', c: 'j' }, q: { n: '简答题', c: 'q' } };

  /* ================= 状态 ================= */
  var S;
  try {
    var raw = JSON.parse(localStorage.getItem(LS) || '{}');
    S = {
      g: raw.g === 'g8' ? 'g8' : 'g7',
      theme: raw.theme || '',
      prog: raw.prog || {},
      wrong: raw.wrong || {},
      hist: raw.hist || [],
      last: raw.last || null,
      memo: raw.memo || {},
      memoHide: raw.memoHide === true
    };
  } catch (e) {
    S = { g: 'g7', theme: '', prog: {}, wrong: {}, hist: [], last: null, memo: {}, memoHide: false };
  }
  function save() {
    try { localStorage.setItem(LS, JSON.stringify(S)); } catch (e) {}
  }

  /* ================= 工具 ================= */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function strip(h) {
    return String(h || '').replace(/<br\s*\/?>/gi, ' ').replace(/<\/(p|li|tr|h\d|div)>/gi, ' ')
      .replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/\s+/g, ' ').trim();
  }
  function pad2(n) { return n < 10 ? '0' + n : '' + n; }
  function pkey(lid) { return S.g + '|' + lid; }
  function progOf(lid) { return S.prog[pkey(lid)] || {}; }
  function lessonMeta(lid) {
    var us = DB.units[S.g];
    for (var i = 0; i < us.length; i++) {
      for (var j = 0; j < us[i].lessons.length; j++) {
        if (us[i].lessons[j].id === lid) return { unit: us[i], lesson: us[i].lessons[j], ui: i, li: j };
      }
    }
    return null;
  }
  function switchGrade(g) {
    if (S.g === g) return;
    S.g = g; save();
    bookSel = null;
    applyTheme();
    go('quiz');
    render();
  }
  function toast(msg) {
    var t = $('#toast');
    t.textContent = msg; t.classList.add('on');
    clearTimeout(t._tm);
    t._tm = setTimeout(function () { t.classList.remove('on'); }, 1700);
  }
  function go(h) {
    if (('#/' + h) === location.hash) { render(); return; }
    location.hash = '#/' + h;
  }

  /* ================= 主题 ================= */
  function applyTheme() {
    var root = document.documentElement;
    var dark = S.theme === 'dark' || (!S.theme && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    root.setAttribute('data-theme', dark ? 'dark' : 'light');
    root.setAttribute('data-g', S.g);
    var btn = $('#themeBtn');
    if (btn) btn.innerHTML = dark ? ICO.sun : ICO.moon;
    var meta = $('meta[name=theme-color]');
    if (meta) meta.setAttribute('content', dark ? '#0F1114' : (S.g === 'g7' ? '#E67E22' : '#2563EB'));
  }

  /* ================= 图标 ================= */
  var ICO = {
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    quiz: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h8a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/><path d="M9.5 2.5h5v3h-5z"/><path d="M9 11h6M9 15h4"/></svg>',
    note: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H17a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6.5A1.5 1.5 0 0 1 5 19.5Z"/><path d="M9 7.5h6M9 11h6M9 14.5h4"/></svg>',
    book: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6.5C12 5 10.5 4 8.5 4H4v14h4.5c2 0 3.5 1 3.5 2.5"/><path d="M12 6.5C12 5 13.5 4 15.5 4H20v14h-4.5c-2 0-3.5 1-3.5 2.5"/><path d="M12 6.5v14"/></svg>',
    me: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.6"/><path d="M5 20.5c0-3.4 3.1-6 7-6s7 2.6 7 6"/></svg>',
    back: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
    right: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
    eye: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    eyeOff: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3l18 18"/><path d="M10.6 5.2A10.5 10.5 0 0 1 12 5c6.4 0 10 7 10 7a17.6 17.6 0 0 1-3.4 4.4"/><path d="M6.6 6.7C3.7 8.6 2 12 2 12s3.6 7 10 7a9.9 9.9 0 0 0 4.4-1"/></svg>'
  };

  /* ================= 判定 ================= */
  function grade(q, a) {
    if (a === undefined || a === null || a === '') return null;
    if (q.t === 'q') return a === 'ok' ? 1 : 0;
    if (q.t === 'm') {
      if (!a || !a.length) return null;
      var u = a.slice().sort(function (x, y) { return x - y; }).join(',');
      return u === q.a.join(',') ? 1 : 0;
    }
    return a === q.a ? 1 : 0;
  }
  function isMulti(q) { return q.t === 'm'; }
  function ansText(q, a) {
    if (q.t === 'q') return strip(a || '（未作答）');
    var arr = Array.isArray(a) ? a : [a];
    return arr.map(function (i) { return 'ABCDEF'[i] || '?'; }).join('');
  }
  function rightText(q) {
    if (q.t === 'q') return '参考要点';
    var arr = Array.isArray(q.a) ? q.a : [q.a];
    return arr.map(function (i) { return 'ABCDEF'[i] || '?'; }).join('');
  }

  /* ================= 统计 ================= */
  function statsOf(g) {
    var total = 0, done = 0, right = 0, units = [];
    DB.units[g].forEach(function (u) {
      var ut = 0, ud = 0, ur = 0;
      u.lessons.forEach(function (l) {
        var qs = DB.quiz[g][l.id] || [];
        var p = S.prog[g + '|' + l.id] || {};
        ut += qs.length; total += qs.length;
        qs.forEach(function (q, i) {
          if (p[i] !== undefined) {
            var gr = grade(q, p[i]);
            if (gr !== null) { ud++; done++; if (gr === 1) { ur++; right++; } }
          }
        });
      });
      units.push({ u: u, total: ut, done: ud, right: ur });
    });
    return { total: total, done: done, right: right, units: units };
  }
  function wrongCount(g) {
    var n = 0;
    Object.keys(S.wrong).forEach(function (k) { if (k.indexOf(g + '|') === 0) n++; });
    return n;
  }

  /* ================= 路由 ================= */
  function parseHash() {
    var h = (location.hash || '').replace(/^#\/?/, '');
    if (!h) return { tab: 'quiz', a: '', b: '' };
    var p = h.split('/');
    return { tab: p[0] || 'quiz', a: p[1] || '', b: p[2] || '' };
  }
  function render() {
    var r = parseHash();
    var tabMap = { quiz: 'quiz', note: 'note', book: 'book', me: 'me', memo: 'quiz' };
    if (!tabMap[r.tab]) r.tab = 'quiz';
    var activeTab = tabMap[r.tab];
    var nav = document.querySelectorAll('.tabbar button');
    for (var i = 0; i < nav.length; i++) nav[i].classList.toggle('on', nav[i].getAttribute('data-tab') === activeTab);
    var view = $('#view');
    view.style.padding = '';
    V = null; VM = null;
    var m = $('#modal'); if (m) m.classList.remove('on');
    var sh = $('#sheet'); if (sh) sh.classList.remove('on');
    var mk = $('#mask'); if (mk) mk.classList.remove('on');
    syncSeg();
    if (r.tab === 'memo') {
      viewMemo(r.a, r.b);
    } else if (r.tab === 'quiz') {
      if (r.a && r.b) viewQuiz(r.a, r.b);
      else if (r.a) viewLessons(r.a);
      else viewQuizHome();
    } else if (r.tab === 'note') {
      if (r.a && r.b) viewNoteLesson(r.a, r.b);
      else if (r.a) viewNoteModule(r.a);
      else viewNoteHome();
    } else if (r.tab === 'book') {
      if (r.a) viewBookUnit(r.a);
      else viewBookHome();
    } else {
      viewMe();
    }
    wrapTables();
  }
  // 表格加横向滚动容器，避免窄屏把列压到断字
  function wrapTables() {
    var ts = $('#view').querySelectorAll('table');
    for (var i = 0; i < ts.length; i++) {
      var t = ts[i];
      if (t.parentNode && t.parentNode.className === 'tw') continue;
      var w = document.createElement('div');
      w.className = 'tw';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    }
  }

  /* ================= 视图：刷题首页 ================= */
  function viewQuizHome() {
    var g = S.g, st = statsOf(g), h = '';
    h += '<div class="page">';
    h += '<div class="page-hd"><h1>' + DB.meta[g].name + ' · 刷题</h1>';
    h += '<p>' + DB.meta[g].book + ' · 6 单元 ' + DB.units[g].reduce(function (a, u) { return a + u.lessons.length; }, 0) + ' 课 · ' + st.total + ' 题</p></div>';

    if (S.last && S.last.g === g && S.last.lid) {
      var lm = lessonMeta(S.last.lid);
      if (lm) {
        var lqs = DB.quiz[g][S.last.lid] || [];
        var doneN = Object.keys(progOf(S.last.lid)).length;
        if (doneN < lqs.length) {
          h += '<div class="resume" data-go="quiz/' + lm.unit.id + '/' + S.last.lid + '">';
          h += '<div class="r-ico">▶</div><div class="r-tx"><b>' + esc(lm.lesson.title) + '</b>';
          h += '<span>已答 ' + doneN + ' / ' + lqs.length + ' 题，继续加油</span></div>';
          h += '<div class="r-go">继续</div></div>';
        }
      }
    }

    h += '<div class="sec-t">单元练习</div>';
    st.units.forEach(function (x) {
      var u = x.u, pct = x.total ? Math.round(x.done / x.total * 100) : 0;
      h += '<button class="unit" data-go="quiz/' + u.id + '">';
      h += '<div class="u-no">第' + (u.no || '') + '单元' + (u.page ? ' · ' + u.page : '') + '</div>';
      h += '<div class="u-t">' + esc(u.title) + '</div>';
      h += '<div class="u-meta"><span>' + u.lessons.length + ' 课</span><span>' + x.total + ' 题</span>';
      if (x.done > 0) h += '<span>已答 ' + x.done + '</span>';
      h += '<span class="go">' + (pct > 0 ? pct + '%' : '进入') + '</span></div>';
      if (pct > 0) h += '<div class="ubar"><i style="width:' + pct + '%"></i></div>';
      h += '</button>';
    });
    h += '</div>';
    $('#view').innerHTML = h;
  }

  /* ================= 视图：课列表 ================= */
  function viewLessons(uid) {
    var g = S.g, unit = null;
    DB.units[g].forEach(function (u) { if (u.id === uid) unit = u; });
    if (!unit) { go('quiz'); return; }
    var h = '<div class="page">';
    h += '<div class="backbar"><button data-go="quiz">' + ICO.back + ' 单元</button>';
    h += '<span class="bb-t">' + unit.lessons.length + ' 课</span></div>';
    h += '<div class="page-hd"><h1>第' + (unit.no || '') + '单元 ' + esc(unit.title) + '</h1>';
    h += '<p>' + DB.meta[g].name + ' · ' + unit.lessons.reduce(function (a, l) { return a + (DB.quiz[g][l.id] || []).length; }, 0) + ' 题</p></div>';
    unit.lessons.forEach(function (l) {
      var qs = DB.quiz[g][l.id] || [], p = progOf(l.id);
      var doneN = 0, rightN = 0;
      qs.forEach(function (q, i) { if (p[i] !== undefined) { var gr = grade(q, p[i]); if (gr !== null) { doneN++; if (gr === 1) rightN++; } } });
      var full = doneN >= qs.length && qs.length > 0;
      h += '<div class="lesson' + (full ? ' done' : '') + '" data-go="quiz/' + uid + '/' + l.id + '">';
      h += '<div class="l-idx">' + (full ? '✓' : parseInt(l.id.replace(/\D/g, ''), 10)) + '</div>';
      h += '<div class="l-main"><div class="l-t">' + esc(l.title) + '</div><div class="l-s">';
      h += '<span>' + qs.length + ' 题</span>';
      if (doneN > 0) { h += '<span>已答 ' + doneN + '</span><em class="' + (rightN / doneN < 0.6 ? 'bad' : '') + '">正确率 ' + Math.round(rightN / doneN * 100) + '%</em>'; }
      else h += '<span>未开始</span>';
      h += '</div></div>';
      h += '<button class="memo-btn" data-go="memo/' + uid + '/' + l.id + '">背题</button>';
      h += '<div class="arrows">' + ICO.right + '</div></div>';
    });
    h += '</div>';
    $('#view').innerHTML = h;
  }

  /* ================= 视图：答题 ================= */
  var V = null;
  var VM = null;   // 背题模式

  function viewQuiz(uid, lid) {
    var g = S.g, qs = DB.quiz[g][lid];
    var lm = lessonMeta(lid);
    if (!qs || !lm) { go('quiz'); return; }
    var saved = progOf(lid);
    V = { uid: uid, lid: lid, qs: qs, i: 0, ans: {}, open: {}, pick: {}, finished: false, unit: lm.unit, lesson: lm.lesson };
    Object.keys(saved).forEach(function (k) { V.ans[+k] = saved[k]; });
    V.i = Math.min(S.last && S.last.g === g && S.last.lid === lid ? (S.last.i || 0) : 0, qs.length - 1);

    var h = '<div class="quizwrap">';
    h += '<div class="qhead"><button class="bt" data-go="quiz/' + uid + '">' + ICO.back + '</button>';
    h += '<div class="mid"><b>' + esc(lm.lesson.title) + '</b><span id="qpos"></span></div>';
    h += '<button class="bt" id="btnMemo2" title="背题模式">' + ICO.book + '</button>';
    h += '<button class="bt" id="btnSheet2" title="答题卡">☰</button></div>';
    h += '<div class="qprog"><i id="qprog"></i></div>';
    h += '<div id="qbody"></div>';
    h += '</div>';
    h += '<div class="qfoot"><button class="btn ghost" id="btnPrev">上一题</button>';
    h += '<button class="sheet-btn" id="btnSheet"><span class="ico">▦</span>答题卡</button>';
    h += '<button class="btn" id="btnNext">下一题</button></div>';
    $('#view').innerHTML = h;
    $('#view').style.padding = '0';
    paintQ();
  }

  function paintQ() {
    var q = V.qs[V.i], a = V.ans[V.i], gr = grade(q, a);
    var locked = gr !== null;
    var ty = TYPES[q.t];
    var showAna = locked || V.open[V.i];

    // 进度
    var answered = 0;
    V.qs.forEach(function (qq, i) { if (grade(qq, V.ans[i]) !== null) answered++; });
    $('#qpos').textContent = (V.i + 1) + ' / ' + V.qs.length + ' · 已答 ' + answered;
    $('#qprog').style.width = (answered / V.qs.length * 100) + '%';

    var h = '<div class="qcard">';
    h += '<div class="qtop"><span class="badge ' + ty.c + '">' + ty.n + '</span><span class="qno">' + pad2(V.i + 1) + '</span></div>';
    h += '<div class="stem">' + esc(q.q) + '</div>';

    if (q.t === 'q') {
      var tv = (V.txt && V.txt[V.i] !== undefined) ? V.txt[V.i] : (typeof a === 'string' && a !== 'ok' && a !== 'no' ? a : '');
      h += '<textarea class="ta" id="qta" placeholder="在这里写下你的答案..."' + (locked ? ' readonly' : '') + '>' + esc(tv) + '</textarea>';
      if (!locked) {
        h += '<div class="selfgrade"><button class="btn soft" id="btnShowRef">查看参考答案</button></div>';
      } else {
        h += '<div class="selfgrade"><button class="btn ' + (gr === 1 ? 'ok' : 'bad') + '" disabled>' + (gr === 1 ? '✓ 已标记：我答对了' : '✕ 已标记：没答对') + '</button></div>';
      }
      if (showAna) {
        h += '<div class="ana"><div style="font-weight:800;color:var(--accText);margin-bottom:4px;">参考答案</div>' + esc(q.a).replace(/\n/g, '<br>') + '<div style="margin-top:9px;">' + q.an + '</div>';
        if (!locked) {
          h += '<div class="selfgrade"><button class="btn ok" data-self="ok">我答对了</button><button class="btn bad" data-self="no">没答对</button></div>';
        }
        h += '</div>';
      }
    } else {
      var opts = q.o || [];
      var pickArr = isMulti(q) ? (V.pick[V.i] || (Array.isArray(a) ? a.slice() : [])) : null;
      h += '<div id="opts">';
      opts.forEach(function (o, oi) {
        var cls = 'opt', res = '';
        var chosen = isMulti(q) ? (pickArr.indexOf(oi) >= 0) : (a === oi);
        if (locked) {
          var inAns = (Array.isArray(q.a) ? q.a : [q.a]).indexOf(oi) >= 0;
          if (inAns) { cls += ' ok'; res = '✓'; }
          else if (chosen) { cls += ' bad'; res = '✕'; }
          else cls += ' fade';
          cls += ' locked';
        } else if (chosen) cls += ' sel';
        h += '<div class="' + cls + '" data-opt="' + oi + '">';
        h += '<span class="k">' + (locked && (Array.isArray(q.a) ? q.a : [q.a]).indexOf(oi) >= 0 ? '✓' : 'ABCDEF'[oi]) + '</span>';
        h += '<span class="tx">' + esc(String(o).replace(/^[A-F][.、．]\s*/, '')) + '</span>';
        if (res) h += '<span class="res">' + res + '</span>';
        h += '</div>';
      });
      h += '</div>';
      if (isMulti(q) && !locked) {
        h += '<div class="selfgrade"><button class="btn" id="btnConfirm"' + (pickArr.length ? '' : ' disabled') + '>确认作答</button></div>';
      }
      if (showAna) h += '<div class="ana">' + q.an + '</div>';
    }
    h += '</div>';
    $('#qbody').innerHTML = h;

    // 按钮状态
    $('#btnPrev').disabled = V.i <= 0;
    $('#btnNext').textContent = V.i >= V.qs.length - 1 ? '完成本课' : '下一题';
    $('#btnNext').className = 'btn' + (V.i >= V.qs.length - 1 ? ' ok' : '');
    wrapTables();
  }

  /* ================= 视图：背题模式 ================= */
  function viewMemo(uid, lid) {
    var g = S.g, qs = DB.quiz[g][lid], lm = lessonMeta(lid);
    if (!qs || !lm) { go('quiz'); return; }
    if (!S.memo) S.memo = {};
    var start = S.memo[lid];
    if (typeof start !== 'number' || start < 0 || start >= qs.length) start = 0;
    VM = { uid: uid, lid: lid, qs: qs, i: start, hide: S.memoHide === true, rev: {}, unit: lm.unit, lesson: lm.lesson };

    var h = '<div class="quizwrap">';
    h += '<div class="qhead"><button class="bt" data-go="quiz/' + uid + '">' + ICO.back + '</button>';
    h += '<div class="mid"><b>' + esc(lm.lesson.title) + '</b><span id="qpos"></span></div>';
    h += '<button class="bt" id="btnEye" title="遮挡答案"></button></div>';
    h += '<div class="qprog"><i id="qprog"></i></div>';
    h += '<div id="qbody"></div>';
    h += '</div>';
    h += '<div class="qfoot"><button class="btn ghost" id="mPrev">上一题</button>';
    h += '<span class="mpos" id="mPos"></span>';
    h += '<button class="btn" id="mNext">下一题</button></div>';
    $('#view').innerHTML = h;
    paintMemo();
  }

  function memoGo(i) {
    if (!VM || i < 0 || i >= VM.qs.length) return;
    VM.i = i;
    if (!S.memo) S.memo = {};
    S.memo[VM.lid] = i;
    save();
    paintMemo();
    window.scrollTo(0, 0);
  }

  function paintMemo() {
    var q = VM.qs[VM.i], ty = TYPES[q.t];
    var hidden = VM.hide && !VM.rev[VM.i];
    $('#qpos').textContent = '背题 ' + (VM.i + 1) + ' / ' + VM.qs.length;
    $('#qprog').style.width = ((VM.i + 1) / VM.qs.length * 100) + '%';
    $('#mPos').textContent = (VM.i + 1) + ' / ' + VM.qs.length;
    var eye = $('#btnEye');
    if (eye) {
      eye.innerHTML = VM.hide ? ICO.eyeOff : ICO.eye;
      eye.setAttribute('data-hide', VM.hide ? '1' : '0');
      eye.title = VM.hide ? '当前：先遮住答案（点一下改回直接看）' : '当前：直接看答案（点一下改成先遮住）';
    }

    var h = '<div class="qcard">';
    h += '<div class="qtop"><span class="badge ' + ty.c + '">' + ty.n + '</span><span class="qno">' + pad2(VM.i + 1) + '</span></div>';
    h += '<div class="stem">' + esc(q.q) + '</div>';

    if (hidden) {
      h += '<button class="reveal" data-reveal="1">轻点显示答案</button>';
    } else if (q.t === 'q') {
      h += '<div class="refans"><b>参考答案</b>' + esc(q.a).replace(/\n/g, '<br>') + '</div>';
      h += '<div class="ana">' + q.an + '</div>';
    } else {
      var idx = Array.isArray(q.a) ? q.a : [q.a];
      (q.o || []).forEach(function (o, oi) {
        var ok = idx.indexOf(oi) >= 0;
        h += '<div class="opt memo' + (ok ? ' ok' : '') + '">';
        h += '<span class="k">' + 'ABCDEF'[oi] + '</span>';
        h += '<span class="tx">' + esc(String(o).replace(/^[A-F][.、．]\s*/, '')) + '</span>';
        if (ok) h += '<span class="res">✓</span>';
        h += '</div>';
      });
      h += '<div class="ana">' + q.an + '</div>';
    }
    h += '</div>';
    $('#qbody').innerHTML = h;

    $('#mPrev').disabled = VM.i <= 0;
    var nx = $('#mNext');
    if (VM.i >= VM.qs.length - 1) { nx.textContent = '去刷题'; nx.className = 'btn ok'; }
    else { nx.textContent = '下一题'; nx.className = 'btn'; }
    wrapTables();
  }

  function record(i, val) {
    V.ans[i] = val;
    var q = V.qs[i], gr = grade(q, val);
    var k = S.g + '|' + V.lid;
    if (!S.prog[k]) S.prog[k] = {};
    S.prog[k][i] = val;
    var wk = S.g + '|' + V.lid + '|' + i;
    if (gr === 1) delete S.wrong[wk];
    else if (gr === 0) S.wrong[wk] = Date.now();
    S.last = { g: S.g, lid: V.lid, i: i };
    save();
  }

  function afterAnswer() {
    paintQ();
    var all = true;
    V.qs.forEach(function (q, i) { if (grade(q, V.ans[i]) === null) all = false; });
    if (all && !V.finished) {
      V.finished = true;
      pushHist();
      setTimeout(showResult, 340);
    }
  }

  function pushHist() {
    var c = 0;
    V.qs.forEach(function (q, i) { if (grade(q, V.ans[i]) === 1) c++; });
    S.hist.unshift({ t: Date.now(), g: S.g, l: V.lid, u: V.uid, n: V.qs.length, c: c });
    if (S.hist.length > 60) S.hist.length = 60;
    save();
  }

  function showResult() {
    var c = 0;
    V.qs.forEach(function (q, i) { if (grade(q, V.ans[i]) === 1) c++; });
    var n = V.qs.length, rate = Math.round(c / n * 100);
    var box = $('#modal');
    box.querySelector('.mbox').innerHTML =
      '<h3>' + (rate >= 90 ? '🎉 太棒了！' : rate >= 70 ? '👍 完成！' : '💪 再练一次') + '</h3>' +
      '<div class="sub">' + esc(V.lesson.title) + '</div>' +
      '<div class="score-ring" style="color:' + (rate >= 80 ? 'var(--ok)' : rate >= 60 ? 'var(--accText)' : 'var(--bad)') + '">' + rate + '<small>%</small></div>' +
      '<div class="stat-row"><div><b>' + c + '</b>答对</div><div><b>' + (n - c) + '</b>答错</div><div><b>' + n + '</b>总题</div></div>' +
      '<div class="acts">' +
      (n - c > 0 ? '<button class="btn block" id="rWrong">回看错题（' + (n - c) + '）</button>' : '') +
      '<button class="btn soft block" id="rExport">导出错题 CSV</button>' +
      '<button class="btn ghost block" id="rAgain">重做本课</button>' +
      '<button class="btn ghost block" id="rBack">返回课列表</button>' +
      '</div>';
    box.classList.add('on');
  }

  /* ================= 答题卡 ================= */
  function openSheet() {
    var h = '<div class="sh-hd"><h3>答题卡</h3><button id="sheetClose">完成</button></div>';
    h += '<div class="legend"><span><i style="background:var(--okSoft);border:1px solid var(--ok)"></i>答对</span>';
    h += '<span><i style="background:var(--badSoft);border:1px solid var(--bad)"></i>答错</span>';
    h += '<span><i style="background:var(--card2);border:1px solid var(--line)"></i>未答</span></div>';
    h += '<div class="grid">';
    V.qs.forEach(function (q, i) {
      var gr = grade(q, V.ans[i]), cls = 'cell';
      if (gr === 1) cls += ' ok'; else if (gr === 0) cls += ' bad';
      if (i === V.i) cls += ' cur';
      h += '<div class="' + cls + '" data-jump="' + i + '">' + (i + 1) + '</div>';
    });
    h += '</div>';
    var sh = $('#sheet');
    sh.innerHTML = h;
    sh.classList.add('on');
    $('#mask').classList.add('on');
  }
  function closeSheet() {
    $('#sheet').classList.remove('on');
    $('#mask').classList.remove('on');
  }

  /* ================= 视图：笔记 ================= */
  function viewNoteHome() {
    var g = S.g, mods = DB.notes[g];
    var h = '<div class="page">';
    h += '<div class="page-hd"><h1>' + DB.meta[g].name + ' · 笔记</h1><p>' + mods.length + ' 模块 · ' + mods.reduce(function (a, m) { return a + m.lessons.length; }, 0) + ' 课 · 支持全文检索</p></div>';
    h += '<div class="search"><span class="ic">🔍</span><input id="sIn" type="search" placeholder="搜索知识点，如「三次握手」「传感器」" autocomplete="off"></div>';
    h += '<div id="sList"></div>';
    h += '<div id="modList">';
    mods.forEach(function (m) {
      h += '<div class="acc" id="acc_' + m.id + '">';
      h += '<button class="acc-hd" data-acc="' + m.id + '">';
      h += '<span class="a-no">' + m.id.replace('m', '') + '</span>';
      h += '<span class="a-t">' + esc(m.title.replace(/^第.模块[：:]/, '')) + '<br><span style="font-size:10.5px;color:var(--tx2);font-weight:600;">' + esc(m.subtitle) + '</span></span>';
      h += '<span class="a-x">▾</span></button>';
      h += '<div class="acc-bd">';
      m.lessons.forEach(function (l) {
        h += '<div class="row" data-go="note/' + m.id + '/' + l.id + '"><span>' + esc(l.title) + '</span><em>读 ›</em></div>';
      });
      h += '</div></div>';
    });
    h += '</div></div>';
    $('#view').innerHTML = h;
  }

  function doSearch(kw) {
    var list = $('#sList'), modList = $('#modList');
    kw = kw.trim();
    if (!kw) { list.innerHTML = ''; modList.style.display = ''; return; }
    modList.style.display = 'none';
    var hits = [];
    DB.notes[S.g].forEach(function (m) {
      m.lessons.forEach(function (l) {
        var fields = { '知识点': l.knowledge, '考点': l.exam, '易混': l.difficulty, '简答': l.qa };
        var found = null, where = '', snip = '';
        Object.keys(fields).forEach(function (fn) {
          if (found) return;
          var txt = strip(fields[fn]);
          var idx = txt.indexOf(kw);
          if (idx >= 0) {
            found = l; where = fn;
            snip = txt.slice(Math.max(0, idx - 30), idx + 90);
          }
        });
        if (!found && l.title.indexOf(kw) >= 0) { found = l; where = '课名'; snip = l.title; }
        if (found) hits.push({ m: m, l: l, where: where, snip: snip });
      });
    });
    if (!hits.length) { list.innerHTML = '<div class="empty"><span class="big">🔍</span>没有找到「' + esc(kw) + '」</div>'; return; }
    var h = '<div class="sec-t">找到 ' + hits.length + ' 条</div>';
    hits.slice(0, 40).forEach(function (x) {
      var s = esc(x.snip).replace(new RegExp(esc(kw).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), '<mark>' + esc(kw) + '</mark>');
      h += '<div class="sres" data-go="note/' + x.m.id + '/' + x.l.id + '">';
      h += '<div class="s-h"><em>' + x.where + '</em>' + esc(x.l.title) + '</div>';
      h += '<div class="s-b">' + s + '</div></div>';
    });
    list.innerHTML = h;
  }

  function viewNoteModule(mid) {
    var mod = null;
    DB.notes[S.g].forEach(function (m) { if (m.id === mid) mod = m; });
    if (!mod) { go('note'); return; }
    var h = '<div class="page">';
    h += '<div class="backbar"><button data-go="note">' + ICO.back + ' 笔记</button><span class="bb-t">' + mod.lessons.length + ' 课</span></div>';
    h += '<div class="page-hd"><h1>' + esc(mod.title) + '</h1><p>' + esc(mod.subtitle) + '</p></div>';
    if (mod.intro) h += '<div class="card" style="padding:13px 14px;margin-bottom:11px;"><div class="kb">' + mod.intro + '</div></div>';
    mod.lessons.forEach(function (l) {
      h += '<div class="lesson" data-go="note/' + mid + '/' + l.id + '">';
      h += '<div class="l-idx">' + parseInt(l.id.replace(/\D/g, ''), 10) + '</div>';
      h += '<div class="l-main"><div class="l-t">' + esc(l.title) + '</div><div class="l-s"><span>知识点 · 考点 · 易混 · 简答</span></div></div>';
      h += '<div class="arrows">' + ICO.right + '</div></div>';
    });
    h += '</div>';
    $('#view').innerHTML = h;
  }

  function viewNoteLesson(mid, lid) {
    var mod = null, les = null;
    DB.notes[S.g].forEach(function (m) { if (m.id === mid) { mod = m; m.lessons.forEach(function (l) { if (l.id === lid) les = l; }); } });
    if (!mod || !les) { go('note'); return; }
    var h = '<div class="page">';
    h += '<div class="backbar"><button data-go="note/' + mid + '">' + ICO.back + ' ' + esc(mod.title.replace(/^第.模块[：:]/, '')) + '</button></div>';
    h += '<div class="page-hd"><h1>' + esc(les.title) + '</h1><p>' + esc(mod.subtitle) + '</p></div>';
    h += '<div class="card" style="padding:14px;"><div class="kb">' + (les.knowledge || '<p>暂无内容</p>') + '</div></div>';
    if (les.exam) h += part('📌 考点聚焦', les.exam);
    if (les.difficulty) h += part('⚠️ 易混辨析', les.difficulty);
    if (les.qa) h += part('✍️ 简答演练', les.qa);
    h += '<div style="margin-top:16px;"><button class="btn block" data-go="quiz/' + unitIdOfLesson(lid) + '/' + lid + '">去做这一课的题 →</button></div>';
    h += '</div>';
    $('#view').innerHTML = h;
  }
  function part(title, html) {
    return '<div class="part"><div class="part-hd">' + title + '</div><div class="part-body"><div class="kb">' + html + '</div></div></div>';
  }
  function unitIdOfLesson(lid) {
    var u = DB.units[S.g];
    for (var i = 0; i < u.length; i++) for (var j = 0; j < u[i].lessons.length; j++) if (u[i].lessons[j].id === lid) return u[i].id;
    return 'u1';
  }

  /* ================= 视图：教材 ================= */
  var bookSel = null;
  function viewBookHome() {
    var g = S.g, bk = DB.book[g];
    if (!bookSel) bookSel = 'outline';
    var h = '<div class="page">';
    h += '<div class="page-hd"><h1>' + DB.meta[g].name + ' · 教材</h1><p>' + esc(DB.meta[g].book) + ' · 课程纲要与单元要点</p></div>';
    h += '<div style="display:flex;gap:6px;overflow-x:auto;padding-bottom:10px;margin-bottom:2px;-webkit-overflow-scrolling:touch;">';
    h += '<button class="btn sm ' + (bookSel === 'outline' ? '' : 'ghost') + '" data-book="outline" style="white-space:nowrap;flex:none">课程纲要</button>';
    bk.units.forEach(function (u) {
      h += '<button class="btn sm ' + (bookSel === u.id ? '' : 'ghost') + '" data-book="' + u.id + '" style="white-space:nowrap;flex:none">第' + u.no + '单元</button>';
    });
    h += '</div>';
    if (bookSel === 'outline') {
      h += '<div class="card" style="padding:14px;"><div class="tb">' + (bk.outline || '<p>暂无纲要</p>') + '</div></div>';
    } else {
      var u = null;
      bk.units.forEach(function (x) { if (x.id === bookSel) u = x; });
      if (!u) { bookSel = 'outline'; return viewBookHome(); }
      h += '<div class="card" style="padding:14px;margin-bottom:10px;"><div class="tb">' + (u.head || '') + '</div></div>';
      u.lessons.forEach(function (l, i) {
        h += '<div class="acc" id="bl_' + i + '">';
        h += '<button class="acc-hd" data-bacc="' + i + '"><span class="a-no">' + (l.no || i + 1) + '</span>';
        h += '<span class="a-t">' + esc(l.title) + '</span><span class="a-x">▾</span></button>';
        h += '<div class="acc-bd"><div class="tb" style="padding-top:8px;">' + (l.html || '<p style="color:var(--tx3)">暂无内容</p>') + '</div>';
        h += '<button class="btn soft sm" style="margin:10px 0 2px;" data-go="quiz/' + u.id + '/' + l.id + '">练这一课（' + ((DB.quiz[g][l.id] || []).length) + ' 题）</button>';
        h += '</div></div>';
      });
    }
    h += '</div>';
    $('#view').innerHTML = h;
    wrapTables();
  }
  function viewBookUnit(uid) { bookSel = uid; go('book'); }

  /* ================= 视图：我的 ================= */
  function viewMe() {
    var g = S.g, st = statsOf(g), g8 = statsOf('g8'), g7 = statsOf('g7');
    var h = '<div class="page">';
    h += '<div class="page-hd"><h1>我的</h1><p>学习进度与错题管理</p></div>';

    var rate = st.done ? Math.round(st.right / st.done * 100) : 0;
    h += '<div class="ov"><div class="big-n">' + st.done + '<small>&nbsp;/ ' + st.total + ' 题</small></div>';
    h += '<div class="ov-sub">' + DB.meta[g].name + '已练题数 · 正确率 ' + rate + '% · 错题 ' + wrongCount(g) + ' 道</div>';
    h += '<div class="ov-bars">';
    [['七年级', g7], ['八年级', g8]].forEach(function (x) {
      var pct = x[1].total ? Math.round(x[1].done / x[1].total * 100) : 0;
      h += '<div class="ov-line"><b>' + x[0].replace('年级', '') + '</b>';
      h += '<div class="bar"><i style="width:' + pct + '%"></i></div>';
      h += '<em>' + x[1].done + '/' + x[1].total + '</em></div>';
    });
    h += '</div></div>';

    var wTotal = wrongCount('g7') + wrongCount('g8');
    h += '<div class="sec-t">错题本（共 ' + wTotal + ' 道）</div>';
    if (!wTotal) {
      h += '<div class="empty" style="padding:26px;"><span class="big">✨</span>还没有错题，继续保持</div>';
    } else {
      var keys = Object.keys(S.wrong).sort(function (a, b) { return S.wrong[b] - S.wrong[a]; });
      var f = S.meFilter || 'all';
      if (f !== 'all') keys = keys.filter(function (k) { return k.indexOf(f + '|') === 0; });
      keys = keys.slice(0, 30);
      h += '<div style="display:flex;gap:6px;margin-bottom:9px;">';
      h += '<button class="btn sm ' + (f !== 'g7' && f !== 'g8' ? '' : 'ghost') + '" data-wf="all" style="flex:1">全部</button>';
      h += '<button class="btn sm ' + (f === 'g7' ? '' : 'ghost') + '" data-wf="g7" style="flex:1">七年级</button>';
      h += '<button class="btn sm ' + (f === 'g8' ? '' : 'ghost') + '" data-wf="g8" style="flex:1">八年级</button>';
      h += '</div>';
      if (!keys.length) h += '<div class="empty" style="padding:24px;">该年级暂无错题</div>';
      keys.forEach(function (k) {
        var p = k.split('|'), kg = p[0], lid = p[1], qi = +p[2];
        var qs = DB.quiz[kg][lid]; if (!qs || !qs[qi]) return;
        var q = qs[qi], lm = null;
        DB.units[kg].forEach(function (u) { u.lessons.forEach(function (l) { if (l.id === lid) lm = { u: u, l: l }; }); });
        h += '<div class="wq" data-go="quiz/' + (lm ? lm.u.id : 'u1') + '/' + lid + '" data-wq="' + k + '">';
        h += '<div class="w-h"><span class="tag">' + (kg === 'g7' ? '七年级' : '八年级') + '</span>' + esc(lm ? lm.l.title : lid) + ' · 第' + (qi + 1) + '题 · ' + TYPES[q.t].n + '</div>';
        h += '<div class="w-q">' + esc(q.q) + '</div></div>';
      });
      h += '<div style="display:flex;gap:7px;margin-top:10px;"><button class="btn soft" id="btnExportAll" style="flex:1">导出全部错题 CSV</button></div>';
    }

    h += '<div class="sec-t">答题记录</div>';
    if (!S.hist.length) {
      h += '<div class="empty" style="padding:24px;"><span class="big">📋</span>完成一课后会记录在这里</div>';
    } else {
      var hs = S.hist.slice(0, 8);
      h += '<div class="card" style="padding:4px 13px;">';
      hs.forEach(function (x) {
        var c = DB.quiz[x.g] && DB.quiz[x.g][x.l]; if (!c) return;
        var lm = null; DB.units[x.g].forEach(function (u) { u.lessons.forEach(function (l) { if (l.id === x.l) lm = l; }); });
        var r = Math.round(x.c / x.n * 100);
        var d = new Date(x.t);
        h += '<div class="hist-row"><div class="h-l"><b>' + esc(lm ? lm.title : x.l) + '</b>';
        h += '<span>' + (d.getMonth() + 1) + '月' + d.getDate() + '日 ' + pad2(d.getHours()) + ':' + pad2(d.getMinutes()) + ' · ' + (x.g === 'g7' ? '七年级' : '八年级') + '</span></div>';
        h += '<div class="h-r ' + (r >= 80 ? 'good' : 'bad') + '">' + x.c + '/' + x.n + '</div></div>';
      });
      h += '</div>';
    }

    h += '<div class="sec-t">设置</div>';
    h += '<div class="card" style="padding:0 13px;">';
    h += '<div class="kv"><span>深色模式</span><div class="switch" id="swTheme"></div></div>';
    h += '<div class="kv"><span>清空本年级进度</span><button class="btn sm ghost" id="btnClear">清空</button></div>';
    h += '</div>';
    h += '<div style="text-align:center;font-size:10.5px;color:var(--tx3);margin-top:18px;line-height:1.7;">信息科技 · 七年级 + 八年级 汇总<br>共 ' + (g7.total + g8.total) + ' 题 · 60 课 · 本地保存，不联网</div>';
    h += '</div>';
    $('#view').innerHTML = h;
    var sw = $('#swTheme');
    if (sw) sw.classList.toggle('on', document.documentElement.getAttribute('data-theme') === 'dark');
  }

  /* ================= 导出 CSV ================= */
  function csvCell(v) {
    v = String(v == null ? '' : v).replace(/"/g, '""');
    return '"' + v + '"';
  }
  function exportWrong(onlyGrade) {
    var rows = [['年级', '单元', '课', '题号', '题型', '题干', '选项', '正确答案', '你的答案', '解析']];
    Object.keys(S.wrong).forEach(function (k) {
      var p = k.split('|'), kg = p[0], lid = p[1], qi = +p[2];
      if (onlyGrade && kg !== onlyGrade) return;
      var qs = DB.quiz[kg][lid]; if (!qs || !qs[qi]) return;
      var q = qs[qi];
      var lm = null, un = '';
      DB.units[kg].forEach(function (u) { u.lessons.forEach(function (l) { if (l.id === lid) { lm = l; un = u.title; } }); });
      var p2 = S.prog[kg + '|' + lid] || {};
      rows.push([
        kg === 'g7' ? '七年级' : '八年级', un, lm ? lm.title : lid, '第' + (qi + 1) + '题',
        TYPES[q.t].n, q.q,
        (q.o || []).map(function (o, i) { return 'ABCDEF'[i] + '. ' + String(o).replace(/^[A-F][.、．]\s*/, ''); }).join(' / '),
        q.t === 'q' ? strip(q.a) : rightText(q),
        q.t === 'q' ? '自评' : ansText(q, p2[qi]),
        strip(q.an)
      ]);
    });
    if (rows.length === 1) { toast('暂无错题可导出'); return; }
    var csv = '\ufeff' + rows.map(function (r) { return r.map(csvCell).join(','); }).join('\r\n');
    var d = new Date();
    var name = '信息科技错题_' + d.getFullYear() + pad2(d.getMonth() + 1) + pad2(d.getDate()) + '.csv';

    // Android 壳：WebView 不支持 a.download，交给原生桥写进「下载」目录
    if (window.AndroidText && typeof window.AndroidText.saveText === 'function') {
      try {
        var r = window.AndroidText.saveText(name, csv);
        if (r && r.charAt(0) === '!') toast(r.slice(1));
        return;
      } catch (e) { /* 落到浏览器方案 */ }
    }

    try {
      var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url; a.download = name;
      document.body.appendChild(a); a.click();
      setTimeout(function () { document.body.removeChild(a); URL.revokeObjectURL(url); }, 400);
      toast('已导出 ' + (rows.length - 1) + ' 道错题');
    } catch (e) { toast('导出失败，请用系统浏览器打开'); }
  }

  /* ================= 事件 ================= */
  document.addEventListener('click', function (e) {
    var t = e.target;

    // 年级切换
    var sg = t.closest ? t.closest('.seg button') : null;
    if (sg) { switchGrade(sg.getAttribute('data-g')); return; }

    // 主题
    if (t.closest && t.closest('#themeBtn')) {
      var dark = document.documentElement.getAttribute('data-theme') === 'dark';
      S.theme = dark ? 'light' : 'dark'; save(); applyTheme();
      var sw = $('#swTheme'); if (sw) sw.classList.toggle('on', !dark);
      return;
    }
    if (t.closest && t.closest('#swTheme')) {
      var d2 = document.documentElement.getAttribute('data-theme') === 'dark';
      S.theme = d2 ? 'light' : 'dark'; save(); applyTheme();
      t.closest('#swTheme').classList.toggle('on', !d2);
      return;
    }

    // 底部导航
    var tb = t.closest ? t.closest('.tabbar button') : null;
    if (tb) { go(tb.getAttribute('data-tab')); return; }

    // 通用跳转
    var gEl = t.closest ? t.closest('[data-go]') : null;
    if (gEl && !(t.closest && t.closest('[data-opt]'))) {
      var dest = gEl.getAttribute('data-go');
      // 错题项：跳到对应题号
      if (gEl.hasAttribute('data-wq')) {
        var parts = gEl.getAttribute('data-wq').split('|');
        S.last = { g: parts[0], lid: parts[1], i: +parts[2] };
        if (parts[0] !== S.g) { S.g = parts[0]; save(); applyTheme(); }
      }
      go(dest); return;
    }

    // ===== 答题页交互 =====
    if (V) {
      var opt = t.closest ? t.closest('[data-opt]') : null;
      if (opt && !opt.classList.contains('locked')) {
        var oi = +opt.getAttribute('data-opt');
        var q = V.qs[V.i], cur = V.ans[V.i];
        if (isMulti(q)) {
          var arr = V.pick[V.i] || (Array.isArray(cur) ? cur.slice() : []);
          var idx = arr.indexOf(oi);
          if (idx >= 0) arr.splice(idx, 1); else arr.push(oi);
          V.pick[V.i] = arr;
          paintQ();
        } else {
          V.open[V.i] = true;
          record(V.i, oi);
          afterAnswer();
        }
        return;
      }
      if (t.id === 'btnConfirm' || (t.closest && t.closest('#btnConfirm'))) {
        var pa = V.pick[V.i] || [];
        if (!pa.length) { toast('请先选择选项'); return; }
        V.open[V.i] = true;
        record(V.i, pa.slice());
        V.pick[V.i] = null;
        afterAnswer();
        return;
      }
      if (t.id === 'btnShowRef') {
        var ta = $('#qta');
        if (ta) { V.txt = V.txt || {}; V.txt[V.i] = ta.value; }
        V.open[V.i] = true;
        paintQ(); return;
      }
      var self = t.closest ? t.closest('[data-self]') : null;
      if (self) {
        record(V.i, self.getAttribute('data-self'));
        afterAnswer(); return;
      }
      if (t.id === 'btnPrev' || (t.closest && t.closest('#btnPrev'))) {
        if (V.i > 0) { V.i--; paintQ(); window.scrollTo(0, 0); }
        return;
      }
      if (t.id === 'btnNext' || (t.closest && t.closest('#btnNext'))) {
        if (V.i < V.qs.length - 1) { V.i++; paintQ(); window.scrollTo(0, 0); }
        else {
          var allDone = true;
          V.qs.forEach(function (qq, i) { if (grade(qq, V.ans[i]) === null) allDone = false; });
          if (!allDone) {
            for (var i = 0; i < V.qs.length; i++) if (grade(V.qs[i], V.ans[i]) === null) { V.i = i; paintQ(); toast('还有未作答的题'); return; }
          }
          if (!V.finished) { V.finished = true; pushHist(); showResult(); }
        }
        return;
      }
      if (t.closest && t.closest('#btnMemo2')) {
        if (!S.memo) S.memo = {};
        S.memo[V.lid] = V.i; save();
        go('memo/' + V.uid + '/' + V.lid); return;
      }
      if (t.closest && (t.closest('#btnSheet') || t.closest('#btnSheet2'))) { openSheet(); return; }
      var jump = t.closest ? t.closest('[data-jump]') : null;
      if (jump) { V.i = +jump.getAttribute('data-jump'); closeSheet(); paintQ(); window.scrollTo(0, 0); return; }
      if (t.id === 'sheetClose') { closeSheet(); return; }
    }

    // ===== 背题模式交互 =====
    if (VM) {
      var rv = t.closest ? t.closest('[data-reveal]') : null;
      if (rv) { VM.rev[VM.i] = true; paintMemo(); return; }
      if (t.closest && t.closest('#btnEye')) {
        VM.hide = !VM.hide; S.memoHide = VM.hide; save();
        if (!VM.hide) VM.rev[VM.i] = true;
        paintMemo(); return;
      }
      if (t.closest && t.closest('#mPrev')) { memoGo(VM.i - 1); return; }
      if (t.closest && t.closest('#mNext')) {
        if (VM.i >= VM.qs.length - 1) { go('quiz/' + VM.uid + '/' + VM.lid); return; }
        memoGo(VM.i + 1); return;
      }
    }

    // 结果弹窗
    if (t.id === 'rWrong') {
      $('#modal').classList.remove('on');
      for (var i2 = 0; i2 < V.qs.length; i2++) {
        if (grade(V.qs[i2], V.ans[i2]) === 0) { V.i = i2; break; }
      }
      paintQ(); window.scrollTo(0, 0); return;
    }
    if (t.id === 'rExport') { exportWrong(S.g); return; }
    if (t.id === 'rAgain') {
      $('#modal').classList.remove('on');
      var k = S.g + '|' + V.lid;
      delete S.prog[k];
      Object.keys(S.wrong).forEach(function (kk) { if (kk.indexOf(S.g + '|' + V.lid + '|') === 0) delete S.wrong[kk]; });
      save();
      var lid2 = V.lid, uid2 = V.uid;
      render(); return;
    }
    if (t.id === 'rBack') { $('#modal').classList.remove('on'); go('quiz/' + V.uid); return; }

    // 折叠：笔记模块
    var acc = t.closest ? t.closest('[data-acc]') : null;
    if (acc) { acc.closest('.acc').classList.toggle('open'); return; }
    var bacc = t.closest ? t.closest('[data-bacc]') : null;
    if (bacc) { bacc.closest('.acc').classList.toggle('open'); return; }

    // 教材切换
    var bk = t.closest ? t.closest('[data-book]') : null;
    if (bk) { bookSel = bk.getAttribute('data-book'); viewBookHome(); window.scrollTo(0, 0); return; }

    // 错题筛选
    var wf = t.closest ? t.closest('[data-wf]') : null;
    if (wf) { S.meFilter = wf.getAttribute('data-wf'); viewMe(); return; }

    // 导出全部
    if (t.id === 'btnExportAll') { exportWrong(null); return; }

    // 清空
    if (t.id === 'btnClear') {
      if (!confirm('确定清空 ' + DB.meta[S.g].name + ' 的全部答题进度和错题记录吗？')) return;
      Object.keys(S.prog).forEach(function (kk) { if (kk.indexOf(S.g + '|') === 0) delete S.prog[kk]; });
      Object.keys(S.wrong).forEach(function (kk) { if (kk.indexOf(S.g + '|') === 0) delete S.wrong[kk]; });
      S.hist = S.hist.filter(function (x) { return x.g !== S.g; });
      save(); viewMe(); toast('已清空'); return;
    }

    // 关闭抽屉/弹窗
    if (t.id === 'mask') { closeSheet(); return; }
    if (t.id === 'modal') { $('#modal').classList.remove('on'); return; }
  });

  // 搜索输入 / 简答输入
  document.addEventListener('input', function (e) {
    if (e.target.id === 'sIn') doSearch(e.target.value);
    if (e.target.id === 'qta' && V) { V.txt = V.txt || {}; V.txt[V.i] = e.target.value; }
  });

  // 滑动切题
  var sx = 0, sy = 0, st = 0, moved = false;
  document.addEventListener('touchstart', function (e) {
    if ((!V && !VM) || e.touches.length !== 1) return;
    if (e.target.closest('#sheet') || e.target.closest('.ta')) return;
    sx = e.touches[0].clientX; sy = e.touches[0].clientY; moved = false; st = Date.now();
  }, { passive: true });
  document.addEventListener('touchmove', function (e) {
    if ((!V && !VM) || e.touches.length !== 1) return;
    var dx = Math.abs(e.touches[0].clientX - sx), dy = Math.abs(e.touches[0].clientY - sy);
    if (dy > dx) moved = true;
  }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if ((!V && !VM) || moved || !e.changedTouches.length) return;
    var dx = e.changedTouches[0].clientX - sx;
    var dy = Math.abs(e.changedTouches[0].clientY - sy);
    if (Date.now() - st > 600) return;
    if (Math.abs(dx) < 60 || dy > 70) return;
    if (VM) {
      if (dx < 0 && VM.i < VM.qs.length - 1) memoGo(VM.i + 1);
      if (dx > 0 && VM.i > 0) memoGo(VM.i - 1);
      return;
    }
    if (dx < 0 && V.i < V.qs.length - 1) { V.i++; paintQ(); window.scrollTo(0, 0); }
    if (dx > 0 && V.i > 0) { V.i--; paintQ(); window.scrollTo(0, 0); }
  }, { passive: true });

  // hash 变化
  window.addEventListener('hashchange', render);

  // 返回键：先关浮层，再回上一层，都没有才退出（Android 壳会调用它）
  window.__handleBack = function () {
    var m = document.getElementById('modal');
    if (m && m.classList.contains('on')) { m.classList.remove('on'); return true; }
    var sh = document.getElementById('sheet');
    if (sh && sh.classList.contains('on')) { closeSheet(); return true; }
    var r = parseHash();
    var base = r.tab === 'memo' ? 'quiz' : r.tab;
    if (r.b) { location.hash = '#/' + base + '/' + r.a; return true; }
    if (r.a) { location.hash = '#/' + base; return true; }
    return false;
  };

  /* ================= 启动 ================= */
  var booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    var seg = $('#seg');
    seg.innerHTML = '<button data-g="g7">七年级</button><button data-g="g8">八年级</button>';
    var tabbar = $('#tabbar');
    tabbar.innerHTML =
      '<button data-tab="quiz"><span class="ico">' + ICO.quiz + '</span>刷题</button>' +
      '<button data-tab="note"><span class="ico">' + ICO.note + '</span>笔记</button>' +
      '<button data-tab="book"><span class="ico">' + ICO.book + '</span>教材</button>' +
      '<button data-tab="me"><span class="ico">' + ICO.me + '</span>我的</button>';
    applyTheme();
    render();
  }
  function syncSeg() {
    var btns = document.querySelectorAll('#seg button');
    for (var i = 0; i < btns.length; i++) btns[i].classList.toggle('on', btns[i].getAttribute('data-g') === S.g);
  }
  if (document.readyState !== 'loading') boot();
  else document.addEventListener('DOMContentLoaded', boot);
})();
