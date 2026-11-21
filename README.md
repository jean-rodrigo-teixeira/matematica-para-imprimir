# Matemática para Imprimir

Acervo gratuito de listas de exercícios de matemática para o Ensino Fundamental (1º ao 9º ano), alinhadas à BNCC e prontas para imprimir em A4.

Cada lista traz:
- cabeçalho com campos de escola, nome, turma e data;
- cerca de 10 questões com espaço para resolução;
- gabarito do professor em página separada (última página do PDF).

## Como usar

- **Site:** abra o catálogo em `docs/index.html` (ou pelo GitHub Pages, quando ativado), escolha a lista e clique em **Baixar PDF**.
- **PDFs direto:** todos os arquivos estão em [`docs/pdf/`](docs/pdf/). O arquivo `todas-as-listas.pdf` junta tudo em um só.

Imprima em A4, tamanho real (100%).

## Listas disponíveis

| Ano | Conteúdo | BNCC | PDF |
|-----|----------|------|-----|
| 2º | Adição e subtração até 100 | EF02MA05, EF02MA06 | [baixar](docs/pdf/2ano-adicao-subtracao.pdf) |
| 3º | Multiplicação | EF03MA03, EF03MA07 | [baixar](docs/pdf/3ano-multiplicacao.pdf) |
| 4º | Divisão | EF04MA04, EF04MA07 | [baixar](docs/pdf/4ano-divisao.pdf) |
| 5º | Frações | EF05MA03, EF05MA04, EF05MA05 | [baixar](docs/pdf/5ano-fracoes.pdf) |
| 5º | Números decimais e dinheiro | EF05MA02, EF05MA07 | [baixar](docs/pdf/5ano-decimais.pdf) |
| 6º | Múltiplos, divisores, MMC e MDC | EF06MA04, EF06MA05, EF06MA06 | [baixar](docs/pdf/6ano-mmc-mdc.pdf) |
| 7º | Números inteiros | EF07MA03, EF07MA04 | [baixar](docs/pdf/7ano-numeros-inteiros.pdf) |
| 7º | Equações do 1º grau | EF07MA18 | [baixar](docs/pdf/7ano-equacoes-1grau.pdf) |
| 8º | Porcentagem e juros simples | EF08MA04 | [baixar](docs/pdf/8ano-porcentagem.pdf) |
| 9º | Teorema de Pitágoras | EF09MA13, EF09MA14 | [baixar](docs/pdf/9ano-pitagoras.pdf) |

## Estrutura

```
docs/            site (index.html) e PDFs gerados — pasta servida pelo GitHub Pages
gerador/
  content.py     conteúdo das listas (enunciados, subitens, gabarito, BNCC)
  build.py       gera o site e os PDFs
  site_template.html
```

## Adicionar ou editar listas

1. Edite `gerador/content.py` (cada lista é um item de `LISTAS`).
2. Rode `python3 gerador/build.py` (requer Python 3 e Google Chrome/Chromium instalado; fontes Fira Sans e Bitter recomendadas).
3. O site e os PDFs em `docs/` são atualizados.
