"""Additive markup/renderer for descriptive suggestions on the existing memo page."""

SUGGESTION_SECTION = '''
<div class="section" id="authoritySuggestions">
<h3>Suggestions, not legal advice</h3>
<p class="notice">Descriptive research leads only. Citation frequency is not
endorsement; contrary signals describe citing decisions' stored Minister-relative
outcomes, not the authority's holding or your memo's position. Verify sources.</p>
<p class="meta" id="suggestionCoverage" role="status"></p>
<h4>Missing authority suggestions</h4><div id="suggestedMissing"></div>
<h4>Potential contrary authority suggestions</h4>
<p class="meta">Requires at least 5 distinct citing decisions and Minister losses
in a strict majority of all those decisions, including mixed and unclassified.</p>
<p class="meta" id="contraryHidden"></p><div id="suggestedContrary"></div>
</div>
'''

SUGGESTION_SCRIPT = r'''
function suggestionRow(authority){
    const why=authority.why||{},o=authority.outcomes||{};
    const tags=(why.shared_tags||[]).map(esc).join(', ')||'none';
    const statutes=(why.shared_statutes||[]).map(esc).join(', ')||'none';
    return `<div class="authority"><strong><a href="/data-explorer?case_id=${encodeURIComponent(authority.id)}">${esc(authority.title)}</a></strong>
    <div class="authority-meta">${esc(authority.citation||authority.id)}</div>
    <div>${esc(authority.citing_decisions)} / ${esc(authority.cohort_denominator)} checked cohort decisions cite this authority.</div>
    <div class="authority-issues">Why: shared tags: ${tags}; shared statutes: ${statutes}.</div>
    <div class="authority-meta">Minister outcomes: won ${esc(o.won)}, lost ${esc(o.lost)}, mixed ${esc(o.mixed)}, unclassified ${esc(o.unclassified)}; denominator ${esc(o.denominator)} distinct citing decisions.</div></div>`;
}
function renderAuthoritySuggestions(s){
    s=s||{};const coverage=s.coverage||{},missing=s.missing||[],contrary=s.contrary||[];
    const statuses={session_unavailable:'Suggestions unavailable without a local session.',no_signals:'No deterministic memo tags or statutes found.',empty_cohort:'No matching stored decisions found.'};
    const warning=coverage.partial?'Partial coverage: caps truncated decisions or citations. Rankings and outcome distributions may change. ':'';
    document.getElementById('suggestionCoverage').textContent=warning+(statuses[s.status]||'')+
        ` Checked cohort: ${s.cohort_denominator||0} decisions. Missing candidates: ${coverage.missing_total||0}; contrary candidates: ${coverage.contrary_total||0}. `+
        (coverage.missing_truncated||coverage.contrary_truncated?'Showing at most ten per list. ':'')+(coverage.note||'');
    document.getElementById('contraryHidden').textContent=`${s.contrary_hidden_below_threshold||0} majority-lost candidates hidden: fewer than 5 distinct citing decisions.`;
    document.getElementById('suggestedMissing').innerHTML=missing.length?missing.map(suggestionRow).join(''):'<div class="empty">No missing suggestions in the checked cohort; this does not establish citation completeness.</div>';
    document.getElementById('suggestedContrary').innerHTML=contrary.length?contrary.map(suggestionRow).join(''):'<div class="empty">No contrary suggestions meet the thresholds in the checked cohort.</div>';
}
'''
