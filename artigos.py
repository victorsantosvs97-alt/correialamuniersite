# -*- coding: utf-8 -*-
# Artigos da aba "Novidades". O mais novo primeiro. Corpo em HTML simples (p, h2, ul, li, b).
# Para incluir um artigo: acrescente um dict no topo da lista, ponha a foto em img/photos/<foto>.jpg e rode build2.py.

ARTIGOS = [
    {
        'slug': 'loja-pode-recusar-cliente-por-causa-do-voto',
        'data': '2026-10-30',
        'categoria': 'Consumidor',
        'titulo': 'A loja pode recusar você <em>por causa do seu voto?</em>',
        'titulo_txt': 'A loja pode recusar você por causa do seu voto?',
        'resumo': 'Depois da eleição, placas e posts barrando clientes por preferência política viraram notícia, e o governo notificou estabelecimentos. A gente explica o que diz a lei e o que fazer se acontecer com você.',
        'foto': 'blog-loja-voto', 'foto_alt': 'Cliente sendo atendido no balcão de uma loja',
        'resumo_box': [
            'Quem vende ao público não pode se recusar a atender quem está disposto a pagar.',
            'Placa ou post barrando um grupo pode ser punido mesmo que ninguém tenha sido barrado de fato.',
            'A regra vale para qualquer lado político. O cliente continua livre para comprar onde quiser.',
            'Se acontecer com você: guarde provas e procure o Procon.',
        ],
        'corpo': '''
<p>Nos dias que se seguiram ao segundo turno, circularam nas redes placas como “proibida a entrada de petistas” e posts de estabelecimentos pedindo que eleitores de um lado não comprassem mais ali. O assunto ganhou o noticiário quando a Secretaria Nacional do Consumidor (Senacon), do Ministério da Justiça, notificou pelo menos quatro estabelecimentos, que receberam cinco dias úteis para se explicar.</p>
<p>A pergunta que muita gente fez é simples: <b>uma loja pode escolher o cliente pelo voto?</b></p>
<h2>O que diz a lei</h2>
<p>Não pode. O Código de Defesa do Consumidor considera prática abusiva recusar atendimento ou recusar a venda a quem se dispõe a pagar (art. 39, incisos II e IX). O mesmo código proíbe a publicidade discriminatória “de qualquer natureza” (art. 37, § 2º). E a Constituição garante que ninguém será privado de direitos por convicção política (art. 5º, VIII).</p>
<p>Por isso, segundo a Senacon, a placa ou a postagem já podem configurar prática abusiva e publicidade discriminatória <b>mesmo sem a comprovação de que alguém foi efetivamente barrado</b>. O anúncio em si já é o problema.</p>
<p>Algumas manchetes falaram em “crime”. Os documentos divulgados até agora, porém, tratam de infrações às regras de consumo, que podem levar a multa e outras sanções administrativas. Uma eventual responsabilização criminal dependeria de cada caso.</p>
<h2>Vale para qualquer lado</h2>
<p>A regra não tem lado. Uma loja não pode barrar eleitor de esquerda, de direita ou de centro. O que conta é a proibição de discriminar o consumidor, e não a bandeira de quem discrimina.</p>
<p>E o dono do negócio continua livre para ter e mostrar a opinião política dele. O que ele não pode é transformar essa opinião em critério para escolher quem atende.</p>
<h2>E o boicote do cliente?</h2>
<p>Do lado de quem compra, a liberdade é total. Deixar de frequentar uma loja por discordar do dono é uma escolha pessoal, e não há regra que obrigue alguém a consumir em determinado lugar. O dever de não discriminar recai sobre quem oferece produtos e serviços ao público.</p>
<h2>E no trabalho?</h2>
<p>O tema também chegou às empresas. O Ministério Público do Trabalho registrou milhares de denúncias de assédio eleitoral neste pleito, boa parte delas nos dias seguintes ao segundo turno. Pressionar empregado a votar em alguém ou dispensá-lo por causa da posição política é tratado como prática discriminatória e pode gerar indenização.</p>
<h2>Se acontecer com você</h2>
<ul>
<li><b>Guarde provas:</b> foto da placa, print do post, data, horário e nome de quem presenciou.</li>
<li><b>Reclame no Procon</b> da sua cidade ou na plataforma consumidor.gov.br.</li>
<li><b>Avalie com um advogado</b> se cabe pedir reparação na Justiça. Cada caso depende do que aconteceu e das provas.</li>
</ul>
''',
        'fontes': [
            ('O Tempo – Governo notifica empresas por práticas abusivas (30/10/2026)', 'https://www.otempo.com.br/economia/2026/10/30/recusar-clientes-por-orientacao-politica-e-crime-e-governo-notifica-empresas-por-praticas-abusivas'),
            ('Jornal de Brasília – Governo cita prática abusiva e notifica empresas', 'https://jornaldebrasilia.com.br/noticias/economia/governo-cita-pratica-abusiva-e-notifica-empresas-que-teriam-recusado-clientes-de-esquerda/'),
            ('Código de Defesa do Consumidor (Lei 8.078/1990)', 'https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm'),
        ],
    },
    {
        'slug': 'pensao-nao-acaba-sozinha-aos-18-anos',
        'data': '2026-10-30',
        'categoria': 'Família',
        'titulo': 'Seu filho fez 18 anos? <em>A pensão não para sozinha.</em>',
        'titulo_txt': 'Seu filho fez 18 anos? A pensão não para sozinha.',
        'resumo': 'Muita gente acredita que a pensão alimentícia termina automaticamente na maioridade. Não termina. Entenda como funciona, o que acontece se o filho estuda e o risco de parar de pagar por conta própria.',
        'foto': 'blog-pensao-18', 'foto_alt': 'Família reunida na praia ao pôr do sol',
        'resumo_box': [
            'A pensão não acaba automaticamente quando o filho completa 18 anos.',
            'Para deixar de pagar, é preciso uma decisão do juiz, e o filho tem direito de se manifestar.',
            'Se o filho estuda, a pensão costuma continuar enquanto durar a formação.',
            'Parar por conta própria gera dívida, e a dívida de pensão pode levar à prisão civil.',
        ],
        'corpo': '''
<p>“Fez 18, acabou a pensão.” A frase é comum, mas não corresponde ao que a Justiça aplica. A maioridade muda a situação, mas <b>não encerra a obrigação sozinha</b>.</p>
<h2>O que diz a Justiça</h2>
<p>O Superior Tribunal de Justiça já pacificou o tema na Súmula 358: o cancelamento da pensão do filho que atingiu a maioridade depende de decisão judicial, com direito de o filho se manifestar, ainda que nos próprios autos do processo de alimentos.</p>
<p>Na prática, quem paga precisa pedir ao juiz a exoneração da pensão, normalmente por meio de uma ação própria. Enquanto não houver decisão, o valor continua devido.</p>
<h2>E se o filho estiver estudando?</h2>
<p>Depois dos 18, a pensão deixa de ser presumida e passa a depender da necessidade de quem recebe. Quando o filho está cursando faculdade ou curso técnico, a Justiça costuma manter a pensão enquanto durar a formação, em geral até por volta dos 24 anos. Não é uma regra automática: cada caso considera a realidade de quem paga e de quem recebe.</p>
<h2>O risco de parar por conta própria</h2>
<p>Quem simplesmente deixa de pagar acumula dívida. As parcelas atrasadas podem ser cobradas na Justiça e, para as três últimas prestações anteriores à cobrança e as que vencerem durante o processo, a lei permite pedir a <b>prisão civil</b> do devedor por até três meses.</p>
<h2>Dá para resolver por acordo?</h2>
<p>Sim. Pai, mãe e filho podem chegar a um acordo sobre o fim ou a redução da pensão, e esse acordo pode ser levado ao juiz para homologação. É o caminho mais rápido e menos desgastante para todos.</p>
<h2>Em qualquer lado da história</h2>
<ul>
<li><b>Se você paga:</b> não pare por conta própria. Peça a exoneração ou faça um acordo homologado.</li>
<li><b>Se você recebe:</b> guarde comprovantes de matrícula e de despesas. Eles mostram a necessidade.</li>
</ul>
''',
        'fontes': [
            ('Superior Tribunal de Justiça – Súmula 358', None),
            ('Código de Processo Civil (Lei 13.105/2015), art. 528', 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm'),
        ],
    },
    {
        'slug': 'heranca-de-imovel-no-brasil-para-quem-mora-fora',
        'data': '2026-10-30',
        'categoria': 'Brasileiros no exterior',
        'titulo': 'Mora fora e herdou um imóvel no Brasil? <em>Dá para resolver sem viajar.</em>',
        'titulo_txt': 'Mora fora e herdou um imóvel no Brasil? Dá para resolver sem viajar.',
        'resumo': 'Inventário, partilha e até a venda do imóvel podem ser conduzidos no Brasil enquanto você continua onde mora. Veja o passo a passo e os cuidados.',
        'foto': 'blog-heranca-exterior', 'foto_alt': 'Asa de avião sobre as nuvens',
        'resumo_box': [
            'Uma procuração feita no país onde você mora permite que o advogado atue por você no Brasil.',
            'Quando os herdeiros estão de acordo, o inventário em regra pode ser feito em cartório, o que costuma ser mais rápido.',
            'Reuniões por vídeo e assinatura eletrônica resolvem quase tudo à distância.',
            'Atenção aos prazos e ao imposto sobre a herança, que varia de estado para estado.',
        ],
        'corpo': '''
<p>Perder alguém da família já é difícil. Quando você mora em outro país e descobre que precisa cuidar de um imóvel no Brasil, a primeira reação costuma ser pensar em passagem, férias e burocracia. <b>Na maioria dos casos, não é preciso viajar.</b></p>
<h2>1. A procuração</h2>
<p>Tudo começa por uma procuração que autoriza o advogado a representar você no Brasil. Ela pode ser feita no consulado brasileiro da sua região ou em cartório do país onde você mora. Neste segundo caso, o documento precisa da apostila da Convenção da Haia (ou de legalização consular, conforme o país) e, se estiver em outro idioma, de tradução juramentada.</p>
<h2>2. O inventário</h2>
<p>O inventário é o procedimento que identifica os bens e define quem fica com o quê. Quando os herdeiros estão de acordo, ele em regra pode ser feito em cartório, sem processo judicial, o que costuma ser bem mais rápido. Se houver discordância, o caminho é o inventário judicial. Nos dois casos, a presença de advogado é obrigatória.</p>
<p>A lei prevê que o inventário seja aberto em até dois meses depois do falecimento. O atraso pode gerar multa sobre o imposto, conforme a regra de cada estado.</p>
<h2>3. Documentos e CPF</h2>
<p>Todo herdeiro precisa de CPF regular. Quem mora fora consegue emitir ou regularizar o CPF pelo consulado ou pela Receita Federal. Também entram certidões do falecido, documentos do imóvel e dos herdeiros. Boa parte pode ser enviada digitalmente.</p>
<h2>4. Imposto sobre a herança</h2>
<p>O ITCMD é cobrado pelo estado, e a alíquota varia. Com a Reforma Tributária, os estados passaram a ser obrigados a cobrar alíquotas progressivas, que aumentam conforme o valor herdado. Vale calcular antes de decidir entre vender ou manter o imóvel.</p>
<h2>5. Vender ou manter</h2>
<p>Concluída a partilha, o imóvel pode ser vendido também por procuração. Em alguns casos, a venda pode até ser autorizada durante o inventário. O dinheiro pode ser transferido para o exterior pelos canais bancários regulares. Ganho de capital e situação fiscal de quem mora fora devem ser avaliados com um contador.</p>
<h2>Como a gente conduz</h2>
<p>As conversas acontecem por vídeo, no horário que funciona no seu fuso. Os documentos são assinados eletronicamente sempre que a lei permite, e você recebe notícias do andamento sem precisar perguntar.</p>
''',
        'fontes': [
            ('Código de Processo Civil (Lei 13.105/2015), arts. 610 e 611', 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm'),
            ('Lei 11.441/2007 – inventário em cartório', 'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11441.htm'),
        ],
    },
]

MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def data_pt(iso):
    a, m, d = iso.split('-')
    return f'{int(d)} de {MESES[int(m) - 1]} de {a}'


def data_en(iso):
    a, m, d = iso.split('-')
    return f'{MONTHS[int(m) - 1]} {int(d)}, {a}'
