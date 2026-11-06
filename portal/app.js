/* Offline, dependency-free navigation. The hash is the complete navigational state. */
(() => {
  'use strict';
  const D = window.KFIELD_DATA, main = document.querySelector('main');
  let disposeView = () => {};
  const e = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const pad = n => String(n).padStart(2,'0');
  const doc = p => 'portal/read/'+p.replace(/\.md$/,'.html');
  const cdoc = (c,n) => doc(c.folder+'/'+n+'.md');
  const course = n => D.courses.find(c => c.number===Number(n));
  const required = c => c.prerequisites.length ? c.prerequisites.map(p => `<a href="#course/${Number(String(p).replace('course-',''))}">${pad(Number(String(p).replace('course-','')))}</a>`).join(' · ') : 'Entry algebra';
  function card(c,heading='h2') { return `<article class="course-card"><div class="card-top"><span class="course-number">${pad(c.number)}</span><span>${c.lessons.length} lessons</span></div><${heading}><a href="#course/${c.number}">${e(c.title)}</a></${heading}><div class="card-bottom"><span>Prerequisites: ${required(c)}</span><a class="arrow" href="#course/${c.number}" aria-label="Explore course ${pad(c.number)}">↗</a></div></article>`; }
  const route = () => { const [path,query=''] = location.hash.slice(1).split('?'); return {path:path||'home',params:new URLSearchParams(query)}; };
  function links(c) { return `<div class="resource-grid">${[['teacher-guide','Teacher guide','Entry skills, pacing and instruction'],['capstone','Capstone & rubric','Assessment task and worked answers'],['terminology','Glossary','Definitions and local conventions'],['sources','Source notes','Attribution and evidence scope'],['course-map','Course map','The lesson sequence and dependencies'],['course','Complete course','All lessons in one reading view']].map(([f,t,d])=>`<a class="resource" href="${cdoc(c,f)}"><span>${t} ↗</span><small>${d}</small></a>`).join('')}</div>`; }
  function catalogue(home,params) {
    main.innerHTML = (home ? `<section class="hero"><div><p class="eyebrow">KRYTRONX · SENIOR CURRICULUM</p><h1>A connected path<br>through the <em>K-Field.</em></h1><p class="hero-copy">From first principles to integrated research. Explore the mathematics, geometry and experimental reasoning of the K-Field, one carefully sequenced lesson at a time.</p><div class="actions"><a class="button" href="#course/1">Begin with course 01 <span>→</span></a><a class="text-link" href="#pathways">Find your pathway ↗</a></div><div class="hero-stats"><span><strong>30</strong> courses</span><span><strong>205</strong> lessons</span><span><strong>7</strong> pathways</span></div></div><div class="hero-art"><img src="portal/brand-logo.png" alt="K-Field — Krytronx"><span>GEOMETRY · INFORMATION · RESEARCH</span></div></section>` : '') + `<section class="section catalog"><div class="section-heading"><div><p class="eyebrow">THE CURRICULUM</p><h${home?'2':'1'}>Explore the courses</h${home?'2':'1'}><p>Follow the full sequence or choose a pathway with its prerequisites.</p></div><a class="text-link" href="portal/read/START-HERE.html">How to use this curriculum ↗</a></div><form id="filters" class="filters" role="search"><div class="search-field"><label for="search">Search courses and reading material</label><input id="search" name="q" type="search" placeholder="Try vectors, chirality, or residual…" value="${e(params.get('q')||'')}" autocomplete="off"></div><div><label for="pathway">Pathway</label><select id="pathway" name="pathway"><option value="">All courses</option>${D.pathways.map((p,i)=>`<option value="${i}" ${params.get('pathway')===String(i)?'selected':''}>${e(p.title)}</option>`).join('')}</select></div><button class="button" type="submit">Search</button><button class="reset" id="clear" type="button">Clear</button></form><p id="result-count" class="result-count" role="status" aria-live="polite"></p><div id="results"></div></section>`;
    const form=document.querySelector('#filters');
    function results() {
      const q=form.q.value.trim().toLocaleLowerCase(), p=form.pathway.value;
      const allowed=p==='' ? D.courses.map(c=>c.number) : D.pathways[Number(p)].required_sequence;
      const tokens=q.split(/\s+/).filter(Boolean), matches=t=>tokens.every(x=>t.toLocaleLowerCase().includes(x));
      const cs=D.courses.filter(c=>allowed.includes(c.number)&&matches(`${pad(c.number)} ${c.title} ${c.capstone}`));
      const docs=q ? D.documents.filter(d=>allowed.includes(d.course)&&matches(d.title+' '+d.text)) : [];
      document.querySelector('#result-count').textContent=q ? `${cs.length} course${cs.length===1?'':'s'} · ${docs.length} matching reading document${docs.length===1?'':'s'}` : `${cs.length} course${cs.length===1?'':'s'}${p!==''?' · '+D.pathways[Number(p)].title:''}`;
      const snippet=d=>{const i=d.text.toLocaleLowerCase().indexOf(tokens[0]); const start=Math.max(0,i-60); return (start?'…':'')+d.text.slice(start,start+230)+'…';};
      document.querySelector('#results').innerHTML=(cs.length?`<div class="course-grid">${cs.map(c=>card(c,home?'h3':'h2')).join('')}</div>`:'')+(docs.length?`<div class="search-readings"><h2>Matching reading material</h2><div class="document-results">${docs.map(d=>`<article><p class="eyebrow">COURSE ${pad(d.course)} · ${e(d.kind)}</p><h3><a href="${d.url}">${e(d.title)}</a></h3><p>${e(snippet(d))}</p></article>`).join('')}</div></div>`:'')+(!cs.length&&!docs.length?'<div class="empty"><h2>No matches found</h2><p>Try a shorter term, a course number, or choose All courses.</p></div>':'');
    }
    let timer;
    disposeView=()=>clearTimeout(timer);
    function sync(replace) { const ps=new URLSearchParams(); if(form.q.value.trim())ps.set('q',form.q.value.trim()); if(form.pathway.value!=='')ps.set('pathway',form.pathway.value); const hash='#'+(replace&&home?'home':'catalog')+(ps.size?'?'+ps:''); if(replace){history.replaceState(null,'',hash);results();}else if(location.hash===hash)results();else location.hash=hash; }
    form.addEventListener('submit',ev=>{ev.preventDefault();clearTimeout(timer);sync(false);});
    form.q.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>sync(true),160);});
    form.pathway.addEventListener('change',()=>sync(true));
    document.querySelector('#clear').addEventListener('click',()=>{form.q.value='';form.pathway.value='';sync(true);form.q.focus();});
    results();
  }
  function render(focus=false) {
    disposeView(); disposeView=()=>{};
    const {path,params}=route();
    if(path==='home'||path==='catalog') catalogue(path==='home',params);
    else if(path==='pathways') main.innerHTML=`<section class="section"><div class="page-intro"><p class="eyebrow">SEVEN WAYS INTO THE CURRICULUM</p><h1>Choose a teaching pathway.</h1><p>Each sequence includes every required earlier course. Select a focus, then move through the courses in the listed order.</p><a class="text-link" href="portal/read/TEACHING-PATHWAYS.html">Read teaching and assessment guidance ↗</a></div><div class="pathway-grid">${D.pathways.map((p,i)=>`<article class="pathway-card"><div class="card-top"><span class="course-number">${pad(i+1)}</span><span>${p.required_sequence.length} courses</span></div><h2>${e(p.title)}</h2><p>${e(p.purpose)}</p><nav class="sequence" aria-label="${e(p.title)} course sequence">${p.required_sequence.map(n=>`<a href="#course/${n}" title="${e(course(n).title)}">${pad(n)}</a>`).join('<span aria-hidden="true">→</span>')}</nav><a class="text-link" href="#catalog?pathway=${i}">Explore this pathway →</a></article>`).join('')}</div></section>`;
    else if(path==='teachers') main.innerHTML=`<section class="section"><div class="page-intro"><p class="eyebrow">FOR EDUCATORS</p><h1>Prepare. Teach. Connect.</h1><p>Find entry skills, pacing, worked answers, capstones and rubrics for every course. The complete sequence spans multiple terms; a lesson may take several class periods.</p><div class="actions"><a class="button" href="portal/read/TEACHING-PATHWAYS.html">Teaching & assessment guide →</a><a class="text-link" href="#pathways">Plan a pathway ↗</a></div></div><div class="teacher-list">${D.courses.map(c=>`<article><div><span class="eyebrow">COURSE ${pad(c.number)}</span><h2><a href="#course/${c.number}">${e(c.title)}</a></h2></div><div class="teacher-links"><a href="${cdoc(c,'teacher-guide')}">Teacher guide ↗</a><a href="${cdoc(c,'capstone')}">Capstone & rubric ↗</a><a href="${cdoc(c,'sources')}">Source notes ↗</a></div></article>`).join('')}</div></section>`;
    else if(/^course\/[1-9]\d*$/.test(path)&&course(path.split('/')[1])) {
      const c=course(path.split('/')[1]);
      main.innerHTML=`<section class="section"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="#catalog">All courses</a><span>/</span><span>Course ${pad(c.number)}</span></nav><div class="course-intro"><div><p class="eyebrow">COURSE ${pad(c.number)} · ${c.lessons.length} LESSONS</p><h1>${e(c.title)}</h1><div class="actions"><a class="button" href="${doc(c.lessons[0].path)}">Start the first lesson →</a><a class="text-link" href="${cdoc(c,'course')}">Read the complete course ↗</a></div></div><aside class="prerequisite-box"><h2>Before you begin</h2><p>Required earlier courses</p><div class="prerequisite-links">${required(c)}</div><a href="${cdoc(c,'teacher-guide')}">Check entry skills ↗</a></aside></div><div class="course-content"><div><h2>The lesson sequence</h2><ol class="lesson-list">${c.lessons.map((l,i)=>`<li><span>${pad(i+1)}</span><a href="${doc(l.path)}">${e(l.title.replace(/^Lesson[\s-]+\d+\s*[—–:-]\s*/i,''))}<b aria-hidden="true">↗</b></a></li>`).join('')}</ol><div class="capstone-callout"><p class="eyebrow">BRING IT TOGETHER</p><h2>Course capstone</h2><p>${e(c.capstone)}</p><a class="text-link" href="${cdoc(c,'capstone')}">Open task, worked answers & rubric →</a></div></div><aside><h2>Course resources</h2>${links(c)}</aside></div><nav class="course-sequence" aria-label="Course sequence">${c.number>1?`<a href="#course/${c.number-1}">← Course ${pad(c.number-1)}</a>`:'<span></span>'}${c.number<30?`<a href="#course/${c.number+1}">Course ${pad(c.number+1)} →</a>`:'<a href="#catalog">All courses →</a>'}</nav></section>`;
    } else main.innerHTML='<section class="section empty"><h1>Page not found</h1><p>This course or view does not exist.</p><a class="button" href="#catalog">Explore the courses</a></section>';
    const title=path==='home'?'K-Field Learning':main.querySelector('h1')?.textContent||'K-Field Learning'; document.title=title+' · Krytronx';
    document.querySelectorAll('.site-header nav a').forEach(a=>{const active=(path.startsWith('course')||path==='catalog')&&a.hash==='#catalog'||a.hash==='#'+path;a.toggleAttribute('aria-current',active);if(active)a.setAttribute('aria-current','page');});
    if(focus){window.scrollTo(0,0);main.focus({preventScroll:true});}
  }
  // Hashes are routes in the catalogue; skip navigation must move focus without replacing one.
  document.querySelector('.skip').addEventListener('click',event=>{
    event.preventDefault();
    main.focus({preventScroll:true});
    main.scrollIntoView({block:'start'});
  });
  window.addEventListener('hashchange',()=>render(true)); render();
})();
