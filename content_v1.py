# -*- coding: utf-8 -*-
# Conteúdo do site, PT e EN. Cada página é HTML de <main>.

FILES = {
    'pt': {'home': 'index.html', 'business': 'empresas.html', 'individuals': 'pessoa-fisica.html',
           'abroad': 'brasileiros-no-exterior.html', 'firm': 'o-escritorio.html', 'contact': 'contato.html',
           'privacy': 'privacidade.html', 'blog': 'novidades.html'},
    'en': {'home': 'index.html', 'business': 'business.html', 'individuals': 'individuals.html',
           'abroad': 'brazilians-abroad.html', 'firm': 'the-firm.html', 'contact': 'contact.html',
           'privacy': 'privacy.html', 'blog': 'news.html'},
}

UI = {
    'pt': {
        'nav': [('business', 'Empresas'), ('individuals', 'Pessoa física'), ('abroad', 'Brasileiros no exterior'), ('firm', 'O escritório'), ('blog', 'Novidades')],
        'cta': 'Agendar conversa', 'menu': 'Menu', 'skip': 'Pular para o conteúdo',
        'sp': 'São Paulo', 'ed': 'Edmonton',
        'foot_nav': 'Navegação', 'foot_contact': 'Contato', 'foot_offices': 'Onde estamos',
        'privacy': 'Política de privacidade',
        'legal': ('Correia Santos &amp; Lamunier Advogados · Sociedade de advogados registrada na OAB/SP sob o nº 48.284 · '
                  'CNPJ 50.719.759/0001-05 · Sócios responsáveis: Cristiane Lamunier Alexandre Mongelli (OAB/SP 152.191) '
                  'e Victor Correia Santos (OAB/SP 452.969).'),
        'legal2': ('Conteúdo exclusivamente informativo, nos termos do Código de Ética e Disciplina da OAB e do Provimento nº 205/2021 '
                   'do Conselho Federal. O escritório atua em direito brasileiro.'),
        'sp_addr': '<b>Sede</b><br>Rua Doutor César, 1368, Santana<br>São Paulo, SP · CEP 02013-080',
        'ed_addr': '<b>Online</b><br>Todo o Brasil e o mundo',
        'now': 'agora',
    },
    'en': {
        'nav': [('business', 'Business'), ('individuals', 'Individuals'), ('abroad', 'Brazilians abroad'), ('firm', 'The firm'), ('blog', 'News')],
        'cta': 'Book a meeting', 'menu': 'Menu', 'skip': 'Skip to content',
        'sp': 'São Paulo', 'ed': 'Edmonton',
        'foot_nav': 'Explore', 'foot_contact': 'Contact', 'foot_offices': 'Where we are',
        'privacy': 'Privacy policy',
        'legal': ('Correia Santos &amp; Lamunier Advogados · Law firm registered with the Brazilian Bar Association, São Paulo Section '
                  '(OAB/SP) under no. 48.284 · CNPJ 50.719.759/0001-05 · Partners: Cristiane Lamunier Alexandre Mongelli (OAB/SP 152.191) '
                  'and Victor Correia Santos (OAB/SP 452.969).'),
        'legal2': ('Information only, in line with the OAB Code of Ethics and Federal Council Provision 205/2021. '
                   'The firm practises Brazilian law only.'),
        'sp_addr': '<b>Head office</b><br>Rua Doutor César, 1368, Santana<br>São Paulo, SP, Brazil · 02013-080',
        'ed_addr': '<b>Online</b><br>All of Brazil and worldwide',
        'now': 'now',
    },
}

META = {
    'pt': {
        'home': ('Correia Santos & Lamunier Advogados', 'Escritório de advocacia com atendimento presencial e online em todo o Brasil e no mundo. Empresas, família, herança, patrimônio, imóveis e brasileiros no exterior, com sócio à frente de cada caso.'),
        'business': ('Advocacia para empresas · Correia Santos & Lamunier', 'Trabalhista empresarial, societário, contratos, holding, saúde e regulatório, consumidor, cobrança e imobiliário para empresas.'),
        'individuals': ('Advocacia para você e sua família · Correia Santos & Lamunier', 'Divórcio, pensão, guarda, inventário, testamento, planejamento patrimonial, imóveis, consumidor, previdenciário e trabalhista.'),
        'abroad': ('Brasileiros no exterior · Correia Santos & Lamunier', 'Herança, imóvel, divórcio, procuração e empresa no Brasil para quem mora fora, sem precisar viajar.'),
        'blog': ('Novidades · Correia Santos & Lamunier', 'Artigos sobre direito do dia a dia, em linguagem simples: consumidor, família, herança, trabalho e brasileiros no exterior.'),
        'firm': ('O escritório · Correia Santos & Lamunier', 'Sociedade de advogados registrada na OAB/SP, com sócio à frente de cada caso e atendimento presencial e online.'),
        'contact': ('Contato · Correia Santos & Lamunier', 'Agende uma conversa com um dos sócios, presencial ou online.'),
        'privacy': ('Política de privacidade · Correia Santos & Lamunier', 'Como tratamos os dados pessoais enviados pelo site, nos termos da LGPD.'),
    },
    'en': {
        'home': ('Correia Santos & Lamunier Advogados', 'Brazilian law firm working in person and online across Brazil and worldwide. Business, family, estates, property and Brazilians abroad, with a partner leading every matter.'),
        'business': ('Brazilian law for business · Correia Santos & Lamunier', 'Employment, corporate, contracts, holding structures, healthcare regulation, consumer defence, debt recovery and commercial property in Brazil.'),
        'individuals': ('Brazilian law for you and your family · Correia Santos & Lamunier', 'Divorce, support, custody, probate, wills, estate planning, property, consumer, pensions and employment rights in Brazil.'),
        'abroad': ('Brazilians abroad · Correia Santos & Lamunier', 'Inheritance, property, divorce, powers of attorney and companies in Brazil for people living overseas, without travelling.'),
        'blog': ('News · Correia Santos & Lamunier', 'Articles on everyday Brazilian law, written in plain Portuguese.'),
        'firm': ('The firm · Correia Santos & Lamunier', 'A law firm registered with OAB/SP, with a partner leading every matter, in person and online.'),
        'contact': ('Contact · Correia Santos & Lamunier', 'Book a conversation with one of the partners, in person or online.'),
        'privacy': ('Privacy policy · Correia Santos & Lamunier', 'How we handle personal data sent through this website under Brazil\'s LGPD.'),
    },
}


