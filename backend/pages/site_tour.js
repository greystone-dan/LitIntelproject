/* iLit site tour: a step-by-step walk through the real site.
   Self-contained: no libraries, no network calls except the site's own search (to find the example decisions).
   The steps are plain data in site_tour_steps.json (injected below as window.ILIT_TOUR).
   State lives in sessionStorage, so the tour survives page changes and a refresh. */
(function(){
  'use strict';
  var DATA=window.ILIT_TOUR||{steps:[],cases:{}};
  var STEPS=DATA.steps||[],CASES=DATA.cases||{};
  var KEY='ilit.tour.v1';
  if(window.top!==window.self||!STEPS.length)return;           // never inside a frame (the Workbench embeds two tools)
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- state ---------- */
  function load(){try{return JSON.parse(sessionStorage.getItem(KEY)||'null')}catch(e){return null}}
  function save(s){try{sessionStorage.setItem(KEY,JSON.stringify(s))}catch(e){}}
  function clear(){try{sessionStorage.removeItem(KEY)}catch(e){}}
  var state=load();
  var run=0;                                                      // bumped whenever a step is (re)started; stale async work checks it
  var ui=null,watch=null;

  /* ---------- small helpers ---------- */
  function sleep(ms){return new Promise(function(r){setTimeout(r,ms)})}
  function visible(el){
    if(!el||!el.getClientRects)return false;
    var r=el.getBoundingClientRect(),cs=getComputedStyle(el);
    return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none';
  }
  function qs(sel){try{return document.querySelector(sel)}catch(e){return null}}
  function findVisible(sel){
    var list=Array.isArray(sel)?sel:[sel];
    for(var i=0;i<list.length;i++){
      var item=list[i],css=typeof item==='string'?item:item.css,re=item&&item.text?new RegExp(item.text,'i'):null,all;
      try{all=document.querySelectorAll(css)}catch(e){continue}
      for(var j=0;j<all.length;j++)if(visible(all[j])&&(!re||re.test(all[j].textContent||'')))return all[j];
    }
    return null;
  }
  async function waitFor(sel,seconds,token){
    var end=Date.now()+(seconds||8)*1000;
    for(;;){
      if(token!==run)return null;
      var el=findVisible(sel);
      if(el)return el;
      if(Date.now()>end)return null;
      await sleep(150);
    }
  }
  function el(tag,cls,text){var n=document.createElement(tag);if(cls)n.className=cls;if(text!=null)n.textContent=text;return n}

  /* ---------- finding the example decisions ---------- */
  var caseIds={};
  async function searchFirst(params){
    var q=new URLSearchParams();
    Object.keys(params).forEach(function(k){
      var v=String(params[k]).replace(/\{(\w+)\}/g,function(_,name){return caseIds[name]!=null?caseIds[name]:''});
      if(v)q.set(k,v);
    });
    q.set('limit','5');
    var r=await fetch('/analytics/search/cases?'+q.toString());
    if(!r.ok)throw new Error('search '+r.status);
    var data=await r.json();
    return (data.results||[])[0]||null;
  }
  function normCite(s){return String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim()}
  async function resolveCase(name){
    if(caseIds[name]!=null)return caseIds[name];
    var spec=CASES[name];
    if(!spec)return null;
    var id=null,lookedUp=false;
    try{
      if(spec.citation){
        var r=await fetch('/analytics/search/cases?'+new URLSearchParams({query:spec.citation,limit:'8'}).toString());
        if(r.ok){
          lookedUp=true;
          var rows=((await r.json()).results)||[],want=normCite(spec.citation);
          var hit=rows.filter(function(x){return normCite(x.citation).indexOf(want)>-1})[0];
          if(hit)id=hit.case_id;
        }
      }else if(spec.search){
        var refs=JSON.stringify(spec).match(/\{(\w+)\}/g)||[];
        for(var k=0;k<refs.length;k++)await resolveCase(refs[k].slice(1,-1));
        var first=await searchFirst(spec.search);
        if(!first&&spec.fallback)first=await searchFirst(spec.fallback);
        if(first)id=first.case_id;
        lookedUp=true;
      }
    }catch(e){}
    // The stored id is only a fallback for when the lookup itself is unavailable, never for a decision the library lacks.
    if(id==null&&!lookedUp&&spec.id!=null)id=spec.id;
    if(id!=null)caseIds[name]=id;
    return id;
  }
  async function resolveUrl(url){
    var names=[],m,re=/\{(\w+)\}/g;
    while((m=re.exec(url)))names.push(m[1]);
    for(var i=0;i<names.length;i++){
      var id=await resolveCase(names[i]);
      if(id==null)return null;
      url=url.replace('{'+names[i]+'}',id);
    }
    return url;
  }

  /* ---------- page matching and navigation ---------- */
  function sameLocation(url){
    var u=new URL(url,location.origin);
    if(u.pathname!==location.pathname)return false;
    var want=u.searchParams,have=new URLSearchParams(location.search);
    var ok=true;
    want.forEach(function(v,k){if(have.get(k)!==v)ok=false});
    // the explorer opens a case reader from case_id; a leftover tab/search must not count as the same page
    if(!want.has('case_id')&&have.has('case_id'))ok=false;
    if(u.hash&&u.hash!==location.hash)ok=false;
    if(!u.hash&&u.pathname==='/workbench'&&location.hash&&location.hash!=='#home')ok=false;
    return ok;
  }

  /* ---------- actions run once a step's page is ready ---------- */
  async function typeInto(input,text,token){
    input.focus();
    input.value='';
    input.dispatchEvent(new Event('input',{bubbles:true}));
    if(reduce){input.value=text;input.dispatchEvent(new Event('input',{bubbles:true}));return}
    for(var i=1;i<=text.length;i++){
      if(token!==run)return;
      input.value=text.slice(0,i);
      input.dispatchEvent(new Event('input',{bubbles:true}));
      await sleep(22);
    }
  }
  async function fillInto(input,text,token){
    input.focus();
    if(reduce){input.value=text;input.dispatchEvent(new Event('input',{bubbles:true}));return}
    input.value='';
    for(var i=0;i<text.length;i+=60){
      if(token!==run)return;
      input.value=text.slice(0,i+60);
      input.dispatchEvent(new Event('input',{bubbles:true}));
      await sleep(12);
    }
    input.scrollTop=0;
  }
  function pickNode(sel,a){
    var all=[];
    try{all=[].slice.call(document.querySelectorAll(sel))}catch(e){}
    all=all.filter(visible);
    if(a.match){var re=new RegExp(a.match,'i');all=all.filter(function(n){return re.test(n.textContent||'')})}
    return all[0]||null;
  }
  async function doAction(a,token){
    if(a.unless&&findVisible(a.unless))return true;
    if(a.when&&!findVisible(a.when))return true;
    if(a.do==='wait'){await sleep(a.ms||500);return true}
    if(a.do==='waitFor')return !!(await waitFor(a.selector,a.timeout||10,token));
    var node=null,end=Date.now()+(a.timeout||6)*1000;
    for(;;){
      if(token!==run)return false;
      node=pickNode(a.selector,a);
      if(node||Date.now()>end)break;
      await sleep(150);
    }
    if(!node)return false;
    switch(a.do){
      case 'type':await typeInto(node,a.text||'',token);break;
      case 'fill':await fillInto(node,(DATA.texts||{})[a.sample]||'',token);break;
      case 'check':if(!node.checked)node.click();break;
      case 'uncheck':if(node.checked)node.click();break;
      case 'click':node.click();break;
      case 'submit':if(node.requestSubmit)node.requestSubmit();else node.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));break;
      case 'scroll':node.scrollIntoView({block:'center'});break;
      default:return false;
    }
    await sleep(150);
    return true;
  }

  /* ---------- the overlay and the card ---------- */
  function build(){
    if(ui)return ui;
    var root=el('div','ilit-tour');root.setAttribute('data-ilit-tour','');
    var shades=['t','l','r','b'].map(function(n){var d=el('div','ilit-tour-shade '+n);root.appendChild(d);return d});
    var ring=el('div','ilit-tour-ring');root.appendChild(ring);
    var card=el('div','ilit-tour-card');
    card.setAttribute('role','dialog');card.setAttribute('aria-label','Site tour');card.setAttribute('tabindex','-1');
    var head=el('div','ilit-tour-head');
    var kicker=el('span','ilit-tour-kicker');
    var exitX=el('button','ilit-tour-x','×');exitX.type='button';exitX.setAttribute('aria-label','Exit the tour');
    head.appendChild(kicker);head.appendChild(exitX);
    var title=el('h2','ilit-tour-title');
    var text=el('p','ilit-tour-text');
    var note=el('p','ilit-tour-note');
    var extra=el('div','ilit-tour-extra');
    var bar=el('div','ilit-tour-bar');var fill=el('i');bar.appendChild(fill);
    var foot=el('div','ilit-tour-foot');
    var count=el('span','ilit-tour-count');
    var btns=el('div','ilit-tour-btns');
    var back=el('button','ilit-tour-btn','Back');back.type='button';
    var skip=el('button','ilit-tour-btn quiet','Skip section');skip.type='button';
    var next=el('button','ilit-tour-btn primary','Next');next.type='button';
    btns.appendChild(back);btns.appendChild(skip);btns.appendChild(next);
    foot.appendChild(count);foot.appendChild(btns);
    [head,title,text,note,extra,bar,foot].forEach(function(n){card.appendChild(n)});
    root.appendChild(card);
    var live=el('div','ilit-tour-live');live.setAttribute('aria-live','polite');root.appendChild(live);
    document.body.appendChild(root);
    exitX.onclick=exit;
    back.onclick=function(){go(-1)};
    next.onclick=function(){go(1)};
    skip.onclick=skipSection;
    ui={root:root,shades:shades,ring:ring,card:card,kicker:kicker,title:title,text:text,note:note,extra:extra,fill:fill,count:count,back:back,skip:skip,next:next,live:live,target:null};
    return ui;
  }
  function destroy(){
    if(watch){cancelAnimationFrame(watch);watch=null}
    if(ui&&ui.root.parentNode)ui.root.parentNode.removeChild(ui.root);
    document.documentElement.classList.remove('ilit-tour-on');
    ui=null;
  }

  function place(){
    if(!ui)return;
    var vw=window.innerWidth,vh=window.innerHeight,pad=6;
    if(ui.target&&!document.contains(ui.target)&&ui.sel)ui.target=findVisible(ui.sel);   // the page re-drew the element: find its replacement
    var t=ui.target&&document.contains(ui.target)&&visible(ui.target)?ui.target:null;
    var card=ui.card,narrow=vw<640;
    var r=null;
    if(t){
      var b=t.getBoundingClientRect();
      var x=Math.max(0,Math.floor(b.left-pad)),y=Math.max(0,Math.floor(b.top-pad));
      var x2=Math.min(vw,Math.ceil(b.right+pad)),y2=Math.min(vh,Math.ceil(b.bottom+pad));
      r={x:x,y:y,w:Math.max(0,x2-x),h:Math.max(0,y2-y)};            // whole pixels, so the four shades meet without a seam
    }
    var sh=ui.shades;
    if(r){
      set(sh[0],0,0,vw,r.y);                       // top
      set(sh[1],0,r.y,r.x,r.h);                    // left
      set(sh[2],r.x+r.w,r.y,Math.max(0,vw-r.x-r.w),r.h); // right
      set(sh[3],0,r.y+r.h,vw,Math.max(0,vh-r.y-r.h));    // bottom
      ui.ring.style.display='block';
      ui.ring.style.transform='translate('+r.x+'px,'+r.y+'px)';
      ui.ring.style.width=r.w+'px';ui.ring.style.height=r.h+'px';
    }else{
      set(sh[0],0,0,vw,vh);set(sh[1],0,0,0,0);set(sh[2],0,0,0,0);set(sh[3],0,0,0,0);
      ui.ring.style.display='none';
    }
    if(narrow){
      card.style.left='0';card.style.right='0';card.style.top='auto';card.style.bottom='0';card.classList.add('sheet');
      return;
    }
    // One fixed place on desktop, so Next is always under the same spot.
    card.classList.remove('sheet');
    card.style.left='auto';card.style.top='auto';card.style.right='20px';card.style.bottom='20px';
  }
  function set(n,x,y,w,h){n.style.transform='translate('+x+'px,'+y+'px)';n.style.width=w+'px';n.style.height=h+'px'}
  function follow(){
    var lastSig='';
    (function tick(){
      if(!ui)return;
      var t=ui.target,sig=t&&document.contains(t)?(function(){var b=t.getBoundingClientRect();return [b.left,b.top,b.width,b.height,window.innerWidth,window.innerHeight,ui.card.offsetHeight].join(',')})():'x'+window.innerWidth+ui.card.offsetHeight;
      if(ui.target&&!document.contains(ui.target))lastSig='';
      if(sig!==lastSig){lastSig=sig;place()}
      watch=requestAnimationFrame(tick);
    })();
  }

  /* ---------- showing a step ---------- */
  function sectionOf(i){return STEPS[i]&&STEPS[i].section}
  function stepsLeftInSection(i){var n=0;for(var k=i;k<STEPS.length&&sectionOf(k)===sectionOf(i);k++)n++;return n}
  function render(i,target,pending){
    var s=STEPS[i],u=build();
    document.documentElement.classList.add('ilit-tour-on');
    u.target=target;u.sel=s.target||null;
    u.kicker.textContent=s.section||'Tour';
    u.title.textContent=s.title||'';
    u.text.textContent=s.text||'';
    u.note.textContent='';u.note.hidden=true;
    u.extra.textContent='';
    u.count.textContent='Step '+(i+1)+' of '+STEPS.length;
    u.fill.style.width=Math.round(((i+1)/STEPS.length)*100)+'%';
    u.back.disabled=i===0;
    u.next.textContent=i===STEPS.length-1?'Done':'Next';
    u.skip.hidden=sectionOf(i)===sectionOf(STEPS.length-1)||!STEPS.slice(i+1).some(function(x){return x.section!==s.section});
    if(s.writes)u.extra.appendChild(el('span','ilit-tour-writes',s.writes));
    (s.buttons||[]).forEach(function(b){
      var btn=el('button','ilit-tour-btn action',b.label);btn.type='button';
      if(b.writes)u.extra.appendChild(el('span','ilit-tour-writes',b.writes));
      btn.onclick=function(){var node=qs(b.click);if(node)node.click();btn.disabled=true};   // never moves on by itself
      u.extra.appendChild(btn);
    });
    u.live.textContent=(s.title||'')+'. '+(s.text||'');
    if(pending){u.card.classList.add('pending')}else u.card.classList.remove('pending');
    place();
    if(!watch)follow();
    if(!pending&&!document.activeElement.closest?.('.ilit-tour-card')){try{u.next.focus({preventScroll:true})}catch(e){}}
  }
  function scrollTo(target){
    if(!target)return;
    var narrow=window.innerWidth<640;
    try{target.scrollIntoView({block:narrow?'start':'center',inline:'nearest',behavior:'auto'})}catch(e){target.scrollIntoView()}
    var b=target.getBoundingClientRect();
    if(narrow){                                                    // leave room for the card docked at the bottom
      var room=window.innerHeight*0.42;
      if(b.bottom>window.innerHeight-room){try{window.scrollBy(0,b.bottom-(window.innerHeight-room)+12)}catch(e){}}
      else window.scrollBy(0,-70);
      return;
    }
    // Desktop: the card sits bottom right; lift the target clear of it when they would overlap.
    var c=ui&&ui.card.getBoundingClientRect();
    if(c&&b.right>c.left-8&&b.left<c.right&&b.bottom>c.top-16){
      var need=b.bottom-(c.top-16),allowed=Math.max(0,b.top-84),by=Math.min(need,allowed);
      if(by>0){try{window.scrollBy(0,by)}catch(e){}}
    }
  }
  var direction=1;
  async function show(i,dir){
    var token=++run;
    direction=dir||direction;
    if(i<0)i=0;
    if(i>=STEPS.length){finish();return}
    var s=STEPS[i];
    state=state||{i:i};
    state.i=i;state.active=true;state.dir=direction;
    save(state);
    build();
    render(i,null,true);
    // 1. be on the right page
    var url=await resolveUrl(s.url);
    if(token!==run)return;
    if(url==null){return skipOver(i,token)}                         // the example decision is not in this library
    if(!sameLocation(url)){
      state.nav=(state.nav&&state.nav.i===i?state.nav:{i:i,n:0});
      state.nav.n++;
      if(state.nav.n>2){state.nav=null;return skipOver(i,token)}   // do not loop if the page will not open
      save(state);
      location.assign(url);
      return;
    }
    state.nav=null;
    if(s.fresh&&direction<0&&state.reloaded!==i){state.reloaded=i;save(state);location.reload();return}   // a page that changes as you use it starts clean when you step back to it
    if(state.reloaded!==i)state.reloaded=null;
    save(state);
    // 2. run the step's actions
    var ok=true;
    for(var k=0;k<(s.before||[]).length;k++){
      var done=await doAction(s.before[k],token);
      if(token!==run)return;
      if(!done&&s.before[k].do==='waitFor'){ok=false;break}
      if(!done&&s.before[k].do==='type'){ok=false;break}
    }
    // 3. find what to point at
    var target=null;
    if(ok){
      if(s.target)target=await waitFor(s.target,s.timeout||8,token);
      else target=null;
    }
    if(token!==run)return;
    if(s.target&&!target)return skipOver(i,token);                  // missing element or data: skip, never break
    render(i,target,false);
    if(target){scrollTo(target);await sleep(reduce?0:120)}
    if(s.hover&&target){hoverOn(target)}else hoverOff();
  }
  var hovered=null;
  function hoverOn(node){
    hoverOff();hovered=node;
    try{node.dispatchEvent(new MouseEvent('mouseover',{bubbles:true,cancelable:true,view:window}))}catch(e){}
  }
  function hoverOff(){
    if(!hovered)return;
    try{hovered.dispatchEvent(new MouseEvent('mouseout',{bubbles:true,cancelable:true,view:window}))}catch(e){}
    hovered=null;
  }
  function skipOver(i,token){
    if(token!==run)return;
    var n=i+direction;
    if(n<0){return show(0,1)}                                       // nothing earlier to go back to
    if(n>=STEPS.length)return finish();
    return show(n,direction);
  }
  function go(d){hoverOff();direction=d;show((state?state.i:0)+d,d)}
  function skipSection(){
    hoverOff();
    var i=state?state.i:0,sec=sectionOf(i),n=i;
    while(n<STEPS.length&&sectionOf(n)===sec)n++;
    direction=1;
    if(n>=STEPS.length)return finish();
    show(n,1);
  }
  function finish(){exit()}
  function exit(){
    run++;hoverOff();
    clear();state=null;destroy();
  }
  // The tour signs in to the Workbench demo (no password, a made-up name) so a pinned case can be shown.
  // It never replaces a session that is already signed in.
  async function demoSignIn(){
    try{
      var me=await (await fetch('/workbench/api/me',{credentials:'same-origin'})).json();
      if(me&&me.signed_in)return;
      await fetch('/workbench/api/signin',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:'Demo analyst'})});
    }catch(e){}
  }
  async function start(){
    state={i:0,active:true};save(state);
    build();render(0,null,true);
    await demoSignIn();
    var url=new URL(location.href);
    if(url.searchParams.has('tour')){url.searchParams.delete('tour');history.replaceState(null,'',url.pathname+url.search+url.hash)}
    show(0,1);
  }

  /* ---------- keyboard ---------- */
  document.addEventListener('keydown',function(e){
    if(!ui||e.defaultPrevented)return;
    var tag=(e.target&&e.target.tagName||'').toLowerCase();
    if(e.key==='Escape'){e.preventDefault();exit();return}
    if(tag==='input'||tag==='textarea'||tag==='select'||(e.target&&e.target.isContentEditable))return;
    if(e.key==='ArrowRight'){e.preventDefault();go(1)}
    else if(e.key==='ArrowLeft'){e.preventDefault();if(state&&state.i>0)go(-1)}
  });

  /* ---------- starting it ---------- */
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-ilit-tour-start]');
    if(!b)return;
    e.preventDefault();
    start();
  });
  window.ilitTour={start:start,exit:exit,steps:STEPS,resolveUrl:resolveUrl,resolveCase:resolveCase};

  function boot(){
    var wants=new URLSearchParams(location.search).get('tour')==='1';
    if(wants&&!(state&&state.active)){start();return}
    if(state&&state.active)show(Math.min(state.i||0,STEPS.length-1),state.dir||direction);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,50)});
  else setTimeout(boot,50);
})();
