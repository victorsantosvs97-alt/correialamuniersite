# -*- coding: utf-8 -*-
import os, shutil, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_v1 import FILES, UI, META
from pages2 import page, PRE
from artigos import ARTIGOS, data_pt
import html as _html

BASE_URL = 'https://correialamunier.com/'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'dist')
FONTS = ('https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;1,8..60,300;1,8..60,400&display=swap')
KEYS = ['home', 'business', 'individuals', 'abroad', 'firm', 'blog', 'contact', 'privacy']


def url(lang, key):
    f = FILES[lang][key]
    p = ('en/' if lang == 'en' else '') + ('' if f == 'index.html' else f)
    return BASE_URL + p


def header(lang, key, pre, npre=''):
    u = UI[lang]
    other = 'en' if lang == 'pt' else 'pt'
    other_href = npre + (('en/' if lang == 'pt' else '../') + FILES[other][key])
    cur = ' aria-current="page"'
    nav = ''.join(
        f'<a href="{npre}{FILES[lang][k]}"{cur if k == key else ""}>{t}</a>' for k, t in u['nav'])
    lang_sw = ('<span>PT</span><a href="%s" hreflang="en" lang="en">EN</a>' % other_href) if lang == 'pt' else \
              ('<a href="%s" hreflang="pt-BR" lang="pt-BR">PT</a><span>EN</span>' % other_href)
    wa = 'Fale no WhatsApp' if lang == 'pt' else 'Chat on WhatsApp'
    return f'''<a class="skip" href="#conteudo">{u['skip']}</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{npre}{FILES[lang]['home']}"><img src="{pre}assets/logo-light.png" alt="Correia Santos &amp; Lamunier Advogados" width="250" height="96"></a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav">{u['menu']}</button>
  <nav id="nav" class="nav" aria-label="Principal">{nav}<a class="btn btn-primary" href="{npre}{FILES[lang]['contact']}">{u['cta']}</a><span class="lang">{lang_sw}</span></nav>
</div></header>
<a class="wa" href="https://wa.me/5511917386432" rel="noopener" aria-label="{wa}"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2Z"/></svg><span>{wa}</span></a>'''


def footer(lang, pre, npre=''):
    u = UI[lang]
    nav = ''.join(f'<li><a href="{npre}{FILES[lang][k]}">{t}</a></li>' for k, t in u['nav'])
    nav += f'<li><a href="{npre}{FILES[lang]["contact"]}">{u["cta"]}</a></li><li><a href="{npre}{FILES[lang]["privacy"]}">{u["privacy"]}</a></li>'
    tag = 'Advocacia próxima para empresas e famílias, onde você estiver.' if lang == 'pt' else 'Personal Brazilian legal advice for companies and families, wherever you are.'
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div><img src="{pre}assets/logo-dark.png" alt="Correia Santos &amp; Lamunier Advogados" width="182" height="70"><p class="tag">{tag}</p><div class="social"><a href="https://www.instagram.com/correiasantoslamunier/" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg></a><a href="https://wa.me/5511917386432" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Z"/></svg></a></div></div>
    <div><h4>{u['foot_nav']}</h4><ul>{nav}</ul></div>
    <div><h4>{u['foot_contact']}</h4><ul><li><a href="https://wa.me/5511917386432" rel="noopener">(11) 91738-6432</a></li><li><a href="mailto:atendimento@correialamunier.com">atendimento@correialamunier.com</a></li><li><a href="https://www.instagram.com/correiasantoslamunier/" rel="noopener">@correiasantoslamunier</a></li></ul></div>
    <div><h4>{u['foot_offices']}</h4><ul><li>{u['sp_addr']}</li><li style="margin-top:10px">{u['ed_addr']}</li></ul></div>
  </div>
  <div class="legal"><p>{u['legal']}</p><p>{u['legal2']}</p><p>© <span data-year>2026</span> Correia Santos &amp; Lamunier Advogados</p></div>
