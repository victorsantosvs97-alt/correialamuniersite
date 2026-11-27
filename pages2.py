# -*- coding: utf-8 -*-
# Site v2 — conteúdo e marcação das páginas (PT e EN)
import os
from content_v1 import FILES
from artigos import ARTIGOS, data_pt, data_en

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTOS = os.path.join(HERE, 'img', 'photos')
PRE = ['']  # prefixo de caminho (definido por página)


def L(lang, key):
    return FILES[lang][key]


def photo(name, alt, fallback, pending=None, eager=False):
    """Foto real se existir em img/photos/<name>.jpg; senão um fundo de reserva da marca."""
    f = os.path.join(PHOTOS, name + '.jpg')
    if os.path.exists(f):
        load = 'eager' if eager else 'lazy'
        return f'<div class="photo"><img src="{PRE[0]}assets/photos/{name}.jpg" alt="{alt}" loading="{load}" decoding="async"></div>'
    tag = f'<span class="pending">{pending}</span>' if pending else ''
    return f'<div class="photo"><div class="ph ph-{fallback}" role="img" aria-label="{alt}"></div>{tag}</div>'


def portrait(name, initials, alt, pending):
    f = os.path.join(PHOTOS, name + '.jpg')
    if os.path.exists(f):
        return f'<div class="photo"><img src="{PRE[0]}assets/photos/{name}.jpg" alt="{alt}" loading="lazy"></div>'
    return f'<div class="photo"><div class="monogram" role="img" aria-label="{alt}">{initials}</div><span class="pending">{pending}</span></div>'


T = {
 'pt': dict(
   pend_photo='Foto em breve',
   book='Agendar uma conversa', know='Conheça o escritório', more='Saiba mais', talk='Falar com um sócio',
   wa='Fale no WhatsApp',
 ),
 'en': dict(
   pend_photo='Photo coming soon',
   book='Book a conversation', know='About the firm', more='Learn more', talk='Talk to a partner',
   wa='Chat on WhatsApp',
 ),
}


def partners(lang):
    t = T[lang]
    if lang == 'pt':
        a = ('Sócia · OAB/SP 152.191', 'Previdenciário e trabalhista: aposentadorias, revisões de benefícios, defesa de empresas e direitos de quem trabalha.')
        b = ('Sócio · OAB/SP 452.969', 'Empresarial, contratos, holding e planejamento patrimonial, família, sucessões, imobiliário e consumidor.')
    else:
        a = ('Partner · OAB/SP 152.191', 'Pensions and employment law: retirement and social-security benefits, employer defence and employee rights.')
        b = ('Partner · OAB/SP 452.969', 'Corporate, contracts, holding structures and estate planning, family, probate, property and consumer law.')
    return f'''<div class="people">
  <article class="person reveal">{portrait('socia-cristiane', 'CL', 'Cristiane Lamunier Alexandre Mongelli', t['pend_photo'])}<div class="txt"><p class="oab">{a[0]}</p><h3>Cristiane Lamunier Alexandre Mongelli</h3><p>{a[1]}</p></div></article>
  <article class="person reveal">{portrait('socio-victor', 'VC', 'Victor Correia Santos', t['pend_photo'])}<div class="txt"><p class="oab">{b[0]}</p><h3>Victor Correia Santos</h3><p>{b[1]}</p></div></article>
</div>'''


def steps(lang):
    s = ([('Conversa', 'Uma reunião com o sócio responsável, presencial ou por vídeo, para entender a sua situação.'),
          ('Análise', 'Lemos os documentos e explicamos os caminhos possíveis, em linguagem simples.'),
          ('Proposta', 'Escopo e honorários combinados por escrito, antes de qualquer passo.'),
          ('Acompanhamento', 'Você recebe notícias do andamento e respostas rápidas durante todo o caso.')]
         if lang == 'pt' else
         [('Conversation', 'A meeting with the partner in charge, in person or by video, to understand your situation.'),
          ('Review', 'We read the documents and explain the options in plain language.'),
          ('Proposal', 'Scope and fees agreed in writing before any step is taken.'),
          ('Follow-through', 'Regular updates and quick answers for as long as the matter runs.')])
    return '<ol class="steps">' + ''.join(f'<li class="reveal"><h3>{a}</h3><p>{b}</p></li>' for a, b in s) + '</ol>'


def cta(lang):
    t = T[lang]
    if lang == 'pt':
        h, p = 'Vamos conversar sobre o <em>seu caso</em>?', 'Conte em poucas linhas do que se trata. Um dos sócios retorna para marcar a conversa, presencial ou online.'
    else:
        h, p = 'Shall we talk about <em>your matter</em>?', 'Tell us briefly what it is about. A partner will get back to you to arrange a meeting, in person or online.'
    return f'''<section class="section-tight cta"><div class="wrap"><div class="box reveal">
  <h2 class="title">{h}</h2><p class="lead">{p}</p>
  <div class="actions center"><a class="btn btn-primary" href="{L(lang,'contact')}">{t['book']}</a><a class="btn btn-ghost" href="https://wa.me/5511917386432" rel="noopener">{t['wa']}</a></div>
</div></div></section>'''


def page_hero(kicker, title, lead, ph_name, ph_fallback, ph_alt, lang):
    return f'''<section class="page-hero"><div class="wrap">
  <p class="kicker">{kicker}</p><h1 class="display">{title}</h1><p class="lead">{lead}</p>
  {photo(ph_name, ph_alt, ph_fallback, None, eager=True)}
</div></section>'''


IG_URL = 'https://www.instagram.com/correiasantoslamunier/'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>'


def instagram(lang):
    if lang == 'pt':
        k, h, p, b = 'Instagram', 'Direito do dia a dia, <em>sem juridiquês.</em>', 'No nosso Instagram, explicamos decisões, leis novas e situações comuns em linguagem simples. Acompanhe.', 'Seguir no Instagram'
    else:
        k, h, p, b = 'Instagram', 'Everyday law, <em>in plain words.</em>', 'On Instagram we explain court decisions, new laws and common situations in plain Portuguese. Follow along.', 'Follow on Instagram'
    return f'''<section class="section-tight"><div class="wrap"><div class="ig reveal">
  <div class="ig-txt"><p class="kicker">{k}</p><h2 class="title">{h}</h2><p class="lead">{p}</p>
    <div class="actions"><a class="btn btn-primary" href="{IG_URL}" rel="noopener">{b}</a></div></div>
  <a class="ig-card" href="{IG_URL}" rel="noopener" aria-label="@correiasantoslamunier no Instagram"><span class="ig-icon">{IG_SVG}</span><span class="ig-handle">@correiasantoslamunier</span><span class="ig-sub">Correia Santos &amp; Lamunier Advogados</span></a>
</div></div></section>'''


