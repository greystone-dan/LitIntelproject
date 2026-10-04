"""Browser-local saved research folders and additive Data Explorer controls."""


RESEARCH_FOLDERS_SCRIPT = r"""
(() => {
  'use strict';
  const STORAGE_KEY = 'ilit.researchFolders.v1';
  const MAX_FOLDERS = 200;
  const MAX_ITEMS_PER_FOLDER = 5000;
  const MAX_NOTE_LENGTH = 5000;
  const app = document.getElementById('researchFoldersApp');
  let storageAvailable = true;
  let state = {version: 1, folders: []};
  let activeCaseId = new URLSearchParams(window.location.search).get('case_id');

  const element = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  const report = (message, isError = false) => {
    let status = document.getElementById('researchFolderNotice');
    if (!status) {
      status = element('div');
      status.id = 'researchFolderNotice';
      status.className = 'research-folder-notice';
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      document.body.prepend(status);
    }
    status.textContent = message;
    status.dataset.state = isError ? 'error' : 'success';
  };
  const normalizeState = (input) => {
    if (!input || input.version !== 1 || !Array.isArray(input.folders) ||
        input.folders.length > MAX_FOLDERS) {
      throw new Error('This is not a supported research-folder backup.');
    }
    const seenFolders = new Set();
    let itemCount = 0;
    const folders = input.folders.map((source) => {
      if (!source || typeof source.id !== 'string' || !source.id ||
          typeof source.name !== 'string' || !Array.isArray(source.items)) {
        throw new Error('A folder in the backup is invalid.');
      }
      const id = source.id.slice(0, 80);
      const name = source.name.trim();
      if (!name || name.length > 100 || seenFolders.has(id) ||
          source.items.length > MAX_ITEMS_PER_FOLDER) {
        throw new Error('A folder name, identifier, or item list is invalid.');
      }
      seenFolders.add(id);
      const seenCases = new Set();
      const items = source.items.map((entry) => {
        const caseId = Number(entry && entry.caseId);
        if (!Number.isSafeInteger(caseId) || caseId <= 0 ||
            typeof entry.note !== 'string' || entry.note.length > MAX_NOTE_LENGTH) {
          throw new Error('A saved case or note in the backup is invalid.');
        }
        if (seenCases.has(caseId)) throw new Error('A folder contains a duplicate case.');
        seenCases.add(caseId);
        itemCount += 1;
        if (itemCount > 10000) throw new Error('The backup contains too many saved cases.');
        return {
          caseId,
          citation: String(entry.citation || '').slice(0, 500),
          name: String(entry.name || '').slice(0, 1000),
          court: String(entry.court || '').slice(0, 200),
          date: String(entry.date || '').slice(0, 100),
          outcome: String(entry.outcome || 'unclassified').slice(0, 200),
          note: entry.note
        };
      });
      return {id, name, items};
    });
    return {version: 1, folders};
  };
  const readState = () => {
    let loaded = {version: 1, folders: []};
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) loaded = normalizeState(JSON.parse(saved));
      const probe = `${STORAGE_KEY}.probe`;
      localStorage.setItem(probe, '1');
      localStorage.removeItem(probe);
      return loaded;
    } catch (error) {
      storageAvailable = false;
      return loaded;
    }
  };
  const saveState = () => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      storageAvailable = true;
      renderStorageWarning();
      return true;
    } catch (error) {
      storageAvailable = false;
      renderStorageWarning();
      report('Browser storage is blocked or full. Changes are only held in memory until this page closes; download a JSON backup before leaving.', true);
      return false;
    }
  };
  const renderStorageWarning = () => {
    let warning = document.getElementById('researchFolderStorageWarning');
    if (storageAvailable) {
      warning?.remove();
      return;
    }
    if (!warning) {
      warning = element('div');
      warning.id = 'researchFolderStorageWarning';
      warning.className = 'research-folder-warning';
      warning.setAttribute('role', 'alert');
      document.body.prepend(warning);
    }
    warning.textContent = 'Browser storage is unavailable. Folders are temporarily held in memory on this page only; export a JSON backup before closing or reloading.';
  };
  const newId = () => {
    if (window.crypto && typeof window.crypto.randomUUID === 'function') {
      return window.crypto.randomUUID();
    }
    return `folder-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  };
  const createFolder = (name) => {
    const clean = String(name || '').trim();
    if (!clean || clean.length > 100) throw new Error('Folder names must be 1 to 100 characters.');
    if (state.folders.length >= MAX_FOLDERS) throw new Error('The folder limit has been reached.');
    const folder = {id: newId(), name: clean, items: []};
    state.folders.push(folder);
    saveState();
    renderFolders();
    return folder;
  };
  const itemFromResponse = (caseId, item, fallback = {}) => {
    const dateValue = item.date || fallback.date || '';
    return {
      caseId,
      citation: String(item.citation || fallback.citation || ''),
      name: String(item.title || item.name || fallback.name || ''),
      court: String(item.court || fallback.court || ''),
      date: dateValue && typeof dateValue === 'object' && dateValue.isoformat
        ? dateValue.isoformat() : String(dateValue),
      outcome: String(item.government_outcome || item.decision_outcome ||
        fallback.outcome || 'unclassified'),
      note: ''
    };
  };
  const fallbackFromCard = (button) => {
    const card = button?.matches('.case-result') ? button :
      button?.closest('.research-folder-result-row')?.querySelector('.case-result');
    return {
      name: card?.querySelector('.result-title')?.textContent || '',
      citation: card?.querySelector('.result-citation')?.textContent || '',
      court: card?.querySelector('.result-context span')?.textContent || ''
    };
  };
  const currentReaderFallback = () => ({
    name: document.getElementById('decisionTitle')?.textContent || '',
    citation: document.getElementById('readerPrintCitation')?.textContent || '',
    court: document.getElementById('decisionMeta')?.textContent || ''
  });
  const selectFolder = async (caseId, fallback = {}) => {
    if (!state.folders.length) {
      const name = window.prompt('Create a folder to add this case to:');
      if (!name || !name.trim()) return;
      try {
        const created = createFolder(name);
        await addToFolder(created, caseId, fallback);
      } catch (error) {
        report(error.message, true);
      }
      return;
    }
    const dialog = document.getElementById('researchFolderPicker');
    const select = dialog.querySelector('select');
    select.replaceChildren();
    state.folders.forEach((folder) => {
      const option = element('option', folder.name);
      option.value = folder.id;
      select.append(option);
    });
    dialog.showModal();
    dialog.dataset.caseId = String(caseId);
    dialog.dataset.fallback = JSON.stringify(fallback);
  };
  const addToFolder = async (folder, caseId, fallback = {}) => {
    if (folder.items.some((item) => item.caseId === caseId)) {
      report(`That case is already in “${folder.name}”.`);
      return;
    }
    let details = {};
    try {
      const response = await fetch(`/analytics/search/cases/${encodeURIComponent(caseId)}`);
      if (!response.ok) throw new Error(`Case details unavailable (${response.status}).`);
      const data = await response.json();
      details = data.case || data;
    } catch (error) {
      if (!fallback.name && !fallback.citation) {
        report(`Could not add case: ${error.message}`, true);
        return;
      }
    }
    folder.items.push(itemFromResponse(caseId, details, fallback));
    saveState();
    renderFolders();
    report(`Added case to “${folder.name}”.`);
  };

  const exportJson = () => {
    const blob = new Blob([JSON.stringify(state, null, 2)], {type: 'application/json'});
    const link = element('a');
    const url = URL.createObjectURL(blob);
    link.href = url;
    link.download = 'research-folders.json';
    link.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    report('Research folders JSON backup downloaded.');
  };
  const importJson = async (file) => {
    try {
      const imported = normalizeState(JSON.parse(await file.text()));
      if (!window.confirm('Replace all current browser-local research folders with this backup?')) return;
      state = imported;
      saveState();
      renderFolders();
      report('Research folders backup imported.');
    } catch (error) {
      report(`Could not import backup: ${error.message}`, true);
    }
  };
  const exportCases = async (folder, format) => {
    const selected = Array.from(document.querySelectorAll(
      `[data-folder-id="${CSS.escape(folder.id)}"] [data-case-select]:checked`
    )).map((checkbox) => Number(checkbox.value));
    if (!selected.length) {
      report('Select at least one case to export.', true);
      return;
    }
    if (selected.length > 500) {
      report('An export can include no more than 500 cases. Select fewer cases.', true);
      return;
    }
    const notes = Object.fromEntries(folder.items
      .filter((item) => selected.includes(item.caseId) && item.note)
      .map((item) => [String(item.caseId), item.note]));
    try {
      const response = await fetch('/api/research-folders/export', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({case_ids: selected, notes, format})
      });
      if (!response.ok) {
        let detail = `Request failed (${response.status})`;
        try { detail = (await response.json()).detail || detail; } catch (error) {}
        throw new Error(detail);
      }
      const blob = await response.blob();
      const link = element('a');
      const url = URL.createObjectURL(blob);
      link.href = url;
      link.download = `research-folder-export.${format}`;
      link.click();
      window.setTimeout(() => URL.revokeObjectURL(url), 1000);
      report(`${selected.length} case${selected.length === 1 ? '' : 's'} exported.`);
    } catch (error) {
      report(`Export unavailable: ${error.message}`, true);
    }
  };
  const renderFolders = () => {
    if (!app) return;
    const list = app.querySelector('#researchFolderList');
    list.replaceChildren();
    if (!state.folders.length) {
      list.append(element('p', 'No folders yet. Create one to start saving authorities.'));
      return;
    }
    state.folders.forEach((folder) => {
      const section = element('section', undefined, 'research-folder-card');
      section.dataset.folderId = folder.id;
      const heading = element('div', undefined, 'research-folder-heading');
      heading.append(element('h2', folder.name));
      const rename = element('button', 'Rename', 'rf-button');
      rename.type = 'button';
      rename.addEventListener('click', () => {
        const name = window.prompt('Rename folder', folder.name);
        if (name === null) return;
        try {
          folder.name = String(name).trim();
          if (!folder.name || folder.name.length > 100) throw new Error('Folder names must be 1 to 100 characters.');
          saveState();
          renderFolders();
        } catch (error) { report(error.message, true); }
      });
      const remove = element('button', 'Delete folder', 'rf-button danger');
      remove.type = 'button';
      remove.addEventListener('click', () => {
        if (!window.confirm(`Delete “${folder.name}” and its ${folder.items.length} saved case(s)?`)) return;
        state.folders = state.folders.filter((candidate) => candidate.id !== folder.id);
        saveState();
        renderFolders();
        report(`Deleted “${folder.name}”.`);
      });
      const csv = element('button', 'Export selected CSV', 'rf-button');
      csv.type = 'button';
      csv.addEventListener('click', () => exportCases(folder, 'csv'));
      const docx = element('button', 'Export selected Word', 'rf-button');
      docx.type = 'button';
      docx.addEventListener('click', () => exportCases(folder, 'docx'));
      heading.append(rename, remove, csv, docx);
      section.append(heading);
      if (!folder.items.length) {
        section.append(element('p', 'This folder has no saved cases yet.'));
      }
      folder.items.forEach((item) => {
        const row = element('article', undefined, 'research-folder-item');
        const choose = element('input');
        choose.type = 'checkbox';
        choose.checked = true;
        choose.value = String(item.caseId);
        choose.dataset.caseSelect = 'true';
        choose.setAttribute('aria-label', `Include ${item.citation || item.name || `case ${item.caseId}`} in export`);
        const summary = element('div', undefined, 'research-folder-case');
        summary.append(element('strong', item.citation || item.name || `Case ${item.caseId}`));
        summary.append(element('div', [item.name, item.court, item.date, item.outcome].filter(Boolean).join(' · ')));
        const noteLabel = element('label', 'Note');
        const note = element('textarea');
        note.maxLength = MAX_NOTE_LENGTH;
        note.value = item.note;
        note.addEventListener('input', () => {
          item.note = note.value;
          saveState();
        });
        noteLabel.append(note);
        const removeCase = element('button', 'Remove case', 'rf-button');
        removeCase.type = 'button';
        removeCase.addEventListener('click', () => {
          folder.items = folder.items.filter((candidate) => candidate.caseId !== item.caseId);
          saveState();
          renderFolders();
        });
        row.append(choose, summary, noteLabel, removeCase);
        section.append(row);
      });
      list.append(section);
    });
  };
  const mountSearchControls = () => {
    const results = document.getElementById('searchResults');
    results?.querySelectorAll('.case-result').forEach((card) => {
      if (card.dataset.researchFolderControl) return;
      card.dataset.researchFolderControl = 'true';
      const button = element('button', 'Add to folder', 'rf-button research-folder-add-case');
      button.type = 'button';
      button.setAttribute('aria-label', `Add ${card.querySelector('.result-title')?.textContent || 'case'} to a research folder`);
      button.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        const caseId = Number(card.dataset.caseId);
        selectFolder(caseId, fallbackFromCard(card));
      });
      card.insertAdjacentElement('afterend', button);
    });
    const toolbar = document.querySelector('#caseReaderPanel .reader-toolbar');
    if (toolbar && !toolbar.querySelector('#addReaderCaseToFolder')) {
      const button = element('button', 'Add to folder', 'reader-evidence-toggle');
      button.id = 'addReaderCaseToFolder';
      button.type = 'button';
      button.addEventListener('click', () => {
        const caseId = Number(activeCaseId);
        if (!Number.isSafeInteger(caseId) || caseId <= 0) {
          report('Open a case before adding it to a folder.', true);
          return;
        }
        selectFolder(caseId, currentReaderFallback());
      });
      toolbar.append(button);
    }
    const actions = document.querySelector('.saved-search-actions');
    if (actions && !actions.querySelector('#researchFoldersLink')) {
      const link = element('a', 'Research folders');
      link.id = 'researchFoldersLink';
      link.href = '/research-folders';
      actions.append(link);
    }
  };

  state = readState();
  renderStorageWarning();
  renderFolders();
  if (!app) {
    mountSearchControls();
    const results = document.getElementById('searchResults');
    if (results) new MutationObserver(mountSearchControls).observe(results, {childList: true, subtree: true});
    const originalOpenDecision = window.openDecision;
    if (typeof originalOpenDecision === 'function') {
      window.openDecision = (caseId, ...args) => {
        activeCaseId = String(caseId);
        return originalOpenDecision(caseId, ...args);
      };
    }
    document.addEventListener('click', (event) => {
      const card = event.target.closest?.('#searchResults .case-result');
      if (card) activeCaseId = card.dataset.caseId;
    }, true);
  } else {
    app.querySelector('#researchFolderCreate').addEventListener('submit', (event) => {
      event.preventDefault();
      const field = app.querySelector('#researchFolderName');
      try {
        createFolder(field.value);
        field.value = '';
        report('Research folder created.');
      } catch (error) { report(error.message, true); }
    });
    app.querySelector('#researchFolderBackup').addEventListener('click', exportJson);
    app.querySelector('#researchFolderImport').addEventListener('change', (event) => {
      const file = event.target.files?.[0];
      if (file) importJson(file);
      event.target.value = '';
    });
  }

  const picker = document.getElementById('researchFolderPicker');
  if (picker) {
    picker.querySelector('[data-rf-cancel]').addEventListener('click', () => picker.close());
    picker.querySelector('[data-rf-create]').addEventListener('click', () => {
      const name = window.prompt('Create a research folder:');
      if (!name || !name.trim()) return;
      try {
        const folder = createFolder(name);
        const select = picker.querySelector('select');
        const option = element('option', folder.name);
        option.value = folder.id;
        select.append(option);
        select.value = folder.id;
        report(`Created “${folder.name}”.`);
      } catch (error) { report(error.message, true); }
    });
    picker.querySelector('[data-rf-add]').addEventListener('click', async () => {
      const folder = state.folders.find((candidate) => candidate.id === picker.querySelector('select').value);
      const caseId = Number(picker.dataset.caseId);
      let fallback = {};
      try { fallback = JSON.parse(picker.dataset.fallback || '{}'); } catch (error) {}
      picker.close();
      if (folder) await addToFolder(folder, caseId, fallback);
    });
  }
})();
"""


