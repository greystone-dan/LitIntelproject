/* iLit site tour: a scripted walk through the real site. The visitor only presses Next (or Back, Skip section, Exit);
   the tour opens the pages, types and clicks for them, and the page underneath does not take clicks while it runs.
   Self-contained: no libraries, no network calls except the site's own search (to find the example decisions).
   The steps are plain data in site_tour_steps.json (injected below as window.ILIT_TOUR).
   State lives in sessionStorage, so the tour survives page changes and a refresh. */
(function(){
  'use strict';
  var DATA=window.ILIT_TOUR||{steps:[],cases:{}};
  var STEPS=DATA.steps||[],CASES=DATA.cases||{};
  var KEY=DATA.key||'ilit.tour.v1',CASE_KEY='ilit.tour.cases';
  if(window.top!==window.self||!STEPS.length)return;           // never inside a frame (the Workbench embeds two tools)
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SVGNS='http://www.w3.org/2000/svg';

  /* ---------- state ---------- */
  function load(k){try{return JSON.parse(sessionStorage.getItem(k||KEY)||'null')}catch(e){return null}}
  function save(s){try{sessionStorage.setItem(KEY,JSON.stringify(s))}catch(e){}}
  function clear(){try{sessionStorage.removeItem(KEY);sessionStorage.removeItem(CASE_KEY)}catch(e){}}
  var state=load();
  var run=0;                                                      // bumped whenever a step is (re)started; stale async work checks it
  var ui=null,watch=null;
  window.__ilitTourTimes=window.__ilitTourTimes||{};

  /* ---------- small helpers ---------- */
  function sleep(ms){return new Promise(function(r){setTimeout(r,ms)})}
  function visible(el){
    if(!el||!el.getClientRects)return false;
    var r=el.getBoundingClientRect(),cs=getComputedStyle(el);
    return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none';
  }
  function qs(sel){try{return document.querySelector(sel)}catch(e){return null}}
  function fillIds(sel){
    if(typeof sel==='string')return sel.replace(/\{(\w+)\}/g,function(_,n){return caseIds[n]!=null?caseIds[n]:'0'});
    if(Array.isArray(sel))return sel.map(fillIds);
    if(sel&&sel.css)return {css:fillIds(sel.css),text:sel.text};
    return sel;
  }
  function findVisible(sel){
    var list=Array.isArray(sel)?sel:[sel];
    for(var i=0;i<list.length;i++){
      var item=fillIds(list[i]),css=typeof item==='string'?item:item&&item.css,re=item&&item.text?new RegExp(item.text,'i'):null,all;
      if(!css)continue;
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
      await sleep(100);
    }
  }
  function el(tag,cls,text){var n=document.createElement(tag);if(cls)n.className=cls;if(text!=null)n.textContent=text;return n}

  /* ---------- finding the example decisions (looked up once per tour, then kept) ---------- */
  var caseIds=load(CASE_KEY)||{};
  function keepIds(){try{sessionStorage.setItem(CASE_KEY,JSON.stringify(caseIds))}catch(e){}}
  function normCite(s){return String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim()}
  var pendingLookups={};
  function resolveCase(name){
    if(caseIds[name]!=null)return Promise.resolve(caseIds[name]);
    if(!pendingLookups[name])pendingLookups[name]=lookup(name);
    return pendingLookups[name];
  }
  async function lookup(name){
    var spec=CASES[name];
    if(!spec)return null;
    var id=null,lookedUp=false;
    try{
      var r=await fetch('/analytics/search/cases?'+new URLSearchParams({query:spec.citation,limit:'8'}).toString());
      if(r.ok){
        lookedUp=true;
        var rows=((await r.json()).results)||[],want=normCite(spec.citation);
        var hit=rows.filter(function(x){return normCite(x.citation).indexOf(want)>-1})[0];
        if(hit)id=hit.case_id;
      }
    }catch(e){}
    // The stored id is only a fallback for when the lookup itself is unavailable, never for a decision the library lacks.
    if(id==null&&!lookedUp&&spec.id!=null)id=spec.id;
    if(id!=null){caseIds[name]=id;keepIds()}
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

  /* ---------- page matching ---------- */
  function sameLocation(url){
    var u=new URL(url,location.origin);
    if(u.pathname!==location.pathname)return false;
    var want=u.searchParams,have=new URLSearchParams(location.search);
    var ok=true;
    want.forEach(function(v,k){if(have.get(k)!==v)ok=false});
    // the explorer opens a case reader from case_id; a leftover case must not count as the search or statistics page
    if(!want.has('case_id')&&have.has('case_id'))ok=false;
    if(u.hash&&u.hash!==location.hash)ok=false;
    if(!u.hash&&u.pathname==='/workbench'&&location.hash&&location.hash!=='#home')ok=false;
    return ok;
  }

  /* ---------- actions the tour performs for the visitor (each one is safe to repeat) ---------- */
  async function typeInto(input,text,token){
    if(input.value===text)return;                                  // already typed (a refresh or Back): do not type it again
    input.focus({preventScroll:true});
    input.value='';
    input.dispatchEvent(new Event('input',{bubbles:true}));
    if(reduce){input.value=text;input.dispatchEvent(new Event('input',{bubbles:true}));return}
    for(var i=1;i<=text.length;i++){
      if(token!==run)return;
      input.value=text.slice(0,i);
      input.dispatchEvent(new Event('input',{bubbles:true}));
      await sleep(28);
    }
    closeSuggestions();
  }
  function closeSuggestions(){var s=qs('#searchSuggestions');if(s)s.hidden=true;var q=qs('#searchQuery');if(q)q.setAttribute('aria-expanded','false')}
  async function fillInto(input,text,token){
    if(input.value===text)return;
    input.focus({preventScroll:true});
    input.value=text;
    input.dispatchEvent(new Event('input',{bubbles:true}));
    input.scrollTop=0;
  }
  function pickNode(sel,a){
    var all=[];
    try{all=[].slice.call(document.querySelectorAll(fillIds(sel)))}catch(e){}
    all=all.filter(visible);
    if(a.match){var re=new RegExp(a.match,'i');all=all.filter(function(n){return re.test(n.textContent||'')})}
    return all[0]||null;
  }
  async function doAction(a,token){
    if(a.unless&&findVisible(a.unless))return true;
    if(a.when&&!findVisible(a.when))return true;
    if(a.do==='wait'){await sleep(reduce?0:(a.ms||300));return true}
    if(a.do==='waitFor')return !!(await waitFor(a.selector,a.timeout||10,token));
    var node=null,end=Date.now()+(a.timeout||5)*1000;
    for(;;){
      if(token!==run)return false;
      node=pickNode(a.selector,a);
      if(node||Date.now()>end)break;
      await sleep(100);
    }
    if(!node)return false;
    if((a.do==='type'||a.show)&&ui&&!(a.do==='type'&&node.value===a.text)){   // let the visitor watch what the tour types or presses
      ui.items=[{node:node,sel:null,label:a.label||''}];fitView(ui.items);place();
      if(a.do!=='type')await sleep(reduce?0:450);
    }
    switch(a.do){
      case 'type':await typeInto(node,a.text||'',token);break;
      case 'fill':await fillInto(node,(DATA.texts||{})[a.sample]||'',token);break;
      case 'check':if(!node.checked)node.click();break;
      case 'uncheck':if(node.checked)node.click();break;
      case 'open':if(!node.open)node.open=true;break;
      case 'click':node.click();break;
      case 'submit':if(node.requestSubmit)node.requestSubmit();else node.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));break;
      case 'scroll':node.scrollIntoView({block:'center'});break;
      default:return false;
    }
    await sleep(60);
    return true;
  }

  /* ---------- the overlay: a dimmed page with one or more lit windows, a ring on each, and the card ---------- */
  function build(){
    if(ui)return ui;
    var root=el('div','ilit-tour');root.setAttribute('data-ilit-tour','');
    var block=el('div','ilit-tour-block');root.appendChild(block);    // the page under the tour takes no clicks
    var svg=document.createElementNS(SVGNS,'svg');svg.setAttribute('class','ilit-tour-dim');svg.setAttribute('aria-hidden','true');
    var path=document.createElementNS(SVGNS,'path');path.setAttribute('fill-rule','evenodd');svg.appendChild(path);root.appendChild(svg);
    var rings=el('div','ilit-tour-rings');root.appendChild(rings);
    var card=el('div','ilit-tour-card');
    card.setAttribute('role','dialog');card.setAttribute('aria-label','Site tour');card.setAttribute('tabindex','-1');
    var head=el('div','ilit-tour-head');
    var kicker=el('span','ilit-tour-kicker');
    var exitX=el('button','ilit-tour-x','×');exitX.type='button';exitX.setAttribute('aria-label','Exit the tour');
    head.appendChild(kicker);head.appendChild(exitX);
    var title=el('h2','ilit-tour-title');
    var text=el('p','ilit-tour-text');
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
    [head,title,text,extra,bar,foot].forEach(function(n){card.appendChild(n)});
    root.appendChild(card);
    var live=el('div','ilit-tour-live');live.setAttribute('aria-live','polite');root.appendChild(live);
    document.body.appendChild(root);
    exitX.onclick=exit;
    back.onclick=function(){go(-1)};
    next.onclick=function(){go(1)};
    skip.onclick=skipSection;
    ui={root:root,path:path,rings:rings,card:card,kicker:kicker,title:title,text:text,extra:extra,fill:fill,count:count,back:back,skip:skip,next:next,live:live,items:[]};
    return ui;
  }
  function destroy(){
    if(watch){cancelAnimationFrame(watch);watch=null}
    if(ui&&ui.root.parentNode)ui.root.parentNode.removeChild(ui.root);
    document.documentElement.classList.remove('ilit-tour-on');
    ui=null;
  }
  // What a step lights up: its target, plus any "also" regions, each with an optional label.
  function itemsFor(s,target){
    var out=[];
    if(target)out.push({node:target,sel:s.target,label:s.label||''});
    (s.also||[]).forEach(function(a){                               // a selector, or {sel: selector, label: "..."}
      var sel=a&&a.sel?a.sel:a;
      out.push({node:findVisible(sel),sel:sel,label:(a&&a.label)||''});
    });
    return out;
  }
  function liveRect(item){
    if(item.node&&!document.contains(item.node))item.node=null;
    if(!item.node&&item.sel)item.node=findVisible(item.sel);     // the page re-drew the element: find its replacement
    return item.node&&visible(item.node)?clipped(item.node):null;
  }
  // The part of an element that can actually be seen: cut by any scrolling panel it sits in.
  function clipped(n){
    var b=n.getBoundingClientRect(),r={left:b.left,top:b.top,right:b.right,bottom:b.bottom,height:b.height,width:b.width};
    for(var p=n.parentElement;p&&p!==document.body&&p!==document.documentElement;p=p.parentElement){
      var cs=getComputedStyle(p);
      if(cs.position==='fixed')break;
      if(cs.overflowY!=='visible'||cs.overflowX!=='visible'){
        var c=p.getBoundingClientRect();
        if(cs.overflowY!=='visible'){r.top=Math.max(r.top,c.top);r.bottom=Math.min(r.bottom,c.bottom)}
        if(cs.overflowX!=='visible'){r.left=Math.max(r.left,c.left);r.right=Math.min(r.right,c.right)}
      }
    }
    if(r.bottom-r.top<2||r.right-r.left<2)return null;
    return r;
  }
  function round(n){return Math.round(n*10)/10}
  function place(){
    if(!ui)return;
    var vw=document.documentElement.clientWidth||window.innerWidth,vh=window.innerHeight,pad=6;
    var narrow=window.innerWidth<640,card=ui.card;
    var floor=narrow&&!card.classList.contains('pending')?vh-card.offsetHeight:vh;   // on a phone nothing is lit behind the sheet
    var holes=[];
    ui.items.forEach(function(item){
      var b=liveRect(item);
      if(!b){holes.push(null);return}
      var x=Math.max(3,b.left-pad),y=Math.max(3,b.top-pad),x2=Math.min(vw-3,b.right+pad),y2=Math.min(floor-3,b.bottom+pad);
      var minH=Math.min(48,b.height),minW=Math.min(24,b.width);   // a sliver at the edge of the screen is not worth a ring
      holes.push(x2-x>=minW&&y2-y>=minH&&x2>x&&y2>y?{x:round(x),y:round(y),w:round(x2-x),h:round(y2-y),label:item.label}:null);
    });
    // one dark sheet with a window cut for each lit region (even-odd fill)
    var d='M0 0H'+vw+'V'+vh+'H0Z';
    holes.forEach(function(h){if(h)d+='M'+h.x+' '+h.y+'h'+h.w+'v'+h.h+'h'+(-h.w)+'Z'});
    ui.path.setAttribute('d',d);
    var rings=ui.rings;
    while(rings.children.length<holes.length){var r=el('div','ilit-tour-ring');r.appendChild(el('span','ilit-tour-tag'));rings.appendChild(r)}
    [].forEach.call(rings.children,function(r,k){
      var h=holes[k];
      if(!h){r.style.display='none';return}
      r.style.display='block';
      r.style.transform='translate('+h.x+'px,'+h.y+'px)';r.style.width=h.w+'px';r.style.height=h.h+'px';
      var tag=r.firstChild;tag.textContent=h.label||'';tag.hidden=!h.label;
      r.classList.toggle('tag-below',h.y<26);
    });
    if(narrow){card.classList.add('sheet');card.style.cssText='left:0;right:0;top:auto;bottom:0'}
    else{card.classList.remove('sheet');card.style.cssText='left:auto;top:auto;right:20px;bottom:20px'}   // one fixed place, so Next never moves
  }
  function follow(){
    var lastSig='';
    (function tick(){
      if(!ui)return;
      var sig=[window.innerWidth,window.innerHeight,ui.card.offsetHeight].concat(ui.items.map(function(item){
        var b=item.node&&document.contains(item.node)?item.node.getBoundingClientRect():null;
        return b?[b.left,b.top,b.width,b.height].join(','):'-';
      })).join('|');
      if(sig!==lastSig){lastSig=sig;place()}
      watch=requestAnimationFrame(tick);
    })();
  }
  // Bring every lit region into view at once, above the card on a phone, without the visitor scrolling.
  function fitView(items,focus){
    var nodes=items.map(function(i){return i.node}).filter(function(n){return n&&visible(n)});
    if(!nodes.length)return;
    var main=items[focus||0]&&items[focus||0].node&&visible(items[focus||0].node)?items[focus||0].node:nodes[0];
    nodes=nodes.filter(function(n){return n!==main}).concat([main]);
    // each region into view inside its own scrolling panel, ending with the main one so it wins any conflict
    nodes.forEach(function(n){try{n.scrollIntoView({block:'nearest',inline:'nearest'})}catch(e){}});
    var narrow=window.innerWidth<640,vh=window.innerHeight;
    var top=12,bottom=narrow?vh-(ui?ui.card.offsetHeight:vh*0.45)-12:vh-12;
    var rects=nodes.map(function(n){return n.getBoundingClientRect()});
    if(!narrow&&ui){                                                // desktop: keep regions in the card's column clear of the card
      var c=ui.card.getBoundingClientRect();
      if(rects.some(function(r){return r.right>c.left-8}))bottom=c.top-12;
    }
    var uTop=Math.min.apply(null,rects.map(function(r){return r.top})),uBottom=Math.max.apply(null,rects.map(function(r){return r.bottom}));
    var room=bottom-top,h=uBottom-uTop,delta;
    if(h<=room)delta=uTop-(top+(room-h)/3);                         // all fit: sit in the upper part of the free space
    else{                                                           // not all fit (a phone): the main region wins
      var m=main.getBoundingClientRect();
      delta=m.height<=room?m.top-(top+(room-m.height)/3):m.top-top;
    }
    if(Math.abs(delta)>2){try{window.scrollBy(0,delta)}catch(e){}}
    clearSticky(main);
  }
  // A bar that stays pinned at the top of the page (a toolbar) can sit over the region: move the region below it.
  function clearSticky(main){
    var block=ui&&ui.root.querySelector('.ilit-tour-block');
    for(var pass=0;pass<2;pass++){
      var m=main.getBoundingClientRect(),x=Math.min(window.innerWidth-2,Math.max(2,m.left+Math.min(40,m.width/2))),y=Math.max(1,m.top+3);
      if(block)block.style.display='none';
      var hit=document.elementFromPoint(x,y);
      if(block)block.style.display='';
      if(!hit||main.contains(hit)||hit.contains(main))return;
      var bar=hit;
      while(bar&&bar!==document.body){var pos=getComputedStyle(bar).position;if(pos==='sticky'||pos==='fixed')break;bar=bar.parentElement}
      if(!bar||bar===document.body)return;
      var need=bar.getBoundingClientRect().bottom+10-m.top;
      if(need<=0)return;
      var box=scrollParent(main);
      try{if(box)box.scrollTop-=need;else window.scrollBy(0,-need)}catch(e){return}
    }
  }
  function scrollParent(n){
    for(var p=n.parentElement;p&&p!==document.body&&p!==document.documentElement;p=p.parentElement){
      var o=getComputedStyle(p).overflowY;
      if((o==='auto'||o==='scroll')&&p.scrollHeight>p.clientHeight)return p;
    }
    return null;
  }

  /* ---------- showing a step ---------- */
  function sectionOf(i){return STEPS[i]&&STEPS[i].section}
  function sectionPlace(i){
    var sec=sectionOf(i),first=i,last=i;
    while(first>0&&sectionOf(first-1)===sec)first--;
    while(last<STEPS.length-1&&sectionOf(last+1)===sec)last++;
    return {n:i-first+1,of:last-first+1};
  }
  function render(i,items,pending){
    var s=STEPS[i],u=build(),sp=sectionPlace(i);
    document.documentElement.classList.add('ilit-tour-on');
    u.items=items||[];
    u.kicker.textContent=(s.section||'Tour')+(sp.of>1?' · '+sp.n+' of '+sp.of:'');
    u.title.textContent=s.title||'';
    u.text.textContent=s.text||'';
    u.extra.textContent='';
    u.count.textContent='Step '+(i+1)+' of '+STEPS.length;
    u.fill.style.width=Math.round(((i+1)/STEPS.length)*100)+'%';
    u.back.disabled=i===0;
    u.next.textContent=i===STEPS.length-1?'Done':'Next';
    u.next.disabled=!!pending;
    u.skip.hidden=sectionOf(i)===sectionOf(STEPS.length-1)||!STEPS.slice(i+1).some(function(x){return x.section!==s.section});
    if(s.writes)u.extra.appendChild(el('span','ilit-tour-writes',s.writes));
    (s.buttons||[]).forEach(function(b){
      var btn=el('button','ilit-tour-btn action',b.label);btn.type='button';
      if(b.writes)u.extra.appendChild(el('span','ilit-tour-writes',b.writes));
      btn.onclick=function(){var node=qs(b.click);if(node)node.click();btn.disabled=true};   // never moves on by itself
      u.extra.appendChild(btn);
    });
    u.live.textContent=pending?'':(s.title||'')+'. '+(s.text||'');
    u.card.classList.toggle('pending',!!pending);
    u.card.setAttribute('data-step',s.id);
    place();
    if(!watch)follow();
    if(!pending){try{u.next.focus({preventScroll:true})}catch(e){}}
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
    if(!state.t0)state.t0=Date.now();
    save(state);
    build();
    render(i,(ui&&ui.items)||[],true);                             // keep the last highlights while the next step gets ready (no flash)
    // 1. be on the right page: the tour clicks through where the site would (via), or opens the page itself
    var url=await resolveUrl(s.url);
    if(token!==run)return;
    if(url==null){return skipOver(i,token)}                         // the example decision is not in this library
    if(!sameLocation(url)){
      state.nav=(state.nav&&state.nav.i===i?state.nav:{i:i,n:0});
      state.nav.n++;
      if(state.nav.n>2){state.nav=null;return skipOver(i,token)}   // do not loop if the page will not open
      save(state);
      var via=s.via&&direction>0&&state.nav.n===1?findVisible(s.via):null;
      if(via){
        via.click();
        var end=Date.now()+6000;
        while(Date.now()<end&&!sameLocation(url)){await sleep(100);if(token!==run)return}
      }
      if(!sameLocation(url)){location.assign(url);return}
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
      if(!done&&(s.before[k].do==='waitFor'||s.before[k].do==='type')){ok=false;break}
    }
    // 3. find what to light up
    var target=null;
    if(ok&&s.target)target=await waitFor(s.target,s.timeout||8,token);
    if(token!==run)return;
    if(s.target&&!target)return skipOver(i,token);                  // missing element or data: skip, never break
    var items=itemsFor(s,target);
    if(s.settle)await sleep(reduce?0:s.settle);                    // let a smooth scroll inside the page finish first
    if(token!==run)return;
    hoverOff();
    render(i,items,false);
    if(!s.noScroll)fitView(items,s.focus||0);
    place();
    if(s.hover&&target)hoverOn(target);
    var ms=Date.now()-state.t0;
    window.__ilitTourTimes[s.id]=ms;ui.card.setAttribute('data-ms',String(ms));
    state.t0=null;save(state);
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
  function go(d){
    if(ui&&ui.card.classList.contains('pending')&&d>0)return;      // one press, one step: wait for this one to finish
    hoverOff();direction=d;
    if(state)state.t0=Date.now();
    show((state?state.i:0)+d,d);
  }
  function skipSection(){
    hoverOff();
    var i=state?state.i:0,sec=sectionOf(i),n=i;
    while(n<STEPS.length&&sectionOf(n)===sec)n++;
    direction=1;
    if(state)state.t0=Date.now();
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
    caseIds={};pendingLookups={};
    state={i:0,active:true,t0:Date.now()};save(state);
    build();render(0,[],true);
    // sign in and look up the example decisions once, together, so later steps do not wait on them
    await Promise.all((DATA.demoSignIn!==false?[demoSignIn()]:[]).concat(Object.keys(CASES).map(resolveCase)));
    var url=new URL(location.href);
    if(url.searchParams.has('tour')){url.searchParams.delete('tour');history.replaceState(null,'',url.pathname+url.search+url.hash)}
    show(0,1);
  }

  /* ---------- keyboard ---------- */
  document.addEventListener('keydown',function(e){
    if(!ui||e.defaultPrevented)return;
    if(e.key==='Escape'){e.preventDefault();exit();return}
    if(e.target&&e.target.closest&&!e.target.closest('.ilit-tour')&&/^(input|textarea|select)$/i.test(e.target.tagName||''))return;
    if(e.key==='ArrowRight'){e.preventDefault();go(1)}
    else if(e.key==='ArrowLeft'){e.preventDefault();if(state&&state.i>0)go(-1)}
  },true);

  /* ---------- starting it ---------- */
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-ilit-tour-start]');
    if(!b)return;
    e.preventDefault();
    start();
  });
  window.ilitTour={start:start,exit:exit,steps:STEPS,resolveUrl:resolveUrl,resolveCase:resolveCase,times:function(){return window.__ilitTourTimes}};

  function boot(){
    var wants=new URLSearchParams(location.search).get('tour')==='1';
    if(wants&&!(state&&state.active)){start();return}
    if(state&&state.active)show(Math.min(state.i||0,STEPS.length-1),state.dir||direction);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,30)});
  else setTimeout(boot,30);
})();