def L(lang, key):
    return FILES[lang][key]


def cta_band(lang):
    if lang == 'pt':
        return f'''
<section class="cta"><div class="shards" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap">
  <h2>Vamos conversar sobre o <em>seu caso</em>?</h2>
  <a class="btn btn-gold" href="{L(lang,'contact')}">Agendar conversa com um sócio</a>
</div></section>'''
    return f'''
<section class="cta"><div class="shards" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap">
  <h2>Shall we talk about <em>your matter</em>?</h2>
  <a class="btn btn-gold" href="{L(lang,'contact')}">Book a meeting with a partner</a>
</div></section>'''


def hero_page(eyebrow, title, lead):
    return f'''
<section class="hero hero-page"><div class="shards" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
</div></section>'''


def practices(items):
    out = ['<div class="practice-list">']
    for h, intro, lis in items:
        li = ''.join(f'<li>{x}</li>' for x in lis)
        out.append(f'<article class="practice"><div><h3>{h}</h3><p class="intro">{intro}</p></div><ul>{li}</ul></article>')
    out.append('</div>')
    return '\n'.join(out)


def partners(lang):
    if lang == 'pt':
        a = ('Sócia', 'Previdenciário e trabalhista. Aposentadorias, revisões e benefícios, defesa de empresas e direitos de quem trabalha.')
        b = ('Sócio', 'Empresarial, contratos, holding e planejamento patrimonial, família, sucessões, imobiliário e consumidor.')
    else:
        a = ('Partner', 'Pensions and employment law: retirement and social-security benefits, employer defence and employee rights.')
        b = ('Partner', 'Corporate, contracts, holding structures and estate planning, family, probate, property and consumer law.')
    return f'''
<div class="partners">
  <article class="partner"><p class="oab">{a[0]} · OAB/SP 152.191</p><h3>Cristiane Lamunier Alexandre Mongelli</h3><p>{a[1]}</p></article>
  <article class="partner"><p class="oab">{b[0]} · OAB/SP 452.969</p><h3>Victor Correia Santos</h3><p>{b[1]}</p></article>
</div>'''


def steps(lang):
    if lang == 'pt':
        s = [('Conversa', 'Reunião com o sócio responsável, presencial ou online, para entender a situação.'),
             ('Análise', 'Leitura dos documentos e explicação dos caminhos possíveis, em linguagem simples.'),
             ('Proposta', 'Escopo e honorários combinados por escrito, antes de qualquer passo.'),
             ('Acompanhamento', 'Notícias do andamento e respostas rápidas durante todo o caso.')]
    else:
        s = [('Conversation', 'A meeting with the partner in charge, in person or online, to understand the situation.'),
             ('Review', 'We read the documents and explain the available options in plain language.'),
             ('Proposal', 'Scope and fees agreed in writing before any step is taken.'),
             ('Follow-through', 'Regular updates and quick answers for as long as the matter runs.')]
    return '<ol class="steps">' + ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in s) + '</ol>'


def page(lang, key):
    return globals()[f'page_{key}'](lang)