_FOLDER_PICKER = """
<dialog id="researchFolderPicker" class="research-folder-picker" aria-labelledby="researchFolderPickerTitle">
  <h2 id="researchFolderPickerTitle">Add case to a folder</h2>
  <label>Folder <select aria-label="Research folder"></select></label>
  <div><button type="button" class="rf-button" data-rf-create>Create folder</button>
  <button type="button" class="rf-button" data-rf-add>Add case</button>
  <button type="button" class="rf-button" data-rf-cancel>Cancel</button></div>
</dialog>
"""


_STYLES = """
<style>
.research-folder-warning,.research-folder-notice{position:relative;z-index:1000;margin:12px auto;padding:10px 14px;max-width:1100px;border-radius:8px;background:#fff7ed;color:#7c2d12;border:1px solid #fdba74;font:500 14px/1.45 system-ui,sans-serif}
.research-folder-notice[data-state="error"]{background:#fef2f2;color:#991b1b;border-color:#fca5a5}
.research-folder-add-case{display:block;margin:4px 0 14px}
.research-folder-picker{border:1px solid #cbd5e1;border-radius:12px;padding:20px;max-width:min(440px,calc(100vw - 32px))}
.research-folder-picker::backdrop{background:rgba(15,23,42,.45)}
.research-folder-picker label{display:grid;gap:6px;margin:12px 0}
.research-folder-picker select{padding:8px}
.research-folder-picker>div{display:flex;flex-wrap:wrap;gap:8px}
.rf-button{border:1px solid #cbd5e1;border-radius:6px;background:#fff;padding:7px 10px;color:#1e3a8a;cursor:pointer}
.rf-button:hover{background:#eff6ff}
.rf-button:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
.rf-button.danger{color:#991b1b}
#researchFoldersApp{max-width:1100px;margin:32px auto;padding:0 20px;font:16px/1.5 system-ui,sans-serif;color:#102038}
#researchFoldersApp h1,#researchFoldersApp h2{font-family:Georgia,serif}
.rf-page-intro{color:#475569}
.rf-page-tools,.research-folder-heading{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
#researchFolderCreate{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}
#researchFolderCreate input{min-width:240px;padding:8px}
.research-folder-card{margin:18px 0;padding:16px;border:1px solid #cbd5e1;border-radius:10px;background:#fff}
.research-folder-heading{justify-content:space-between}
.research-folder-heading h2{margin:4px auto 4px 0}
.research-folder-item{display:grid;grid-template-columns:auto minmax(150px,1fr) minmax(180px,1fr) auto;gap:12px;align-items:start;border-top:1px solid #e2e8f0;padding:12px 0}
.research-folder-case div{color:#475569;font-size:14px}
.research-folder-item label{display:grid;gap:4px}
.research-folder-item textarea{min-height:48px;width:100%;box-sizing:border-box}
@media(max-width:700px){.research-folder-item{grid-template-columns:auto 1fr}.research-folder-item label{grid-column:2}.research-folder-item>button{grid-column:2;justify-self:start}}
</style>
"""


