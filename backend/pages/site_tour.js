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
  var STEPS=(DATA.introOn?DATA.intro||[]:[]).concat(DATA.steps||[]),CASES=DATA.cases||{};   // the About introduction is kept, switched off until those pages are final
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
    if(a.do==='wait'){await sleep(a.ms||300);return true}
    if(a.do==='waitFor')return !!(await waitFor(a.selector,a.timeout||10,token));
    var times=Math.max(1,a.times||1);
    for(var n=0;n<times;n++){
      var node=await findNode(a,token);
      if(!node)return n>0;
      if(live&&ui&&a.do!=='fill'){
        ui.items=[{node:node,sel:null}];
        await bringIntoView(node,token);
        if(a.high)await lift(node,token);
        place();
        await pointAt(node,token);
        if(token!==run)return false;
        if(a.do!=='type'&&a.do!=='hover'&&a.do!=='glide')await press();
      }
      else if(a.do!=='fill'&&a.do!=='type'&&(!onScreen(node)||a.high)){try{nativeIntoView.call(node,{block:a.high?'start':'center'})}catch(e){}}   // Back or a refresh: no show, but act where it can be seen
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
    root.appendChild(el('div','ilit-tour-block'));                  // the page underneath cannot be clicked during the tour (Daniel, 10-09)
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
    var exitX=el('button','ilit-tour-x','× Exit tour');exitX.type='button';exitX.setAttribute('aria-label','Exit the tour');exitX.title='Exit the tour (Esc)';
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
    lockPage(true);
    return ui;
  }
  function destroy(){
    if(watch){cancelAnimationFrame(watch);watch=null}
    if(ui&&ui.root.parentNode)ui.root.parentNode.removeChild(ui.root);
    document.documentElement.classList.remove('ilit-tour-on');
    slowScrolling(false);
    lockPage(false);
    ui=null;
  }
  // While the tour runs the visitor only steers it: the card scrolls, the dock's buttons and Esc work, and nothing else on the page
  // takes a click, a wheel or touch scroll, or a key. The tour's own actions are synthetic events, so they still go through.
  var SCROLL_KEYS=/^(Spacebar|PageUp|PageDown|Home|End|ArrowUp|ArrowDown|Enter)$/,PAGE_KEYS=/^(PageUp|PageDown|Home|End|ArrowUp|ArrowDown)$/;
  function hold(e){
    if(!ui||!e.isTrusted)return;
    var scroll=e.type==='wheel'||e.type==='touchmove'||(e.type==='keydown'&&PAGE_KEYS.test(e.key));   // these scroll the page even from the dock
    var inside=e.target&&e.target.closest&&e.target.closest(scroll?'.ilit-tour-card':'.ilit-tour-card,.ilit-tour-dock');
    if(inside)return;                                              // the card's own text scrolls, the buttons press
    if(e.type==='keydown'&&(e.ctrlKey||e.metaKey||e.altKey||!(SCROLL_KEYS.test(e.key)||e.key.length===1)))return;   // Esc, the arrows that step the tour, Tab, browser shortcuts
    e.preventDefault();e.stopPropagation();
  }
  var HELD=['wheel','touchmove','mousedown','pointerdown','click','dblclick','contextmenu','auxclick','keydown'];
  function lockPage(on){
    HELD.forEach(function(t){(on?window.addEventListener:window.removeEventListener).call(window,t,hold,{capture:true,passive:false})});
    document.documentElement.classList.toggle('ilit-tour-locked',!!on);
  }
  // What a step lights up: its target, plus any "also" regions.
  function itemsFor(s,target){
    var out=[];
    if(target)out.push({node:target,sel:s.target,span:s.span});     // span: the ring reaches on round these too (one ring for a block of parts)
    (s.also||[]).forEach(function(a){                               // a selector, or {sel: selector}
      var sel=a&&a.sel?a.sel:a;
      out.push({node:findVisible(sel),sel:sel});
    });
    return out;
  }
  function liveRect(item){
    if(item.node&&!document.contains(item.node))item.node=null;
    if(!item.node&&item.sel)item.node=findVisible(item.sel);     // the page re-drew the element: find its replacement
    if(!item.node||!visible(item.node))return null;
    var r=clipped(shownBox(item.node));
    spanNodes(item).forEach(function(n){var c=clipped(n);if(r&&c)r=unite(r,c)});
    return r;
  }
  function spanNodes(item){return (item.span||[]).map(function(sel){return findVisible(sel)}).filter(Boolean)}
  function unite(a,b){var r={left:Math.min(a.left,b.left),top:Math.min(a.top,b.top),right:Math.max(a.right,b.right),bottom:Math.max(a.bottom,b.bottom)};r.width=r.right-r.left;r.height=r.bottom-r.top;return r}
  // An item's whole box on the page (its span included), whether or not all of it can be seen.
  function fullRect(item){
    var r=shownBox(item.node).getBoundingClientRect();r={left:r.left,top:r.top,right:r.right,bottom:r.bottom};
    spanNodes(item).forEach(function(n){r=unite(r,n.getBoundingClientRect())});
    r.width=r.right-r.left;r.height=r.bottom-r.top;return r;
  }
  // An element its own small frame cuts off for good (a long name in a one-line field that hides the rest): the
  // frame is what can be seen, so the ring goes round the frame.
  function shownBox(n){
    for(var p=n.parentElement,d=0;p&&d<3&&p!==document.body;p=p.parentElement,d++){
      var cs=getComputedStyle(p),r=n.getBoundingClientRect(),b=p.getBoundingClientRect();
      if(cs.overflowX==='auto'||cs.overflowX==='scroll'||cs.overflowY==='auto'||cs.overflowY==='scroll')break;
      if(b.width>r.width*2+8||b.height>r.height*2+8)break;         // only a frame about its own size, never a whole panel
      if((cs.overflowX!=='visible'||cs.overflowY!=='visible')&&(r.left<b.left-1||r.right>b.right+1||r.top<b.top-1||r.bottom>b.bottom+1))return p;
    }
    return n;
  }
  // The part of an element that can actually be seen: cut by any scrolling panel it sits in.
  function clipped(n){
    var b=n.getBoundingClientRect(),r={left:b.left,top:b.top,right:b.right,bottom:b.bottom,height:b.height,width:b.width};
    for(var p=n.parentElement;p&&p!==document.body&&p!==document.documentElement;p=p.parentElement){
      var cs=getComputedStyle(p);
      if(cs.position==='fixed')break;
      if(cs.overflowY!=='visible'||cs.overflowX!=='visible'){
        var c=(cs.overflowY==='auto'||cs.overflowY==='scroll')?boxView(p,n):p.getBoundingClientRect();   // a panel's pinned toolbar hides what scrolls under it
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
    var holes=[],rects=ui.items.map(liveRect),across=null;
    rects.forEach(function(b){if(b)across=across?unite(across,b):b});  // how wide all the lit regions are together
    ui.items.forEach(function(item,k){
      var b=rects[k];
      if(!b){holes.push(null);return}
      var x=Math.max(3,b.left-pad),y=Math.max(3,b.top-pad),x2=Math.min(vw-3,b.right+pad),y2=Math.min(floor,b.bottom+pad);
      item.capped=false;
      if(b.bottom>floor-pad-2&&fullRect(item).bottom>floor-pad+2){   // taller than the screen: ring its first whole rows
        var limit=floor-pad-roomBelow(across,vw),end=limit-b.top>=150?rowsEnd(item.node,limit):null;
        if(end==null&&limit<floor-pad)end=rowsEnd(item.node,floor-pad);
        if(end!=null){y2=Math.min(y2,end+pad);item.capped=true}
      }
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
  // A region taller than the screen is ringed round its top part only, ending under its last whole row (a result, a
  // list entry), never through the middle of one. When the card has no room beside it, the ring stops short to leave
  // the card a place below it.
  function roomBelow(b,vw){
    if(!ui)return 0;
    var W=Math.min(ui.card.offsetWidth,320),gap=20,m=14;
    if(b.left-gap-W>=m||vw-b.right-gap-W>=m)return 0;              // it fits beside
    return ui.card.offsetHeight+gap+m;
  }
  function rowsEnd(node,limit){
    var top=node.getBoundingClientRect().top,end=null;
    for(var n=node,d=0;n&&d<6;d++){
      var cut=null;
      [].forEach.call(n.children,function(k){
        if(!visible(k))return;
        var r=k.getBoundingClientRect();
        if(r.bottom<=limit){if(r.bottom>top+40)end=Math.max(end||0,r.bottom)}
        else if(r.top<limit&&!cut)cut=k;
      });
      if(!cut||cut.getBoundingClientRect().height<limit-cut.getBoundingClientRect().top+160)break;   // a row the cut falls in: end above it
      n=cut;                                                        // a large block the cut falls in: look at its rows
    }
    return end;
  }
  // The card stays where it is for as long as that place is clear: on the screen, off the control bar, and covering
  // no lit region and not the pointer. Only when it must move does it pick a new place: beside the region it is
  // about (right, left, below or above; the side it was on last wins a tie), else the clearest corner. So between
  // clicks it moves only when it would otherwise hide something, and then glides there once.
  // While the page glides it waits, and moves (if it must) when the page is still. When no place at its usual width
  // is clear, a narrower card is tried before it settles for covering part of a lit region.
  var NEAR=360,HOLD=350;                                           // HOLD ms: how long something must sit under the card before it moves                                                    // px: a card further than this from its region moves closer
  var cardAt=null,SIDE_COST={right:0,left:120,below:260,above:420,corner:4000};   // beside reads best, then below, then above
  function placeCard(focus,holes,vw,floor){
    var c=ui.card;
    if(cardAt&&gliding)return;
    if(cardAt){
      var here=pickCard(focus,holes,vw,floor,cardAt.width);
      if(here.kept){ui.blocked=0;setCard(here.x,here.y,here.side,cardAt.width);return}
      // while the tour is busy clicking, something only passing under the card (the page settling after a click) does not
      // move it: it has to stay in the way a moment. A card that has just spoken moves at once.
      var now=Date.now();
      if(!ui.card.classList.contains('pending')||onPointer(cardAt))ui.blocked=now-HOLD;   // the pointer never waits under it
      else if(!ui.blocked)ui.blocked=now;
      if(now-ui.blocked<HOLD){ui.recheck=ui.blocked+HOLD;return}
      ui.blocked=0;
    }
    var wide=pickCard(focus,holes,vw,floor,'');
    if(wide.cover>0){
      var narrow=pickCard(focus,holes,vw,floor,'320px');
      if(narrow.cover===0){setCard(narrow.x,narrow.y,narrow.side,'320px');return}
      c.style.width='';
    }
    setCard(wide.x,wide.y,wide.side,'');
  }
  function pickCard(focus,holes,vw,floor,width){
    var c=ui.card;
    if(c.style.width!==width)c.style.width=width;
    var W=c.offsetWidth,H=c.offsetHeight,m=14,gap=20,keep=12,lit=holes.filter(Boolean);
    var blocks=lit.slice(),pt=pointerBox();
    if(pt)blocks.push(pt);
    keepClear().forEach(function(b){blocks.push(b)});                // the site's header and any bar pinned at the top
    function clampY(v){return Math.max(m,Math.min(floor-H-m,v))}
    function clampX(v){return Math.max(m,Math.min(vw-W-m,v))}
    function overlap(x,y,h,k){k=k||0;return Math.max(0,Math.min(x+W,h.x+h.w+k)-Math.max(x,h.x-k))*Math.max(0,Math.min(y+H,h.y+h.h+k)-Math.max(y,h.y-k))}
    function onScreen(x,y){return x>=m-1&&x+W<=vw-m+1&&y>=m-1&&y+H<=floor-m+1}
    function clear(x,y,k){return onScreen(x,y)&&!blocks.some(function(h){return overlap(x,y,h,k)>0})}
    function near(x,y){return !focus||c.classList.contains('pending')||Math.max(focus.x-(x+W),x-(focus.x+focus.w),focus.y-(y+H),y-(focus.y+focus.h))<=NEAR}   // still beside what it explains (while the tour clicks, it waits where it spoke)
    if(cardAt&&cardAt.width===width&&clear(cardAt.x,cardAt.y,0)&&near(cardAt.x,cardAt.y))return {x:cardAt.x,y:cardAt.y,side:cardAt.side,cover:0,kept:true};
    if(cardAt&&cardAt.width===width){                               // grown taller or wider at the edge of the screen: nudge it back on
      var nx=clampX(cardAt.x),ny=clampY(cardAt.y);
      if(clear(nx,ny,0)&&near(nx,ny))return {x:nx,y:ny,side:cardAt.side,cover:0,kept:true};
    }
    var spots=[];
    if(focus){
      var h=focus;
      spots.push([h.x+h.w+gap,clampY(h.y),'right'],[h.x-gap-W,clampY(h.y),'left'],[clampX(h.x),h.y+h.h+gap,'below'],[clampX(h.x),h.y-gap-H,'above'],
        [clampX(h.x+h.w-W),h.y+h.h+gap,'below'],[clampX(h.x+h.w-W),h.y-gap-H,'above'],
        [vw-W-m,clampY(h.y),'right'],[m,clampY(h.y),'left']);       // the same height, at the edge of the screen
    }
    var corners=[[vw-W-m,clampY(floor-H-m),'corner'],[m,clampY(floor-H-m),'corner'],[vw-W-m,m+70,'corner'],[m,m+70,'corner']];
    var best=null;
    spots.concat(corners).forEach(function(p,k){
      var x=p[0],y=p[1];
      if(!onScreen(x,y))return;                                     // off the screen or over the control bar
      var cover=0;blocks.forEach(function(b){cover+=overlap(x,y,b,b.soft?0:keep)*(b.soft?0.3:1)});
      var score=cover*10+SIDE_COST[p[2]]+(cardAt&&p[2]===cardAt.side?0:600)+(focus?Math.hypot(x+W/2-(focus.x+focus.w/2),y+H/2-(focus.y+focus.h/2)):0)
        +(cardAt?Math.hypot(x-cardAt.x,y-cardAt.y)*0.5:0);           // and the shorter move
      if(!best||score<best.score)best={x:x,y:y,side:p[2],score:score};
    });
    if(!best)best={x:clampX(vw-W-m),y:clampY(floor-H-m),side:'corner'};
    var cover=0;blocks.forEach(function(b){cover+=overlap(best.x,best.y,b,0)});
    return {x:Math.round(best.x),y:Math.round(best.y),side:best.side,cover:cover};
  }
  // Page furniture the card should not hide (soft: a lit region matters more): the site header while it shows, and a
  // bar pinned to the top of the screen (Research's search bar), across the whole width.
  function keepClear(){
    var out=[],vw=document.documentElement.clientWidth||window.innerWidth;
    [].forEach.call(document.querySelectorAll('.topbar'),function(n){
      var r=n.getBoundingClientRect();
      if(r.bottom>0&&r.height>0&&visible(n))out.push({x:0,y:r.top,w:vw,h:r.height,soft:1});
    });
    var pin=Math.max(pinnedTop(40),pinnedTop(vw/2),pinnedTop(vw-40));
    if(pin>0)out.push({x:0,y:0,w:vw,h:pin,soft:1});
    return out;
  }
  function onPointer(at){
    var p=pointerBox();
    return !!(p&&at)&&at.x<p.x+p.w&&at.x+ui.card.offsetWidth>p.x&&at.y<p.y+p.h&&at.y+ui.card.offsetHeight>p.y;
  }
  // Would the card, gliding from where it is to (x, y), pass over the pointer on the way?
  function glidesOverPointer(x,y){
    if(!cardAt||!pointerBox())return false;
    for(var k=0;k<=12;k++)if(onPointer({x:cardAt.x+(x-cardAt.x)*k/12,y:cardAt.y+(y-cardAt.y)*k/12}))return true;
    return false;
  }
  function setCard(x,y,side,width){
    var c=ui.card,to='translate('+x+'px,'+y+'px)';
    if(c.style.width!==width)c.style.width=width;
    if(!ui.shown){c.style.transition='none'}                        // the first time on a page it appears in place, without a slide
    if(ui.shown&&c.style.transform!==to&&!ui.fading&&glidesOverPointer(x,y)){   // it would slide across the pointer: fade over instead
      ui.fading=true;c.style.transition='opacity .14s ease';c.style.opacity='0';
      setTimeout(function(){
        if(!ui)return;
        c.style.transition='none';c.style.transform='translate('+cardAt.x+'px,'+cardAt.y+'px)';c.getBoundingClientRect();
        c.style.transition='opacity .2s ease';c.style.opacity='';
        setTimeout(function(){if(ui){c.style.transition='';ui.fading=false}},220);
      },150);
    }
    else if(!ui.fading)c.style.transform=to;
    if(!ui.shown){c.getBoundingClientRect();c.style.transition='';ui.shown=true}
    cardAt={x:x,y:y,side:side||(cardAt&&cardAt.side),width:width};
  }
  function follow(){
    var lastSig='';
    (function tick(){
      if(!ui)return;
      var sig=[window.innerWidth,window.innerHeight,ui.card.offsetHeight,ui.card.offsetWidth].concat(ui.items.map(function(item){
        var b=item.node&&document.contains(item.node)?item.node.getBoundingClientRect():null;
        return b?[b.left,b.top,b.width,b.height].join(','):'-';
      })).join('|');
      if(sig!==lastSig||(ui.recheck&&Date.now()>=ui.recheck)){lastSig=sig;ui.recheck=0;place()}
      watch=requestAnimationFrame(tick);
    })();
  }
  // The page's own element at a point, under the tour's card and control bar.
  function pageAt(x,y){
    var all=document.elementsFromPoint?document.elementsFromPoint(x,y):[document.elementFromPoint(x,y)];
    for(var k=0;k<all.length;k++)if(all[k]&&!(ui&&ui.root.contains(all[k])))return all[k];
    return null;
  }
  // How far down the screen a bar pinned at the top reaches (a page's sticky search bar or header), at this column.
  function pinnedTop(x){
    var low=0;
    [2,24,48].forEach(function(y){                                  // a bar pinned a little below the top edge counts too
      for(var n=pageAt(Math.max(2,Math.min(window.innerWidth-2,x)),y);n&&n!==document.body&&n!==document.documentElement;n=n.parentElement){
        var pos=getComputedStyle(n).position;
        if(pos==='sticky'||pos==='fixed'){var r=n.getBoundingClientRect();if(r.top<=50&&r.bottom<window.innerHeight*0.4)low=Math.max(low,r.bottom);break}
      }
    });
    return low;
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
    var hit=pageAt(x,y);
    return !!hit&&!node.contains(hit)&&!hit.contains(node);
  }
  function inView(node){
    var r=clipped(node);
    if(!r||covered(node))return false;
    var f=freeArea(node),shown=Math.min(r.bottom,f.bottom)-Math.max(r.top,f.top),full=node.getBoundingClientRect();
    if(r.top<f.top-2)return false;                                  // its top is cut off: the visitor would not see where it starts
    var box=scrollParent(node),pb=box?box.getBoundingClientRect():null;
    var room=Math.min(f.bottom,pb?pb.bottom:f.bottom)-Math.max(f.top,pb?pb.top:f.top);
    if(full.height<=room-8)                                         // it fits: show all of it, so the ring goes right round it
      return Math.abs(r.top-full.top)<2&&Math.abs(r.bottom-full.bottom)<2&&r.bottom<=f.bottom;
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
      var b=boxView(box),r=node.getBoundingClientRect();
      if(r.top<b.top||r.bottom>b.bottom){
        await glide(box,r.top-b.top-Math.max(12,(b.height-Math.min(r.height,b.height))/3),token);
      }
      if(inView(node))return;
    }
    var f=freeArea(node),m=node.getBoundingClientRect(),room=f.bottom-f.top;
    await glide(null,m.height<=room?m.top-(f.top+Math.min(90,(room-m.height)/2)):m.top-f.top-8,token);
    for(var t=0;t<3&&token===run&&underBar(node);t++)await clearSticky(node,token);
  }
  // For something that opens below itself (a citation card): bring it into the upper part of its panel first.
  async function lift(node,token){
    var box=scrollParent(node),r=node.getBoundingClientRect(),top=box?Math.max(0,box.getBoundingClientRect().top):0,h=box?box.getBoundingClientRect().bottom-top:dockTop();
    if(r.top-top>h*0.4)await glide(box,r.top-top-h*0.2,token);
  }
  // Every lit region should be seen whole, so its ring goes right round it. After the main region is in view, move the
  // page (or the panel a region scrolls in) only as far as needed to show the rest too, without losing the main one's
  // top; a page introduced from its top moves down only far enough to show its region whole.
  async function showWhole(items,focus,token,keepTop){
    var main=items[focus];
    if(!main||!main.node||!visible(main.node))return;
    items.forEach(function(it){if(it.node&&visible(it.node))unclip(it.node)});
    for(var k=0;k<items.length;k++){                               // a region in a panel that scrolls: bring it in there
      var it=items[k];
      if(!it.node||!visible(it.node))continue;
      var box=scrollParent(it.node);
      if(!box||(main.node!==it.node&&box.contains(main.node)))continue;
      var b=boxView(box),r=fullRect(it);
      if(it===main)items.forEach(function(o){                       // the others lit in the same panel too, when they all fit
        if(o===main||!o.node||!visible(o.node)||scrollParent(o.node)!==box)return;
        var w=unite(r,fullRect(o));
        if(w.height<=b.height-16)r=w;
      });
      if(r.height>b.height-16)continue;
      if(r.top<b.top+8)await glide(box,r.top-b.top-8,token);
      else if(r.bottom>b.bottom-8)await glide(box,r.bottom-b.bottom+8,token);
      if(token!==run)return;
    }
    var f=freeArea(main.node),u=null;
    items.forEach(function(it){if(it.node&&visible(it.node)&&!scrollParent(it.node)||it===main){var r=fullRect(it);u=u?unite(u,r):r}});
    if(!u)return;
    var room=f.bottom-f.top,mr=fullRect(main),all=u;
    if(u.height>room-8)u=mr;                                       // not all of it fits: the main region whole, at least
    if(u.height>room-8){                                           // not even that (a long list): start it all at the top of the screen
      var lift=all.top-(f.top+8);
      if(!keepTop&&lift>2&&!scrollParent(main.node))await glide(null,lift,token);
      for(var t=0;t<3&&token===run&&underBar(main.node);t++)await clearSticky(main.node,token);
      return;
    }
    var d=0;
    if(u.bottom>f.bottom-6)d=Math.min(u.bottom-f.bottom+10,u.top-f.top);
    else if(u.top<f.top+2)d=u.top-f.top-10;
    if(Math.abs(d)>2)await glide(null,d,token);
    for(var t=0;t<3&&token===run&&underBar(main.node);t++)await clearSticky(main.node,token);   // scrolling can pin a bar over its top
  }
  // A box that clips without a scroll bar (the reader's frame) can still be left scrolled by a jump inside it, which
  // hides the top or bottom of a region for good: put it back.
  function unclip(node){
    for(var p=node.parentElement;p&&p!==document.body&&p!==document.documentElement;p=p.parentElement){
      var o=getComputedStyle(p).overflowY;
      if((o!=='hidden'&&o!=='clip')||!p.scrollTop)continue;
      var r=node.getBoundingClientRect(),b=p.getBoundingClientRect();
      if(r.top<b.top-1||r.bottom>b.bottom+1)p.scrollTop=0;
    }
  }
  // A wide region leaves the card no place beside it. If the region and the card fit one above the other, move the page
  // so the region sits at the top of the free area and the card can speak below it, instead of covering part of it.
  async function makeRoom(s,main,token){
    if(!ui||!main||!main.node||!visible(main.node)||scrollParent(main.node))return;
    ui.title.textContent=s.title||'';ui.text.textContent=s.text||'';ui.extra.textContent='';   // the card as it will read
    var W=ui.card.offsetWidth,H=ui.card.offsetHeight+24,vw=document.documentElement.clientWidth||window.innerWidth;   // a line to spare
    var r=fullRect(main),f=freeArea(main.node),gap=20,m=14;
    if(r.left-gap-W>=m||vw-r.right-gap-W>=m)return;                 // there is room at a side
    if(r.top-gap-H>=Math.max(f.top,m)||r.bottom+gap+H<=f.bottom)return;   // or above or below as it is
    if(r.height+gap+H>f.bottom-f.top-8)return;                      // the two cannot fit one above the other
    var d=r.top-(f.top+8);
    if(d>2)await glide(null,d,token);
  }
  async function steady(node,token){
    var last=-1,still=0;
    for(var k=0;k<40&&still<5;k++){
      var h=Math.round(node.getBoundingClientRect().height);
      still=h===last?still+1:0;last=h;
      if(still<5)await sleep(80);
      if(token!==run)return;
    }
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
  // How much of the top of an element a bar pinned to the screen (a sticky header) hides: 0 when none does.
  function stickyAt(main){                                         // the bar pinned over the start of an element, if any
    for(var a=main;a&&a!==document.body;a=a.parentElement)if(getComputedStyle(a).position==='fixed')return null;   // a tooltip or dialog floats above the page
    var m=main.getBoundingClientRect(),x=Math.min(window.innerWidth-2,Math.max(2,m.left+Math.min(40,m.width/2))),y=Math.max(1,m.top+3);
    var hit=pageAt(x,y);
    if(!hit||main.contains(hit)||hit.contains(main))return null;
    var bar=hit;
    while(bar&&bar!==document.body){var pos=getComputedStyle(bar).position;if(pos==='sticky'||pos==='fixed')break;bar=bar.parentElement}
    return bar&&bar!==document.body?bar:null;
  }
  function underBar(main){
    var bar=stickyAt(main),m=main.getBoundingClientRect();
    if(!bar)return 0;
    var under=bar.getBoundingClientRect().bottom-m.top;
    return under>6?under:0;                                         // a tab strip's few pixels of overlap are its design
  }
  async function clearSticky(main,token){
    var under=underBar(main);
    if(!under)return;
    var need=under+10,box=scrollParent(main);
    if(box&&box.scrollTop>0&&box.contains(stickyAt(main))){await glide(box,-Math.min(need,box.scrollTop),token);return}   // a header pinned inside its panel: scroll the panel back
    await glide(box&&box.scrollTop>=need?box:null,-need,token);
  }
  // The part of a scrolling panel its content shows in: below a toolbar pinned at the panel's top.
  function boxView(box,inside){                                     // inside: an element in that toolbar is not hidden by it
    var b=box.getBoundingClientRect(),top=b.top;
    [0.25,0.5,0.75].forEach(function(f){
      for(var n=pageAt(b.left+b.width*f,b.top+4);n&&n!==box&&box.contains(n);n=n.parentElement){
        var pos=getComputedStyle(n).position;
        if(pos==='sticky'||pos==='fixed'){var r=n.getBoundingClientRect();if(r.bottom<b.top+b.height*0.4&&!(inside&&n.contains(inside)))top=Math.max(top,r.bottom);break}
      }
    });
    return {top:top,bottom:b.bottom,left:b.left,right:b.right,height:b.bottom-top,width:b.width};
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
    var from={x:pointer.x,y:pointer.y};
    pointer.x=x;pointer.y=y;c.classList.add('on');place();          // the card makes way for where the pointer is going first
    pointer.x=from.x;pointer.y=from.y;
    var dist=Math.hypot(x-pointer.x,y-pointer.y);
    var ms=reduce||dist<4?0:Math.round(Math.min(1200,Math.max(520,dist*1.36)));   // already there (a button clicked again): no wait
    c.style.transitionDuration=ms+'ms, .2s';
    c.style.transform='translate('+x+'px,'+y+'px)';
    pointer.x=x;pointer.y=y;
    await sleep(reduce||!ms?0:ms+250);
  }
  async function press(){
    if(!ui)return;
    ui.cursor.classList.remove('press');ui.cursor.getBoundingClientRect();ui.cursor.classList.add('press');
    await sleep(reduce?0:420);
  }
  function hidePointer(){if(ui){ui.cursor.classList.remove('on');pointer.x=null}}
  // Where the pointer is (with a margin), so the card never sits on it.
  function pointerBox(){return ui&&pointer.x!=null&&ui.cursor.classList.contains('on')?{x:pointer.x-14,y:pointer.y-13,w:46,h:46}:null}

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
    // the pointer has done its job once the card speaks: it goes, so it never sits on the card (a hover result keeps it)
    if(!pending&&!(mode==='show'&&(s.hover||(s.act||[]).some(function(a){return a.do==='hover'}))))hidePointer();
    u.count.textContent='Step '+(i+1)+' of '+STEPS.length;
    clearTimeout(u.slow);
    if(pending)u.slow=setTimeout(function(){if(ui&&ui.card.classList.contains('pending'))ui.count.textContent='Loading…'},900);   // only a slow step says so
    u.fill.style.width=Math.round(((i+1)/STEPS.length)*100)+'%';
    u.back.disabled=i===0;
    u.next.textContent=i===STEPS.length-1&&mode==='show'?'Done':'Next';
    u.next.disabled=pending;
    // in the last section there is nothing to skip to: the button fades out but keeps its room, so Next does not shift
    u.skip.style.visibility=sectionOf(i)===sectionOf(STEPS.length-1)||!STEPS.slice(i+1).some(function(x){return x.section!==s.section})?'hidden':'';
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
    if(url==null)return skipOver(i,token,'no-case');                         // the example decision is not in this library
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
      if(!done&&(s.before[k].do==='waitFor'||s.before[k].do==='type'))return skipOver(i,token,'before');
    }
    // 3. a step that acts first says what it will do, lighting the place
    if(s.act&&s.act.length&&state.phase!=='back'&&state.phase!=='show'){
      var first=s.act.filter(function(a){return a.selector&&a.do!=='waitFor'&&!(a.unless&&findVisible(a.unless))&&!(a.when&&!findVisible(a.when))})[0];
      var spotSel=s.sayTarget||(first&&first.selector);
      var node=spotSel?(await waitFor(spotSel,first&&first.timeout||8,token)):null;
      if(token!==run)return;
      if(!node&&!s.sayTarget&&first){if(s.optional)return skipOver(i,token,'say-target')}
      if(node)await bringIntoView(node,token);
      if(token!==run)return;
      state.phase='say';
      render(i,node?[{node:node,sel:spotSel}]:[],'say');ready(i,'say');
      return;
    }
    if(s.act)for(var q=0;q<s.act.length;q++){                      // Back or a refresh: the same result, without the show
      var ok=await doAction(s.act[q],token,false);
      if(token!==run)return;
      if(!ok&&(s.act[q].do==='waitFor'||s.act[q].do==='type'))return skipOver(i,token,'act-quiet');
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
      if(!ok&&(s.act[k].do==='waitFor'||s.act[k].do==='type'||s.act[k].required))return skipOver(i,token,'act');
    }
    await settleScroll(token);
    return result(i,token);
  }
  // Next on "lead": the pointer goes to the tab or link and presses it.
  async function navigate(i,url,token,live){
    var s=STEPS[i];
    state.nav=(state.nav&&state.nav.i===i?state.nav:{i:i,n:0});
    state.nav.n++;
    if(state.nav.n>2){state.nav=null;return skipOver(i,token,'page')}     // do not loop if the page will not open
    if(live||(state.phase!=='show'&&state.phase!=='back'))state.phase='nav';   // Back or a refresh arrives showing the result
    save(state);
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
    if(s.target&&!target)return skipOver(i,token,'target');                  // missing element or data: skip, never break
    var items=itemsFor(s,target);
    if(s.settle)await sleep(reduce?0:s.settle);
    if(token!==run)return;
    var main=(items[s.focus||0]||{}).node||target;
    if(main)await steady(main,token);                               // a list that is still filling in: wait until it stops growing
    if(token!==run)return;
    if(!s.noScroll&&!s.top)await bringIntoView(main,token);
    if(!s.noScroll)await showWhole(items,s.focus||0,token,s.top);         // then the rest of what is lit, when it all fits
    if(!s.noScroll)await makeRoom(s,items[s.focus||0],token);       // and room for the card beside or below it
    if(token!==run)return;
    if(s.optional&&main&&!onScreen(main))return skipOver(i,token,'off-screen');  // there but out of sight: skip it
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
  function skipOver(i,token,why){
    if(token!==run)return;
    (window.__ilitTourSkips=window.__ilitTourSkips||[]).push(STEPS[i].id+': '+(why||'?'));
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
  // The tour's fixed demo requests ("cache" in the steps file) are also kept by the server for a few hours
  // (backend/tour_cache.py), so asking for them early makes every later step quick. A few at a time, in step order.
  var cacheWarmed=false;
  function warmCache(){
    if(cacheWarmed)return;cacheWarmed=true;
    var queue=(DATA.cache||[]).filter(function(u){return !/\{(\w+)\}/.test(u)||u.match(/\{(\w+)\}/g).every(function(m){return caseIds[m.slice(1,-1)]!=null})}).map(fillIds);
    function next(){var u=queue.shift();if(u)fetch(u,{credentials:'same-origin'}).catch(function(){}).then(next)}
    for(var k=0;k<3;k++)next();
  }
  function warm(){
    warmCache();
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
    caseIds={};pendingLookups={};cardAt=null;
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
  // Where everything is on screen right now, for the tour check (scripts/check_site_tour.py): each lit element's full
  // box and the part of it its panels let show, each ring, the card, the control bar and the pointer.
  function geometry(){
    if(!ui)return null;
    function box(b){return b?{x:round(b.left),y:round(b.top),w:round(b.right-b.left),h:round(b.bottom-b.top)}:null}
    var rings=[].map.call(ui.rings.children,function(r){return r.style.display==='none'?null:box(r.getBoundingClientRect())});
    return {vw:document.documentElement.clientWidth||window.innerWidth,vh:window.innerHeight,focus:ui.focus,
      card:box(ui.card.getBoundingClientRect()),dock:box(ui.dock.getBoundingClientRect()),
      cursor:ui.cursor.classList.contains('on')?box(ui.cursor.getBoundingClientRect()):null,
      keep:keepClear().map(function(b){return {x:round(b.x),y:round(b.y),w:round(b.w),h:round(b.h)}}),
      items:ui.items.map(function(item,k){
        var n=item.node&&document.contains(item.node)&&visible(item.node)?item.node:null;
        var room=null;
        if(n){                                                      // the height it could be seen in: the screen, or its panel
          var f=freeArea(n),sp=scrollParent(n),pb=sp?boxView(sp):null,top=Math.max(f.top,pb?pb.top:f.top);
          room={y:round(top),h:round(Math.min(f.bottom,pb?pb.bottom:f.bottom)-top)};
        }
        return {full:n?box(fullRect(item)):null,seen:n?box(liveRect(item)):null,ring:rings[k]||null,room:room,capped:!!item.capped,underBar:n?round(underBar(shownBox(n))):0};
      })};
  }
  window.ilitTour={start:start,exit:exit,steps:STEPS,resolveUrl:resolveUrl,resolveCase:resolveCase,geometry:geometry,times:function(){return window.__ilitTourTimes}};

  function boot(){
    var wants=new URLSearchParams(location.search).get('tour')==='1';
    if(wants&&!(state&&state.active)){start();return}
    if(state&&state.active){show(Math.min(state.i||0,STEPS.length-1),state.dir||direction);return}
    setTimeout(prewarm,2500);                                       // the page with the tour button: get the demo data ready
  }
  async function prewarm(){
    if(!document.querySelector('[data-ilit-tour-start]')||(state&&state.active))return;
    try{if(sessionStorage.getItem('ilit.tour.warm'))return;sessionStorage.setItem('ilit.tour.warm','1')}catch(e){return}
    await Promise.all(Object.keys(CASES).map(resolveCase));
    warmCache();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,30)});
  else setTimeout(boot,30);
})();
