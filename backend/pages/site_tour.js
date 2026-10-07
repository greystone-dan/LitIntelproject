/* iLit site tour: a scripted walk through the real site. The visitor only presses Next (or Back, Skip section, Exit);
   the tour opens the pages, types and clicks for them with a visible pointer, and the visitor can scroll and look
   around the page at any time before pressing Next.
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
    if(input.value===text){                                        // already typed (a refresh or Back): do not type it again,
      input.dispatchEvent(new Event('input',{bubbles:true}));        // but let the page show its matches again
      closeSuggestions();return;
    }
    input.focus({preventScroll:true});
    input.value='';
    input.dispatchEvent(new Event('input',{bubbles:true}));
    if(reduce){input.value=text;input.dispatchEvent(new Event('input',{bubbles:true}));return}
    for(var i=1;i<=text.length;i++){
      if(token!==run)return;
      input.value=text.slice(0,i);
      input.dispatchEvent(new Event('input',{bubbles:true}));
      await sleep(55);
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
    if(typeof sel!=='string')return findVisible(sel);                // {css,text,pin} or a list of alternatives
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
    if((a.do==='type'||a.show||a.do==='drop')&&ui&&!(a.do==='type'&&node.value===a.text)){   // the visitor watches the pointer go there
      ui.items=[{node:node,sel:null}];
      await bringIntoView(node,token);place();
      await pointAt(node,token);
      if(token!==run)return false;
      if(a.do!=='type')await press();
    }
    switch(a.do){
      case 'type':await typeInto(node,a.text||'',token);break;
      case 'fill':await fillInto(node,(DATA.texts||{})[a.sample]||'',token);break;
      case 'check':if(!node.checked)node.click();break;
      case 'uncheck':if(node.checked)node.click();break;
      case 'open':if(!node.open)node.open=true;break;
      case 'click':node.click();break;
      case 'submit':if(node.requestSubmit)node.requestSubmit();else node.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));break;
      case 'scroll':node.scrollIntoView({block:'center',behavior:reduce?'auto':'smooth'});break;
      case 'drop':if(!(await dropFile(node,a)))return false;break;
      default:return false;
    }
    await sleep(60);
    return true;
  }

  // Drop one of the tour's own fictional sample files on a drop zone, as a person dragging it from their desktop would.
  async function dropFile(zone,a){
    try{
      var r=await fetch(a.file,{credentials:'same-origin'});
      if(!r.ok)return false;
      var blob=await r.blob(),file=new File([blob],a.name||a.file.split('/').pop(),{type:blob.type||'application/octet-stream'});
      var dt=new DataTransfer();dt.items.add(file);
      zone.dispatchEvent(new DragEvent('dragenter',{bubbles:true,cancelable:true,dataTransfer:dt}));
      await sleep(reduce?0:350);
      zone.dispatchEvent(new DragEvent('drop',{bubbles:true,cancelable:true,dataTransfer:dt}));
      return true;
    }catch(e){return false}
  }

  /* ---------- the overlay: a lightly shaded page with a clear border round what each step is about, a pointer, and the card.
     Nothing blocks the page: the visitor can scroll and look around before pressing Next. ---------- */
  function build(){
    if(ui)return ui;
    var root=el('div','ilit-tour');root.setAttribute('data-ilit-tour','');
    var svg=document.createElementNS(SVGNS,'svg');svg.setAttribute('class','ilit-tour-dim');svg.setAttribute('aria-hidden','true');
    var path=document.createElementNS(SVGNS,'path');path.setAttribute('fill-rule','evenodd');svg.appendChild(path);root.appendChild(svg);
    var rings=el('div','ilit-tour-rings');root.appendChild(rings);
    var cursor=el('div','ilit-tour-cursor');cursor.setAttribute('aria-hidden','true');
    cursor.innerHTML='<svg viewBox="0 0 24 24" width="26" height="26"><path d="M4 2l15 11.2-6.6 1.1 3.9 7.3-2.9 1.5-3.9-7.4L4 20.7z" fill="#202522" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    root.appendChild(cursor);
    var card=el('div','ilit-tour-card');
    card.setAttribute('role','dialog');card.setAttribute('aria-label','Site tour');card.setAttribute('tabindex','-1');
    var head=el('div','ilit-tour-head');
    var kicker=el('span','ilit-tour-kicker');
    var exitX=el('button','ilit-tour-x','×');exitX.type='button';exitX.setAttribute('aria-label','Exit the tour');
    head.appendChild(kicker);head.appendChild(exitX);
    var title=el('h2','ilit-tour-title');
    var text=el('p','ilit-tour-text');
    var hint=el('p','ilit-tour-note');
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
    [head,title,text,hint,extra,bar,foot].forEach(function(n){card.appendChild(n)});
    root.appendChild(card);
    var live=el('div','ilit-tour-live');live.setAttribute('aria-live','polite');root.appendChild(live);
    document.body.appendChild(root);
    exitX.onclick=exit;
    back.onclick=function(){go(-1)};
    next.onclick=function(){go(1)};
    skip.onclick=skipSection;
    ui={root:root,path:path,rings:rings,cursor:cursor,card:card,kicker:kicker,title:title,text:text,hint:hint,extra:extra,fill:fill,count:count,back:back,skip:skip,next:next,live:live,items:[]};
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
  // The free part of the screen: above the bottom sheet on a phone, left of the card on a desktop when they overlap.
  // How far down the screen a bar pinned at the top reaches (a page's sticky search bar or header), at this column.
  function pinnedTop(x){
    var hit=document.elementFromPoint(Math.max(2,Math.min(window.innerWidth-2,x)),2);
    for(var n=hit;n&&n!==document.body&&n!==document.documentElement;n=n.parentElement){
      var pos=getComputedStyle(n).position;
      if(pos==='sticky'||pos==='fixed'){var b=n.getBoundingClientRect().bottom;return b<window.innerHeight*0.4?b:0}
    }
    return 0;
  }
  function freeArea(node){
    var narrow=window.innerWidth<640,vh=window.innerHeight,top=12,bottom=vh-12;
    if(node)top=Math.max(top,pinnedTop(node.getBoundingClientRect().left+20)+10);
    if(ui&&narrow)bottom=vh-ui.card.offsetHeight-12;
    else if(ui&&node){
      var c=ui.card.getBoundingClientRect(),r=node.getBoundingClientRect();
      if(r.right>c.left-8&&r.height<c.top-24)bottom=c.top-12;     // in the card's column: keep it above the card
    }
    return {top:top,bottom:bottom};
  }
  function onScreen(node){
    var r=clipped(node),vw=document.documentElement.clientWidth||window.innerWidth;
    return !!r&&r.right>8&&r.left<vw-8&&r.bottom>8&&r.top<window.innerHeight-8;
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
    return r.bottom<=f.bottom||shown>=Math.min(350,(r.bottom-r.top)*0.6);   // mostly on screen is enough: do not move the page
  }
  // Scroll only when the region is not already on screen, smoothly, and only as far as needed: the page should not jump.
  async function bringIntoView(node,token){
    if(!node||!visible(node)||inView(node))return;
    var full=node.getBoundingClientRect(),cut=clipped(node);
    if(!cut||cut.right-cut.left<Math.min(full.width,window.innerWidth)*0.8){   // hidden sideways in a row that scrolls across
      try{node.scrollIntoView({block:'nearest',inline:'nearest',behavior:reduce?'auto':'smooth'})}catch(e){}
      await settleScroll(token);
      if(inView(node))return;
    }
    var box=scrollParent(node);
    if(clipped(node)&&covered(node)){                               // on screen but under a pinned bar: move it out from under, no more
      var before=node.getBoundingClientRect().top;clearSticky(node);await settleScroll(token);
      if(node.getBoundingClientRect().top!==before&&inView(node))return;
    }
    if(box){                                                        // inside a scrolling panel: scroll the panel first
      var b=box.getBoundingClientRect(),r=node.getBoundingClientRect();
      if(r.top<b.top||r.bottom>b.bottom){
        try{box.scrollBy({top:r.top-b.top-Math.max(12,(b.height-Math.min(r.height,b.height))/3),behavior:reduce?'auto':'smooth'})}catch(e){}
        await settleScroll(token);
      }
      if(inView(node))return;
    }
    var f=freeArea(node),m=node.getBoundingClientRect(),room=f.bottom-f.top;
    var delta=m.height<=room?m.top-(f.top+Math.min(90,(room-m.height)/2)):m.top-f.top-8;
    try{window.scrollBy({top:delta,behavior:reduce?'auto':'smooth'})}catch(e){window.scrollBy(0,delta)}
    await settleScroll(token);
    if(covered(node)){clearSticky(node);await settleScroll(token)}
  }
  async function settleScroll(token){                               // wait until a smooth scroll has stopped moving
    if(reduce)return;
    var last=null,still=0;
    for(var k=0;k<40&&still<3;k++){
      await sleep(40);
      if(token!==run)return;
      var sig=window.scrollY+','+document.documentElement.scrollTop;
      [].forEach.call(document.querySelectorAll('.v6-body,.fmt-decision,#decisionBody,.reader-scroll'),function(n){sig+=','+n.scrollTop});
      still=sig===last?still+1:0;last=sig;
    }
  }
  /* ---------- the pointer ---------- */
  var pointer={x:null,y:null};
  async function pointAt(node,token){
    if(!ui||!node)return;
    var c=ui.cursor,r=clipped(node)||node.getBoundingClientRect();
    var x=Math.round(r.left+Math.min(r.width/2,Math.max(16,r.width*0.3))),y=Math.round(r.top+Math.min(r.height/2,22));
    if(pointer.x==null){                                            // first appearance: start from the card
      var cr=ui.card.getBoundingClientRect();
      c.style.transition='none';c.style.transform='translate('+Math.round(cr.left+30)+'px,'+Math.round(cr.top+20)+'px)';
      c.getBoundingClientRect();c.style.transition='';
    }
    c.classList.add('on');
    var dist=pointer.x==null?400:Math.hypot(x-pointer.x,y-pointer.y);
    var ms=reduce?0:Math.round(Math.min(900,Math.max(380,dist*1.1)));
    c.style.transitionDuration=ms+'ms';
    c.style.transform='translate('+x+'px,'+y+'px)';
    pointer.x=x;pointer.y=y;
    await sleep(ms+120);
  }
  async function press(){
    if(!ui)return;
    ui.cursor.classList.remove('press');ui.cursor.getBoundingClientRect();ui.cursor.classList.add('press');
    await sleep(reduce?0:260);
  }
  function hidePointer(){if(ui){ui.cursor.classList.remove('on');pointer.x=null}}
  // A bar that stays pinned at the top of the page (a toolbar) can sit over the region: move the region below it.
  function clearSticky(main){
    var m=main.getBoundingClientRect(),x=Math.min(window.innerWidth-2,Math.max(2,m.left+Math.min(40,m.width/2))),y=Math.max(1,m.top+3);
    var hit=document.elementFromPoint(x,y);
    if(!hit||main.contains(hit)||hit.contains(main))return;
    var bar=hit;
    while(bar&&bar!==document.body){var pos=getComputedStyle(bar).position;if(pos==='sticky'||pos==='fixed')break;bar=bar.parentElement}
    if(!bar||bar===document.body)return;
    var need=bar.getBoundingClientRect().bottom+10-m.top;
    if(need<=0)return;
    var box=scrollParent(main),how=reduce?'auto':'smooth';
    try{if(box&&box.scrollTop>=need)box.scrollBy({top:-need,behavior:how});else window.scrollBy({top:-need,behavior:how})}catch(e){}
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
  var EXPLORE_HINT='Scroll and look around as much as you like, then press Next.';
  function render(i,items,pending,lead){
    var s=STEPS[i],u=build(),sp=sectionPlace(i);
    document.documentElement.classList.add('ilit-tour-on');
    if(u.items!==items){u.root.classList.add('moving');clearTimeout(u.moving);u.moving=setTimeout(function(){if(ui)ui.root.classList.remove('moving')},420)}
    u.items=items||[];
    u.root.classList.toggle('explore',!!s.explore&&!pending);
    u.kicker.textContent=(s.section||'Tour')+(sp.of>1?' · '+sp.n+' of '+sp.of:'');
    u.title.textContent=lead?lead:(s.title||'');
    u.text.textContent=lead?'':(s.text||'');
    u.hint.textContent=!lead&&!pending&&s.explore?EXPLORE_HINT:'';
    u.extra.textContent='';
    u.count.textContent='Step '+(i+1)+' of '+STEPS.length;
    clearTimeout(u.slow);
    if(pending)u.slow=setTimeout(function(){if(ui&&ui.card.classList.contains('pending'))ui.count.textContent='Loading…'},600);   // only a slow step says so
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
      var via=s.via&&direction>0&&state.nav.n===1?findVisible(fillIds(s.via)):null;
      // "OK, let's move on": the pointer goes where a person would click (via clicks it; point only shows it, then the
      // tour opens the page itself, for links that would open somewhere the tour cannot follow, such as a frame)
      var spot=via||(s.point&&direction>0&&state.nav.n===1?findVisible(fillIds(s.point)):null);
      if(direction>0&&state.nav.n===1&&(s.lead||spot)){
        render(i,spot?[{node:spot,sel:null}]:[],true,s.lead||'Moving on');
        if(spot){
          await bringIntoView(spot,token);place();
          await pointAt(spot,token);if(token!==run)return;
          await press();if(token!==run)return;
        }else await sleep(reduce?0:900);
      }
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
    if(s.top&&direction>0){                                         // a page is introduced from its top before its parts
      if(window.scrollY>4){try{window.scrollTo({top:0,behavior:reduce?'auto':'smooth'})}catch(e){window.scrollTo(0,0)}await settleScroll(token)}
      if(token!==run)return;
    }
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
    if(!s.noScroll&&!s.top)await bringIntoView((items[s.focus||0]||{}).node||target,token);
    if(token!==run)return;
    var main=(items[s.focus||0]||{}).node||target;
    if(s.optional&&main&&!onScreen(main))return skipOver(i,token);  // there but out of sight in this layout (a phone): skip it
    render(i,items,false);
    place();
    if(s.hover&&target){await pointAt(target,token);if(token!==run)return;hoverOn(target)}
    else if(!s.keepPointer)hidePointer();
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
    state={i:0,active:true,t0:Date.now()};save(state);
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