def practice_grid(items):
    out = []
    for h, intro, lis in items:
        li = ''.join(f'<li>{x}</li>' for x in lis)
        out.append(f'<article class="practice reveal"><h3>{h}</h3><p class="intro">{intro}</p><ul>{li}</ul></article>')
    return '<div class="practice-grid">' + ''.join(out) + '</div>'


# ======================================================================= INÍCIO
def page_home(lang):
    t = T[lang]
    pt = lang == 'pt'
    areas = ([
        ('Empresas', 'Trabalhista', 'Prevenir o passivo e defender a empresa quando a reclamação chega.', 'business'),
        ('Empresas', 'Societário e contratos', 'Regras claras entre sócios, clientes e fornecedores.', 'business'),
        ('Empresas e famílias', 'Holding e patrimônio', 'A sucessão da empresa e da família organizada em vida.', 'business'),
        ('Empresas', 'Saúde e regulatório', 'Clínicas, farmácias e cannabis medicinal: LGPD e Anvisa.', 'business'),
        ('Para você', 'Família', 'Divórcio, pensão, guarda e união estável, com cuidado.', 'individuals'),
        ('Para você', 'Herança e inventário', 'Partilha em cartório ou na Justiça, com respeito ao momento.', 'individuals'),
        ('Para você', 'Imóveis', 'Comprar, vender, regularizar e resolver conflitos.', 'individuals'),
        ('Para você', 'Previdenciário', 'Aposentadorias, revisões e pedidos negados pelo INSS.', 'individuals'),
        ('Para você', 'Consumidor', 'Voos cancelados, bancos e serviços que não cumpriram o prometido.', 'individuals'),
        ('Mora fora', 'Brasileiros no exterior', 'Herança, imóvel e documentos no Brasil, sem precisar viajar.', 'abroad'),
    ] if pt else [
        ('Business', 'Employment', 'Reducing exposure and defending the company when a claim arrives.', 'business'),
        ('Business', 'Corporate and contracts', 'Clear rules between partners, customers and suppliers.', 'business'),
        ('Business and families', 'Holdings and estate planning', 'Succession in the family and the family business, planned ahead.', 'business'),
        ('Business', 'Healthcare regulation', 'Clinics, pharmacies and medical cannabis: data protection and ANVISA.', 'business'),
        ('Individuals', 'Family', 'Divorce, support, custody and common-law unions, handled with care.', 'individuals'),
        ('Individuals', 'Inheritance and probate', 'Estates settled at a notary or in court, at the family’s pace.', 'individuals'),
        ('Individuals', 'Property', 'Buying, selling, regularising and resolving disputes.', 'individuals'),
        ('Individuals', 'Pensions', 'Retirement, benefit reviews and INSS refusals.', 'individuals'),
        ('Individuals', 'Consumer', 'Cancelled flights, banks and services that fell short.', 'individuals'),
        ('Living abroad', 'Brazilians abroad', 'Inheritance, property and paperwork in Brazil without travelling.', 'abroad'),
    ])
    cards = ''.join(f'<a class="card" href="{L(lang,k)}"><span class="tag">{tg}</span><h3>{h}</h3><p>{p}</p><span class="more">{t["more"]}</span></a>' for tg, h, p, k in areas)

    if pt:
        faq = [
            ('Vocês atendem só em São Paulo?', 'Não. Atendemos empresas e famílias em todo o Brasil e brasileiros em qualquer país. Os processos são eletrônicos e as reuniões podem ser por vídeo, então a distância não é obstáculo.'),
            ('Posso ser atendido totalmente online?', 'Sim. Reuniões por vídeo, assinatura eletrônica e processos digitais permitem conduzir quase tudo à distância, no Brasil ou no exterior. Quando algo exige presença, explicamos antes.'),
            ('Como são definidos os honorários?', 'Depois da primeira conversa, o sócio responsável envia uma proposta por escrito, com o escopo do trabalho e os honorários. Nada começa sem a sua concordância.'),
            ('Quem vai cuidar do meu caso?', 'Um dos sócios, do começo ao fim. Você fala diretamente com quem conduz o seu caso.'),
            ('Moro fora do Brasil. Como funciona a procuração?', 'Explicamos como outorgar a procuração no país onde você mora e quais documentos são necessários, para que possamos representar você no Brasil.'),
            ('O que eu conto fica em sigilo?', 'Sim. O sigilo profissional é um dever do advogado. As informações do seu caso ficam entre você e o escritório.'),
        ]
    else:
        faq = [
            ('Do you only work in São Paulo?', 'No. We act for companies and families across Brazil and for Brazilians in any country. Court files are electronic and meetings can be held by video, so distance is not an obstacle.'),
            ('Can everything be handled online?', 'Yes. Video meetings, e-signatures and electronic court files let us handle almost everything remotely, in Brazil or abroad. When something requires attendance in person, we tell you in advance.'),
            ('How are fees set?', 'After the first conversation, the partner in charge sends a written proposal with the scope of work and the fees. Nothing starts without your agreement.'),
            ('Who will handle my matter?', 'One of the partners, from start to finish. You speak directly to the person running your matter.'),
            ('I live outside Brazil. How does the power of attorney work?', 'We explain how to grant a power of attorney in your country of residence and which documents are needed, so we can represent you in Brazil.'),
            ('Is what I tell you confidential?', 'Yes. Professional secrecy is a legal duty for lawyers in Brazil. Your information stays between you and the firm.'),
        ]
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)

    if pt:
        hero = ('Correia Santos &amp; Lamunier Advogados', 'Do seu lado, <em>do começo ao fim.</em>',
                'Advocacia próxima para empresas e famílias, onde você estiver.')
        glass = '<span><i class="dot"></i><b>Sócio</b> à frente de cada caso</span><span><i class="dot"></i><b>Presencial</b> e online</span><span><i class="dot"></i>Todo o Brasil e o mundo</span>'
        tiles = (('Para empresas', 'Menos risco na operação. Defesa firme quando o processo chega.'),
                 ('Para você e sua família', 'Família, herança e patrimônio tratados com escuta e discrição.'))
        stmt = ('<span>Quem atende você</span> <span>é quem conduz</span> <span>o seu caso.</span>',
                'Somos um escritório de porte boutique. Não há repasse para equipes que você não conhece: cada cliente fala diretamente com o sócio responsável, recebe explicações claras e combina tudo por escrito.')
        rail = ('Em que podemos ajudar', 'Áreas de atuação')
        how = ('Como trabalhamos', 'Um jeito de advogar que <em>cabe na sua vida.</em>')
        bento = [('Prevenção primeiro', 'Contratos, rotinas e documentos revistos antes do conflito, quando resolver custa menos.'),
                 ('Áreas integradas', 'Trabalhista, societário, família e patrimônio olhando o mesmo caso juntos.'),
                 ('Transparência', 'Escopo e honorários por escrito, antes de qualquer passo.'),
                 ('Atendimento digital', 'Vídeo, assinatura eletrônica e processos digitais, de onde você estiver.')]
        big = ('Sócio no atendimento', 'Quem recebe você é quem conduz o caso. Sem intermediários, sem respostas genéricas.')
        abroad = ('Mora fora do Brasil?', 'Resolvemos no Brasil <em>sem você precisar viajar.</em>',
                  'Seja qual for o país em que você mora, cuidamos do que precisa ser resolvido no Brasil, com atendimento 100% online.',
                  [('Herança no Brasil', 'Inventário com herdeiro morando fora'), ('Imóvel no Brasil', 'Venda, locação e regularização à distância'),
                   ('Divórcio e sentenças estrangeiras', 'Divórcio no Brasil e validade de decisões de fora'), ('Representação', 'Procuração e atuação em seu nome')],
                  'Agora no Brasil', 'Agora onde você está', 'Ver como funciona')
        start = ('Como começamos', 'Quatro passos, <em>sem compromisso</em> até a proposta.')
        team = ('Sócios', 'Quem vai cuidar de você.')
        faqh = ('Perguntas frequentes', 'Antes de conversar.')
    else:
        hero = ('Correia Santos &amp; Lamunier Advogados', 'On your side, <em>from start to finish.</em>',
                'Personal Brazilian legal advice for companies and families, wherever you are.')
        glass = '<span><i class="dot"></i><b>Partner-led</b> on every matter</span><span><i class="dot"></i><b>In person</b> and online</span><span><i class="dot"></i>All of Brazil and worldwide</span>'
        tiles = (('For business', 'Less risk in day-to-day operations. A firm defence when a claim arrives.'),
                 ('For you and your family', 'Family, inheritance and wealth handled with attention and discretion.'))
        stmt = ('<span>The lawyer you meet</span> <span>is the lawyer who runs</span> <span>your matter.</span>',
                'We are a boutique firm. There is no hand-off to people you have never met: every client speaks directly to the partner in charge, gets clear explanations and agrees everything in writing.')
        rail = ('How we can help', 'Practice areas')
        how = ('How we work', 'Legal advice that <em>fits your life.</em>')
        bento = [('Prevention first', 'Contracts and routines reviewed before a dispute, when solving it costs less.'),
                 ('Joined-up advice', 'Employment, corporate, family and estate issues looked at together.'),
                 ('Transparency', 'Scope and fees in writing before any step is taken.'),
                 ('Fully digital', 'Video, e-signatures and electronic court files, wherever you are.')]
        big = ('Partner-led', 'The person who welcomes you runs your matter. No intermediaries, no generic answers.')
        abroad = ('Living outside Brazil?', 'We handle it in Brazil <em>so you don’t have to travel.</em>',
                  'Whichever country you live in, we take care of what needs to be resolved in Brazil, working fully online.',
                  [('Inheritance in Brazil', 'Probate when an heir lives overseas'), ('Property in Brazil', 'Selling, letting and regularising from a distance'),
                   ('Divorce and foreign judgments', 'Divorce in Brazil and recognition of foreign decisions'), ('Representation', 'Powers of attorney and acting on your behalf')],
                  'Now in Brazil', 'Now where you are', 'How it works')
        start = ('Getting started', 'Four steps, <em>no commitment</em> until the proposal.')
        team = ('Partners', 'Who will look after you.')
        faqh = ('Questions', 'Before we talk.')

    checks = ''.join(f'<li><div><b>{a}</b><span>{b}</span></div></li>' for a, b in abroad[3])
    bento_html = ''.join(
        f'<div class="reveal{" dark" if i == 1 else ""}"><span class="glyph">{g}</span><h3>{h}</h3><p>{p}</p></div>'
        for i, ((h, p), g) in enumerate(zip(bento, ['§', '∞', '✓', '↗'])))

    return f'''
<section class="hero"><div class="wrap">
  <div class="hero-logo"><img src="{PRE[0]}assets/logo-hero.png" alt="Correia Santos &amp; Lamunier Advogados" width="380" height="145"></div>
  <h1 class="display">{hero[1]}</h1>
  <p class="lead">{hero[2]}</p>
  <div class="actions"><a class="btn btn-primary" href="{L(lang,'contact')}">{t['book']}</a><a class="more" href="{L(lang,'firm')}">{t['know']}</a></div>
  <div class="hero-media">{photo('hero-sao-paulo', 'São Paulo' if pt else 'São Paulo skyline', 'city', None, eager=True)}<p class="glass">{glass}</p></div>
</div></section>

<section class="section-tight"><div class="wrap tiles">
  <a class="tile tile-dark reveal" href="{L(lang,'business')}">{photo('empresas', '', 'business')}<div class="tile-body"><h2>{tiles[0][0]}</h2><p>{tiles[0][1]}</p><div class="actions"><span class="more">{t['more']}</span></div></div></a>
  <a class="tile tile-light reveal" href="{L(lang,'individuals')}">{photo('familia', '', 'family')}<div class="tile-body"><h2>{tiles[1][0]}</h2><p>{tiles[1][1]}</p><div class="actions"><span class="more">{t['more']}</span></div></div></a>
</div></section>

<section class="section bg-dark on-dark"><div class="wrap statement-wrap">
  <p class="statement" data-statement>{stmt[0]}</p>
  <p class="lead">{stmt[1]}</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="rail-head"><div class="head" style="margin:0"><p class="kicker">{rail[0]}</p><h2 class="title">{rail[1]}</h2></div>
    <div class="rail-btns" aria-hidden="true"><button type="button" data-rail="-1">‹</button><button type="button" data-rail="1">›</button></div></div>
  <div class="rail" id="rail">{cards}</div>
</div></section>

<section class="section bg-sand"><div class="wrap">
  <div class="head"><p class="kicker">{how[0]}</p><h2 class="title">{how[1]}</h2></div>
  <div class="bento">
    <div class="big reveal">{photo('reuniao', '', 'meeting')}<div class="txt"><h3>{big[0]}</h3><p>{big[1]}</p></div></div>
    {bento_html}
  </div>
</div></section>

<section class="section"><div class="wrap split">
  {photo('exterior', '', 'abroad')}
  <div class="head" style="margin:0">
    <p class="kicker">{abroad[0]}</p><h2 class="title">{abroad[1]}</h2><p class="lead">{abroad[2]}</p>
    <ul class="checks">{checks}</ul>
    <div class="clocks"><div class="clock"><small>{abroad[4]}</small><b data-tz="America/Sao_Paulo">--:--</b></div><div class="clock"><small>{abroad[5]}</small><b data-tz="local">--:--</b></div></div>
    <div class="actions" style="margin-top:12px"><a class="more" href="{L(lang,'abroad')}">{abroad[6]}</a></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="head center"><p class="kicker">{start[0]}</p><h2 class="title">{start[1]}</h2></div>
  {steps(lang)}
</div></section>

<section class="section"><div class="wrap">
  <div class="head"><p class="kicker">{team[0]}</p><h2 class="title">{team[1]}</h2></div>
  {partners(lang)}
</div></section>

<section class="section bg-white"><div class="wrap narrow">
  <div class="head"><p class="kicker">{faqh[0]}</p><h2 class="title">{faqh[1]}</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>
{blog_teaser(lang)}
{instagram(lang)}
{cta(lang)}'''


