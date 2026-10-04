// Installed after all reader/navigation wrappers. No backend evidence is changed.
(() => {
  const seenThisSession = new Set();
  const key = kind => `ilit.tour.v1.${kind}`;
  function seen(kind) {
    if (seenThisSession.has(kind)) return true;
    try { return localStorage.getItem(key(kind)) === 'done'; } catch (_) { return false; }
  }
  function remember(kind) {
    seenThisSession.add(kind);
    try { localStorage.setItem(key(kind), 'done'); } catch (_) { /* session fallback */ }
  }
  const steps = {
    search: [
      ['#searchQuery', 'Find a case', 'Enter a case name or citation. Suggestions help you find stored decisions.'],
      ['#quickFilters', 'Narrow the search', 'Filter by court or outcome. More filters includes year, judge, and full decision text.'],
      ['#searchResults', 'Read a result', 'Run Search, then open a result and check its identity, source, and available text.'],
      ['.search-actions', 'Export results', 'Download CSV, or Download Word after a successful search with results. Verify the records before using them.']
    ],
    reader: [
      ['#decisionTitle', 'Check the decision', 'Check the title, citation, court, date, and source before relying on this decision.'],
      ['#readerViewToggle', 'Read the text', 'Read the available decision text in full, or choose chunk breakdown to read it in smaller sections.'],
      ['#decisionBody', 'Follow evidence', 'Case citations, statutes, and tags are separate signals. Read linked authorities and verify the proposition yourself.'],
      ['#decisionTarget', 'Inspect case information', 'Info shows case facts; Advanced shows technical details. Evidence tabs show citations, tags, acts and precedents.'],
      ['.return-to-results', 'Return to results', 'Go back to your search. A local match is not a legal citator opinion or a guarantee of complete coverage.']
    ]
  };
  const dialog = document.createElement('dialog');
  dialog.id = 'researchTour';
  dialog.setAttribute('aria-labelledby', 'tourTitle');
  dialog.setAttribute('aria-describedby', 'tourText tourProgress');
  dialog.innerHTML = '<h2 id="tourTitle"></h2><p id="tourProgress" aria-live="polite"></p><p id="tourText"></p><div class="tour-actions"><button type="button" id="tourBack">Back</button><button type="button" id="tourNext">Next</button><button type="button" id="tourDismiss">Dismiss tour</button></div>';
  document.body.append(dialog);
  let kind = null, index = 0, previousFocus = null, highlighted = null;
  const visible = selector => {
    const element = document.querySelector(selector);
    return element && !element.closest('[hidden]') && element.getClientRects().length > 0;
  };
  function available(name) {
    return name === 'search'
      ? visible('#searchPanel') && !visible('#caseReaderPanel')
      : visible('#caseReaderPanel') && !!readerState.payload?.readerData && !!readerState.caseId;
  }
  function unhighlight() {
    highlighted?.classList.remove('tour-highlight');
    highlighted = null;
  }
  function finish(mark = true, restore = true) {
    if (!kind) return;
    if (mark) remember(kind);
    kind = null;
    unhighlight();
    dialog.close();
    if (restore) {
      const target = previousFocus?.isConnected && visibleElement(previousFocus)
        ? previousFocus : document.querySelector(visible('#caseReaderPanel') ? '#readerTourButton' : '#searchTourButton');
      target?.focus();
    }
  }
  function visibleElement(element) {
    return !element.closest('[hidden]') && element.getClientRects().length > 0;
  }
  function paint() {
    if (!available(kind)) { finish(false); return; }
    unhighlight();
    const [selector, title, text] = steps[kind][index];
    document.getElementById('tourTitle').textContent = title;
    document.getElementById('tourText').textContent = text;
    document.getElementById('tourProgress').textContent = `Step ${index + 1} of ${steps[kind].length}`;
    highlighted = document.querySelector(selector);
    if (highlighted && visibleElement(highlighted)) {
      highlighted.classList.add('tour-highlight');
      highlighted.scrollIntoView({block: 'center'});
    }
    document.getElementById('tourBack').disabled = index === 0;
    document.getElementById('tourNext').textContent = index === steps[kind].length - 1 ? 'Finish tour' : 'Next';
    document.getElementById('tourNext').focus();
  }
  function start(name, force = false) {
    if (kind === name || !available(name) || (!force && seen(name))) return;
    finish(false, false);
    previousFocus = document.activeElement;
    kind = name;
    index = 0;
    dialog.showModal(); // Native modal makes the surrounding page inert.
    paint();
  }
  document.getElementById('tourNext').onclick = () => {
    if (index === steps[kind].length - 1) finish();
    else { index++; paint(); }
  };
  document.getElementById('tourBack').onclick = () => { if (index > 0) { index--; paint(); } };
  document.getElementById('tourDismiss').onclick = () => finish();
  dialog.addEventListener('cancel', event => { event.preventDefault(); finish(); });
  dialog.addEventListener('keydown', event => {
    if (event.key === 'Escape') { event.preventDefault(); finish(); return; }
    if (event.key !== 'Tab') return;
    const controls = [...dialog.querySelectorAll('button')].filter(button => !button.disabled);
    const first = controls[0], last = controls[controls.length - 1];
    if (event.shiftKey && (document.activeElement === first || !dialog.contains(document.activeElement))) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && (document.activeElement === last || !dialog.contains(document.activeElement))) {
      event.preventDefault(); first.focus();
    }
  });
  dialog.addEventListener('focusout', () => {
    queueMicrotask(() => {
      if (kind && !dialog.contains(document.activeElement)) document.getElementById('tourNext').focus();
    });
  });
  function addButton(parent, id, name) {
    const button = document.createElement('button');
    button.id = id; button.type = 'button'; button.textContent = 'Take the tour';
    button.onclick = () => start(name, true);
    parent?.append(button);
  }
  addButton(document.querySelector('#caseSearch .search-actions'), 'searchTourButton', 'search');
  addButton(document.querySelector('#caseReaderPanel .reader-toolbar'), 'readerTourButton', 'reader');
  // Reader success occurs inside the original loader, including an initial deep link.
  const previousSetReaderMode = setReaderMode;
  setReaderMode = function(...args) {
    const result = previousSetReaderMode(...args);
    if (available('reader') && kind !== 'reader') start('reader');
    return result;
  };
  const previousOpen = openDecision;
  let tourLoad = 0;
  openDecision = async function(caseId) {
    const load = ++tourLoad;
    finish(false, false);
    await previousOpen(caseId);
    if (load === tourLoad && readerState.caseId === Number(caseId) && available('reader')) start('reader');
  };
  const previousClose = closeDecisionReader;
  closeDecisionReader = function(...args) {
    tourLoad++;
    finish(false, false);
    const result = previousClose(...args);
    start('search');
    return result;
  };
  const previousActivate = activateResearchTab;
  activateResearchTab = function(...args) {
    tourLoad++;
    finish(false, false);
    const result = previousActivate(...args);
    // Defer until openDecision has had a chance to reveal the reader.
    queueMicrotask(() => start('search'));
    return result;
  };
  const params = researchEntryParams;
  if ((params.get('tab') || 'search') === 'search') {
    const query = params.get('query'), court = params.get('court'), fullText = params.get('search_full_text');
    if (query !== null) document.getElementById('searchQuery').value = query.slice(0, 500);
    if (court !== null) document.getElementById('courtFilter').value = ['FC', 'FCA', 'SCC'].includes(court) ? court : '';
    if (fullText !== null) document.getElementById('searchFullText').checked = fullText === 'true';
    if (court || fullText === 'true') {
      document.getElementById('advancedSearchOptions').hidden = false;
      document.getElementById('toggleAdvancedSearch').setAttribute('aria-expanded', 'true');
    }
    qfSync();
    updateSearchFilterSummary();
  }
  if (params.get('tab') === 'judge-profile' && params.has('judge_query')) {
    document.getElementById('judgeProfileQuery').value = params.get('judge_query').slice(0, 120);
    document.getElementById('judgeProfileSearchMeta').textContent = 'Example name filled in. Search stored profiles by name.';
  }
  // Start deep-linked readers only after every existing wrapper and this tour
  // controller has been installed (including immediately resolved/cached loads).
  if (Number.isInteger(initialCaseId) && initialCaseId > 0 && (params.get('tab') || 'search') === 'search') openDecision(initialCaseId);
  start('search');
  if (available('reader')) start('reader');
})();
