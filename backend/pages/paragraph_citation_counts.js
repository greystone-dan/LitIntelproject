/* Optional later-decision heatmap; never rewrites source blocks or offsets. */
(() => {
  const button = document.getElementById('readerParagraphCountsToggle');
  const coverage = document.getElementById('readerParagraphCountsCoverage');
  if (!button || !coverage) return;
  let enabled = false, data = null, request = null, generation = 0;
  const originalTitles = new WeakMap();
  const formatted = () => readerState.payload && readerState.mode === 'normalized' && readerState.formatted !== false;

  function applyCounts() {
    button.disabled = !formatted();
    document.querySelectorAll('#decisionBody .fmt-para').forEach(para => {
      if (para.hasAttribute('data-citation-heat')) {
        const title = originalTitles.get(para);
        if (title === null) para.removeAttribute('title');
        else if (title !== undefined) para.setAttribute('title', title);
        para.removeAttribute('data-citation-heat');
        para.querySelector('.reader-paragraph-count-label')?.remove();
      }
    });
    if (!enabled || !data || !data.chronology_known || !formatted()) return;
    const maximum = Math.max(1, ...Object.values(data.counts));
    document.querySelectorAll('#decisionBody .fmt-para').forEach(para => {
      const number = Number(para.dataset.para);
      if (!Object.hasOwn(data.counts, number)) return;
      const count = data.counts[number];
      const label = `Cited by ${count} later decision${count === 1 ? '' : 's'}`;
      originalTitles.set(para, para.getAttribute('title'));
      para.setAttribute('title', label);
      para.dataset.citationHeat = count === 0 ? '0' : String(Math.min(3, Math.ceil(3 * count / maximum)));
      const text = document.createElement('span');
      text.className = 'reader-paragraph-count-label';
      text.textContent = label;
      para.append(text);
    });
  }

  function resetCounts() {
    generation++;
    request?.abort();
    request = null;
    enabled = false;
    data = null;
    button.setAttribute('aria-pressed', 'false');
    coverage.textContent = '';
    applyCounts();
    button.disabled = true;
  }

  button.addEventListener('click', async () => {
    enabled = !enabled;
    button.setAttribute('aria-pressed', String(enabled));
    applyCounts();
    if (!enabled) {
      request?.abort();
      request = null;
      generation++;
      coverage.textContent = '';
      return;
    }
    const current = ++generation, caseId = readerState.caseId;
    const showCoverage = () => {
      coverage.textContent = data.chronology_known
        ? `${data.citing_decisions_with_usable_pinpoint} of ${data.total_citing_decisions} later citing decisions have a usable paragraph pinpoint; ${data.citing_decisions_without_usable_pinpoint} have none. ${data.citations_without_usable_pinpoint} of ${data.total_citations} stored citation occurrences lack a usable pinpoint. Shading is relative to the highest paragraph count in this decision; zero counts are unshaded. Counts cover resolved citations in this library, not citation treatment.`
        : 'Decision date unavailable: later-decision counts cannot be established.';
    };
    if (data) { showCoverage(); return; }
    coverage.textContent = 'Loading later-decision paragraph citation counts…';
    request = new AbortController();
    try {
      const response = await fetch(`/api/cases/${caseId}/paragraph-citation-counts`, {signal: request.signal});
      if (!response.ok) throw new Error(`Request failed (${response.status})`);
      const result = await response.json();
      if (current !== generation || !enabled || readerState.caseId !== caseId || !readerState.payload) return;
      if (result.case_id !== Number(caseId) || !result.counts || Object.values(result.counts).some(count => !Number.isInteger(count) || count < 0)) {
        throw new Error('Invalid paragraph citation counts');
      }
      data = result;
      showCoverage();
      applyCounts();
    } catch (error) {
      if (current !== generation || error.name === 'AbortError') return;
      enabled = false;
      button.setAttribute('aria-pressed', 'false');
      applyCounts();
      coverage.textContent = 'Paragraph citation counts unavailable. Existing reader shading is unchanged; try again.';
    } finally {
      if (current === generation) request = null;
    }
  });

  const previousMode = setReaderMode;
  setReaderMode = function(mode) { previousMode(mode); applyCounts(); };
  const previousOpen = openDecision;
  openDecision = async function(caseId) {
    resetCounts();
    const current = generation;
    try { await previousOpen(caseId); }
    finally { if (current === generation) applyCounts(); }
  };
  const previousClose = closeDecisionReader;
  closeDecisionReader = function() { resetCounts(); previousClose(); };
  applyCounts();
})();