# ---------------------------------------------------------------- INÍCIO
def page_home(lang):
    if lang == 'pt':
        return f'''
<section class="hero"><div class="shards" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap">
  <p class="eyebrow">Advocacia · São Paulo e Edmonton</p>
  <h1>Advocacia com sócio à frente de <em>cada caso</em></h1>
  <p class="lead">Atendemos empresas e famílias com prevenção, contratos e defesa, no Brasil ou de onde você estiver. Quem atende você é quem conduz o seu caso.</p>
  <div class="hero-actions"><a class="btn btn-gold" href="{L(lang,'contact')}">Agendar conversa</a><a class="btn btn-line" href="{L(lang,'firm')}">Conheça o escritório</a></div>
</div></section>

<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Como podemos ajudar</p><h2>Duas frentes, o mesmo cuidado</h2></div>
  <div class="doors">
    <a class="door" href="{L(lang,'business')}"><p class="eyebrow">Para empresas</p><h3>Menos risco na operação, defesa firme quando o processo chega</h3>
      <p>Trabalhista, societário, contratos, holding e saúde, com foco em prevenir antes de litigar.</p>
      <ul><li>Trabalhista</li><li>Societário</li><li>Contratos</li><li>Holding</li><li>Saúde</li></ul><span class="go">Ver áreas para empresas →</span></a>
    <a class="door" href="{L(lang,'individuals')}"><p class="eyebrow">Para você e sua família</p><h3>Família, herança, patrimônio e imóveis tratados com discrição</h3>
      <p>Momentos delicados conduzidos com escuta, linguagem clara e honorários combinados por escrito.</p>
      <ul><li>Família</li><li>Inventário</li><li>Patrimônio</li><li>Imóveis</li><li>Previdenciário</li></ul><span class="go">Ver áreas para pessoa física →</span></a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Como trabalhamos</p><h2>Conhecer o seu contexto antes que o problema cresça</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Sócio no atendimento</h3><p>Quem atende é quem conduz. Sem repasse para equipes que você não conhece.</p></div>
    <div class="pillar"><h3>Prevenção primeiro</h3><p>Contratos, rotinas e documentos revistos antes do conflito, quando resolver custa menos.</p></div>
    <div class="pillar"><h3>Áreas integradas</h3><p>Trabalhista, societário, família e patrimônio olhando o mesmo caso juntos.</p></div>
    <div class="pillar"><h3>Atendimento digital</h3><p>Reuniões online, assinatura eletrônica e processos digitais, no Brasil ou fora dele.</p></div>
  </div>
</div></section>

<section class="band band-paper"><div class="wrap abroad">
  <div class="section-head" style="margin:0"><p class="eyebrow">Mora fora do Brasil?</p><h2>Resolvemos no Brasil, <em>sem você precisar viajar</em></h2>
    <p class="lead">Com sedes em São Paulo e em Edmonton, no Canadá, e atendimento 100% online, cuidamos do que brasileiros que vivem no exterior precisam resolver no Brasil.</p>
    <p><a class="btn btn-navy" href="{L(lang,'abroad')}">Ver como funciona</a></p></div>
  <ul>
    <li><b>Herança no Brasil</b><span>Inventário com herdeiro morando fora do país</span></li>
    <li><b>Imóvel no Brasil</b><span>Venda, locação e regularização à distância</span></li>
    <li><b>Divórcio e decisões estrangeiras</b><span>Divórcio no Brasil e validade de sentença estrangeira</span></li>
    <li><b>Representação</b><span>Procuração e atuação em seu nome no Brasil</span></li>
  </ul>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Como começamos</p><h2>Quatro passos, sem compromisso até a proposta</h2></div>
  {steps(lang)}
</div></section>

<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Sócios</p><h2>Quem conduz o seu caso</h2></div>
  {partners(lang)}
</div></section>
{cta_band(lang)}'''
    return f'''
<section class="hero"><div class="shards" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap">
  <p class="eyebrow">Brazilian law · São Paulo and Edmonton</p>
  <h1>A partner leading <em>every matter</em></h1>
  <p class="lead">We advise companies and families on Brazilian law: prevention, contracts and litigation, in Brazil or wherever you are. The lawyer you speak to is the lawyer who runs your matter.</p>
  <div class="hero-actions"><a class="btn btn-gold" href="{L(lang,'contact')}">Book a meeting</a><a class="btn btn-line" href="{L(lang,'firm')}">About the firm</a></div>
</div></section>

<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">How we help</p><h2>Two practices, the same care</h2></div>
  <div class="doors">
    <a class="door" href="{L(lang,'business')}"><p class="eyebrow">For business</p><h3>Less risk in day-to-day operations, a firm defence when a claim arrives</h3>
      <p>Employment, corporate, contracts, holding structures and healthcare, with prevention before litigation.</p>
      <ul><li>Employment</li><li>Corporate</li><li>Contracts</li><li>Holdings</li><li>Healthcare</li></ul><span class="go">Business practice areas →</span></a>
    <a class="door" href="{L(lang,'individuals')}"><p class="eyebrow">For you and your family</p><h3>Family, inheritance, wealth and property handled with discretion</h3>
      <p>Sensitive moments handled with attention, plain language and fees agreed in writing.</p>
      <ul><li>Family</li><li>Probate</li><li>Estate planning</li><li>Property</li><li>Pensions</li></ul><span class="go">Individual practice areas →</span></a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">How we work</p><h2>Understanding your situation before the problem grows</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Partner-led</h3><p>The person you meet runs your matter. No hand-off to people you have never spoken to.</p></div>
    <div class="pillar"><h3>Prevention first</h3><p>Contracts and routines reviewed before a dispute, when solving it costs less.</p></div>
    <div class="pillar"><h3>Joined-up advice</h3><p>Employment, corporate, family and estate issues looked at together.</p></div>
    <div class="pillar"><h3>Fully digital</h3><p>Online meetings, e-signatures and electronic court files, in Brazil or abroad.</p></div>
  </div>
</div></section>

<section class="band band-paper"><div class="wrap abroad">
  <div class="section-head" style="margin:0"><p class="eyebrow">Living outside Brazil?</p><h2>We handle it in Brazil, <em>so you don’t have to travel</em></h2>
    <p class="lead">With offices in São Paulo and Edmonton, Canada, and working fully online, we help Brazilians abroad deal with legal matters back home.</p>
    <p><a class="btn btn-navy" href="{L(lang,'abroad')}">How it works</a></p></div>
  <ul>
    <li><b>Inheritance in Brazil</b><span>Probate when an heir lives overseas</span></li>
    <li><b>Property in Brazil</b><span>Selling, letting and regularising from a distance</span></li>
    <li><b>Divorce and foreign judgments</b><span>Divorce in Brazil and recognition of foreign decisions</span></li>
    <li><b>Representation</b><span>Powers of attorney and acting on your behalf in Brazil</span></li>
  </ul>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Getting started</p><h2>Four steps, no commitment until the proposal</h2></div>
  {steps(lang)}
</div></section>

<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Partners</p><h2>Who will handle your matter</h2></div>
  {partners(lang)}
</div></section>
{cta_band(lang)}'''


