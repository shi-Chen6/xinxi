const {JSDOM}=require('jsdom');
const fs=require('fs');
const ROOT='C:/Users/shi/Desktop/信息科技';
const NODE_PATH='C:/Users/shi/.workbuddy/binaries/node/workspace/node_modules';

function load(file){
  const h=fs.readFileSync(ROOT+'/'+file,'utf-8');
  const s0=h.indexOf('<script>'),s1=h.lastIndexOf('</script>');
  const js=h.substring(s0+8,s1);
  let b=0;for(let c of js){if(c==='{')b++;if(c==='}')b--;}
  return {h,js,braces:b};
}

function check(file, name){
  const {h,js,braces}=load(file);
  console.log(`\n=== ${name} ===`);
  console.log('  大小:',(h.length/1024|0)+'KB | JS括号:',braces,'(0=OK)');
  console.log('  @media手机适配:', h.includes('@media'));
  console.log('  链接到八年级笔记:', h.includes('八年级备考知识笔记.html'));
  console.log('  链接到八年级教材:', h.includes('八年级教材参考.html'));
  console.log('  链接到八年级刷题:', h.includes('八年级刷题练习.html'));
  return {h,js};
}

const notes=check('八年级备考知识笔记.html','备考知识笔记');
const quiz=check('八年级刷题练习.html','刷题练习');
const tb=check('八年级教材参考.html','教材参考');

// 笔记页 jsdom 渲染
(async()=>{
  const dom=new JSDOM(fs.readFileSync(ROOT+'/八年级备考知识笔记.html','utf-8'),{runScripts:'dangerously'});
  await new Promise(r=>setTimeout(r,400));
  const d=dom.window.document;
  console.log('\n[笔记页渲染] 模块Tab:',d.querySelectorAll('.tab-btn').length,'(应6) | 课程卡片:',d.querySelectorAll('.lesson-card').length,'(应30)');
  console.log('  每课含4板块:',d.querySelectorAll('.section-content').length,'(应120)');
  console.log('  刷题链接数:',d.querySelectorAll('.quiz-link').length,'(应30)');
  const ql=d.querySelector('.quiz-link');
  console.log('  示例刷题链接:',ql?ql.getAttribute('href'):'无');

  // 刷题页 jsdom 渲染 + 模拟答题
  const dom2=new JSDOM(fs.readFileSync(ROOT+'/八年级刷题练习.html','utf-8'),{runScripts:'dangerously'});
  await new Promise(r=>setTimeout(r,400));
  const d2=dom2.window.document, W2=dom2.window;
  const tabs=d2.querySelectorAll('.tab-nav button, .tab-btn');
  console.log('\n[刷题页渲染] 模块Tab:',tabs.length,'(应6)');
  W2.pickLesson(0);
  const cards=d2.querySelectorAll('.quiz-card');
  console.log('  选课后题卡数:',cards.length,'(应1,单题模式)');
  console.log('  课程映射数:',W2._lessonMap?Object.keys(W2._lessonMap).length:0,'(应30)');
  const total=W2._questions.length;
  console.log('  总题数:',total,'(应600)');
  // 模拟答前5题
  let ok=true;
  for(let i=0;i<5;i++){
    const q=W2._questions[i];
    try{ if(q.type==='short') W2.onShortAnswer(i); else if(q.type==='multi') (Array.isArray(q.answer)?q.answer:[q.answer]).forEach(x=>W2.selectOption(i,x)); else W2.selectOption(i,q.answer); }
    catch(e){ ok=false; console.log('  答题崩溃 Q'+(i+1)+':',e.message); break; }
  }
  console.log('  前5题作答无崩溃:',ok);
  // 跳转到L27验证字母答案已归一化(此数据已全数字)
  console.log('  全部答案为数字(无字母):', W2._questions.every(q=> q.type==='short' ? typeof q.answer==='string' : (q.type==='multi'? Array.isArray(q.answer): typeof q.answer==='number')));

  // 教材参考页 jsdom 渲染
  const dom3=new JSDOM(fs.readFileSync(ROOT+'/八年级教材参考.html','utf-8'),{runScripts:'dangerously'});
  await new Promise(r=>setTimeout(r,400));
  const d3=dom3.window.document;
  console.log('\n[教材参考渲染] 单元Tab:',d3.querySelectorAll('#unit-nav .tab-btn').length,'(应6)');
  console.log('  课程纲要卡片:',d3.getElementById('outline')?1:0);
  console.log('  单元内容课程块:',d3.querySelectorAll('.lesson-block').length,'(第一单元应5)');
  console.log('  教材页刷题链接:',d3.querySelectorAll('.quiz-link').length,'(应5,首单元)');
  // 搜索测试
  dom3.window.searchText('传感器');
  console.log('  搜索"传感器"匹配数:',d3.querySelectorAll('mark').length);
})();