# ======================================================================= EMPRESAS
def page_business(lang):
    pt = lang == 'pt'
    if pt:
        items = [
            ('Trabalhista empresarial', 'Prevenir o passivo e defender a empresa quando a reclamação chega, até o TST.',
             ['Rotinas de RH, jornadas e políticas internas', 'Planos de premiação e remuneração variável', 'Terceirização e cota de aprendizes',
              'Advertências, notificações e desligamentos', 'Defesa e preparação para audiências', 'Recursos aos Tribunais Regionais e ao TST']),
            ('Societário', 'Regras claras entre sócios, definidas antes de o conflito aparecer.',
             ['Constituição e alterações contratuais', 'Acordo de sócios ou de quotistas', 'Entrada, saída e retirada de sócio',
              'Apuração de haveres e cessão de quotas', 'Compra e venda de empresa ou ponto comercial', 'Representação de sócio que mora no exterior']),
            ('Contratos', 'Contratos que protegem a operação e evitam discussão depois.',
             ['Clientes e fornecedores', 'Prestação de serviços e parcerias', 'Locação comercial', 'Confidencialidade e não concorrência',
              'Revisão e negociação de minutas', 'Notificações extrajudiciais']),
            ('Holding e planejamento patrimonial', 'A sucessão da empresa familiar organizada em vida. Com a Reforma Tributária, o ITCMD passou a ser obrigatoriamente progressivo (EC 132/2023).',
             ['Holding familiar e patrimonial', 'Sucessão na empresa de família', 'Doações com reserva de usufruto', 'Cláusulas de proteção do patrimônio',
              'Acordo de família entre herdeiros', 'Inventário, quando chegar a hora']),
            ('Saúde e regulatório', 'Clínicas, consultórios, farmácias e cannabis medicinal.',
             ['Adequação à LGPD para dados de pacientes', 'Contratos com fornecedores de prontuário', 'Plano de resposta a incidentes',
              'Novas regras da Anvisa para cannabis medicinal', 'Associações de pacientes', 'Sociedade entre profissionais de saúde']),
            ('Consumidor, crédito e imobiliário', 'Defesa da empresa e recuperação do que lhe é devido.',
             ['Defesa em ações de clientes e Procon', 'Responsabilidade civil e indenizações', 'Cobrança extrajudicial e judicial',
              'Execuções e ações monitórias', 'Compra e locação de imóvel comercial', 'Venda de ponto comercial (trespasse)']),
        ]
        sectors = ['Hotelaria e hospitalidade', 'Clínicas e farmácias', 'Bares, cafés e restaurantes', 'Indústria e comércio',
                   'Engenharia e manutenção', 'Serviços e pesquisa de mercado', 'Associações e entidades', 'Empresas familiares']
        hero = page_hero('Para empresas', 'Do dia a dia da operação <em>ao tribunal.</em>',
                         'Prevenção, contratos e defesa conduzidos por um sócio que conhece o seu negócio.', 'empresas', 'business', 'Reunião de negócios', lang)
        h2, sec, note, st = 'O que fazemos pela sua empresa.', 'Setores que já atendemos', 'Por dever de sigilo profissional, não divulgamos nomes de clientes.', 'Como começamos'
    else:
        items = [
            ('Employment law for employers', 'Reducing exposure and defending the company when a claim is filed, up to the Superior Labour Court.',
             ['HR routines, working hours and policies', 'Bonus and variable-pay plans', 'Outsourcing and apprenticeship quotas',
              'Warnings, notices and terminations', 'Defences and hearing preparation', 'Appeals to the Regional Courts and the TST']),
            ('Corporate', 'Clear rules between shareholders, agreed before any dispute.',
             ['Incorporation and amendments', 'Shareholders’ agreements', 'Entry and exit of partners',
              'Valuing a departing partner’s share', 'Sale and purchase of businesses', 'Acting for partners who live abroad']),
            ('Contracts', 'Contracts that protect the business and prevent disputes later.',
             ['Customers and suppliers', 'Services and partnerships', 'Commercial leases', 'Confidentiality and non-compete',
              'Drafting, review and negotiation', 'Formal notices']),
            ('Holding structures and estate planning', 'Succession in a family business planned during the owners’ lifetime. Brazil’s tax reform made inheritance tax (ITCMD) mandatorily progressive (Amendment 132/2023).',
             ['Family holding companies', 'Family-business succession', 'Gifts with retained usufruct', 'Asset-protection clauses',
              'Family agreements between heirs', 'Probate when the time comes']),
            ('Healthcare regulation', 'Clinics, practices, pharmacies and medical cannabis.',
             ['LGPD compliance for patient data', 'Electronic-records provider contracts', 'Incident-response plans',
              'New ANVISA rules on medical cannabis', 'Patient associations', 'Partnerships between health professionals']),
            ('Consumer, debt recovery and property', 'Defending the company and recovering what it is owed.',
             ['Defence in consumer claims', 'Civil liability and damages', 'Out-of-court and court debt recovery',
              'Enforcement and summary proceedings', 'Commercial property', 'Sale of a going concern']),
        ]
        sectors = ['Hospitality', 'Clinics and pharmacies', 'Bars, cafés and restaurants', 'Industry and trade',
                   'Engineering and maintenance', 'Services and market research', 'Associations', 'Family businesses']
        hero = page_hero('For business', 'From daily operations <em>to court.</em>',
                         'Prevention, contracts and litigation led by a partner who knows your business.', 'empresas', 'business', 'Business meeting', lang)
        h2, sec, note, st = 'What we do for your company.', 'Sectors we have served', 'Professional secrecy rules mean we do not disclose client names.', 'Getting started'
    pills = ''.join(f'<span class="pill">{s}</span>' for s in sectors)
    return f'''{hero}
<section class="section-tight"><div class="wrap"><div class="head"><h2 class="title">{h2}</h2></div>{practice_grid(items)}</div></section>
<section class="section bg-dark on-dark"><div class="wrap"><div class="head"><p class="kicker">{sec}</p></div><div class="pills">{pills}</div><p class="note">{note}</p></div></section>
<section class="section bg-white"><div class="wrap"><div class="head center"><p class="kicker">{st}</p></div>{steps(lang)}</div></section>
{cta(lang)}'''