# ---------------------------------------------------------------- EMPRESAS
def page_business(lang):
    if lang == 'pt':
        items = [
            ('Trabalhista empresarial', 'Prevenir o passivo e defender a empresa quando a reclamação chega, até o TST.',
             ['Revisão de rotinas de RH, jornadas e políticas internas', 'Planos de premiação e remuneração variável',
              'Terceirização e cota de aprendizes', 'Advertências, notificações e desligamentos',
              'Contestações e preparação de prepostos e testemunhas', 'Recursos aos Tribunais Regionais e ao TST']),
            ('Societário', 'Regras claras entre sócios, definidas antes de o conflito aparecer.',
             ['Constituição da sociedade e alterações contratuais', 'Acordo de sócios ou de quotistas',
              'Entrada, saída e retirada de sócio', 'Apuração de haveres e cessão de quotas',
              'Compra e venda de empresa ou de ponto comercial', 'Representação de sócio que mora no exterior']),
            ('Contratos', 'Contratos que protegem a operação e evitam discussão depois.',
             ['Contratos com clientes e fornecedores', 'Prestação de serviços e parcerias',
              'Locação comercial', 'Confidencialidade e não concorrência', 'Revisão e negociação de minutas', 'Notificações extrajudiciais']),
            ('Holding e planejamento patrimonial', 'A sucessão da empresa familiar organizada em vida.',
             ['Holding familiar e patrimonial', 'Sucessão na empresa de família', 'Doações com reserva de usufruto',
              'Cláusulas de proteção do patrimônio', 'Acordo de família entre herdeiros', 'Inventário, quando chegar a hora']),
            ('Saúde e regulatório', 'Clínicas, consultórios, farmácias e cannabis medicinal.',
             ['Adequação à LGPD para dados de pacientes', 'Contratos com fornecedores de prontuário eletrônico',
              'Plano de resposta a incidentes de dados', 'Novas regras da Anvisa para cannabis medicinal',
              'Estruturação de associações de pacientes', 'Sociedade entre profissionais de saúde']),
            ('Consumidor, crédito e imobiliário', 'Defesa da empresa e recuperação do que lhe é devido.',
             ['Defesa em ações de clientes e Procon', 'Responsabilidade civil e indenizações',
              'Cobrança extrajudicial e judicial', 'Execuções e ações monitórias',
              'Compra e locação de imóvel comercial', 'Venda de ponto comercial (trespasse)']),
        ]
        sectors = ['Hotelaria e hospitalidade', 'Clínicas e farmácias', 'Bares, cafés e restaurantes', 'Indústria e comércio',
                   'Engenharia e manutenção', 'Serviços e pesquisa de mercado', 'Associações e entidades', 'Empresas familiares']
        return (hero_page('Para empresas', 'Assessoria jurídica para empresas, da <em>rotina</em> ao tribunal',
                          'Prevenção, contratos e defesa conduzidos por um sócio que conhece a sua operação.')
                + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Áreas de atuação</p><h2>O que fazemos pela sua empresa</h2></div>
  {practices(items)}
</div></section>
<section class="band band-navy"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Setores que já atendemos</p><h2>Experiência em operações de diferentes portes</h2></div>
  <div class="chips">{''.join(f'<span class="chip">{s}</span>' for s in sectors)}</div>
  <p class="note">Por dever de sigilo profissional, não divulgamos nomes de clientes.</p>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Como começamos</p><h2>Do primeiro contato à parceria</h2></div>
  {steps(lang)}
</div></section>
{cta_band(lang)}''')
    items = [
        ('Employment law for employers', 'Reducing exposure and defending the company when a claim is filed, up to the Superior Labour Court (TST).',
         ['HR routines, working hours and internal policies', 'Bonus and variable-pay plans', 'Outsourcing and apprenticeship quotas',
          'Warnings, notices and terminations', 'Defences and witness preparation for hearings', 'Appeals to the Regional Courts and the TST']),
        ('Corporate', 'Clear rules between shareholders, agreed before any dispute.',
         ['Incorporation and amendments to articles', 'Shareholders’ and quotaholders’ agreements', 'Entry and exit of partners',
          'Valuation of a departing partner’s share', 'Sale and purchase of companies and businesses', 'Acting for partners who live abroad']),
        ('Contracts', 'Contracts that protect the business and prevent disputes later.',
         ['Customer and supplier agreements', 'Services and partnership agreements', 'Commercial leases',
          'Confidentiality and non-compete', 'Drafting, review and negotiation', 'Formal notices']),
        ('Holding structures and estate planning', 'Planning succession in a family business during the owners’ lifetime.',
         ['Family and asset-holding companies', 'Family-business succession', 'Gifts with retained usufruct',
          'Asset-protection clauses', 'Family agreements between heirs', 'Probate when the time comes']),
        ('Healthcare regulation', 'Clinics, practices, pharmacies and medical cannabis.',
         ['LGPD (Brazilian data protection) compliance for patient data', 'Contracts with electronic-records providers',
          'Data-incident response plans', 'New ANVISA rules on medical cannabis',
          'Setting up patient associations', 'Partnerships between health professionals']),
        ('Consumer, debt recovery and property', 'Defending the company and recovering what it is owed.',
         ['Defence in consumer claims', 'Civil liability and damages', 'Out-of-court and court debt recovery',
          'Enforcement and summary proceedings', 'Buying and leasing commercial property', 'Sale of a going concern']),
    ]
    sectors = ['Hospitality', 'Clinics and pharmacies', 'Bars, cafés and restaurants', 'Industry and trade',
               'Engineering and maintenance', 'Services and market research', 'Associations', 'Family businesses']
    return (hero_page('For business', 'Brazilian legal advice for companies, from <em>daily operations</em> to court',
                      'Prevention, contracts and litigation led by a partner who knows your business.')
            + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Practice areas</p><h2>What we do for your company</h2></div>
  {practices(items)}
</div></section>
<section class="band band-navy"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Sectors we have served</p><h2>Experience with businesses of different sizes</h2></div>
  <div class="chips">{''.join(f'<span class="chip">{s}</span>' for s in sectors)}</div>
  <p class="note">Professional secrecy rules mean we do not disclose client names.</p>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Getting started</p><h2>From first contact to an ongoing relationship</h2></div>
  {steps(lang)}
</div></section>
{cta_band(lang)}''')


