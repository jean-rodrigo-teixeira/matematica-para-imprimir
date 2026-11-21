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

## Trilha do 1º ano

Sequência de 49 passos curtos, inspirada no que há de melhor em três abordagens:
- **Kumon:** avanço em passos bem pequenos, muita repetição e folhas de treino cronometradas;
- **Método de Singapura:** concreto → pictórico → abstrato, ligações de números, fazer 10 e modelo de barras para problemas;
- **Khan Academy:** domínio antes de avançar (critério de 90% de acertos na Folha B, indicado no gabarito).

Cada passo tem **Folha A** (com apoio visual), **Folha B** (treino) e **gabarito do professor** com objetivo, critério de avanço e habilidades BNCC.

| Unidade | Tema | Passos | PDF |
|---|---|---|---|
| 1 | Contar e escrever até 10 | 1. Contar até 5, 2. Contar até 10, 3. Escrever os números de 0 a 10, 4. Quadro de dez, 5. Antes, depois e entre, 6. Mais, menos e igual, 7. Números ordinais | [PDF](docs/pdf/1ano-unidade-1.pdf) |
| 2 | Compor e decompor até 10 | 8. As partes do 5, 9. As partes do 6 e do 7, 10. As partes do 8 e do 9, 11. Amigos do 10, 12. Ligações de números até 10 | [PDF](docs/pdf/1ano-unidade-2.pdf) |
| 3 | Adição até 10 | 13. Juntar com figuras, 14. Somar 1, 15. Somar 2, 16. Somar 0 e somar 3, 17. Adição na reta numérica, 18. Treino: adição até 10, 19. Problemas de juntar e acrescentar | [PDF](docs/pdf/1ano-unidade-3.pdf) |
| 4 | Subtração até 10 | 20. Tirar com figuras, 21. Tirar 1, 22. Tirar 2, 23. Subtração na reta numérica, 24. Quanto falta?, 25. Treino: subtração até 10, 26. Famílias de fatos, 27. Problemas de tirar, separar e comparar | [PDF](docs/pdf/1ano-unidade-4.pdf) |
| 5 | Números até 20 | 28. Contar até 20, 29. Dez e mais, 30. Ordem e comparação até 20, 31. Dobros, 32. Fazer 10 para somar, 33. Treino: adição até 20, 34. Subtração até 20, 35. Problemas até 20 | [PDF](docs/pdf/1ano-unidade-5.pdf) |
| 6 | Números até 100 | 36. Contar de 10 em 10, 37. Dezenas e unidades, 38. Quadro de 100, 39. Contar de 2 em 2, de 5 em 5 e comparar, 40. Somar e tirar com dezenas | [PDF](docs/pdf/1ano-unidade-6.pdf) |
| 7 | Geometria e localização | 41. Figuras planas, 42. Sólidos geométricos, 43. Padrões e sequências, 44. Posição e localização | [PDF](docs/pdf/1ano-unidade-7.pdf) |
| 8 | Medidas, tempo, dinheiro e dados | 45. Comparar comprimentos, 46. Calendário, 47. Dinheiro: cédulas e moedas, 48. Certo, talvez ou impossível, 49. Tabelas e gráficos | [PDF](docs/pdf/1ano-unidade-8.pdf) |

Trilha inteira em um arquivo: [`docs/pdf/1ano-trilha-completa.pdf`](docs/pdf/1ano-trilha-completa.pdf).

## Listas avulsas (2º ao 9º ano)

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
  content.py     listas avulsas do 2º ao 9º ano (enunciados, gabarito, BNCC)
  primeiro_ano.py  trilha do 1º ano (exercícios gerados com gabarito calculado)
  figuras.py     figuras SVG (quadro de dez, ligações de números, reta, barras, material dourado…)
  render1.py     layout das folhas da trilha
  build.py       gera o site e os PDFs
  site_template.html
```

## Adicionar ou editar listas

1. Edite `gerador/content.py` (cada lista é um item de `LISTAS`).
2. Rode `python3 gerador/build.py` (requer Python 3 e Google Chrome/Chromium instalado; fontes Fira Sans e Bitter recomendadas).
3. O site e os PDFs em `docs/` são atualizados.