def inject_research_folders(html: str) -> str:
    """Add the shared folder script and controls to the active Data Explorer."""
    fragment = _STYLES + _FOLDER_PICKER + f"<script>{RESEARCH_FOLDERS_SCRIPT}</script>"
    if "</body>" not in html:
        return html + fragment
    return html.replace("</body>", fragment + "</body>", 1)


def research_folders_page_html() -> str:
    """Render the standalone browser-local folder manager."""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Research folders | iLIT</title>
  {_STYLES}
</head>
<body>
  <main id="researchFoldersApp">
    <p><a href="/data-explorer">← Back to Data Explorer</a></p>
    <h1>Saved research folders</h1>
    <p class="rf-page-intro">Folders and notes stay in this browser profile. Use the JSON backup to move or preserve them.</p>
    <form id="researchFolderCreate">
      <label for="researchFolderName">New folder name</label>
      <input id="researchFolderName" maxlength="100" required autocomplete="off">
      <button class="rf-button" type="submit">Create folder</button>
    </form>
    <div class="rf-page-tools">
      <button id="researchFolderBackup" class="rf-button" type="button">Download JSON backup</button>
      <label class="rf-button">Import JSON backup
        <input id="researchFolderImport" type="file" accept="application/json,.json">
      </label>
    </div>
    <p id="researchFolderNotice" role="status" aria-live="polite"></p>
    <div id="researchFolderList"></div>
  </main>
  {_FOLDER_PICKER}
  <script>{RESEARCH_FOLDERS_SCRIPT}</script>
</body>
</html>"""
