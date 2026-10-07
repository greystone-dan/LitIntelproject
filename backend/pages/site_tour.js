/* iLit site tour: a scripted walk through the real site. The visitor only presses Next (or Back, Skip section, Exit).
   Each step first says what is about to happen and lights the place; Next then moves a visible pointer there, slowly,
   and the tour clicks or types for the visitor; the result is lit and explained. The page scrolls only when it must,
   and then slowly. The speech card sits beside what it explains; the control bar stays in one place.
   Self-contained: no libraries, no network calls except the site's own (to find the example decisions).
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
    if(sel&&sel.css)return {css:fillIds(sel.css),text:sel.text,pin:sel.pin};
    return sel;
  }
  function findVisible(sel){
    var list=Array.isArray(sel)?sel:[sel];
    for(var i=0;i<list.length;i++){
      var item=fillIds(list[i]),css=typeof item==='string'?item:item&&item.css,re=item&&item.text?new RegExp(item.text,'i'):null,all;
      if(!css)continue;
      try{all=document.querySelectorAll(css)}catch(e){continue}
      for(var j=0;j<all.length;j++)if(visible(all[j])&&(!re||re.test(all[j].textContent||''))&&(!item.pin||hasPinpoint(all[j])))return all[j];
    }
    return null;
  }
  // A marked citation that the reader matched to a library case at a named paragraph, so its card shows that passage.
  function hasPinpoint(node){
    var id=node.getAttribute('data-cite-id');
    if(!id)return false;
    try{
      var p=window.readerState&&window.readerState.payload||(typeof readerState!=='undefined'?readerState.payload:null);   // the reader's own data
      var rows=((p&&p.readerData&&p.readerData.citations)||[]).concat((p&&p.citations)||[]);
      for(var k=0;k<rows.length;k++)if(String(rows[k].id)===id)return rows[k].target_case_id!=null&&rows[k].target_paragraph!=null;
    }catch(e){}
    return false;
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
    // A decision chosen for the tour can leave the library or lose its filters: then take the first that the same search finds.
    if(id==null&&lookedUp&&spec.search){
      try{
        var url=await resolveUrl(spec.search);
        var s2=url&&await fetch(url);
        var first=s2&&s2.ok?(((await s2.json()).results)||[])[0]:null;
        if(first)id=first.case_id;
      }catch(e){}
    }
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
    // the explorer opens a case reader from case_id, and About has sub-pages: a leftover one must not count as the page
    ['case_id','about'].forEach(function(k){if(!want.has(k)&&have.has(k))ok=false});
    if(u.hash&&u.hash!==location.hash)ok=false;
    if(!u.hash&&u.pathname==='/workbench'&&location.hash&&location.hash!=='#home')ok=false;
    return ok;
  }

  /* ---------- actions the tour performs for the visitor (each one is safe to repeat) ----------
     A step can do things twice over: "before" gets the page ready without showing it (opening a panel the step
     needs), and "act" is what the visitor watches after the card has said what is about to happen. */
  async function typeInto(input,text,token,live){
    if(input.value===text){                                        // already typed (a refresh or Back): do not type it again,
      input.dispatchEvent(new Event('input',{bubbles:true}));        // but let the page show its matches again
      closeSuggestions();return;
    }
    input.focus({preventScroll:true});
    input.value='';
    input.dispatchEvent(new Event('input',{bubbles:true}));
    if(reduce||!live){input.value=text;input.dispatchEvent(new Event('input',{bubbles:true}));closeSuggestions();return}
    for(var i=1;i<=text.length;i++){
      if(token!==run)return;
      input.value=text.slice(0,i);
      input.dispatchEvent(new Event('input',{bubbles:true}));
      await sleep(90);
    }
    closeSuggestions();
  }
  function closeSuggestions(){var s=qs('#searchSuggestions');if(s)s.hidden=true;var q=qs('#searchQuery');if(q)q.setAttribute('aria-expanded','false')}
  async function fillInto(input,text){
    if(input.value===text)return;
    input.focus({preventScroll:true});
    input.value=text;
    input.dispatchEvent(new Event('input',{bubbles:true}));
    input.scrollTop=0;
  }
  function pickNode(sel,a){
    if(typeof sel!=='string')return findVisible(sel);                // {css,text,pin} or a list of alternatives
    var all=[];
    try{all=[].slice.call(document.querySelectorAll(fillIds(sel)))}catch(e){}
    all=all.filter(visible);
    if(a&&a.match){var re=new RegExp(a.match,'i');all=all.filter(function(n){return re.test(n.textContent||'')})}
    return all[0]||null;
  }
  async function findNode(a,token){
    var end=Date.now()+(a.timeout||5)*1000;
    for(;;){
      if(token!==run)return null;
      var node=pickNode(a.selector,a);
      if(node||Date.now()>end)return node;
      await sleep(100);
    }
  }
  // live: the visitor watches the pointer travel there first (and the page glide, when it has to move).
  async function doAction(a,token,live){
    if(a.unless&&findVisible(a.unless))return true;
    if(a.when&&!findVisible(a.when))return true;
    if(a.do==='wait'){await sleep(reduce||!live?0:(a.ms||300));return true}
    if(a.do==='waitFor')return !!(await waitFor(a.selector,a.timeout||10,token));
    var times=Math.max(1,a.times||1);
    for(var n=0;n<times;n++){
      var node=await findNode(a,token);
      if(!node)return n>0;
      if(live&&ui&&a.do!=='fill'){
        ui.items=[{node:node,sel:null}];
        await bringIntoView(node,token);place();
        await pointAt(node,token);
        if(token!==run)return false;
        if(a.do!=='type'&&a.do!=='hover'&&a.do!=='glide')await press();
      }
      if(a.do!=='hover')hoverOff();
      switch(a.do){
        case 'type':await typeInto(node,a.text||'',token,live);break;
        case 'fill':await fillInto(node,(DATA.texts||{})[a.sample]||'');break;
        case 'check':if(!node.checked)node.click();break;
        case 'uncheck':if(node.checked)node.click();break;
        case 'open':if(!node.open)node.open=true;break;
        case 'click':node.click();break;
        case 'hover':hoverOn(node);break;
        case 'glide':if(!live)node.scrollIntoView({block:'nearest'});break;   // live: bringIntoView above already moved it, slowly
        case 'submit':if(node.requestSubmit)node.requestSubmit();else node.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));break;
        case 'drop':if(!(await dropFile(node,a,live)))return false;break;
        default:return false;
      }
      if(live&&times>1){await sleep(reduce?0:300);await settleScroll(token);await sleep(reduce?0:(a.pause||900))}
      else await sleep(live?(a.pause||250):60);
    }
    return true;
  }

  // Drop one of the tour's own fictional sample files on a drop zone, as a person dragging it from their desktop would.
  async function dropFile(zone,a,live){
    try{
      var r=await fetch(a.file,{credentials:'same-origin'});
      if(!r.ok)return false;
      var blob=await r.blob(),file=new File([blob],a.name||a.file.split('/').pop(),{type:blob.type||'application/octet-stream'});
      var dt=new DataTransfer();dt.items.add(file);
      zone.dispatchEvent(new DragEvent('dragenter',{bubbles:true,cancelable:true,dataTransfer:dt}));
      await sleep(reduce||!live?0:600);
      zone.dispatchEvent(new DragEvent('drop',{bubbles:true,cancelable:true,dataTransfer:dt}));
      return true;
    }catch(e){return false}
  }

  /* ---------- the overlay ----------
     A light shade with a clear border round what the step is about; a speech card that sits beside that region and
     moves with it; and, apart from it, a control bar that never moves, so the visitor's mouse can rest on Next.
     Nothing blocks the page. */
  function build(){
    if(ui)return ui;
    var root=el('div','ilit-tour');root.setAttribute('data-ilit-tour','');
    var svg=document.createElementNS(SVGNS,'svg');svg.setAttribute('class','ilit-tour-dim');svg.setAttribute('aria-hidden','true');
    var path=document.createElementNS(SVGNS,'path');path.setAttribute('fill-rule','evenodd');svg.appendChild(path);root.appendChild(svg);
    var rings=el('div','ilit-tour-rings');root.appendChild(rings);
    var cursor=el('div','ilit-tour-cursor');cursor.setAttribute('aria-hidden','true');
    cursor.innerHTML='<svg viewBox="0 0 24 24" width="26" height="26"><path d="M4 2l15 11.2-6.6 1.1 3.9 7.3-2.9 1.5-3.9-7.4L4 20.7z" fill="#202522" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    root.appendChild(cursor);
    // the speech card
    var card=el('div','ilit-tour-card');
    card.setAttribute('role','dialog');card.setAttribute('aria-label','Site tour');card.setAttribute('tabindex','-1');
    var kicker=el('div','ilit-tour-kicker');
    var title=el('h2','ilit-tour-title');
    var text=el('p','ilit-tour-text');
    var extra=el('div','ilit-tour-extra');
    [kicker,title,text,extra].forEach(function(n){card.appendChild(n)});
    root.appendChild(card);
    // the control bar
    var dock=el('div','ilit-tour-dock');dock.setAttribute('role','toolbar');dock.setAttribute('aria-label','Tour controls');
    var where=el('div','ilit-tour-where');
    var count=el('span','ilit-tour-count');
    var bar=el('div','ilit-tour-bar');var fill=el('i');bar.appendChild(fill);
    where.appendChild(count);where.appendChild(bar);
    var back=el('button','ilit-tour-btn','Back');back.type='button';
    var skip=el('button','ilit-tour-btn quiet','Skip section');skip.type='button';
    var next=el('button','ilit-tour-btn primary','Next');next.type='button';
    var exitX=el('button','ilit-tour-x','×');exitX.type='button';exitX.setAttribute('aria-label','Exit the tour');exitX.title='Exit the tour';
    [where,back,skip,next,exitX].forEach(function(n){dock.appendChild(n)});
    root.appendChild(dock);
    var live=el('div','ilit-tour-live');live.setAttribute('aria-live','polite');root.appendChild(live);
    document.body.appendChild(root);
    exitX.onclick=exit;
    back.onclick=function(){go(-1)};
    next.onclick=function(){go(1)};
    skip.onclick=skipSection;
    ui={root:root,path:path,rings:rings,cursor:cursor,card:card,dock:dock,kicker:kicker,title:title,text:text,extra:extra,fill:fill,count:count,back:back,skip:skip,next:next,live:live,items:[],focus:0};
    slowScrolling(true);
    return ui;
  }
  function destroy(){
    if(watch){cancelAnimationFrame(watch);watch=null}
    if(ui&&ui.root.parentNode)ui.root.parentNode.removeChild(ui.root);
    document.documentElement.classList.remove('ilit-tour-on');
    slowScrolling(false);
    ui=null;
  }
  // What a step lights up: its target, plus any "also" regions.
  function itemsFor(s,target){
    var out=[];
    if(target)out.push({node:target,sel:s.target});
    (s.also||[]).forEach(function(a){                               // a selector, or {sel: selector}
      var sel=a&&a.sel?a.sel:a;
      out.push({node:findVisible(sel),sel:sel});
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
  function dockTop(){return ui?ui.dock.getBoundingClientRect().top:window.innerHeight}
  function place(){
    if(!ui)return;
    var vw=document.documentElement.clientWidth||window.innerWidth,vh=window.innerHeight,pad=6,floor=dockTop()-4;
    var holes=[];
    ui.items.forEach(function(item){
      var b=liveRect(item);
      if(!b){holes.push(null);return}
      var x=Math.max(3,b.left-pad),y=Math.max(3,b.top-pad),x2=Math.min(vw-3,b.right+pad),y2=Math.min(floor,b.bottom+pad);
      var minH=Math.min(40,b.height),minW=Math.min(24,b.width);   // a sliver at the edge of the screen is not worth a ring
      holes.push(x2-x>=minW&&y2-y>=minH&&x2>x&&y2>y?{x:round(x),y:round(y),w:round(x2-x),h:round(y2-y)}:null);
    });
    // one light shade with a window cut for each region (even-odd fill)
    var d='M0 0H'+vw+'V'+vh+'H0Z';
    holes.forEach(function(h){if(h)d+='M'+h.x+' '+h.y+'h'+h.w+'v'+h.h+'h'+(-h.w)+'Z'});
    ui.path.setAttribute('d',d);
    var rings=ui.rings;
    while(rings.children.length<holes.length)rings.appendChild(el('div','ilit-tour-ring'));
    [].forEach.call(rings.children,function(r,k){
      var h=holes[k];
      if(!h){r.style.display='none';return}
      r.style.display='block';
      r.style.transform='translate('+h.x+'px,'+h.y+'px)';r.style.width=h.w+'px';r.style.height=h.h+'px';
    });
    placeCard(holes[ui.focus]||holes.filter(Boolean)[0]||null,holes,vw,floor);
  }
  // The card speaks beside the region it is about: to its right, left, below or above, whichever covers no lit region
  // (and least of the page); failing that, the corner of the screen that covers the least. Never over the control bar.
  function placeCard(focus,holes,vw,floor){
    var c=ui.card,W=c.offsetWidth,H=c.offsetHeight,m=14,gap=20,lit=holes.filter(Boolean);
    function clampY(v){return Math.max(m,Math.min(floor-H-m,v))}
    function clampX(v){return Math.max(m,Math.min(vw-W-m,v))}
    function overlap(x,y,h){return Math.max(0,Math.min(x+W,h.x+h.w)-Math.max(x,h.x))*Math.max(0,Math.min(y+H,h.y+h.h)-Math.max(y,h.y))}
    var spots=[];
    if(focus){
      var h=focus;
      spots.push([h.x+h.w+gap,clampY(h.y),0],[h.x-gap-W,clampY(h.y),1],[clampX(h.x),h.y+h.h+gap,2],[clampX(h.x),h.y-gap-H,3],
        [clampX(h.x+h.w-W),h.y+h.h+gap,2],[clampX(h.x+h.w-W),h.y-gap-H,3]);
    }
    spots.push([vw-W-m,clampY(floor-H-m),6],[m,clampY(floor-H-m),6],[vw-W-m,m+70,7],[m,m+70,7],[clampX((vw-W)/2),clampY((floor-H)/2),8]);
    var best=null;
    spots.forEach(function(p){
      var x=p[0],y=p[1];
      if(x<m-1||x+W>vw-m+1||y<m-1||y+H>floor-m+1)return;            // off the screen or over the control bar
      var cover=0;lit.forEach(function(h){cover+=overlap(x,y,h)});
      var score=cover*10+p[2]*2000+(focus?Math.hypot(x+W/2-(focus.x+focus.w/2),y+H/2-(focus.y+focus.h/2)):0);
      if(!best||score<best.score)best={x:x,y:y,score:score};
    });
    if(!best)best={x:clampX(vw-W-m),y:clampY(floor-H-m)};
    c.style.transform='translate('+Math.round(best.x)+'px,'+Math.round(best.y)+'px)';
  }
  function follow(){
    var lastSig='';
    (function tick(){
      if(!ui)return;
      var sig=[window.innerWidth,window.innerHeight,ui.card.offsetHeight,ui.card.offsetWidth].concat(ui.items.map(function(item){
        var b=item.node&&document.contains(item.node)?item.node.getBoundingClientRect():null;
        return b?[b.left,b.top,b.width,b.height].join(','):'-';
      })).join('|');
      if(sig!==lastSig){lastSig=sig;place()}
      watch=requestAnimationFrame(tick);
    })();
  }
  // How far down the screen a bar pinned at the top reaches (a page's sticky search bar or header), at this column.
  function pinnedTop(x){
    var hit=document.elementFromPoint(Math.max(2,Math.min(window.innerWidth-2,x)),2);
    for(var n=hit;n&&n!==document.body&&n!==document.documentElement;n=n.parentElement){
      var pos=getComputedStyle(n).position;
      if(pos==='sticky'||pos==='fixed'){var b=n.getBoundingClientRect().bottom;return b<window.innerHeight*0.4?b:0}
    }
    return 0;
  }
  // The free part of the screen: below any pinned bar, above the control bar.
  function freeArea(node){
    var top=12,bottom=dockTop()-14;
    if(node)top=Math.max(top,pinnedTop(node.getBoundingClientRect().left+20)+10);
    return {top:top,bottom:bottom};
  }
  function onScreen(node){
    var r=clipped(node),vw=document.documentElement.clientWidth||window.innerWidth;
    return !!r&&r.right>8&&r.left<vw-8&&r.bottom>8&&r.top<dockTop()-8;
  }
  // Something pinned to the screen (a toolbar, a sticky header) sits over the start of the region.
  function covered(node){
    var r=clipped(node);
    if(!r)return true;
    var x=Math.min(window.innerWidth-2,Math.max(2,r.left+Math.min(40,(r.right-r.left)/2))),y=Math.min(window.innerHeight-2,Math.max(1,r.top+Math.min(12,(r.bottom-r.top)/2)));
    var hit=document.elementFromPoint(x,y);                          // the tour's own layer takes no pointer events, so it is not hit
    return !!hit&&!node.contains(hit)&&!hit.contains(node);
  }
  function inView(node){
    var r=clipped(node);
    if(!r||covered(node))return false;
    var f=freeArea(node),shown=Math.min(r.bottom,f.bottom)-Math.max(r.top,f.top);
    if(r.top<f.top-2)return false;                                  // its top is cut off: the visitor would not see where it starts
    return r.bottom<=f.bottom||shown>=Math.min(320,(r.bottom-r.top)*0.6);   // mostly on screen is enough: do not move the page
  }

  /* ---------- slow scrolling: the page never jumps ---------- */
  var gliding=0;
  function scrollTopOf(box){return box?box.scrollTop:(window.scrollY||document.documentElement.scrollTop)}
  function setScroll(box,v){
    try{if(box)box.scrollTo({top:v,behavior:'instant'});else window.scrollTo({top:v,behavior:'instant'})}
    catch(e){if(box)box.scrollTop=v;else window.scrollTo(0,v)}
  }
  function glide(box,delta,token){
    var from=scrollTopOf(box),max=box?box.scrollHeight-box.clientHeight:document.documentElement.scrollHeight-window.innerHeight;
    var to=Math.max(0,Math.min(max,from+delta));
    if(Math.abs(to-from)<2)return Promise.resolve();
    if(reduce){setScroll(box,to);return Promise.resolve()}
    var ms=Math.round(Math.min(2600,Math.max(900,Math.abs(to-from)*1.7))),t0=null;
    gliding++;
    return new Promise(function(done){
      function frame(now){
        if(t0==null)t0=now;
        var k=Math.min(1,(now-t0)/ms),e=k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2;
        if(token!=null&&token!==run)k=1;
        else setScroll(box,from+(to-from)*e);
        if(k<1)requestAnimationFrame(frame);else{gliding--;done()}
      }
      requestAnimationFrame(frame);
    });
  }
  // While the tour runs, the site's own "jump to" moves (Find, Search this decision, the Outline) glide slowly too.
  var nativeIntoView=Element.prototype.scrollIntoView;
  function slowScrolling(on){
    if(!on){Element.prototype.scrollIntoView=nativeIntoView;return}
    if(reduce)return;
    Element.prototype.scrollIntoView=function(opts){
      if(!ui||!opts||typeof opts!=='object'||opts.behavior!=='smooth')return nativeIntoView.apply(this,arguments);
      var box=scrollParent(this),r=this.getBoundingClientRect(),top=0,h=window.innerHeight,block=opts.block||'start',d;
      if(box){var b=box.getBoundingClientRect();top=Math.max(0,b.top);h=Math.min(window.innerHeight,b.bottom)-top}
      else h=Math.min(h,dockTop())-top;
      if(block==='center')d=r.top-top-(h-r.height)/2;
      else if(block==='nearest')d=r.top<top?r.top-top-12:(r.bottom>top+h?r.bottom-top-h+12:0);
      else d=r.top-top-12;
      glide(box,d,null);
    };
  }
  // Scroll only when the region is not already on screen, slowly, and only as far as needed.
  async function bringIntoView(node,token){
    if(!node||!visible(node)||inView(node))return;
    var full=node.getBoundingClientRect(),cut=clipped(node);
    if(!cut||cut.right-cut.left<Math.min(full.width,window.innerWidth)*0.8){   // hidden sideways in a row that scrolls across
      try{nativeIntoView.call(node,{block:'nearest',inline:'nearest',behavior:reduce?'auto':'smooth'})}catch(e){}
      await settleScroll(token);
      if(inView(node))return;
    }
    if(clipped(node)&&covered(node)){                               // on screen but under a pinned bar: move it out from under, no more
      var before=node.getBoundingClientRect().top;await clearSticky(node,token);
      if(node.getBoundingClientRect().top!==before&&inView(node))return;
    }
    var box=scrollParent(node);
    if(box){                                                        // inside a scrolling panel: scroll the panel first
      var b=box.getBoundingClientRect(),r=node.getBoundingClientRect();
      if(r.top<b.top||r.bottom>b.bottom){
        await glide(box,r.top-b.top-Math.max(12,(b.height-Math.min(r.height,b.height))/3),token);
      }
      if(inView(node))return;
    }
    var f=freeArea(node),m=node.getBoundingClientRect(),room=f.bottom-f.top;
    await glide(null,m.height<=room?m.top-(f.top+Math.min(90,(room-m.height)/2)):m.top-f.top-8,token);
    if(covered(node))await clearSticky(node,token);
  }
  async function settleScroll(token){                               // wait until every scroll has stopped moving
    if(reduce)return;
    var last=null,still=0;
    for(var k=0;k<90&&still<3;k++){
      await sleep(40);
      if(token!==run)return;
      var sig=gliding+','+window.scrollY;
      [].forEach.call(document.querySelectorAll('.reader-pane,.v6-pane,#decisionTarget,#decisionBody,.fmt-decision'),function(n){sig+=','+n.scrollTop});
      still=sig===last&&!gliding?still+1:0;last=sig;
    }
  }
  // A bar that stays pinned at the top of the page (a toolbar) can sit over the region: move the region below it.
  async function clearSticky(main,token){
    var m=main.getBoundingClientRect(),x=Math.min(window.innerWidth-2,Math.max(2,m.left+Math.min(40,m.width/2))),y=Math.max(1,m.top+3);
    var hit=document.elementFromPoint(x,y);
    if(!hit||main.contains(hit)||hit.contains(main))return;
    var bar=hit;
    while(bar&&bar!==document.body){var pos=getComputedStyle(bar).position;if(pos==='sticky'||pos==='fixed')break;bar=bar.parentElement}
    if(!bar||bar===document.body)return;
    var need=bar.getBoundingClientRect().bottom+10-m.top;
    if(need<=0)return;
    var box=scrollParent(main);
    await glide(box&&box.scrollTop>=need?box:null,-need,token);
  }
  function scrollParent(n){
    for(var p=n.parentElement;p&&p!==document.body&&p!==document.documentElement;p=p.parentElement){
      var o=getComputedStyle(p).overflowY;
      if((o==='auto'||o==='scroll')&&p.scrollHeight>p.clientHeight)return p;
    }
    return null;
  }

  /* ---------- the pointer: it starts where the visitor's mouse is (on Next) and moves at an easy pace ---------- */
  var pointer={x:null,y:null};
  async function pointAt(node,token){
    if(!ui||!node)return;
    var c=ui.cursor,r=clipped(node)||node.getBoundingClientRect();
    var x=Math.round(r.left+Math.min(r.width/2,Math.max(16,r.width*0.3))),y=Math.round(r.top+Math.min(r.height/2,22));
    if(pointer.x==null){                                            // first appearance: from the Next button
      var nb=ui.next.getBoundingClientRect();
      pointer.x=Math.round(nb.left+nb.width/2);pointer.y=Math.round(nb.top+nb.height/2);
      c.style.transition='none';c.style.transform='translate('+pointer.x+'px,'+pointer.y+'px)';
      c.getBoundingClientRect();c.style.transition='';
    }
    c.classList.add('on');
    var dist=Math.hypot(x-pointer.x,y-pointer.y);
    var ms=reduce?0:Math.round(Math.min(1500,Math.max(650,dist*1.7)));
    c.style.transitionDuration=ms+'ms, .2s';
    c.style.transform='translate('+x+'px,'+y+'px)';
    pointer.x=x;pointer.y=y;
    await sleep(reduce?0:ms+250);
  }
  async function press(){
    if(!ui)return;
    ui.cursor.classList.remove('press');ui.cursor.getBoundingClientRect();ui.cursor.classList.add('press');
    await sleep(reduce?0:420);
  }
  function hidePointer(){if(ui){ui.cursor.classList.remove('on');pointer.x=null}}

  /* ---------- showing a step ----------
     A step can have up to three moments, each ended by Next:
       lead  "OK, let's move on to ..." with the place it will click lit (only when the step is on another page);
       say   what is about to happen, with the place it will happen lit (only for a step that acts);
       show  the result, lit, with the explanation. */
  function sectionOf(i){return STEPS[i]&&STEPS[i].section}
  function sectionPlace(i){
    var sec=sectionOf(i),first=i,last=i;
    while(first>0&&sectionOf(first-1)===sec)first--;
    while(last<STEPS.length-1&&sectionOf(last+1)===sec)last++;
    return {n:i-first+1,of:last-first+1};
  }
  function render(i,items,mode,focus){
    var s=STEPS[i],u=build(),sp=sectionPlace(i),pending=mode==='pending';
    document.documentElement.classList.add('ilit-tour-on');
    if(items&&u.items!==items){u.root.classList.add('moving');clearTimeout(u.moving);u.moving=setTimeout(function(){if(ui)ui.root.classList.remove('moving')},650)}
    if(items)u.items=items;
    u.focus=focus||0;
    if(!pending){
      u.kicker.textContent=(s.section||'Tour')+(sp.of>1?' · '+sp.n+' of '+sp.of:'');
      u.title.textContent=mode==='lead'?s.lead:(s.title||'');
      u.text.textContent=mode==='lead'?(s.leadText||''):mode==='say'?(s.say||''):(s.text||'');
      u.extra.textContent='';
      if(mode==='show'){
        if(s.writes)u.extra.appendChild(el('span','ilit-tour-writes',s.writes));
        (s.buttons||[]).forEach(function(b){
          var btn=el('button','ilit-tour-btn action',b.label);btn.type='button';
          if(b.writes)u.extra.appendChild(el('span','ilit-tour-writes',b.writes));
          btn.onclick=function(){var node=qs(b.click);if(node)node.click();btn.disabled=true};   // never moves on by itself
          u.extra.appendChild(btn);
        });
      }
      u.live.textContent=u.title.textContent+'. '+u.text.textContent;
      u.card.setAttribute('data-step',s.id);
      u.card.setAttribute('data-phase',mode);
    }
    u.count.textContent='Step '+(i+1)+' of '+STEPS.length;
    clearTimeout(u.slow);
    if(pending)u.slow=setTimeout(function(){if(ui&&ui.card.classList.contains('pending'))ui.count.textContent='Loading…'},900);   // only a slow step says so
    u.fill.style.width=Math.round(((i+1)/STEPS.length)*100)+'%';
    u.back.disabled=i===0;
    u.next.textContent=i===STEPS.length-1&&mode==='show'?'Done':'Next';
    u.next.disabled=pending;
    u.skip.hidden=sectionOf(i)===sectionOf(STEPS.length-1)||!STEPS.slice(i+1).some(function(x){return x.section!==s.section});
    u.card.classList.toggle('pending',pending);
    if(pending)u.card.removeAttribute('data-ms');
    u.dock.classList.toggle('pending',pending);
    place();
    if(!watch)follow();
    if(!pending){try{u.next.focus({preventScroll:true})}catch(e){}}
  }
  function ready(i,mode){                                           // the card is up and Next is live: note how long it took
    var s=STEPS[i];
    var ms=state&&state.t0?Date.now()-state.t0:0;window.__ilitTourTimes[s.id+(mode==='show'?'':':'+mode)]=ms;ui.card.setAttribute('data-ms',String(ms));
    if(state)state.t0=null;
    save(state);
  }
  var direction=1;
  async function show(i,dir){
    var token=++run;
    direction=dir||direction;
    if(i<0)i=0;
    if(i>=STEPS.length){finish();return}
    var s=STEPS[i];
    state=state||{i:i};
    if(state.i!==i)state.phase=direction>0?'enter':'back';
    state.i=i;state.active=true;state.dir=direction;
    if(!state.t0)state.t0=Date.now();
    save(state);
    build();
    render(i,null,'pending');                                      // keep the last highlights while this step gets ready (no flash)
    // 1. be on the right page
    var url=await resolveUrl(s.url);
    if(token!==run)return;
    if(url==null)return skipOver(i,token);                         // the example decision is not in this library
    if(!sameLocation(url)){
      if((state.phase==='enter'||state.phase==='lead')&&s.lead){     // "OK, let's move on": light the place it will click, wait for Next
        var spot=findVisible(fillIds(s.via||s.point||''));
        if(spot)await bringIntoView(spot,token);
        if(token!==run)return;
        state.phase='lead';
        render(i,spot?[{node:spot,sel:null}]:[],'lead');ready(i,'lead');
        return;
      }
      return navigate(i,url,token,false);
    }
    state.nav=null;
    if(s.fresh&&direction<0&&state.reloaded!==i){state.reloaded=i;save(state);location.reload();return}   // a page that changes as you use it starts clean when you step back to it
    if(state.reloaded!==i)state.reloaded=null;
    if(s.top&&state.phase!=='show'&&scrollTopOf(null)>4){await glide(null,-scrollTopOf(null),token);if(token!==run)return}   // a page is introduced from its top
    // 2. get the page ready, quietly
    for(var k=0;k<(s.before||[]).length;k++){
      var done=await doAction(s.before[k],token,false);
      if(token!==run)return;
      if(!done&&(s.before[k].do==='waitFor'||s.before[k].do==='type'))return skipOver(i,token);
    }
    // 3. a step that acts first says what it will do, lighting the place
    if(s.act&&s.act.length&&state.phase!=='back'&&state.phase!=='show'){
      var first=s.act.filter(function(a){return a.selector&&a.do!=='waitFor'&&!(a.unless&&findVisible(a.unless))&&!(a.when&&!findVisible(a.when))})[0];
      var spotSel=s.sayTarget||(first&&first.selector);
      var node=spotSel?(await waitFor(spotSel,first&&first.timeout||8,token)):null;
      if(token!==run)return;
      if(!node&&!s.sayTarget&&first){if(s.optional)return skipOver(i,token)}
      if(node)await bringIntoView(node,token);
      if(token!==run)return;
      state.phase='say';
      render(i,node?[{node:node,sel:spotSel}]:[],'say');ready(i,'say');
      return;
    }
    if(s.act)for(var q=0;q<s.act.length;q++){                      // Back or a refresh: the same result, without the show
      var ok=await doAction(s.act[q],token,false);
      if(token!==run)return;
      if(!ok&&(s.act[q].do==='waitFor'||s.act[q].do==='type'))return skipOver(i,token);
    }
    return result(i,token);
  }
  // Next on "say": the pointer goes and does it, then the result is shown.
  async function perform(i){
    var token=++run,s=STEPS[i];
    render(i,null,'pending');
    for(var k=0;k<s.act.length;k++){
      var ok=await doAction(s.act[k],token,true);
      if(token!==run)return;
      if(!ok&&(s.act[k].do==='waitFor'||s.act[k].do==='type'||s.act[k].required))return skipOver(i,token);
    }
    await settleScroll(token);
    return result(i,token);
  }
  // Next on "lead": the pointer goes to the tab or link and presses it.
  async function navigate(i,url,token,live){
    var s=STEPS[i];
    state.nav=(state.nav&&state.nav.i===i?state.nav:{i:i,n:0});
    state.nav.n++;
    if(state.nav.n>2){state.nav=null;return skipOver(i,token)}     // do not loop if the page will not open
    state.phase='nav';save(state);
    var spot=live?findVisible(fillIds(s.via||s.point||'')):null;
    if(spot){
      ui.items=[{node:spot,sel:null}];
      await bringIntoView(spot,token);place();
      await pointAt(spot,token);if(token!==run)return;
      await press();if(token!==run)return;
    }
    var via=live&&s.via?findVisible(fillIds(s.via)):null;
    if(via){
      via.click();
      var end=Date.now()+6000;
      while(Date.now()<end&&!sameLocation(url)){await sleep(100);if(token!==run)return}
    }
    if(!sameLocation(url)){location.assign(url);return}
    return show(i,1);
  }
  async function result(i,token){
    var s=STEPS[i];
    var target=null;
    if(s.target)target=await waitFor(s.target,s.timeout||8,token);
    if(token!==run)return;
    if(s.target&&!target)return skipOver(i,token);                  // missing element or data: skip, never break
    var items=itemsFor(s,target);
    if(s.settle)await sleep(reduce?0:s.settle);
    if(token!==run)return;
    var main=(items[s.focus||0]||{}).node||target;
    if(!s.noScroll&&!s.top)await bringIntoView(main,token);
    if(token!==run)return;
    if(s.optional&&main&&!onScreen(main))return skipOver(i,token);  // there but out of sight: skip it
    if(!s.act&&!s.hover)hidePointer();
    if(s.hover&&target){await pointAt(target,token);if(token!==run)return;hoverOn(target)}
    state.phase='show';
    render(i,items,'show',s.focus||0);ready(i,'show');
  }
  var hovered=null;
  function hoverOn(node){
    hoverOff();hovered=node;
    try{node.dispatchEvent(new MouseEvent('mouseover',{bubbles:true,cancelable:true,view:window}))}catch(e){}
    try{node.dispatchEvent(new MouseEvent('mousemove',{bubbles:true,cancelable:true,view:window}))}catch(e){}
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
    state.phase=direction>0?'enter':'back';
    return show(n,direction);
  }
  function go(d){
    if(!state||!ui)return;
    if(ui.card.classList.contains('pending')&&d>0)return;          // one press, one move: wait for this one to finish
    var i=state.i||0;
    state.t0=Date.now();
    if(d>0&&state.phase==='lead'){direction=1;var tk=++run;render(i,null,'pending');return resolveUrl(STEPS[i].url).then(function(u){if(tk===run)return u==null?skipOver(i,tk):navigate(i,u,tk,true)})}
    if(d>0&&state.phase==='say'){direction=1;return perform(i)}
    hoverOff();
    direction=d;
    state.phase=d>0?'enter':'back';
    show(i+d,d);
  }
  function skipSection(){
    hoverOff();
    var i=state?state.i:0,sec=sectionOf(i),n=i;
    while(n<STEPS.length&&sectionOf(n)===sec)n++;
    direction=1;
    if(state){state.t0=Date.now();state.phase='enter'}
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
  // Ask the server for the slow read-only data ahead of the steps that show it, so those steps open at once.
  // An entry is a URL; {url,top:{by,key,then}} also loads the item with the highest "by" from that list;
  // {post,sample} or {post,file} runs the demo document through the reader (only the tour's own fictional samples are
  // cached by the server; anything a person pastes or uploads is read once and dropped).
  function warm(){
    (DATA.warm||[]).forEach(function(w){
      try{
        if(typeof w==='string'){fetch(w,{credentials:'same-origin'}).catch(function(){});return}
        if(w.post&&w.file){
          fetch(w.file,{credentials:'same-origin'}).then(function(r){return r.ok?r.blob():null}).then(function(blob){
            if(!blob)return;var body=new FormData();body.append('file',new File([blob],w.name||w.file.split('/').pop()));
            return fetch(w.post,{method:'POST',credentials:'same-origin',body:body});
          }).catch(function(){});return}
        if(w.post){fetch(w.post,{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({text:(DATA.texts||{})[w.sample]||'',title:w.title||'Pasted text'})}).catch(function(){});return}
        if(w.years){                                                 // {url,years:{back,then:[...]}}: the same statistics for the
          fetch(w.url,{credentials:'same-origin'}).then(function(r){return r.ok?r.json():null}).then(function(d){   // last few years filed
            var ys=((d&&d.by_year)||[]).map(function(r){return Number(r.year)}).filter(function(y){return y>0});
            if(!ys.length)return;
            var from=String(Math.max.apply(null,ys)-w.years.back);
            w.years.then.forEach(function(u){fetch(u.replace('{}',from),{credentials:'same-origin'}).catch(function(){})});
          }).catch(function(){});return}
        fetch(w.url,{credentials:'same-origin'}).then(function(r){return r.ok?r.json():[]}).then(function(rows){
          var best=null;(rows||[]).forEach(function(r){if(!best||(r[w.top.by]||0)>(best[w.top.by]||0))best=r});
          if(best)fetch(w.top.then.replace('{}',encodeURIComponent(best[w.top.key])),{credentials:'same-origin'}).catch(function(){});
        }).catch(function(){});
      }catch(e){}
    });
  }
  async function start(){
    caseIds={};pendingLookups={};
    state={i:0,active:true,t0:Date.now(),phase:'enter'};save(state);
    build();render(0,[],true);
    // sign in and look up the example decisions once, together, so later steps do not wait on them
    await Promise.all((DATA.demoSignIn!==false?[demoSignIn()]:[]).concat(Object.keys(CASES).map(resolveCase)));
    warm();
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
