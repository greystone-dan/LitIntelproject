/* Additive, source-traceable indicator for the active case reader. */
(() => {
	const banner = document.getElementById('readerOverrulingRisk');
	if (!banner) return;

	let requestVersion = 0;

	function clearOverrulingRisk() {
		banner.hidden = true;
		banner.replaceChildren();
	}

	function addRiskDetail(parent, label, value) {
		const line = document.createElement('p');
		const name = document.createElement('strong');
		name.textContent = `${label}: `;
		line.append(name, document.createTextNode(String(value || 'Not recorded')));
		parent.append(line);
	}

	function renderOverrulingRisk(payload) {
		const flags = Array.isArray(payload?.flags) ? payload.flags : [];
		clearOverrulingRisk();
		if (!flags.length) return;

		const heading = document.createElement('strong');
		heading.textContent = flags.some(flag => flag.assignment === 'indirect')
			? 'Potential legal-development indicator: this case may be affected.'
			: 'This case is itself a listed legal-development authority; other cases may be affected by it.';
		// The full notice is folded behind one line so it cannot push the decision off screen.
		const more = document.createElement('details');
		const summary = document.createElement('summary');
		summary.textContent = 'Details and sources';
		more.append(summary);
		more.open = false;
		banner.append(heading, more);
		addRiskDetail(more, 'Assessment', payload.assessment);

		flags.forEach(flag => {
			const item = document.createElement('div');
			item.className = 'overruling-risk-flag';
			addRiskDetail(item, 'Listed development', `${flag.event || 'Unspecified'} (${flag.event_date || 'date not recorded'})`);
			addRiskDetail(item, 'Decision date', flag.decision_date);
			addRiskDetail(item, 'Rationale', flag.rationale);
			addRiskDetail(item, 'Source', flag.source);
			addRiskDetail(item, 'How assigned', flag.how_assigned);
			addRiskDetail(item, 'Review notice', flag.notice);
			more.append(item);
		});
		banner.hidden = false;
	}

	async function loadOverrulingRisk(caseId, version) {
		try {
			const response = await fetch(`/api/overruling-risk/${encodeURIComponent(caseId)}`);
			if (!response.ok) return;
			const payload = await response.json();
			if (version !== requestVersion || readerState.caseId !== Number(caseId)) return;
			renderOverrulingRisk(payload);
		} catch (_error) {
			// A failed risk lookup is not evidence that no indicator exists.
			if (version === requestVersion) clearOverrulingRisk();
		}
	}

	const previousOpenDecision = openDecision;
	openDecision = async function(caseId) {
		clearOverrulingRisk();
		const version = ++requestVersion;
		await previousOpenDecision(caseId);
		if (!readerState.payload || readerState.caseId !== Number(caseId)) return;
		void loadOverrulingRisk(caseId, version);
	};

	const previousCloseDecisionReader = closeDecisionReader;
	closeDecisionReader = function() {
		requestVersion += 1;
		clearOverrulingRisk();
		previousCloseDecisionReader();
	};
})();