# ---------------------------------------------------------------- PESSOA FÍSICA
def page_individuals(lang):
    if lang == 'pt':
        items = [
            ('Família', 'Momentos difíceis conduzidos com cuidado e firmeza.',
             ['Divórcio consensual em cartório ou judicial', 'Partilha de bens', 'Pensão alimentícia: pedido, revisão e cobrança',
              'Guarda compartilhada e convivência', 'União estável: reconhecimento e dissolução', 'Pacto antenupcial']),
            ('Herança e inventário', 'Cuidar da partilha com respeito ao momento da família.',
             ['Inventário em cartório, quando possível', 'Inventário judicial', 'Partilha entre herdeiros',
              'Testamento', 'Herdeiro que mora no exterior', 'Alvarás e regularização de bens']),
            ('Planejamento patrimonial', 'Com a Reforma Tributária, o ITCMD passou a ser obrigatoriamente progressivo em todo o país (EC 132/2023). Planejar em vida evita conflitos e surpresas.',
             ['Holding familiar', 'Doações com reserva de usufruto', 'Cláusulas de proteção do patrimônio',
              'Organização da sucessão', 'Acordos entre herdeiros', 'Revisão do planejamento ao longo do tempo']),
            ('Imóveis', 'O imóvel é, muitas vezes, o maior bem da família.',
             ['Análise de documentos antes de comprar', 'Contratos de compra e venda e de locação', 'Usucapião judicial e em cartório',
              'Regularização de imóvel e de escritura', 'Problemas com construtoras e loteadoras', 'Conflitos de vizinhança']),
            ('Consumidor', 'Quando o serviço contratado não é entregue como prometido.',
             ['Voos cancelados e bagagem extraviada', 'Pacotes e agências de viagem', 'Cobranças indevidas de bancos',
              'Produtos e serviços com defeito', 'Negativação indevida', 'Indenizações']),
            ('Previdenciário e trabalhista', 'Os seus direitos como segurado e como trabalhador.',
             ['Aposentadoria e planejamento previdenciário', 'Revisão de benefícios', 'Pedidos negados pelo INSS',
              'Verbas de rescisão não pagas', 'Horas extras e adicionais', 'Reconhecimento de vínculo']),
        ]
        profiles = ['Famílias em inventário', 'Mães e pais em questões de pensão e guarda', 'Compradores e donos de imóveis',
                    'Aposentados e segurados do INSS', 'Trabalhadores', 'Consumidores e passageiros', 'Brasileiros que moram fora',
                    'Famílias organizando o patrimônio']
        return (hero_page('Para você e sua família', 'Advocacia humanizada, em linguagem que <em>você entende</em>',
                          'Família, herança, patrimônio, imóveis e direitos do dia a dia, com honorários sempre combinados por escrito.')
                + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Áreas de atuação</p><h2>Em que podemos ajudar você</h2></div>
  {practices(items)}
</div></section>
<section class="band band-navy"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Quem já confiou em nós</p><h2>Pessoas e famílias em diferentes momentos da vida</h2></div>
  <div class="chips">{''.join(f'<span class="chip">{s}</span>' for s in profiles)}</div>
  <p class="note">Por dever de sigilo profissional, não divulgamos nomes de clientes nem detalhes de casos.</p>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Como começamos</p><h2>Quatro passos, sem compromisso até a proposta</h2></div>
  {steps(lang)}
</div></section>
{cta_band(lang)}''')
    items = [
        ('Family', 'Difficult moments handled with care and resolve.',
         ['Uncontested divorce at a notary or in court', 'Division of assets', 'Child and spousal support: claims, reviews and enforcement',
          'Shared custody and contact', 'Common-law (stable) unions', 'Prenuptial agreements']),
        ('Inheritance and probate', 'Dividing an estate with respect for the family’s moment.',
         ['Out-of-court probate at a notary, when possible', 'Court probate', 'Division between heirs',
          'Wills', 'Heirs living abroad', 'Court authorisations and asset regularisation']),
        ('Estate planning', 'Brazil’s tax reform made inheritance and gift tax (ITCMD) mandatorily progressive nationwide (Constitutional Amendment 132/2023). Planning ahead avoids disputes and surprises.',
         ['Family holding companies', 'Gifts with retained usufruct', 'Asset-protection clauses',
          'Succession planning', 'Agreements between heirs', 'Periodic review of the plan']),
        ('Property', 'A home is often a family’s largest asset.',
         ['Title checks before buying', 'Sale, purchase and lease agreements', 'Adverse possession (usucapião)',
          'Regularising property and deeds', 'Disputes with developers', 'Neighbour disputes']),
        ('Consumer', 'When a service you paid for is not delivered as promised.',
         ['Cancelled flights and lost luggage', 'Travel agencies and packages', 'Unfair bank charges',
          'Defective products and services', 'Wrongful credit listings', 'Damages']),
        ('Pensions and employment', 'Your rights as an insured person and as an employee.',
         ['Retirement and pension planning', 'Benefit reviews', 'Benefits refused by the INSS',
          'Unpaid termination amounts', 'Overtime and allowances', 'Recognition of employment']),
    ]
    profiles = ['Families going through probate', 'Parents dealing with support and custody', 'Home buyers and owners',
                'Retirees and INSS beneficiaries', 'Employees', 'Consumers and air passengers', 'Brazilians living abroad',
                'Families organising their wealth']
    return (hero_page('For you and your family', 'Personal legal advice in language <em>you understand</em>',
                      'Family, inheritance, wealth, property and everyday rights under Brazilian law, with fees always agreed in writing.')
            + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Practice areas</p><h2>How we can help you</h2></div>
  {practices(items)}
</div></section>
<section class="band band-navy"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Who has trusted us</p><h2>People and families at different stages of life</h2></div>
  <div class="chips">{''.join(f'<span class="chip">{s}</span>' for s in profiles)}</div>
  <p class="note">Professional secrecy rules mean we do not disclose client names or case details.</p>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Getting started</p><h2>Four steps, no commitment until the proposal</h2></div>
  {steps(lang)}
</div></section>
{cta_band(lang)}''')