# ======================================================================= PESSOA FÍSICA
def page_individuals(lang):
    pt = lang == 'pt'
    if pt:
        items = [
            ('Família', 'Momentos difíceis conduzidos com cuidado e firmeza.',
             ['Divórcio em cartório ou judicial', 'Partilha de bens', 'Pensão: pedido, revisão e cobrança', 'Guarda compartilhada e convivência',
              'União estável', 'Pacto antenupcial']),
            ('Herança e inventário', 'Cuidar da partilha com respeito ao momento da família.',
             ['Inventário em cartório, quando possível', 'Inventário judicial', 'Partilha entre herdeiros', 'Testamento',
              'Herdeiro que mora no exterior', 'Alvarás e regularização de bens']),
            ('Planejamento patrimonial', 'Com a Reforma Tributária, o ITCMD passou a ser obrigatoriamente progressivo em todo o país (EC 132/2023). Planejar em vida evita conflitos e surpresas.',
             ['Holding familiar', 'Doações com reserva de usufruto', 'Cláusulas de proteção', 'Organização da sucessão',
              'Acordos entre herdeiros', 'Revisão do planejamento ao longo do tempo']),
            ('Imóveis', 'O imóvel é, muitas vezes, o maior bem da família.',
             ['Análise de documentos antes de comprar', 'Compra, venda e locação', 'Usucapião judicial e em cartório',
              'Regularização de imóvel e escritura', 'Construtoras e loteadoras', 'Conflitos de vizinhança']),
            ('Consumidor', 'Quando o serviço contratado não é entregue como prometido.',
             ['Voos cancelados e bagagem extraviada', 'Pacotes e agências de viagem', 'Cobranças indevidas de bancos',
              'Produtos e serviços com defeito', 'Negativação indevida', 'Indenizações']),
            ('Previdenciário e trabalhista', 'Os seus direitos como segurado e como trabalhador.',
             ['Aposentadoria e planejamento previdenciário', 'Revisão de benefícios', 'Pedidos negados pelo INSS',
              'Verbas de rescisão não pagas', 'Horas extras e adicionais', 'Reconhecimento de vínculo']),
        ]
        hero = page_hero('Para você e sua família', 'Advocacia que escuta <em>antes de falar.</em>',
                         'Família, herança, patrimônio, imóveis e direitos do dia a dia, com honorários sempre combinados por escrito.', 'familia', 'family', 'Família reunida', lang)
        h2, st = 'Em que podemos ajudar você.', 'Como começamos'
    else:
        items = [
            ('Family', 'Difficult moments handled with care and resolve.',
             ['Divorce at a notary or in court', 'Division of assets', 'Support: claims, reviews and enforcement', 'Shared custody and contact',
              'Common-law unions', 'Prenuptial agreements']),
            ('Inheritance and probate', 'Settling an estate with respect for the family’s moment.',
             ['Out-of-court probate, when possible', 'Court probate', 'Division between heirs', 'Wills',
              'Heirs living abroad', 'Court authorisations and asset regularisation']),
            ('Estate planning', 'Brazil’s tax reform made inheritance and gift tax (ITCMD) mandatorily progressive (Amendment 132/2023). Planning ahead avoids disputes and surprises.',
             ['Family holding companies', 'Gifts with retained usufruct', 'Asset-protection clauses', 'Succession planning',
              'Agreements between heirs', 'Periodic review']),
            ('Property', 'A home is often a family’s largest asset.',
             ['Title checks before buying', 'Sale, purchase and leases', 'Adverse possession (usucapião)',
              'Regularising property and deeds', 'Disputes with developers', 'Neighbour disputes']),
            ('Consumer', 'When a service you paid for is not delivered as promised.',
             ['Cancelled flights and lost luggage', 'Travel agencies and packages', 'Unfair bank charges',
              'Defective products and services', 'Wrongful credit listings', 'Damages']),
            ('Pensions and employment', 'Your rights as an insured person and as an employee.',
             ['Retirement and pension planning', 'Benefit reviews', 'Benefits refused by the INSS',
              'Unpaid termination amounts', 'Overtime and allowances', 'Recognition of employment']),
        ]
        hero = page_hero('For you and your family', 'Legal advice that listens <em>before it speaks.</em>',
                         'Family, inheritance, wealth, property and everyday rights under Brazilian law, with fees always agreed in writing.', 'familia', 'family', 'Family together', lang)
        h2, st = 'How we can help you.', 'Getting started'
    return f'''{hero}
<section class="section-tight"><div class="wrap"><div class="head"><h2 class="title">{h2}</h2></div>{practice_grid(items)}</div></section>
<section class="section bg-white"><div class="wrap"><div class="head center"><p class="kicker">{st}</p></div>{steps(lang)}</div></section>
{cta(lang)}'''


