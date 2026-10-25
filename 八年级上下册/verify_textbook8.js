const fs = require('fs');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync('C:/Users/shi/Desktop/信息科技/八年级教材参考.html', 'utf-8');
const errors = [];
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  beforeParse(window) {
    window.scrollTo = () => {};
    window.HTMLElement.prototype.scrollIntoView = function(){};
  }
});
const { window } = dom;
window.addEventListener('error', e => errors.push('window error: ' + e.message));

// Wait for DOMContentLoaded handlers
setTimeout(() => {
  const doc = window.document;
  const nav = doc.getElementById('side-nav');
  const navItems = nav ? nav.querySelectorAll('.nav-item') : [];
  console.log('NAV items:', navItems.length, navItems.length === 7 ? 'OK' : 'FAIL');
  const active0 = doc.querySelector('.nav-item.active');
  console.log('Default active label:', active0 ? active0.textContent : '(none)', active0 && active0.dataset.idx === '-1' ? 'OK' : 'FAIL');
  const panel0 = doc.getElementById('panel');
  console.log('Default panel has outline-card:', panel0.querySelector('.outline-card') ? 'OK' : 'FAIL');

  // Switch to unit 0
  const fn = window.switchPanel;
  fn(0);
  const panel1 = doc.getElementById('panel');
  const unitCard = panel1.querySelector('.unit-card');
  console.log('Unit panel rendered:', unitCard ? 'OK' : 'FAIL');
  const lessons = panel1.querySelectorAll('.lesson');
  console.log('Unit 0 lessons:', lessons.length, lessons.length === 5 ? 'OK' : 'FAIL');
  const banner = panel1.querySelector('.unit-banner h2');
  console.log('Unit banner title:', banner ? banner.textContent : '(none)');
  const quizLinks = panel1.querySelectorAll('.quiz-link');
  console.log('Quiz links in unit 0:', quizLinks.length, quizLinks.length === 5 ? 'OK' : 'FAIL');

  // Switch to unit 5 (security)
  fn(5);
  const panel5 = doc.getElementById('panel');
  const secLessons = panel5.querySelectorAll('.lesson');
  console.log('Unit 5 lessons:', secLessons.length, secLessons.length === 5 ? 'OK' : 'FAIL');
  const secTitle = panel5.querySelector('.unit-banner h2');
  console.log('Unit 5 title:', secTitle ? secTitle.textContent : '(none)');

  // Search test
  fn(-1); // back to outline for search breadth
  window.searchText('传感器');
  const marks = doc.querySelectorAll('#main mark');
  console.log('Search "传感器" marks:', marks.length, marks.length > 0 ? 'OK' : 'FAIL');
  const cntText = doc.getElementById('search-count').textContent;
  console.log('Search count text:', cntText);
  // jumpMark
  window.jumpMark(1);
  const cntAfter = doc.getElementById('search-count').textContent;
  console.log('After jumpMark(1):', cntAfter);

  console.log('JS errors:', errors.length ? errors.join('; ') : 'none');
  console.log('=== VERIFY DONE ===');
}, 500);
