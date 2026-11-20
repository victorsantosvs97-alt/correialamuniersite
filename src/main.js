/* Correia Santos & Lamunier Advogados — scripts do site */
(function () {
  document.documentElement.classList.add('js');
  // Endereço do serviço de formulário (ex.: https://formspree.io/f/xxxxxxx).
  // Vazio + site hospedado no Netlify: usa os Formulários do Netlify.
  // Vazio fora do Netlify: abre o e-mail do visitante já preenchido.
  var FORM_ENDPOINT = 'https://formsubmit.co/ajax/atendimento@correialamunier.com';
  var EMAIL = 'atendimento@correialamunier.com';
  var lang = document.documentElement.lang === 'en' ? 'en' : 'pt';
  var T = {
    pt: { open: 'Menu', close: 'Fechar', sending: 'Enviando…', ok: 'Mensagem enviada. Retornaremos em breve.',
          err: 'Não foi possível enviar agora. Escreva para ' + EMAIL + '.',
          mail: 'Abrimos o seu aplicativo de e-mail com a mensagem pronta. Se ele não abrir, escreva para ' + EMAIL + '.',
          consent: 'Para enviar, marque a autorização de uso dos dados.', subject: 'Contato pelo site' },
    en: { open: 'Menu', close: 'Close', sending: 'Sending…', ok: 'Message sent. We will get back to you shortly.',
          err: 'We could not send it right now. Please write to ' + EMAIL + '.',
          mail: 'Your email app should open with the message ready. If it does not, please write to ' + EMAIL + '.',
          consent: 'Please tick the data-use consent box to send.', subject: 'Website enquiry' }
  }[lang];

  // Menu no celular
  var btn = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? T.close : T.open;
    });
  }

  // Horário local (elementos com data-tz)
  function hora(tz) {
    try {
      return new Intl.DateTimeFormat(lang === 'en' ? 'en-US' : 'pt-BR', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: tz === 'local' ? undefined : tz }).format(new Date());
    } catch (e) { return '--:--'; }
  }
  function tick() {
    document.querySelectorAll('[data-tz]').forEach(function (el) { el.textContent = hora(el.getAttribute('data-tz')); });
  }
  tick(); setInterval(tick, 30000);

  // Página inicial: o logo do topo assume o lugar do logo do cabeçalho até a rolagem
  var hl = document.querySelector('.hero-logo');
  if (hl) {
    var root = document.documentElement; root.classList.add('js-home');
    var onScroll = function () { root.classList.toggle('scrolled', window.scrollY > hl.getBoundingClientRect().height + hl.offsetTop - 60); };
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Frase em destaque: as partes acendem conforme a rolagem
  var st = document.querySelector('[data-statement]');
  if (st) {
    var parts = st.querySelectorAll('span');
    var light = function () {
      var r = st.getBoundingClientRect(), vh = window.innerHeight || 800;
      var prog = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      parts.forEach(function (sp, i) { sp.classList.toggle('lit', prog > (i + 0.4) / parts.length); });
    };
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) parts.forEach(function (sp) { sp.classList.add('lit'); });
    else { light(); window.addEventListener('scroll', light, { passive: true }); window.addEventListener('resize', light); }
  }

  // Carrossel de áreas
  var rail = document.getElementById('rail');
  document.querySelectorAll('[data-rail]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!rail) return;
      var card = rail.querySelector('.card');
      var step = card ? card.getBoundingClientRect().width + 18 : 300;
      rail.scrollBy({ left: step * parseInt(b.getAttribute('data-rail'), 10), behavior: 'smooth' });
    });
  });

  // Ano no rodapé
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Formulário
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  function say(msg, cls) { status.textContent = msg; status.className = 'form-status ' + (cls || ''); }
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (form.querySelector('.hp input').value) return; // robô
    if (!form.reportValidity()) return;
    if (!document.getElementById('f-consent').checked) { say(T.consent, 'err'); return; }
    var data = new FormData(form);
    data.delete('_gotcha'); data.delete('form-name');
    data.set('_subject', 'Novo contato pelo site'); data.set('_template', 'table'); data.set('_captcha', 'false');
    var h = location.hostname;
    if (!FORM_ENDPOINT && (/netlify\.app$/.test(h) || /correialamunier\.com$/.test(h))) {
      // Formulários do Netlify: o envio vai para a própria página
      say(T.sending);
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
        .then(function (r) { if (!r.ok) throw new Error(); form.reset(); say(T.ok, 'ok'); })
        .catch(function () { say(T.err, 'err'); });
      return;
    }
    if (FORM_ENDPOINT) {
      say(T.sending);
      fetch(FORM_ENDPOINT, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error(); form.reset(); say(T.ok, 'ok'); })
        .catch(function () { say(T.err, 'err'); });
      return;
    }
    var linhas = [];
    data.forEach(function (v, k) { if (k !== '_gotcha' && k !== 'consentimento') linhas.push(k + ': ' + v); });
    window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(T.subject) + '&body=' + encodeURIComponent(linhas.join('\n'));
    say(T.mail, 'ok');
  });
})();