# ======================================================================= EXTERIOR
def page_abroad(lang):
    pt = lang == 'pt'
    if pt:
        items = [
            ('Herança no Brasil', 'Quando um familiar falece no Brasil e você mora fora.',
             ['Inventário com herdeiro no exterior', 'Procuração para representar você', 'Partilha e transferência de bens',
              'Venda de imóvel do espólio', 'Contas e investimentos no Brasil', 'Documentos emitidos fora']),
            ('Imóvel no Brasil', 'Vender, alugar ou regularizar sem precisar viajar.',
             ['Venda por não residente', 'Locação e administração', 'Escritura e matrícula', 'Usucapião',
              'Conflitos com inquilinos e vizinhos', 'Recebimento seguro dos valores']),
            ('Família à distância', 'Divórcio, pensão e guarda quando uma das partes mora fora.',
             ['Divórcio no Brasil', 'Validade de sentença estrangeira', 'Pensão alimentícia internacional',
              'Guarda e convivência entre países', 'Autorização de viagem de filhos', 'Pacto antenupcial']),
            ('Empresa e documentos', 'A sua vida no Brasil em ordem enquanto você está fora.',
             ['Representação de sócio no exterior', 'Alterações societárias à distância', 'Encerramento de empresa',
              'Pendências de CPF e cadastros', 'Procurações em geral', 'Acompanhamento de processos']),
        ]
        hero = page_hero('Brasileiros no exterior', 'Longe do Brasil, <em>perto de quem resolve.</em>',
                         'Atendemos de forma 100% online quem vive fora, em qualquer país, e precisa cuidar de algo no Brasil.', 'exterior', 'abroad', 'Viagem', lang)
        h2 = 'As situações mais comuns de quem mora fora.'
        how = ('Atendimento à distância', 'Tudo resolvido de onde você estiver.')
        vals = [('Reuniões por vídeo', 'No horário que funciona para você, no seu fuso.'), ('Assinatura eletrônica', 'Documentos assinados digitalmente sempre que a lei permite.'),
                ('Procuração', 'Explicamos como outorgar a procuração no país onde você mora.'), ('Andamento informado', 'Notícias por e-mail ou WhatsApp, sem você precisar perguntar.')]
        clocks = ('Agora no Brasil', 'Agora onde você está')
        note = 'O escritório atua exclusivamente com direito brasileiro. Questões de imigração, vistos ou leis de outros países devem ser tratadas com um profissional local.'
    else:
        items = [
            ('Inheritance in Brazil', 'When a relative dies in Brazil and you live abroad.',
             ['Probate with an heir overseas', 'Powers of attorney', 'Division and transfer of assets',
              'Selling estate property', 'Bank accounts and investments', 'Documents issued abroad']),
            ('Property in Brazil', 'Selling, letting or regularising without travelling.',
             ['Sales by non-residents', 'Leases and management', 'Deeds and land registry', 'Adverse possession',
              'Tenant and neighbour disputes', 'Secure receipt of proceeds']),
            ('Family across borders', 'Divorce, support and custody when one party lives abroad.',
             ['Divorce in Brazil', 'Recognition of foreign judgments', 'International child support',
              'Custody between countries', 'Travel authorisation for children', 'Prenuptial agreements']),
            ('Companies and paperwork', 'Your affairs in Brazil in order while you are away.',
             ['Acting for partners abroad', 'Corporate changes at a distance', 'Winding up a company',
              'CPF and registration issues', 'General powers of attorney', 'Monitoring court cases']),
        ]
        hero = page_hero('Brazilians abroad', 'Far from Brazil, <em>close to the solution.</em>',
                         'We work fully online for people who live abroad, in any country, and need something done in Brazil.', 'exterior', 'abroad', 'Travel', lang)
        h2 = 'The most common situations for Brazilians overseas.'
        how = ('Working remotely', 'Everything handled from wherever you are.')
        vals = [('Video meetings', 'At a time that works for you, in your time zone.'), ('E-signatures', 'Documents signed digitally wherever the law allows.'),
                ('Powers of attorney', 'We explain how to grant one in your country of residence.'), ('Regular updates', 'News by email or WhatsApp, without having to chase.')]
        clocks = ('Now in Brazil', 'Now where you are')
        note = 'The firm practises Brazilian law only. Immigration, visa or foreign-law questions should be taken to a local professional.'
    v = ''.join(f'<div class="reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in vals)
    return f'''{hero}
<section class="section-tight"><div class="wrap"><div class="head"><h2 class="title">{h2}</h2></div>{practice_grid(items)}</div></section>
<section class="section bg-sand"><div class="wrap">
  <div class="head"><p class="kicker">{how[0]}</p><h2 class="title">{how[1]}</h2></div>
  <div class="values">{v}</div>
  <div class="clocks" style="margin-top:28px"><div class="clock"><small>{clocks[0]}</small><b data-tz="America/Sao_Paulo">--:--</b></div><div class="clock"><small>{clocks[1]}</small><b data-tz="local">--:--</b></div></div>
  <p class="note" style="color:var(--muted)">{note}</p>
</div></section>
{cta(lang)}'''


# ======================================================================= O ESCRITÓRIO
def page_firm(lang):
    pt = lang == 'pt'
    if pt:
        hero = page_hero('O escritório', 'Advocacia feita <em>à mão.</em>',
                         'Fugimos do atendimento impessoal: cada cliente fala diretamente com o sócio que conduz o caso, do primeiro contato à solução.', 'escritorio', 'meeting', 'Escritório', lang)
        prose = '''<p class="kicker">Quem somos</p><h2 class="title">Correia Santos &amp; Lamunier Advogados</h2>
    <p>Somos uma sociedade de advogados registrada na Ordem dos Advogados do Brasil, Secção de São Paulo, sob o nº 48.284, com sede em Santana, na capital paulista.</p>
    <p>Atendemos empresas e famílias em todo o Brasil e no mundo, presencialmente ou online. A estrutura enxuta permite que os sócios acompanhem pessoalmente cada caso e que as áreas trabalhem juntas quando uma questão envolve mais de um tema.</p>
    <p>Acreditamos em uma advocacia humanizada: escuta atenta, linguagem clara, honorários combinados por escrito e notícias frequentes sobre o andamento.</p>'''
        vals = [('Ética', 'Atuação dentro do Código de Ética da OAB, sem promessa de resultado.'), ('Sigilo', 'Tudo o que você conta fica entre você e o escritório.'),
                ('Transparência', 'Escopo e honorários por escrito antes de qualquer passo.'), ('Proximidade', 'Contato direto com o sócio e retorno rápido.')]
        team, vh, oh = ('Sócios', 'Quem vai cuidar de você.'), ('Nossos compromissos', 'O que você pode esperar.'), ('Onde estamos', 'Sede em São Paulo. Atendimento em todo o Brasil e no mundo.')
        offices = [('Agora', 'America/Sao_Paulo', 'São Paulo · Brasil · Sede', 'Rua Doutor César, 1368, Santana<br>CEP 02013-080'),
                   ('Agora onde você está', 'local', 'Online · Brasil e mundo', 'Reuniões por vídeo, de qualquer cidade ou país.')]
    else:
        hero = page_hero('The firm', 'Legal work, <em>made by hand.</em>',
                         'No impersonal service: every client speaks directly to the partner who runs the matter, from first contact to resolution.', 'escritorio', 'meeting', 'Office', lang)
        prose = '''<p class="kicker">Who we are</p><h2 class="title">Correia Santos &amp; Lamunier Advogados</h2>
    <p>We are a Brazilian law firm registered with the Brazilian Bar Association, São Paulo Section (OAB/SP), under no. 48.284, with our head office in Santana, São Paulo.</p>
    <p>We act for companies and families across Brazil and around the world, in person or online. Our lean structure lets the partners follow each matter personally and lets our practice areas work together when an issue touches more than one field.</p>
    <p>We believe in client-centred legal work: careful listening, plain language, fees agreed in writing and regular updates.</p>'''
        vals = [('Ethics', 'We follow the OAB Code of Ethics and never promise outcomes.'), ('Confidentiality', 'What you tell us stays between you and the firm.'),
                ('Transparency', 'Scope and fees in writing before any step.'), ('Accessibility', 'Direct contact with your partner and prompt replies.')]
        team, vh, oh = ('Partners', 'Who will look after you.'), ('Our commitments', 'What you can expect.'), ('Where we are', 'Head office in São Paulo. Serving clients across Brazil and worldwide.')
        offices = [('Now', 'America/Sao_Paulo', 'São Paulo · Brazil · Head office', 'Rua Doutor César, 1368, Santana<br>02013-080'),
                   ('Now where you are', 'local', 'Online · Brazil and worldwide', 'Video meetings from any city or country.')]
    v = ''.join(f'<div class="reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in vals)
    o = ''.join(f'<div class="office reveal"><p class="time">{n} · <span data-tz="{tz}">--:--</span></p><p class="city">{c}</p><p>{a}</p></div>' for n, tz, c, a in offices)
    return f'''{hero}
<section class="section-tight"><div class="wrap"><div class="prose">{prose}</div></div></section>
<section class="section bg-white"><div class="wrap"><div class="head"><p class="kicker">{team[0]}</p><h2 class="title">{team[1]}</h2></div>{partners(lang)}</div></section>
<section class="section"><div class="wrap"><div class="head"><p class="kicker">{vh[0]}</p><h2 class="title">{vh[1]}</h2></div><div class="values">{v}</div></div></section>
<section class="section bg-sand"><div class="wrap"><div class="head"><p class="kicker">{oh[0]}</p><h2 class="title">{oh[1]}</h2></div><div class="offices">{o}</div></div></section>
{cta(lang)}'''


# ======================================================================= CONTATO
def page_contact(lang):
    pt = lang == 'pt'
    if pt:
        opts = ['Empresa: trabalhista', 'Empresa: societário ou contratos', 'Holding e planejamento patrimonial', 'Saúde e regulatório',
                'Família', 'Herança e inventário', 'Imóveis', 'Consumidor', 'Previdenciário', 'Trabalhista (trabalhador)',
                'Moro fora do Brasil', 'Outro assunto']
        lab = dict(k='Contato', h='Vamos <em>conversar.</em>', lead='Conte em poucas linhas do que se trata. Um dos sócios retorna para marcar a reunião, presencial ou online. Atendemos em todo o Brasil e no mundo.',
                   name='Nome completo', email='E-mail', phone='Telefone ou WhatsApp', country='País onde mora', ph_country='Brasil', kind='Você é',
                   k1='Pessoa física', k2='Empresa', area='Assunto', msg='Mensagem',
                   hint='Descreva o assunto em linhas gerais. Não envie documentos nem detalhes sigilosos por aqui; eles serão tratados na reunião.',
                   hp='Não preencha', consent='Autorizo o uso destes dados para que o escritório retorne o meu contato, conforme a', pol='Política de privacidade',
                   send='Enviar mensagem', wa='WhatsApp e telefone', mail='E-mail', sp='Sede · São Paulo', ed='Atendimento', ig='Instagram',
                   sp_addr='Rua Doutor César, 1368, Santana<br>São Paulo, SP · CEP 02013-080', ed_addr='Presencial em São Paulo e online em todo o Brasil e no mundo.')
    else:
        opts = ['Business: employment', 'Business: corporate or contracts', 'Holding structures and estate planning', 'Healthcare regulation',
                'Family', 'Inheritance and probate', 'Property', 'Consumer', 'Pensions', 'Employment (employee)',
                'I live outside Brazil', 'Something else']
        lab = dict(k='Contact', h='Let’s <em>talk.</em>', lead='Tell us briefly what it is about. A partner will get back to you to arrange a meeting, in person or online. We serve clients across Brazil and worldwide.',
                   name='Full name', email='Email', phone='Phone or WhatsApp', country='Country of residence', ph_country='Your country', kind='You are',
                   k1='An individual', k2='A company', area='Subject', msg='Message',
                   hint='Describe the matter in general terms. Please do not send documents or confidential details here; we will cover them in the meeting.',
                   hp='Leave blank', consent='I agree that the firm may use these details to reply to me, as described in the', pol='Privacy policy',
                   send='Send message', wa='WhatsApp and phone', mail='Email', sp='Head office · São Paulo', ed='Meetings', ig='Instagram',
                   sp_addr='Rua Doutor César, 1368, Santana<br>São Paulo, SP, Brazil · 02013-080', ed_addr='In person in São Paulo and online across Brazil and worldwide.')
    o = ''.join(f'<option>{x}</option>' for x in opts)
    return f'''<section class="page-hero"><div class="wrap"><p class="kicker">{lab['k']}</p><h1 class="display">{lab['h']}</h1><p class="lead">{lab['lead']}</p></div></section>
<section class="section-tight" style="padding-top:0"><div class="wrap contact">
  <div class="form-card"><form id="contact-form" name="contato" method="POST" novalidate>
    <div class="row2"><div class="field"><label for="f-name">{lab['name']}</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">{lab['email']}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
    <div class="row2"><div class="field"><label for="f-phone">{lab['phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-country">{lab['country']}</label><input id="f-country" name="country" autocomplete="country-name" placeholder="{lab['ph_country']}"></div></div>
    <div class="row2"><div class="field"><label for="f-kind">{lab['kind']}</label><select id="f-kind" name="profile"><option>{lab['k1']}</option><option>{lab['k2']}</option></select></div>
      <div class="field"><label for="f-area">{lab['area']}</label><select id="f-area" name="subject">{o}</select></div></div>
    <div class="field"><label for="f-msg">{lab['msg']}</label><textarea id="f-msg" name="message" required maxlength="1500"></textarea><p class="hint">{lab['hint']}</p></div>
    <div class="hp" aria-hidden="true"><label for="f-hp">{lab['hp']}</label><input id="f-hp" name="_gotcha" tabindex="-1" autocomplete="off"></div>
    <label class="consent" for="f-consent"><input id="f-consent" name="consentimento" type="checkbox" value="sim"><span>{lab['consent']} <a href="{L(lang,'privacy')}">{lab['pol']}</a>.</span></label>
    <div><button class="btn btn-primary" type="submit">{lab['send']}</button></div>
    <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
  </form></div>
  <aside class="side">
    <div class="item"><small>{lab['wa']}</small><a class="big" href="https://wa.me/5511917386432" rel="noopener">+55 11 91738-6432</a></div>
    <div class="item"><small>{lab['mail']}</small><a class="big" href="mailto:atendimento@correialamunier.com">atendimento@correialamunier.com</a></div>
    <div class="item"><small>{lab['sp']}</small><p>{lab['sp_addr']}</p></div>
    <div class="item"><small>{lab['ed']}</small><p>{lab['ed_addr']}</p></div>
    <div class="item"><small>{lab['ig']}</small><a class="big" href="https://www.instagram.com/correiasantoslamunier/" rel="noopener">@correiasantoslamunier</a></div>
  </aside>
</div></section>'''


# ======================================================================= PRIVACIDADE
def page_privacy(lang):
    import content_v1
    html = content_v1.page_privacy(lang)
    # reaproveita o texto da v1, só troca a moldura
    start = html.index('<div class="prose">')
    end = html.rindex('</div></div></section>')
    body = html[start:end]
    body = body.replace(' As fontes tipográficas são carregadas do serviço Google Fonts, que recebe o endereço IP do visitante para entregar os arquivos.', '')
    body = body.replace(' Typefaces are loaded from Google Fonts, which receives the visitor’s IP address to deliver the files.', '')
    if lang == 'pt':
        head = '<section class="page-hero"><div class="wrap"><p class="kicker">Privacidade</p><h1 class="display">Política de <em>privacidade.</em></h1><p class="lead">Como tratamos os dados pessoais enviados por este site, nos termos da Lei nº 13.709/2018 (LGPD).</p></div></section>'
    else:
        head = '<section class="page-hero"><div class="wrap"><p class="kicker">Privacy</p><h1 class="display">Privacy <em>policy.</em></h1><p class="lead">How we handle personal data sent through this website under Brazil’s General Data Protection Law (LGPD).</p></div></section>'
    return head + f'<section class="section-tight" style="padding-top:0"><div class="wrap">{body}</div></section>'


# ======================================================================= NOVIDADES
def art_href(lang, a):
    return ('../' if lang == 'en' else '') + f"novidades/{a['slug']}.html"


def post_card(lang, a, feature=False):
    d = data_pt(a['data']) if lang == 'pt' else data_en(a['data'])
    tag = a['categoria'] + (' · em português' if lang == 'en' else '')
    img = f'<div class="post-img"><img src="{PRE[0]}assets/photos/{a["foto"]}.jpg" alt="{a["foto_alt"]}" loading="lazy" decoding="async"></div>'
    read = 'Ler artigo' if lang == 'pt' else 'Read (in Portuguese)'
    cls = 'post post-feature reveal' if feature else 'post reveal'
    return (f'<a class="{cls}" href="{art_href(lang, a)}">{img}<div class="post-txt">'
            f'<p class="post-meta"><span class="post-tag">{tag}</span><span>{d}</span></p>'
            f'<h2>{a["titulo"]}</h2><p class="post-sum">{a["resumo"]}</p><span class="more">{read}</span></div></a>')


def page_blog(lang):
    pt = lang == 'pt'
    k, h, l = (('Novidades', 'Direito do dia a dia, <em>sem juridiquês.</em>',
                'Notícias, decisões e dúvidas comuns explicadas em linguagem simples. O que mudou, o que isso tem a ver com você e o que fazer.')
               if pt else ('News', 'Everyday Brazilian law, <em>in plain words.</em>',
                'Court decisions, new rules and common questions explained simply. Our articles are written in Portuguese.'))
    feat, rest = ARTIGOS[0], ARTIGOS[1:]
    grid = ''.join(post_card(lang, a) for a in rest)
    return f'''<section class="page-hero blog-hero"><div class="wrap"><p class="kicker">{k}</p><h1 class="display">{h}</h1><p class="lead">{l}</p></div></section>
<section class="section-tight" style="padding-top:0"><div class="wrap">
  {post_card(lang, feat, feature=True)}
  <div class="post-grid">{grid}</div>
  <p class="note">{'Conteúdo informativo. Cada caso tem suas particularidades e deve ser avaliado por um advogado.' if pt else 'For information only. Every case has its own details and should be assessed by a lawyer.'}</p>
</div></section>
{instagram(lang)}
{cta(lang)}'''


def blog_teaser(lang):
    pt = lang == 'pt'
    k, h = ('Novidades', 'O que está <em>em pauta.</em>') if pt else ('News', 'What’s <em>in the news.</em>')
    cards = ''.join(post_card(lang, a) for a in ARTIGOS[:3])
    allh = FILES[lang]['blog']
    return f'''<section class="section-tight"><div class="wrap">
  <div class="rail-head"><div class="head" style="margin-bottom:0"><p class="kicker">{k}</p><h2 class="title">{h}</h2></div><a class="more" href="{allh}">{'Ver todas as novidades' if pt else 'See all articles'}</a></div>
  <div class="post-grid three">{cards}</div>
</div></section>'''


def page(lang, key, pre):
    PRE[0] = pre
    return globals()[f'page_{key}'](lang)