# ---------------------------------------------------------------- EXTERIOR
def page_abroad(lang):
    if lang == 'pt':
        items = [
            ('Herança no Brasil', 'Quando um familiar falece no Brasil e você mora fora.',
             ['Inventário com herdeiro no exterior', 'Procuração para representar você', 'Partilha e transferência de bens',
              'Venda de imóvel do espólio', 'Contas e investimentos no Brasil', 'Orientação sobre documentos emitidos fora']),
            ('Imóvel no Brasil', 'Vender, alugar ou regularizar sem precisar viajar.',
             ['Venda de imóvel por não residente', 'Contratos de locação e administração', 'Regularização de escritura e matrícula',
              'Usucapião', 'Conflitos com inquilinos e vizinhos', 'Recebimento seguro dos valores']),
            ('Família à distância', 'Divórcio, pensão e guarda quando uma das partes mora fora.',
             ['Divórcio no Brasil', 'Validade no Brasil de sentença estrangeira', 'Pensão alimentícia internacional',
              'Guarda e convivência entre países', 'Autorização de viagem de filhos', 'Pacto antenupcial']),
            ('Empresa e documentos', 'Manter a vida no Brasil em ordem enquanto você está fora.',
             ['Representação de sócio residente no exterior', 'Alterações societárias à distância', 'Encerramento de empresa',
              'Pendências de CPF e cadastros', 'Procurações em geral', 'Acompanhamento de processos em andamento']),
        ]
        return (hero_page('Brasileiros no exterior', 'Mora fora? Resolvemos no Brasil <em>sem você precisar viajar</em>',
                          'Com sedes em São Paulo e em Edmonton, no Canadá, atendemos de forma 100% online quem vive longe e precisa cuidar de algo no Brasil.')
                + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">O que fazemos</p><h2>As situações mais comuns de quem mora fora</h2></div>
  {practices(items)}
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Atendimento à distância</p><h2>Tudo resolvido sem sair de onde você está</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Reuniões por vídeo</h3><p>No horário que funciona para você, considerando o seu fuso.</p></div>
    <div class="pillar"><h3>Assinatura eletrônica</h3><p>Contratos e documentos assinados digitalmente, sempre que a lei permite.</p></div>
    <div class="pillar"><h3>Procuração</h3><p>Orientamos como outorgar a procuração no país onde você mora.</p></div>
    <div class="pillar"><h3>Andamento informado</h3><p>Notícias do caso por e-mail ou WhatsApp, sem você precisar perguntar.</p></div>
  </div>
  <div class="section-head" style="margin-top:56px"><p class="eyebrow">Duas sedes</p><h2>São Paulo e Edmonton</h2></div>
  <div class="offices">
    <div class="office"><p class="time"><span data-tz="America/Sao_Paulo">--:--</span> em São Paulo agora</p><p class="city">São Paulo · Brasil</p><p>Sede do escritório e acompanhamento dos processos.</p></div>
    <div class="office"><p class="time"><span data-tz="America/Edmonton">--:--</span> em Edmonton agora</p><p class="city">Edmonton · Canadá</p><p>Atendimento a brasileiros que vivem no Canadá e na América do Norte.</p></div>
  </div>
  <p class="note">O escritório atua exclusivamente com direito brasileiro. Questões de imigração, vistos ou leis de outros países devem ser tratadas com um profissional local.</p>
</div></section>
{cta_band(lang)}''')
    items = [
        ('Inheritance in Brazil', 'When a relative dies in Brazil and you live abroad.',
         ['Probate with an heir overseas', 'Powers of attorney to act for you', 'Division and transfer of assets',
          'Selling estate property', 'Bank accounts and investments in Brazil', 'Guidance on documents issued abroad']),
        ('Property in Brazil', 'Selling, letting or regularising without travelling.',
         ['Sales by non-residents', 'Leases and property management agreements', 'Regularising deeds and land registry',
          'Adverse possession (usucapião)', 'Disputes with tenants and neighbours', 'Secure receipt of proceeds']),
        ('Family across borders', 'Divorce, support and custody when one party lives abroad.',
         ['Divorce in Brazil', 'Recognition of foreign judgments in Brazil', 'International child support',
          'Custody and contact between countries', 'Travel authorisation for children', 'Prenuptial agreements']),
        ('Companies and paperwork', 'Keeping your affairs in Brazil in order while you are away.',
         ['Acting for partners resident abroad', 'Corporate changes at a distance', 'Winding up a company',
          'CPF and registration issues', 'General powers of attorney', 'Monitoring ongoing court cases']),
    ]
    return (hero_page('Brazilians abroad', 'Living abroad? We handle it in Brazil <em>so you don’t have to travel</em>',
                      'From our offices in São Paulo and Edmonton, Canada, we work fully online for people who live far away and need something done in Brazil.')
            + f'''
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we do</p><h2>The most common situations for Brazilians overseas</h2></div>
  {practices(items)}
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Working remotely</p><h2>Everything handled from wherever you are</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Video meetings</h3><p>At a time that works for you, whatever your time zone.</p></div>
    <div class="pillar"><h3>E-signatures</h3><p>Contracts and documents signed digitally wherever the law allows.</p></div>
    <div class="pillar"><h3>Powers of attorney</h3><p>We explain how to grant a power of attorney in your country of residence.</p></div>
    <div class="pillar"><h3>Regular updates</h3><p>News on your matter by email or WhatsApp, without you having to chase.</p></div>
  </div>
  <div class="section-head" style="margin-top:56px"><p class="eyebrow">Two offices</p><h2>São Paulo and Edmonton</h2></div>
  <div class="offices">
    <div class="office"><p class="time"><span data-tz="America/Sao_Paulo">--:--</span> in São Paulo now</p><p class="city">São Paulo · Brazil</p><p>Head office and management of court cases.</p></div>
    <div class="office"><p class="time"><span data-tz="America/Edmonton">--:--</span> in Edmonton now</p><p class="city">Edmonton · Canada</p><p>Serving Brazilians living in Canada and North America.</p></div>
  </div>
  <p class="note">The firm practises Brazilian law only. Immigration, visa or foreign-law questions should be taken to a local professional.</p>
</div></section>
{cta_band(lang)}''')


# ---------------------------------------------------------------- O ESCRITÓRIO
def page_firm(lang):
    if lang == 'pt':
        return (hero_page('O escritório', 'Uma sociedade de advogados com <em>atendimento artesanal</em>',
                          'Fugimos do atendimento impessoal: cada cliente fala diretamente com o sócio que conduz o caso, do primeiro contato à solução.')
                + f'''
<section class="band"><div class="wrap">
  <div class="prose">
    <p class="eyebrow">Quem somos</p>
    <h2>Correia Santos &amp; Lamunier Advogados</h2>
    <p>Somos uma sociedade de advogados registrada na Ordem dos Advogados do Brasil, Secção de São Paulo, sob o nº 48.284, com sede em Santana, na capital paulista, e também em Edmonton, no Canadá.</p>
    <p>Atendemos empresas e famílias. A estrutura enxuta permite que os sócios acompanhem pessoalmente cada caso e que as áreas trabalhem juntas quando uma questão envolve mais de um tema.</p>
    <p>Acreditamos em uma advocacia humanizada: escuta atenta, linguagem clara, honorários combinados por escrito e notícias frequentes sobre o andamento.</p>
  </div>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Sócios</p><h2>Quem conduz o seu caso</h2></div>
  {partners(lang)}
</div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Nossos compromissos</p><h2>O que você pode esperar</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Ética</h3><p>Atuação dentro do Código de Ética da OAB, sem promessa de resultado.</p></div>
    <div class="pillar"><h3>Sigilo</h3><p>Tudo o que você conta fica entre você e o escritório.</p></div>
    <div class="pillar"><h3>Transparência</h3><p>Escopo e honorários por escrito antes de qualquer passo.</p></div>
    <div class="pillar"><h3>Proximidade</h3><p>Contato direto com o sócio e retorno rápido.</p></div>
  </div>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Sedes</p><h2>São Paulo e Edmonton</h2></div>
  <div class="offices">
    <div class="office"><p class="time"><span data-tz="America/Sao_Paulo">--:--</span> agora</p><p class="city">São Paulo · Brasil</p><p>Rua Doutor César, 1368, Santana<br>CEP 02013-080</p></div>
    <div class="office"><p class="time"><span data-tz="America/Edmonton">--:--</span> agora</p><p class="city">Edmonton · Canadá</p><p>Edmonton, Alberta</p></div>
  </div>
</div></section>
{cta_band(lang)}''')
    return (hero_page('The firm', 'A law firm with a <em>personal approach</em>',
                      'No impersonal service: every client speaks directly to the partner who runs the matter, from first contact to resolution.')
            + f'''
<section class="band"><div class="wrap">
  <div class="prose">
    <p class="eyebrow">Who we are</p>
    <h2>Correia Santos &amp; Lamunier Advogados</h2>
    <p>We are a Brazilian law firm registered with the Brazilian Bar Association, São Paulo Section (OAB/SP), under no. 48.284, with our head office in Santana, São Paulo, and a second office in Edmonton, Canada.</p>
    <p>We act for companies and families. Our lean structure lets the partners follow each matter personally and lets our practice areas work together when an issue touches more than one field.</p>
    <p>We believe in client-centred legal work: careful listening, plain language, fees agreed in writing and regular updates on progress.</p>
  </div>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Partners</p><h2>Who will handle your matter</h2></div>
  {partners(lang)}
</div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Our commitments</p><h2>What you can expect</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Ethics</h3><p>We follow the OAB Code of Ethics and never promise outcomes.</p></div>
    <div class="pillar"><h3>Confidentiality</h3><p>What you tell us stays between you and the firm.</p></div>
    <div class="pillar"><h3>Transparency</h3><p>Scope and fees in writing before any step is taken.</p></div>
    <div class="pillar"><h3>Accessibility</h3><p>Direct contact with your partner and prompt replies.</p></div>
  </div>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Offices</p><h2>São Paulo and Edmonton</h2></div>
  <div class="offices">
    <div class="office"><p class="time"><span data-tz="America/Sao_Paulo">--:--</span> now</p><p class="city">São Paulo · Brazil</p><p>Rua Doutor César, 1368, Santana<br>02013-080</p></div>
    <div class="office"><p class="time"><span data-tz="America/Edmonton">--:--</span> now</p><p class="city">Edmonton · Canada</p><p>Edmonton, Alberta</p></div>
  </div>
</div></section>
{cta_band(lang)}''')


# ---------------------------------------------------------------- CONTATO
def page_contact(lang):
    if lang == 'pt':
        opts = ['Empresa: trabalhista', 'Empresa: societário ou contratos', 'Holding e planejamento patrimonial', 'Saúde e regulatório',
                'Família', 'Herança e inventário', 'Imóveis', 'Consumidor', 'Previdenciário', 'Trabalhista (trabalhador)',
                'Moro fora do Brasil', 'Outro assunto']
        o = ''.join(f'<option>{x}</option>' for x in opts)
        return (hero_page('Contato', 'Agende uma conversa com <em>um dos sócios</em>',
                          'Conte em poucas linhas do que se trata. Retornamos para marcar a reunião, presencial ou online.')
                + f'''
<section class="band"><div class="wrap contact">
  <form id="contact-form" name="contato" method="POST" novalidate>
    <div class="row2">
      <div class="field"><label for="f-name">Nome completo</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">E-mail</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-phone">Telefone ou WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-country">País onde mora</label><input id="f-country" name="country" autocomplete="country-name" placeholder="Brasil"></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-kind">Você é</label><select id="f-kind" name="profile"><option>Pessoa física</option><option>Empresa</option></select></div>
      <div class="field"><label for="f-area">Assunto</label><select id="f-area" name="subject">{o}</select></div>
    </div>
    <div class="field"><label for="f-msg">Mensagem</label><textarea id="f-msg" name="message" required maxlength="1500"></textarea>
      <p class="hint">Descreva o assunto em linhas gerais. Não envie documentos nem detalhes sigilosos por aqui; eles serão tratados na reunião.</p></div>
    <div class="hp" aria-hidden="true"><label for="f-hp">Não preencha</label><input id="f-hp" name="_gotcha" tabindex="-1" autocomplete="off"></div>
    <label class="consent" for="f-consent"><input id="f-consent" name="consentimento" type="checkbox" value="sim">
      <span>Autorizo o uso destes dados para que o escritório retorne o meu contato, conforme a <a href="{L(lang,'privacy')}">Política de privacidade</a>.</span></label>
    <div><button class="btn btn-navy" type="submit">Enviar mensagem</button></div>
    <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
  </form>
  <aside class="info-card">
    <div><h3>WhatsApp e telefone</h3><a class="big" href="https://wa.me/5511917386432" rel="noopener">(11) 91738-6432</a></div>
    <div><h3>E-mail</h3><a class="big" href="mailto:atendimento@correialamunier.com">atendimento@correialamunier.com</a></div>
    <div><h3>São Paulo · Brasil</h3><p>Rua Doutor César, 1368, Santana<br>São Paulo, SP · CEP 02013-080</p></div>
    <div><h3>Edmonton · Canadá</h3><p>Edmonton, Alberta</p></div>
    <div><h3>Instagram</h3><a href="https://www.instagram.com/correiasantoslamunier/" rel="noopener">@correiasantoslamunier</a></div>
  </aside>
</div></section>''')
    opts = ['Business: employment', 'Business: corporate or contracts', 'Holding structures and estate planning', 'Healthcare regulation',
            'Family', 'Inheritance and probate', 'Property', 'Consumer', 'Pensions', 'Employment (employee)',
            'I live outside Brazil', 'Something else']
    o = ''.join(f'<option>{x}</option>' for x in opts)
    return (hero_page('Contact', 'Book a conversation with <em>one of the partners</em>',
                      'Tell us briefly what it is about. We will get back to you to arrange a meeting, in person or online.')
            + f'''
<section class="band"><div class="wrap contact">
  <form id="contact-form" name="contato" method="POST" novalidate>
    <div class="row2">
      <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-phone">Phone or WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-country">Country of residence</label><input id="f-country" name="country" autocomplete="country-name" placeholder="Brazil"></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-kind">You are</label><select id="f-kind" name="profile"><option>An individual</option><option>A company</option></select></div>
      <div class="field"><label for="f-area">Subject</label><select id="f-area" name="subject">{o}</select></div>
    </div>
    <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required maxlength="1500"></textarea>
      <p class="hint">Describe the matter in general terms. Please do not send documents or confidential details here; we will cover them in the meeting.</p></div>
    <div class="hp" aria-hidden="true"><label for="f-hp">Leave blank</label><input id="f-hp" name="_gotcha" tabindex="-1" autocomplete="off"></div>
    <label class="consent" for="f-consent"><input id="f-consent" name="consentimento" type="checkbox" value="yes">
      <span>I agree that the firm may use these details to reply to me, as described in the <a href="{L(lang,'privacy')}">Privacy policy</a>.</span></label>
    <div><button class="btn btn-navy" type="submit">Send message</button></div>
    <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
  </form>
  <aside class="info-card">
    <div><h3>WhatsApp and phone</h3><a class="big" href="https://wa.me/5511917386432" rel="noopener">+55 11 91738-6432</a></div>
    <div><h3>Email</h3><a class="big" href="mailto:atendimento@correialamunier.com">atendimento@correialamunier.com</a></div>
    <div><h3>São Paulo · Brazil</h3><p>Rua Doutor César, 1368, Santana<br>São Paulo, SP · 02013-080</p></div>
    <div><h3>Edmonton · Canada</h3><p>Edmonton, Alberta</p></div>
    <div><h3>Instagram</h3><a href="https://www.instagram.com/correiasantoslamunier/" rel="noopener">@correiasantoslamunier</a></div>
  </aside>
</div></section>''')


# ---------------------------------------------------------------- PRIVACIDADE
def page_privacy(lang):
    if lang == 'pt':
        return (hero_page('Privacidade', 'Política de privacidade', 'Como tratamos os dados pessoais enviados por este site, nos termos da Lei nº 13.709/2018 (LGPD).')
                + '''
<section class="band"><div class="wrap"><div class="prose">
  <h2>Quem é o controlador</h2>
  <p>Correia Santos &amp; Lamunier Advogados, CNPJ 50.719.759/0001-05, Rua Doutor César, 1368, Santana, São Paulo, SP, CEP 02013-080. Contato para assuntos de dados pessoais: atendimento@correialamunier.com.</p>
  <h2>Quais dados coletamos</h2>
  <p>Apenas os dados que você informa no formulário de contato: nome, e-mail, telefone, país de residência, perfil, assunto e a mensagem.</p>
  <h2>Para que usamos</h2>
  <ul><li>Responder ao seu contato e agendar a reunião;</li><li>Avaliar se o escritório pode atender o assunto informado;</li><li>Preparar a proposta de honorários, se você solicitar.</li></ul>
  <p>As bases legais são o seu consentimento e a realização de procedimentos preliminares a um contrato, a seu pedido (art. 7º, I e V, da LGPD).</p>
  <h2>Com quem compartilhamos</h2>
  <p>Os dados não são vendidos nem cedidos a terceiros. Podem ser processados pelos prestadores que mantêm o site, o formulário e o e-mail do escritório, apenas para essa finalidade.</p>
  <h2>Por quanto tempo guardamos</h2>
  <p>Pelo tempo necessário para responder ao contato. Se você se tornar cliente, os dados passam a seguir as regras de guarda da relação profissional e do sigilo da advocacia.</p>
  <h2>Seus direitos</h2>
  <p>Você pode pedir confirmação, acesso, correção, eliminação dos dados ou revogar o consentimento a qualquer momento (art. 18 da LGPD), escrevendo para atendimento@correialamunier.com.</p>
  <h2>Cookies</h2>
  <p>Este site não usa cookies de publicidade nem de rastreamento. As fontes tipográficas são carregadas do serviço Google Fonts, que recebe o endereço IP do visitante para entregar os arquivos.</p>
  <p class="hint">Última atualização: outubro de 2026.</p>
</div></div></section>''')
    return (hero_page('Privacy', 'Privacy policy', 'How we handle personal data sent through this website under Brazil’s General Data Protection Law (Law 13,709/2018, “LGPD”).')
            + '''
<section class="band"><div class="wrap"><div class="prose">
  <h2>Controller</h2>
  <p>Correia Santos &amp; Lamunier Advogados, CNPJ 50.719.759/0001-05, Rua Doutor César, 1368, Santana, São Paulo, SP, Brazil, 02013-080. Data-protection contact: atendimento@correialamunier.com.</p>
  <h2>What we collect</h2>
  <p>Only what you enter in the contact form: name, email, phone, country of residence, profile, subject and message.</p>
  <h2>Why we use it</h2>
  <ul><li>To reply to you and arrange a meeting;</li><li>To assess whether the firm can take on the matter;</li><li>To prepare a fee proposal, if you ask for one.</li></ul>
  <p>The legal bases are your consent and steps taken at your request before entering into a contract (LGPD art. 7, I and V).</p>
  <h2>Who we share it with</h2>
  <p>We do not sell or pass on your data. It may be processed by the providers that run the website, the form and the firm’s email, for this purpose only.</p>
  <h2>How long we keep it</h2>
  <p>For as long as needed to reply. If you become a client, the data follows the record-keeping and professional-secrecy rules of that relationship.</p>
  <h2>Your rights</h2>
  <p>You may ask for confirmation, access, correction or deletion of your data, or withdraw consent at any time (LGPD art. 18), by writing to atendimento@correialamunier.com.</p>
  <h2>Cookies</h2>
  <p>This site uses no advertising or tracking cookies. Typefaces are loaded from Google Fonts, which receives the visitor’s IP address to deliver the files.</p>
  <p class="hint">Last updated: October 2026.</p>
</div></div></section>''')
