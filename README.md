# Site — Correia Santos & Lamunier Advogados

Código-fonte de **correialamunier.com** (português e inglês). Hospedagem: GitHub Pages.

## Como funciona
- Toda alteração enviada para a branch `main` dispara o workflow **Publicar site**
  (`.github/workflows/publicar.yml`): ele roda `python build2.py`, gera a pasta `dist/` e publica.
- Não há limite de publicações por mês.

## Onde mexer
| O quê | Arquivo |
|---|---|
| Textos das páginas (PT e EN) | `content_v1.py` |
| Estrutura das páginas | `pages2.py` |
| Cabeçalho, rodapé, sitemap, montagem | `build2.py` |
| Artigos da aba Novidades | `artigos.py` (novo artigo no topo da lista) + foto em `img/photos/` |
| Estilo e comportamento | `src/styles.css`, `src/main.js` |
| Logos e imagens | `img/` |
| Imagens da assinatura de e-mail (não remover) | `assinatura/` |

## Formulário de contato
Enviado pelo FormSubmit para correia@correialamunier.com (`FORM_ENDPOINT` em `src/main.js`).

## Domínio
Domínio registrado na Hostinger; DNS gerenciado na zona do Netlify (inclui os registros do
Microsoft 365 — MX, SPF e autodiscover — que não devem ser apagados).
Raiz aponta para o GitHub Pages (A 185.199.108-111.153) e `www` é CNAME para
`victorsantosvs97-alt.github.io`.

## Gerar localmente
```
python3 build2.py   # gera dist/
```
