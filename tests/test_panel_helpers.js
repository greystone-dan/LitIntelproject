// Dependency-free, no network/DB: execute the actual helper and owner callbacks.
// Run from any directory: node tests/test_panel_helpers.js
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const helper = read('backend/degraded_mode.py').match(/return r"""<script>\n([\s\S]*?)\n<\/script>"""/)[1];
const source = read('backend/pages/data_explorer.py');
const queue = source.slice(source.indexOf('const panelRequests='), source.indexOf('function readerPanelCurrent'));
const dashboard = read('backend/pages/fc_analytics.py').match(/FC_ANALYTICS_JS = r"""[\s\S]*?<script>\n([\s\S]*?)<\/script>/)[1];
const unhandled = [];
process.on('unhandledRejection', error => unhandled.push(error));

class Element {
    constructor(tag = 'div') {
        this.tag = tag; this.children = []; this.parent = null;
        this.listeners = {}; this.attributes = {}; this.disabled = false;
        this.dataset = {}; this.style = {}; this._text = ''; this.connected = false;
        this.classList = {add() {}, remove() {}};
    }
    get isConnected() { return this.connected || !!this.parent?.isConnected; }
    set textContent(value) { this.replaceChildren(); this._text = String(value); }
    get textContent() { return this._text + this.children.map(child => child.textContent).join(''); }
    setAttribute(key, value) { this.attributes[key] = value; }
    append(...children) {
        for (const child of children) { child.remove(); child.parent = this; this.children.push(child); }
    }
    appendChild(child) { this.append(child); return child; }
    prepend(child) { child.remove(); child.parent = this; this.children.unshift(child); }
    replaceChildren(...children) {
        for (const child of this.children) child.parent = null;
        this.children = []; this._text = ''; this.append(...children);
    }
    contains(child) { return this === child || this.children.some(node => node.contains(child)); }
    remove() {
        if (this.parent) this.parent.children = this.parent.children.filter(child => child !== this);
        this.parent = null;
    }
    addEventListener(name, callback) { (this.listeners[name] ||= []).push(callback); }
    click() { if (!this.disabled) for (const callback of this.listeners.click || []) callback({target: this}); }
}
const nodes = new Map();
const box = id => {
    if (!nodes.has(id)) { const node = new Element(); node.connected = true; nodes.set(id, node); }
    return nodes.get(id);
};
const document = {
    createElement: tag => new Element(tag),
    createElementNS: (_, tag) => new Element(tag),
    createTextNode: text => { const node = new Element(); node.textContent = text; return node; },
    getElementById: box,
    querySelectorAll: () => [],
    querySelector: () => null,
};
const requests = [];
let respond = async () => ({ok: true, json: async () => ({value: 'healthy'})});
const context = vm.createContext({
    document, URL, URLSearchParams, Intl, console, setTimeout,
    location: {href: 'http://fixture/data-explorer?tab=search', search: '?tab=search'},
    history: {replaceState() {}}, window: {},
    fetch: async url => { requests.push(url); return respond(url); },
});
vm.runInContext(helper + '\n' + queue + '\nthis.panel=fetchPanel;this.owner=fetchCurrentPanel;', context);
const retry = node => {
    const visit = item => item.tag === 'button' ? item : item.children.map(visit).find(Boolean);
    return visit(node);
};
const tick = () => new Promise(resolve => setImmediate(resolve));
const good = data => ({ok: true, json: async () => data});

async function retryContracts() {
    const failed = box('retry'), healthy = box('sibling');
    healthy.textContent = 'healthy';
    respond = async () => ({ok: false});
    let renders = 0;
    const options = {render: data => {
        renders++; failed.textContent = data.value;
        const action = new Element('button'); action.addEventListener('click', () => { renders++; });
        failed.append(action);
    }};
    await context.panel('/retry', failed, options);
    const button = retry(failed);
    let release;
    respond = () => new Promise(resolve => { release = resolve; });
    const before = requests.length;
    button.click(); button.click();
    assert.equal(button.disabled, true);
    await tick();
    const pending = context.panel('/retry', failed, options);
    assert.equal(requests.length, before + 1);
    release(good({value: 'retried'}));
    await pending;
    assert.equal(renders, 1);
    retry(failed).click();
    assert.equal(renders, 2, 'success event wiring runs on Retry');
    assert.equal(healthy.textContent, 'healthy');

    respond = async () => good({});
    let attempts = 0;
    await context.panel('/render-throws', failed, {render: () => {
        if (++attempts === 1) throw new Error('private renderer detail');
        failed.textContent = 'renderer recovered';
    }});
    retry(failed).click(); await tick();
    assert.equal(attempts, 2);
    assert.equal(failed.textContent, 'renderer recovered');
}

async function selectionContracts() {
    const target = box('selection');
    let release;
    respond = () => new Promise(resolve => { release = resolve; });
    const rendered = [];
    const first = context.owner('/old', target, {render: () => rendered.push('old')});
    await tick();
    const before = requests.length;
    const skipped = context.owner('/skipped', target, {render: () => rendered.push('skipped')});
    const last = context.owner('/latest', target, {render: () => rendered.push('latest')});
    release(good({}));
    await first;
    respond = async () => good({});
    await Promise.all([skipped, last]);
    assert.deepEqual(rendered, ['latest']);
    assert.equal(requests.length, before + 1);

    respond = async () => ({ok: false});
    await context.owner('/retry-old', target, {render: () => rendered.push('stale retry')});
    const old = retry(target);
    respond = () => new Promise(resolve => { release = resolve; });
    old.click(); await tick();
    const next = context.owner('/after-retry', target, {render: () => rendered.push('after retry')});
    await tick();
    release(good({})); respond = async () => good({});
    await next;
    assert.deepEqual(rendered, ['latest', 'after retry']);

    let current = true, enters = 0;
    respond = () => new Promise(resolve => { release = resolve; });
    const stale = context.owner('/stale', target, {isCurrent: () => current, render: () => enters++});
    await tick(); current = false; release(good({})); await stale;
    assert.equal(enters, 0);
}

async function dashboardContracts() {
    // Stub only chart primitives/options. Execute the real load, shared renderer
    // and independent owner callbacks; a DOM implementation is not a chart engine.
    const instrument = `
fillOptions=function(){};
renderKpis=function(){ $('fcxKpis').textContent='dashboard healthy'; };
for(const [key,view] of Object.entries(VIEWS)){
 view.chart=view.table=function(){ $(view.box).textContent=key+' healthy'; };
}
renderCounsel=function(){ $('fcxCounsel').textContent='counsel healthy'; };
this.dashboardLoad=load;
`;
    vm.runInContext(dashboard.replace(/\}\)\(\);\s*$/, instrument + '\n})();'), context);
    let dashboardFails = true, judgeFails = false;
    respond = async url => {
        if (url.includes('/dashboard?')) return dashboardFails ? {ok: false} : good({kpis: {files: 42}});
        if (url.includes('/judges?')) return judgeFails ? {ok: false} : good({judges: [{name: 'fixture'}]});
        return good({counsel: [{name: 'fixture'}]});
    };
    const before = requests.length;
    await context.dashboardLoad();
    assert.equal(requests.length, before + 3);
    assert.equal(box('fcxJudges').textContent, 'judges healthy');
    assert.equal(box('fcxCounsel').textContent, 'counsel healthy');
    assert.equal(box('fcxKpis').textContent, 'This section could not load.Retry');
    dashboardFails = false;
    retry(box('fcxKpis')).click(); await tick();
    assert.equal(requests.length, before + 4, 'shared dashboard Retry makes exactly one request');
    assert.equal(box('fcxFunnel').textContent, 'funnel healthy');
    assert.equal(box('fcxJudges').textContent, 'judges healthy');
    judgeFails = true;
    await context.dashboardLoad();
    assert.equal(box('fcxKpis').textContent, 'dashboard healthy');
    assert.equal(box('fcxJudges').textContent, 'This section could not load.Retry');
    assert.equal(box('fcxCounsel').textContent, 'counsel healthy');
    judgeFails = false;
    retry(box('fcxJudges')).click(); await tick();
    assert.equal(box('fcxJudges').textContent, 'judges healthy');
    assert.equal(box('fcxFunnel').textContent, 'funnel healthy');
}

(async () => {
    // Network/status/JSON failures never enter a successful renderer.
    // (The retry tests separately exercise renderer failures.)
    let rendered = 0;
    const healthy = box('healthy'), failed = box('failed');
    healthy.textContent = 'healthy sibling';
    for (const failure of [
        async () => { throw new Error('private network detail'); },
        async () => ({ok: false, json: async () => { throw new Error('must not read failed status'); }}),
        async () => ({ok: true, json: async () => { throw new Error('private JSON detail'); }}),
    ]) {
        respond = failure;
        await context.panel('/failure', failed, {
            onError: () => { failed.textContent = 'legacy cleanup'; },
            render: () => rendered++,
        });
        assert.equal(rendered, 0);
        assert.equal(failed.textContent, 'This section could not load.Retry');
        assert.equal(healthy.textContent, 'healthy sibling');
    }
    await retryContracts();
    await selectionContracts();
    await dashboardContracts();
    await tick();
    assert.deepEqual(unhandled, []);
    console.log('Panel helper and owner fixtures passed.');
})().catch(error => { console.error(error); process.exitCode = 1; });
