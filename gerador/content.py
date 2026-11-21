# -*- coding: utf-8 -*-
"""Conteúdo das listas piloto. Cada questão: t (enunciado), items (subitens),
space (espaço p/ resposta: s, m, l), ans (gabarito), fig (svg opcional)."""


def fr(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'


def mx(i, a, b):  # número misto
    return f'{i}&#8239;{fr(a, b)}'


SQ = '<sup>2</sup>'

FIG_FRACAO = '''<svg class="fig" viewBox="0 0 312 62" width="260" role="img" aria-label="Retângulo dividido em 6 partes iguais, 4 pintadas">
<g stroke="#222" stroke-width="2">
<rect x="6" y="6" width="50" height="50" fill="#bdbdbd"/><rect x="56" y="6" width="50" height="50" fill="#bdbdbd"/>
<rect x="106" y="6" width="50" height="50" fill="#bdbdbd"/><rect x="156" y="6" width="50" height="50" fill="#bdbdbd"/>
<rect x="206" y="6" width="50" height="50" fill="#fff"/><rect x="256" y="6" width="50" height="50" fill="#fff"/></g></svg>'''

FIG_TRI = '''<svg class="fig" viewBox="0 0 230 150" width="200" role="img" aria-label="Triângulo retângulo com catetos a e b e hipotenusa c">
<polygon points="20,130 200,130 20,20" fill="none" stroke="#222" stroke-width="2"/>
<polyline points="20,114 36,114 36,130" fill="none" stroke="#222" stroke-width="1.5"/>
<text x="110" y="147" font-size="15" text-anchor="middle" font-style="italic">b</text>
<text x="8" y="80" font-size="15" text-anchor="middle" font-style="italic">a</text>
<text x="122" y="68" font-size="15" text-anchor="middle" font-style="italic">c</text></svg>'''

FIG_ESCADA = '''<svg class="fig" viewBox="0 0 200 160" width="160" role="img" aria-label="Escada apoiada em uma parede">
<line x1="150" y1="10" x2="150" y2="140" stroke="#222" stroke-width="5"/>
<line x1="10" y1="140" x2="190" y2="140" stroke="#222" stroke-width="2"/>
<line x1="60" y1="140" x2="150" y2="22" stroke="#555" stroke-width="3"/>
<text x="92" y="74" font-size="13">5 m</text><text x="96" y="156" font-size="13">3 m</text>
<text x="156" y="84" font-size="13">?</text></svg>'''


LISTAS = [
 {
  "slug": "2ano-adicao-subtracao", "ano": 2, "titulo": "Adição e subtração até 100",
  "tema": "Números", "bncc": "EF02MA05, EF02MA06",
  "q": [
   {"t": "Calcule:", "items": ["23 + 45 =", "37 + 28 =", "56 + 19 =", "64 + 27 ="], "space": "s",
    "ans": "a) 68 &nbsp; b) 65 &nbsp; c) 75 &nbsp; d) 91"},
   {"t": "Calcule:", "items": ["78 − 35 =", "62 − 27 =", "90 − 46 =", "83 − 58 ="], "space": "s",
    "ans": "a) 43 &nbsp; b) 35 &nbsp; c) 44 &nbsp; d) 25"},
   {"t": "Complete com o número que falta:", "items": ["34 + ____ = 50", "____ − 20 = 45", "70 − ____ = 38"], "space": "s",
    "ans": "a) 16 &nbsp; b) 65 &nbsp; c) 32"},
   {"t": "Ana tinha 48 figurinhas e ganhou 25 da prima. Quantas figurinhas Ana tem agora?", "space": "m", "ans": "73 figurinhas"},
   {"t": "Em um ônibus havia 52 passageiros. No ponto, desceram 17. Quantos passageiros ficaram no ônibus?", "space": "m", "ans": "35 passageiros"},
   {"t": "Pedro tem 36 bolinhas de gude. João tem 19 bolinhas a mais que Pedro. Quantas bolinhas João tem?", "space": "m", "ans": "55 bolinhas"},
   {"t": "Uma turma tem 28 alunos. Hoje faltaram 6. Quantos alunos vieram à aula?", "space": "m", "ans": "22 alunos"},
   {"t": "Na feira, Dona Rosa vendeu 45 laranjas de manhã e 38 à tarde. Quantas laranjas ela vendeu no dia?", "space": "m", "ans": "83 laranjas"},
   {"t": "Continue a sequência: &nbsp; 15, 25, 35, ____, ____, ____", "space": "s", "ans": "45, 55, 65"},
   {"t": "Um livro tem 80 páginas. Lucas já leu 47. Quantas páginas faltam para ele terminar o livro?", "space": "m", "ans": "33 páginas"},
  ]},
 {
  "slug": "3ano-multiplicacao", "ano": 3, "titulo": "Multiplicação",
  "tema": "Números", "bncc": "EF03MA03, EF03MA07",
  "q": [
   {"t": "Calcule:", "items": ["3 × 7 =", "4 × 8 =", "6 × 5 =", "7 × 9 =", "8 × 6 =", "9 × 4 ="], "space": "s",
    "ans": "a) 21 &nbsp; b) 32 &nbsp; c) 30 &nbsp; d) 63 &nbsp; e) 48 &nbsp; f) 36"},
   {"t": "Escreva cada adição como uma multiplicação e dê o resultado:", "items": ["5 + 5 + 5 + 5", "7 + 7 + 7"], "space": "s",
    "ans": "a) 4 × 5 = 20 &nbsp; b) 3 × 7 = 21"},
   {"t": "Uma caixa tem 6 ovos. Quantos ovos há em 5 caixas?", "space": "m", "ans": "30 ovos"},
   {"t": "Uma sala tem 4 fileiras com 8 carteiras em cada uma. Quantas carteiras há na sala?", "space": "m", "ans": "32 carteiras"},
   {"t": "Calcule o dobro e o triplo de cada número:", "items": ["12", "15"], "space": "s",
    "ans": "a) dobro 24, triplo 36 &nbsp; b) dobro 30, triplo 45"},
   {"t": "Uma bicicleta tem 2 rodas. Quantas rodas têm 9 bicicletas?", "space": "m", "ans": "18 rodas"},
   {"t": "Um pacote de figurinhas custa R$ 3. Quanto custam 7 pacotes?", "space": "m", "ans": "R$ 21"},
   {"t": "Calcule:", "items": ["23 × 3 =", "14 × 5 =", "32 × 4 =", "25 × 6 ="], "space": "m",
    "ans": "a) 69 &nbsp; b) 70 &nbsp; c) 128 &nbsp; d) 150"},
   {"t": "Bia tem 4 camisetas e 3 bermudas. De quantas maneiras diferentes ela pode se vestir usando uma camiseta e uma bermuda?", "space": "m", "ans": "12 maneiras"},
   {"t": "Complete:", "items": ["6 × ____ = 42", "____ × 8 = 56", "9 × ____ = 81"], "space": "s",
    "ans": "a) 7 &nbsp; b) 7 &nbsp; c) 9"},
  ]},
 {
  "slug": "4ano-divisao", "ano": 4, "titulo": "Divisão",
  "tema": "Números", "bncc": "EF04MA04, EF04MA07",
  "q": [
   {"t": "Calcule:", "items": ["24 ÷ 6 =", "45 ÷ 5 =", "63 ÷ 7 =", "56 ÷ 8 ="], "space": "s",
    "ans": "a) 4 &nbsp; b) 9 &nbsp; c) 9 &nbsp; d) 7"},
   {"t": "Efetue as divisões e indique o quociente e o resto:", "items": ["29 ÷ 4", "50 ÷ 6", "38 ÷ 5", "67 ÷ 9"], "space": "m",
    "ans": "a) 7, resto 1 &nbsp; b) 8, resto 2 &nbsp; c) 7, resto 3 &nbsp; d) 7, resto 4"},
   {"t": "Calcule:", "items": ["84 ÷ 4 =", "96 ÷ 3 =", "125 ÷ 5 =", "144 ÷ 6 ="], "space": "m",
    "ans": "a) 21 &nbsp; b) 32 &nbsp; c) 25 &nbsp; d) 24"},
   {"t": "36 balas foram repartidas igualmente entre 4 crianças. Quantas balas cada criança recebeu?", "space": "m", "ans": "9 balas"},
   {"t": "Uma professora vai formar grupos de 5 alunos com os 32 alunos da turma. Quantos grupos completos ela consegue formar? Quantos alunos sobram?", "space": "m", "ans": "6 grupos completos; sobram 2 alunos"},
   {"t": "Um carro leva 4 pessoas por viagem. Qual é o menor número de viagens necessário para levar 30 pessoas?", "space": "m", "ans": "8 viagens (7 viagens completas levam 28; falta mais uma para 2 pessoas)"},
   {"t": "Três irmãos vão dividir igualmente R$ 120. Quanto cada um vai receber?", "space": "m", "ans": "R$ 40"},
   {"t": "Em uma divisão, o divisor é 7, o quociente é 12 e o resto é 3. Qual é o dividendo?", "space": "m", "ans": "87 (7 × 12 + 3)"},
   {"t": "Uma granja guarda ovos em caixas de 12. Com 150 ovos, quantas caixas ficam completas? Quantos ovos sobram?", "space": "m", "ans": "12 caixas; sobram 6 ovos"},
   {"t": "Calcule:", "items": ["a metade de 64", "a terça parte de 45", "a quarta parte de 80"], "space": "s",
    "ans": "a) 32 &nbsp; b) 15 &nbsp; c) 20"},
  ]},
 {
  "slug": "5ano-fracoes", "ano": 5, "titulo": "Frações",
  "tema": "Números", "bncc": "EF05MA03, EF05MA04, EF05MA05",
  "q": [
   {"t": "Que fração da figura está pintada? Escreva também a fração simplificada.", "fig": FIG_FRACAO, "space": "s",
    "ans": f"{fr(4,6)} = {fr(2,3)}"},
   {"t": "Uma pizza foi dividida em 8 pedaços iguais e Carla comeu 3. Que fração da pizza Carla comeu? Que fração sobrou?", "space": "m",
    "ans": f"Comeu {fr(3,8)}; sobrou {fr(5,8)}"},
   {"t": "Simplifique as frações:", "items": [fr(6,8), fr(10,15), fr(12,18), fr(20,25)], "space": "s",
    "ans": f"a) {fr(3,4)} &nbsp; b) {fr(2,3)} &nbsp; c) {fr(2,3)} &nbsp; d) {fr(4,5)}"},
   {"t": "Complete com &gt;, &lt; ou =:", "items": [f"{fr(3,5)} ___ {fr(2,5)}", f"{fr(1,3)} ___ {fr(1,4)}", f"{fr(2,4)} ___ {fr(1,2)}", f"{fr(3,8)} ___ {fr(3,4)}"], "space": "s",
    "ans": "a) &gt; &nbsp; b) &gt; &nbsp; c) = &nbsp; d) &lt;"},
   {"t": f"Escreva em ordem crescente: &nbsp; {fr(1,2)}, &nbsp; {fr(1,4)}, &nbsp; {fr(3,4)}, &nbsp; {fr(1,8)}", "space": "s",
    "ans": f"{fr(1,8)}, {fr(1,4)}, {fr(1,2)}, {fr(3,4)}"},
   {"t": "Complete para obter frações equivalentes:", "items": [f"{fr(3,4)} = {fr('____',12)}", f"{fr(2,5)} = {fr(8,'____')}"], "space": "s",
    "ans": "a) 9 &nbsp; b) 20"},
   {"t": "Calcule:", "items": [f"{fr(2,7)} + {fr(3,7)} =", f"{fr(5,9)} − {fr(2,9)} =", f"{fr(1,2)} + {fr(1,4)} =", f"{fr(3,4)} − {fr(1,2)} ="], "space": "m",
    "ans": f"a) {fr(5,7)} &nbsp; b) {fr(3,9)} = {fr(1,3)} &nbsp; c) {fr(3,4)} &nbsp; d) {fr(1,4)}"},
   {"t": "Calcule:", "items": [f"{fr(2,3)} de 24", f"{fr(3,5)} de 40"], "space": "s", "ans": "a) 16 &nbsp; b) 24"},
   {"t": f"Uma turma tem 30 alunos, e {fr(2,5)} deles são meninos. Quantos meninos e quantas meninas há na turma?", "space": "m",
    "ans": "12 meninos e 18 meninas"},
   {"t": "Escreva como número misto:", "items": [fr(7,4), fr(11,3)], "space": "s",
    "ans": f"a) {mx(1,3,4)} &nbsp; b) {mx(3,2,3)}"},
  ]},
 {
  "slug": "5ano-decimais", "ano": 5, "titulo": "Números decimais e dinheiro",
  "tema": "Números", "bncc": "EF05MA02, EF05MA07",
  "q": [
   {"t": "Escreva na forma decimal:", "items": ["três décimos", "vinte e cinco centésimos", "um inteiro e sete décimos"], "space": "s",
    "ans": "a) 0,3 &nbsp; b) 0,25 &nbsp; c) 1,7"},
   {"t": "Complete com &gt;, &lt; ou =:", "items": ["0,5 ___ 0,45", "2,3 ___ 2,30", "1,08 ___ 1,8"], "space": "s",
    "ans": "a) &gt; &nbsp; b) = &nbsp; c) &lt;"},
   {"t": "Escreva em ordem crescente: &nbsp; 0,7 &nbsp; 0,07 &nbsp; 1,2 &nbsp; 0,72", "space": "s", "ans": "0,07; 0,7; 0,72; 1,2"},
   {"t": "Calcule:", "items": ["2,5 + 1,3 =", "4,75 + 2,5 =", "8,4 − 3,2 =", "10 − 4,35 ="], "space": "m",
    "ans": "a) 3,8 &nbsp; b) 7,25 &nbsp; c) 5,2 &nbsp; d) 5,65"},
   {"t": "Júlia comprou um caderno de R$ 12,50 e uma caneta de R$ 3,75. Quanto ela gastou? Se pagou com uma nota de R$ 20,00, quanto recebeu de troco?", "space": "m",
    "ans": "Gastou R$ 16,25; troco de R$ 3,75"},
   {"t": "Calcule:", "items": ["0,8 × 10 =", "3,25 × 100 =", "45 ÷ 10 =", "7,2 ÷ 10 ="], "space": "s",
    "ans": "a) 8 &nbsp; b) 325 &nbsp; c) 4,5 &nbsp; d) 0,72"},
   {"t": "Um litro de leite custa R$ 4,90. Quanto custam 3 litros?", "space": "m", "ans": "R$ 14,70"},
   {"t": "Escreva cada fração na forma decimal:", "items": [fr(1,2), fr(3,4), fr(1,5), fr(7,10)], "space": "s",
    "ans": "a) 0,5 &nbsp; b) 0,75 &nbsp; c) 0,2 &nbsp; d) 0,7"},
   {"t": "Mariana tem 1,45 m de altura e o irmão dela tem 1,28 m. Qual é a diferença de altura entre os dois?", "space": "m", "ans": "0,17 m (17 cm)"},
   {"t": "Rafael correu 3,6 km de manhã e 2,8 km à tarde. Quantos quilômetros ele correu no dia?", "space": "m", "ans": "6,4 km"},
  ]},
 {
  "slug": "6ano-mmc-mdc", "ano": 6, "titulo": "Múltiplos, divisores, MMC e MDC",
  "tema": "Números", "bncc": "EF06MA04, EF06MA05, EF06MA06",
  "q": [
   {"t": "Escreva os cinco primeiros múltiplos não nulos de:", "items": ["6", "9"], "space": "s",
    "ans": "a) 6, 12, 18, 24, 30 &nbsp; b) 9, 18, 27, 36, 45"},
   {"t": "Escreva todos os divisores de:", "items": ["18", "24"], "space": "s",
    "ans": "a) 1, 2, 3, 6, 9, 18 &nbsp; b) 1, 2, 3, 4, 6, 8, 12, 24"},
   {"t": "Circule os números primos: &nbsp; 2 &nbsp; 9 &nbsp; 11 &nbsp; 15 &nbsp; 17 &nbsp; 21 &nbsp; 23 &nbsp; 27", "space": "s", "ans": "2, 11, 17 e 23"},
   {"t": "Decomponha em fatores primos:", "items": ["36", "60", "84"], "space": "m",
    "ans": f"a) 2{SQ} × 3{SQ} &nbsp; b) 2{SQ} × 3 × 5 &nbsp; c) 2{SQ} × 3 × 7"},
   {"t": "Calcule o MMC:", "items": ["MMC(4, 6)", "MMC(8, 12)", "MMC(10, 15)", "MMC(6, 8, 9)"], "space": "m",
    "ans": "a) 12 &nbsp; b) 24 &nbsp; c) 30 &nbsp; d) 72"},
   {"t": "Calcule o MDC:", "items": ["MDC(12, 18)", "MDC(24, 36)", "MDC(35, 49)", "MDC(40, 60)"], "space": "m",
    "ans": "a) 6 &nbsp; b) 12 &nbsp; c) 7 &nbsp; d) 20"},
   {"t": "O número 1.236 é divisível por 2? Por 3? Por 5? Por 9? Justifique usando os critérios de divisibilidade.", "space": "m",
    "ans": "Por 2: sim (termina em 6). Por 3: sim (1+2+3+6 = 12). Por 5: não. Por 9: não (12 não é múltiplo de 9)."},
   {"t": "Dois ônibus saem juntos do terminal às 7h. Um sai a cada 15 minutos e o outro a cada 20 minutos. A que horas eles sairão juntos novamente?", "space": "m",
    "ans": "Às 8h (MMC(15, 20) = 60 minutos)"},
   {"t": "Duas fitas, de 24 cm e 36 cm, serão cortadas em pedaços iguais, do maior tamanho possível, sem sobras. Qual será o tamanho de cada pedaço? Quantos pedaços serão obtidos?", "space": "m",
    "ans": "12 cm cada (MDC = 12); 5 pedaços (2 + 3)"},
   {"t": "Ana visita a avó a cada 6 dias e Bia, a cada 8 dias. Hoje as duas se encontraram lá. Daqui a quantos dias elas se encontrarão de novo na casa da avó?", "space": "m",
    "ans": "24 dias (MMC(6, 8) = 24)"},
  ]},
 {
  "slug": "7ano-numeros-inteiros", "ano": 7, "titulo": "Números inteiros",
  "tema": "Números", "bncc": "EF07MA03, EF07MA04",
  "q": [
   {"t": "Escreva em ordem crescente: &nbsp; −5, &nbsp; 3, &nbsp; 0, &nbsp; −12, &nbsp; 7, &nbsp; −1", "space": "s", "ans": "−12, −5, −1, 0, 3, 7"},
   {"t": "Complete com &gt; ou &lt;:", "items": ["−3 ___ −8", "−4 ___ 2", "0 ___ −6"], "space": "s",
    "ans": "a) &gt; &nbsp; b) &lt; &nbsp; c) &gt;"},
   {"t": "Responda:", "items": ["Qual é o módulo de −9?", "Qual é o oposto de 14?"], "space": "s", "ans": "a) 9 &nbsp; b) −14"},
   {"t": "Calcule:", "items": ["(−7) + (+4)", "(−6) + (−9)", "(+12) + (−5)", "(−8) − (+3)", "(+5) − (−6)", "(−10) − (−4)"], "space": "m",
    "ans": "a) −3 &nbsp; b) −15 &nbsp; c) 7 &nbsp; d) −11 &nbsp; e) 11 &nbsp; f) −6"},
   {"t": "Calcule:", "items": ["(−4) × (+6)", "(−7) × (−3)", "(+48) ÷ (−8)", "(−36) ÷ (−9)"], "space": "s",
    "ans": "a) −24 &nbsp; b) 21 &nbsp; c) −6 &nbsp; d) 4"},
   {"t": "Resolva as expressões:", "items": ["(−3) × 4 + (−10) ÷ 2", "15 − (−2) × (−5)"], "space": "m",
    "ans": "a) −17 &nbsp; b) 5"},
   {"t": "De madrugada, a temperatura em uma cidade era de −4 °C. Até o meio-dia, subiu 11 °C. Qual era a temperatura ao meio-dia?", "space": "m", "ans": "7 °C"},
   {"t": "Carlos tinha R$ 150,00 na conta e fez uma compra de R$ 230,00 no débito. Qual ficou sendo o saldo da conta?", "space": "m", "ans": "−R$ 80,00 (saldo negativo de 80 reais)"},
   {"t": "Um mergulhador está a 18 metros abaixo do nível do mar (−18 m) e sobe 7 metros. Em que posição ele fica?", "space": "m", "ans": "−11 m (11 metros abaixo do nível do mar)"},
   {"t": "Calcule as potências:", "items": ["(−2)<sup>3</sup>", "(−3)<sup>2</sup>"], "space": "s", "ans": "a) −8 &nbsp; b) 9"},
  ]},
 {
  "slug": "7ano-equacoes-1grau", "ano": 7, "titulo": "Equações do 1º grau",
  "tema": "Álgebra", "bncc": "EF07MA18",
  "q": [
   {"t": "Resolva as equações:", "items": ["<i>x</i> + 7 = 15", "<i>x</i> − 9 = 4", "3<i>x</i> = 27", f"{fr('<i>x</i>',4)} = 6"], "space": "m",
    "ans": "a) <i>x</i> = 8 &nbsp; b) <i>x</i> = 13 &nbsp; c) <i>x</i> = 9 &nbsp; d) <i>x</i> = 24"},
   {"t": "Resolva as equações:", "items": ["2<i>x</i> + 5 = 17", "5<i>x</i> − 8 = 27", "4<i>x</i> + 3 = 2<i>x</i> + 11", "3(<i>x</i> − 2) = 15", "7<i>x</i> − 4 = 3<i>x</i> + 20"], "space": "l",
    "ans": "a) 6 &nbsp; b) 7 &nbsp; c) 4 &nbsp; d) 7 &nbsp; e) 6"},
   {"t": "Resolva as equações:", "items": [f"{fr('<i>x</i>',2)} + 3 = 10", f"{fr('<i>x</i> + 4',3)} = 5"], "space": "m",
    "ans": "a) <i>x</i> = 14 &nbsp; b) <i>x</i> = 11"},
   {"t": "Verifique se 5 é solução da equação 2<i>x</i> − 3 = <i>x</i> + 2.", "space": "s", "ans": "Sim: 2·5 − 3 = 7 e 5 + 2 = 7"},
   {"t": "Pensei em um número, multipliquei por 3 e somei 4. O resultado foi 31. Em que número pensei?", "space": "m", "ans": "9"},
   {"t": "A soma de dois números consecutivos é 47. Quais são esses números?", "space": "m", "ans": "23 e 24"},
   {"t": "A idade de Pedro é o triplo da idade do filho. Juntos, eles têm 48 anos. Qual é a idade de cada um?", "space": "m", "ans": "Filho: 12 anos; Pedro: 36 anos"},
   {"t": "Um retângulo tem perímetro de 40 cm. O comprimento tem 4 cm a mais que a largura. Quais são as medidas do retângulo?", "space": "m", "ans": "Largura 8 cm e comprimento 12 cm"},
   {"t": "Um celular foi comprado com entrada de R$ 200,00 mais 5 parcelas iguais, num total de R$ 950,00. Qual é o valor de cada parcela?", "space": "m", "ans": "R$ 150,00"},
   {"t": "Uma corrida de táxi custa R$ 6,00 fixos mais R$ 2,50 por quilômetro rodado. Uma pessoa pagou R$ 31,00. Quantos quilômetros ela percorreu?", "space": "m", "ans": "10 km"},
  ]},
 {
  "slug": "8ano-porcentagem", "ano": 8, "titulo": "Porcentagem e juros simples",
  "tema": "Números", "bncc": "EF08MA04",
  "q": [
   {"t": "Escreva cada porcentagem na forma decimal e na forma de fração irredutível:", "items": ["25%", "40%", "5%"], "space": "s",
    "ans": f"a) 0,25 = {fr(1,4)} &nbsp; b) 0,4 = {fr(2,5)} &nbsp; c) 0,05 = {fr(1,20)}"},
   {"t": "Calcule:", "items": ["10% de 350", "25% de 80", "15% de 200", "120% de 50"], "space": "m",
    "ans": "a) 35 &nbsp; b) 20 &nbsp; c) 30 &nbsp; d) 60"},
   {"t": "Uma camiseta custa R$ 150,00 e está com 20% de desconto. Qual é o preço com desconto?", "space": "m", "ans": "R$ 120,00"},
   {"t": "Um salário de R$ 2.500,00 teve aumento de 8%. Qual é o novo salário?", "space": "m", "ans": "R$ 2.700,00"},
   {"t": "Em uma turma de 40 alunos, 14 são meninas. Qual é a porcentagem de meninas?", "space": "m", "ans": "35%"},
   {"t": "O preço de um produto passou de R$ 80,00 para R$ 92,00. Qual foi a porcentagem de aumento?", "space": "m", "ans": "15%"},
   {"t": "Uma pessoa aplicou R$ 1.000,00 a juros simples de 2% ao mês, durante 6 meses. Quanto recebeu de juros? Qual é o montante ao final?", "space": "m",
    "ans": "Juros de R$ 120,00; montante de R$ 1.120,00"},
   {"t": "Um produto custava R$ 200,00. Teve aumento de 10% e, depois, desconto de 10% sobre o novo preço. Qual é o preço final? Ele voltou ao valor inicial?", "space": "m",
    "ans": "R$ 198,00; não voltou ao valor inicial"},
   {"t": "Em uma pesquisa com 500 pessoas, 60% preferem ônibus ao metrô. Quantas pessoas preferem ônibus?", "space": "m", "ans": "300 pessoas"},
   {"t": "O litro da gasolina custa R$ 6,00. Um posto dá 5% de desconto para pagamento no Pix. Quanto custa o litro no Pix?", "space": "m", "ans": "R$ 5,70"},
  ]},
 {
  "slug": "9ano-pitagoras", "ano": 9, "titulo": "Teorema de Pitágoras",
  "tema": "Geometria", "bncc": "EF09MA13, EF09MA14",
  "q": [
   {"t": f"No triângulo retângulo abaixo, <i>a</i> e <i>b</i> são os catetos e <i>c</i> é a hipotenusa. Calcule <i>c</i> quando:", "fig": FIG_TRI,
    "items": ["<i>a</i> = 6 e <i>b</i> = 8", "<i>a</i> = 5 e <i>b</i> = 12", "<i>a</i> = 9 e <i>b</i> = 12"], "space": "m",
    "ans": "a) 10 &nbsp; b) 13 &nbsp; c) 15"},
   {"t": "Calcule a medida do cateto desconhecido:", "items": ["hipotenusa 25 e cateto 7", "hipotenusa 17 e cateto 15"], "space": "m",
    "ans": "a) 24 &nbsp; b) 8"},
   {"t": "Verifique se os triângulos com as medidas abaixo são retângulos:", "items": ["7, 24 e 25", "6, 7 e 9"], "space": "m",
    "ans": f"a) Sim: 7{SQ} + 24{SQ} = 49 + 576 = 625 = 25{SQ} &nbsp; b) Não: 6{SQ} + 7{SQ} = 85 ≠ 81 = 9{SQ}"},
   {"t": "Uma escada de 5 m está apoiada em uma parede, com o pé a 3 m da parede. A que altura a escada toca a parede?", "fig": FIG_ESCADA, "space": "m", "ans": "4 m"},
   {"t": "A tela de uma TV retangular mede 40 cm por 30 cm. Quanto mede a diagonal dessa tela?", "space": "m", "ans": "50 cm"},
   {"t": "Calcule a diagonal de um quadrado de lado 5 cm. Dê a resposta na forma de raiz e o valor aproximado.", "space": "m", "ans": "5√2 cm ≈ 7,07 cm"},
   {"t": "Calcule a altura de um triângulo equilátero de lado 6 cm.", "space": "m", "ans": "3√3 cm ≈ 5,20 cm"},
   {"t": "Uma pipa está presa a uma linha esticada de 50 m. A distância horizontal entre a pessoa e o ponto logo abaixo da pipa é de 30 m. A que altura está a pipa? (Desconsidere a altura da pessoa.)", "space": "m", "ans": "40 m"},
   {"t": "Calcule a distância entre os pontos A(1, 2) e B(7, 10) no plano cartesiano.", "space": "m", "ans": "10 (√(6² + 8²) = √100)"},
   {"t": "Um terreno retangular mede 12 m por 16 m. Quantos metros de cerca são necessários para cercar apenas a diagonal do terreno?", "space": "m", "ans": "20 m"},
  ]},
]
