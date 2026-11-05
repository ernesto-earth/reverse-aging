(() => {
  const pages = [...document.querySelectorAll('[data-page]')];
  const navLinks = [...document.querySelectorAll('[data-nav]')];
  const moreBtn = document.querySelector('.more-btn');
  const sheet = document.getElementById('more-sheet');
  const baseTitle = document.title;
  let currentPage = null;

  function showPage(id) {
    const page = pages.find(p => p.id === id) || pages[0];
    if (currentPage !== page) {
      pages.forEach(p => { p.hidden = p !== page; });
      currentPage = page;
      document.title = page.id === 'ueberblick' ? baseTitle : `${page.dataset.title} · Reverse Aging Routinen`;
    }
    navLinks.forEach(a => {
      if (a.dataset.nav === page.id) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    const inMore = sheet && sheet.querySelector(`[data-nav="${page.id}"]`);
    moreBtn?.classList.toggle('current', !!inMore);
    return page;
  }

  function selectTab(id, focus) {
    const tabs = [...document.querySelectorAll('[role="tab"][data-tab]')];
    const target = tabs.find(t => t.dataset.tab === id);
    if (!target) return;
    tabs.forEach(t => {
      const on = t === target;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) target.focus();
  }

  function openAncestors(el) {
    if (el.tagName === 'DETAILS') el.open = true;
    let d = el.parentElement && el.parentElement.closest('details');
    while (d) { d.open = true; d = d.parentElement && d.parentElement.closest('details'); }
  }

  function route() {
    const raw = decodeURIComponent(location.hash.slice(1));
    const [first, sub] = raw.split('/');
    closeSheet();
    if (!first || pages.some(p => p.id === first)) {
      const page = showPage(first || 'ueberblick');
      if (sub) selectTab(sub);
      window.scrollTo(0, 0);
      const h1 = page.querySelector('h1');
      if (first && h1) h1.focus({ preventScroll: true });
      return;
    }
    const el = document.getElementById(first);
    if (!el) { showPage('ueberblick'); window.scrollTo(0, 0); return; }
    const page = el.closest('[data-page]');
    if (page) showPage(page.id);
    const panel = el.closest('[role="tabpanel"]');
    if (panel) selectTab(panel.id.replace('panel-', ''));
    openAncestors(el);
    requestAnimationFrame(() => el.scrollIntoView({ block: 'start' }));
  }

  // Tabs: Klick und Pfeiltasten
  document.querySelectorAll('[role="tablist"]').forEach(list => {
    list.addEventListener('click', e => {
      const btn = e.target.closest('[role="tab"][data-tab]');
      if (btn) selectTab(btn.dataset.tab);
    });
    list.addEventListener('keydown', e => {
      if (!['ArrowLeft', 'ArrowRight'].includes(e.key)) return;
      const tabs = [...list.querySelectorAll('[role="tab"]')];
      if (!tabs[0]?.dataset.tab) { const i = tabs.indexOf(document.activeElement); const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length]; n.click(); n.focus(); e.preventDefault(); return; }
      const i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      const next = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
      selectTab(next.dataset.tab, true);
      e.preventDefault();
    });
  });

  // Überblick am Handy: Heute / Woche / Quartal
  const rswitch = document.querySelector('.rswitch');
  const rgrid = document.querySelector('.rgrid');
  rswitch?.addEventListener('click', e => {
    const btn = e.target.closest('[data-r]');
    if (!btn) return;
    rswitch.querySelectorAll('[data-r]').forEach(b => { const on = b === btn; b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
    rgrid.dataset.active = btn.dataset.r;
  });

  // "Mehr"-Menü am Handy
  function closeSheet() {
    if (!sheet) return;
    sheet.hidden = true;
    moreBtn?.setAttribute('aria-expanded', 'false');
  }
  moreBtn?.addEventListener('click', e => {
    e.stopPropagation();
    const open = sheet.hidden;
    sheet.hidden = !open;
    moreBtn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', e => {
    if (sheet && !sheet.hidden && !sheet.contains(e.target)) closeSheet();
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSheet(); });

  // Gleicher Anker erneut geklickt: trotzdem hinspringen
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (a && a.getAttribute('href') === location.hash) { e.preventDefault(); route(); }
  });

  addEventListener('hashchange', route);
  route();
})();