</div></footer>'''


def jsonld():
    return json.dumps({
        "@context": "https://schema.org", "@type": "LegalService",
        "name": "Correia Santos & Lamunier Advogados", "url": BASE_URL,
        "email": "atendimento@correialamunier.com", "telephone": "+55 11 91738-6432",
        "image": BASE_URL + "assets/og.png",
        "address": [
            {"@type": "PostalAddress", "streetAddress": "Rua Doutor César, 1368, Santana", "addressLocality": "São Paulo",
             "addressRegion": "SP", "postalCode": "02013-080", "addressCountry": "BR"}],
        "sameAs": ["https://www.instagram.com/correiasantoslamunier/"], "areaServed": ["BR", "Worldwide"], "knowsLanguage": ["pt-BR", "en"]}, ensure_ascii=False)


def head(lang, key, pre, artifact=False):
    title, desc = META[lang][key]
    alt_pt, alt_en = url('pt', key), url('en', key)
    ld = f'<script type="application/ld+json">{jsonld()}</script>' if key == 'home' else ''
    common = f'''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{pre}assets/favicon.png">
<link rel="preload" href="{pre}assets/fonts/source-serif-4-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/styles.css">'''
    if artifact:
        return '<meta name="claude:viewport-fit-sides" content="cover">\n' + common
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{common}
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="pt-BR" href="{alt_pt}"><link rel="alternate" hreflang="en" href="{alt_en}"><link rel="alternate" hreflang="x-default" href="{alt_pt}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang, key)}"><meta property="og:image" content="{BASE_URL}assets/og.png">
<meta property="og:locale" content="{'pt_BR' if lang == 'pt' else 'en_US'}">
{ld}'''


def render(lang, key, artifact=False):
    pre = '../' if lang == 'en' else ''
    body = f'''{header(lang, key, pre)}
<main id="conteudo">{page(lang, key, pre)}
</main>
{footer(lang, pre)}
<script src="{pre}assets/main.js" defer></script>'''
    if artifact:
        return head(lang, key, pre, True) + '\n' + body + '\n'
    hl = 'pt-BR' if lang == 'pt' else 'en'
    return f'<!doctype html>\n<html lang="{hl}">\n<head>\n{head(lang, key, pre)}\n</head>\n<body>\n{body}\n</body>\n</html>\n'


def render_article(a):
    pre = npre = '../'
    PRE[0] = pre
    title = a['titulo_txt'] + ' · Correia Santos & Lamunier'
    u = BASE_URL + f"novidades/{a['slug']}.html"
    box = ''.join(f'<li>{x}</li>' for x in a['resumo_box'])
    fontes = ''.join((f'<li><a href="{h}" rel="noopener">{t}</a></li>' if h else f'<li>{t}</li>') for t, h in a['fontes'])
    head_html = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{_html.escape(title)}</title>
<meta name="description" content="{_html.escape(a['resumo'])}">
<link rel="icon" type="image/png" href="{pre}assets/favicon.png">
<link rel="preload" href="{pre}assets/fonts/source-serif-4-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/styles.css">
<link rel="canonical" href="{u}">
<meta property="og:type" content="article"><meta property="og:title" content="{_html.escape(a['titulo_txt'])}"><meta property="og:description" content="{_html.escape(a['resumo'])}">
<meta property="og:url" content="{u}"><meta property="og:image" content="{BASE_URL}assets/photos/{a['foto']}.jpg"><meta property="og:locale" content="pt_BR">"""
    from pages2 import cta, post_card
    outros = [x for x in ARTIGOS if x['slug'] != a['slug']][:2]
    mais = ''.join(post_card('pt', x).replace('href="novidades/', 'href="') for x in outros)
    main = f"""<article class="article">
<header class="art-head"><div class="wrap narrow">
  <a class="back" href="{npre}{FILES['pt']['blog']}">‹ Todas as novidades</a>
  <p class="post-meta"><span class="post-tag">{a['categoria']}</span><span>{data_pt(a['data'])}</span></p>
  <h1 class="display art-title">{a['titulo']}</h1>
  <p class="lead">{a['resumo']}</p>
