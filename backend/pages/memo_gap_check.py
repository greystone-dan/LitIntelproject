"""Escaped page section for rule-based memo gap suggestions."""

GAP_SECTION = '''
<div class="section" id="memoGapSuggestions">
<h3>Suggestions for review, not legal advice</h3>
<p class="meta">Rule-based research leads from stored decisions sharing the memo's
top deterministic tags. Counts describe checked cohorts, not legal completeness or
endorsement.</p>
<p class="meta" id="gapCoverage" role="status"></p>
<p class="meta" id="gapTags"></p>
<h4>Authorities often cited by tagged decisions but absent from the memo</h4>
<div id="gapMissing"></div>
<h4>Possibly contrary on a matched tag</h4>
<p class="meta">Shown only when at least 8 distinct citing decisions on a tag had a
higher Minister-loss rate than all decisions with that tag. Unclassified decisions
remain in both denominators.</p>
<p class="meta" id="gapContraryHidden"></p><div id="gapContrary"></div>
</div>
'''

GAP_SCRIPT = r'''
function gapRate(rate){
    return `${esc(rate.rate_percent)}% (${esc(rate.against_minister)}/`+
        `${esc(rate.denominator)})`;
}
function gapTagLine(detail){
    const outcomes=detail.outcomes||{},baseline=detail.baseline_outcomes||{};
    return `<div class="authority-issues">${esc(detail.tag)}: `+
        `${esc(detail.citing_decisions)} / ${esc(detail.tag_denominator)} decisions `+
        `cite this authority; Minister losses ${esc(outcomes.lost)} / `+
        `${esc(detail.citing_decisions)}, baseline ${esc(baseline.lost)} / `+
        `${esc(detail.tag_denominator)}; unclassified ${esc(outcomes.unclassified)} / `+
        `${esc(baseline.unclassified)}.</div>`;
}
function gapRow(authority,contrary=false){
    const tags=(authority.tags_matched||[]).map(gapTagLine).join('');
    const comparisons=contrary?(authority.contrary_tags||[]).map(item=>
        `<div class="authority-issues">${esc(item.tag)}: `+
        `citing-decision Minister-loss rate ${gapRate(item.authority)}; `+
        `tag baseline ${gapRate(item.tag_baseline)}. Unclassified: `+
        `${esc(item.authority.unclassified)} / `+
        `${esc(item.tag_baseline.unclassified)}.</div>`
    ).join(''):'';
    return `<div class="authority"><strong><a `+
        `href="/data-explorer?case_id=${encodeURIComponent(authority.id)}">`+
        `${esc(authority.title)}</a></strong>`+
        `<div class="authority-meta">${esc(authority.citation||authority.id)}</div>`+
        `<div>${esc(authority.citing_decisions)} / `+
        `${esc(authority.cohort_denominator)} checked tagged decisions cite this `+
        `authority.</div>`+
        `<div class="authority-issues">Why suggested: ${esc(authority.why)}</div>`+
        `${tags}${comparisons}</div>`;
}
function renderMemoGapSuggestions(s){
    s=s||{};
    const coverage=s.coverage||{},missing=s.missing||[];
    const contrary=s.possibly_contrary||[];
    const statuses={
        empty_memo:'No memo text to analyze.',
        no_tags:'No deterministic memo tags found.',
        session_unavailable:'Gap suggestions unavailable without a local session.',
        empty_cohort:'No stored decisions matched the memo tags.'
    };
    const warning=coverage.partial?
        'Partial coverage: caps truncated decisions or citations; rankings and rates '+
        'may change. ':'';
    const totals=` Checked tagged-decision denominator: `+
        `${s.cohort_denominator||0}. Missing suggestions: `+
        `${coverage.missing_total||0}; possibly contrary: `+
        `${coverage.contrary_total||0}. `;
    const truncated=(coverage.missing_truncated||coverage.contrary_truncated)?
        'Showing at most ten per list. ':'';
    document.getElementById('gapCoverage').textContent=warning+
        (statuses[s.status]||'')+totals+truncated+(coverage.note||'');
    const tags=(s.top_tags||[]).map(item=>
        `${esc(item.tag)} (${esc(item.memo_mentions)} mentions)`
    ).join(', ')||'none';
    document.getElementById('gapTags').textContent=`Memo top tags: ${tags}`;
    document.getElementById('gapContraryHidden').textContent=
        `${s.contrary_hidden_below_threshold||0} otherwise higher-loss authority/tag `+
        `comparisons hidden below 8 citing decisions.`;
    const emptyMissing='<div class="empty">No missing-authority suggestions in the '+
        'checked cohorts; this does not establish citation completeness.</div>';
    const emptyContrary='<div class="empty">No possibly contrary suggestions meet '+
        'the per-tag threshold in the checked cohorts.</div>';
    document.getElementById('gapMissing').innerHTML=missing.length?
        missing.map(item=>gapRow(item)).join(''):emptyMissing;
    document.getElementById('gapContrary').innerHTML=contrary.length?
        contrary.map(item=>gapRow(item,true)).join(''):emptyContrary;
}
'''