</div></header>
<div class="wrap"><div class="photo art-photo"><img src="{pre}assets/photos/{a['foto']}.jpg" alt="{a['foto_alt']}" decoding="async"></div></div>
<div class="wrap narrow art-body">
  <aside class="art-box"><p class="kicker">Em resumo</p><ul>{box}</ul></aside>
  {a['corpo']}
  <div class="art-src"><p class="kicker">Fontes</p><ul>{fontes}</ul></div>
  <p class="note">Conteúdo informativo, nos termos do Provimento nº 205/2021 do Conselho Federal da OAB. Cada caso tem suas particularidades e deve ser avaliado por um advogado.</p>
</div>
</article>
{'<section class="section-tight"><div class="wrap"><div class="head"><p class="kicker">Leia também</p></div><div class="post-grid">' + mais + '</div></div></section>' if mais else ''}
{cta('pt')}"""
    for v in FILES['pt'].values():
        main = main.replace(f'href="{v}"', f'href="../{v}"')
    body = f"""{header('pt', 'blog', pre, npre)}
<main id="conteudo">{main}
</main>
{footer('pt', pre, npre)}
<script src="{pre}assets/main.js" defer></script>"""
    return f'<!doctype html>\n<html lang="pt-BR">\n<head>\n{head_html}\n</head>\n<body>\n{body}\n</body>\n</html>\n'


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'en'))
    os.makedirs(os.path.join(OUT, 'assets'))
    for f in ['styles.css', 'main.js']:
        shutil.copy(os.path.join(HERE, 'src', f), os.path.join(OUT, 'assets', f))
    for f in os.listdir(os.path.join(HERE, 'img')):
        if f.endswith('.png'):
            shutil.copy(os.path.join(HERE, 'img', f), os.path.join(OUT, 'assets', f))
    shutil.copytree(os.path.join(HERE, 'fonts'), os.path.join(OUT, 'assets', 'fonts'))
    os.makedirs(os.path.join(OUT, 'assets', 'photos'), exist_ok=True)
    for f in os.listdir(os.path.join(HERE, 'img', 'photos')):
        shutil.copy(os.path.join(HERE, 'img', 'photos', f), os.path.join(OUT, 'assets', 'photos', f))
    for lang in ['pt', 'en']:
        for k in KEYS:
            p = os.path.join(OUT, 'en' if lang == 'en' else '', FILES[lang][k])
            open(p, 'w', encoding='utf-8').write(render(lang, k))
    os.makedirs(os.path.join(OUT, 'novidades'), exist_ok=True)
    for a in ARTIGOS:
        open(os.path.join(OUT, 'novidades', a['slug'] + '.html'), 'w', encoding='utf-8').write(render_article(a))
    # prévia no Claude: página inicial sem esqueleto
    open(os.path.join(HERE, 'artifact-index.html'), 'w', encoding='utf-8').write(render('pt', 'home', artifact=True))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ['pt', 'en']:
        for k in KEYS:
            sm.append(f'<url><loc>{url(lang, k)}</loc>'
                      f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{url("pt", k)}"/>'
                      f'<xhtml:link rel="alternate" hreflang="en" href="{url("en", k)}"/></url>')
    for a in ARTIGOS:
        sm.append(f"<url><loc>{BASE_URL}novidades/{a['slug']}.html</loc><lastmod>{a['data']}</lastmod></url>")
    sm.append('</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n')
    # GitHub Pages: dominio proprio e sem processamento Jekyll
    open(os.path.join(OUT, 'CNAME'), 'w').write('correialamunier.com\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    # Imagens da assinatura de e-mail do Victor (links usados no Outlook). NAO REMOVER:
    # sem esta pasta, toda publicacao apaga /assinatura/ e as assinaturas ficam com '?'.
    shutil.copytree(os.path.join(HERE, 'assinatura'), os.path.join(OUT, 'assinatura'))
    print('ok')


main()
