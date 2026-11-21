# -*- coding: utf-8 -*-
"""Trilha do 1º ano: passos pequenos (Kumon), apoio concreto-pictórico-abstrato e
ligações de números/modelo de barras (Singapura), domínio antes de avançar (Khan).
Cada passo tem Folha A (com apoio visual) e Folha B (treino). Gabarito calculado aqui."""
import random
from figuras import (objs, dots, tenframe, bond, numline, rods, bar_model, bar_compare, trace_row,
                     shape_row, shape, solid, money, svg, ICONES, NOMES, SHAPE_NOME, INK, FILL)

BX = '<span class="bx"></span>'
BXW = '<span class="bx w"></span>'


def EX(v):
    return f'<span class="bx exv">{v}</span>'


def blk(instr, items, cols=2, example=None, size="", note=""):
    """items: lista de (html, resposta). example: html já preenchido (não entra no gabarito)."""
    return {"instr": instr, "items": items, "cols": cols, "example": example, "size": size, "note": note}


def free(instr, html):
    return {"instr": instr, "items": [(html, None)], "cols": 1, "example": None, "size": "", "note": "", "free": True}


NOMES_P = ["Ana", "Bia", "Caio", "Davi", "Eva", "Léo", "Mia", "Theo", "Lia", "Gabi", "Rafa", "Nina", "João", "Duda", "Iago", "Luna"]


def nome_obj(icon, n):
    s, p, g = NOMES[icon]
    return s if n == 1 else p


def quant(icon):
    return "Quantas" if NOMES[icon][2] == "f" else "Quantos"


PASSOS = []
UNIDADES = []


def unidade(titulo, bncc):
    UNIDADES.append({"n": len(UNIDADES) + 1, "titulo": titulo, "bncc": bncc, "passos": []})


def passo(slug, titulo, objetivo):
    def deco(fn):
        u = UNIDADES[-1]
        n = len(PASSOS) + 1
        rng = random.Random(f"1ano-{slug}")
        folhas = fn(rng)
        p = {"slug": f"1ano-p{n:02d}-{slug}", "n": n, "titulo": titulo, "objetivo": objetivo,
             "unidade": u["n"], "unidade_titulo": u["titulo"], "bncc": u["bncc"], "folhas": folhas}
        PASSOS.append(p)
        u["passos"].append(p)
        return fn
    return deco


# ---------- utilidades de geração ----------
def shuffled(rng, seq):
    s = list(seq)
    rng.shuffle(s)
    return s


def pick(rng, pool, k):
    """k elementos do pool, repetindo o mínimo e evitando vizinhos iguais."""
    out = []
    while len(out) < k:
        out += shuffled(rng, pool)
    out = out[:k]
    for i in range(1, len(out)):
        if out[i] == out[i - 1]:
            for j in range(i + 1, len(out)):
                if out[j] != out[i - 1]:
                    out[i], out[j] = out[j], out[i]
                    break
    return out


def drill(rng, pairs, k, op="+"):
    """Itens de treino estilo Kumon: 'a op b = □'."""
    ps = pick(rng, pairs, k)
    items = []
    for a, b in ps:
        r = a + b if op == "+" else a - b
        items.append((f"{a} {op_s(op)} {b} = {BX}", r))
    return items


def op_s(op):
    return "+" if op == "+" else "−"


def eq_items(rng, triples, k):
    """triples: (html, resposta) já prontos."""
    return pick(rng, triples, k)


def seq_row(nums, blanks):
    cells = []
    for i, v in enumerate(nums):
        cells.append(BX if i in blanks else f'<span class="cell">{v}</span>')
    return '<span class="seq">' + "".join(cells) + "</span>"


def seq_items(rng, start, end, step, length, nblank, k):
    items = []
    starts = list(range(start, end - step * (length - 1) + 1, step)) if step > 0 else list(range(start, end - step * (length - 1) - 1, step))
    for s in pick(rng, starts, k):
        nums = [s + i * step for i in range(length)]
        bl = sorted(rng.sample(range(1, length), nblank))
        items.append((seq_row(nums, bl), ", ".join(str(nums[i]) for i in bl)))
    return items


# =====================================================================
unidade("Contar e escrever até 10", "EF01MA01, EF01MA02, EF01MA04, EF01MA05")


@passo("contar-ate-5", "Contar até 5", "Contar objetos de 1 a 5 e registrar a quantidade com algarismos.")
def _(rng):
    ic = pick(rng, ICONES, 13)
    ns = pick(rng, [1, 2, 3, 4, 5], 13)
    A = [blk("Conte e escreva quantos há.", [(f'{objs(n, ic[i])} {BX}', n) for i, n in enumerate(ns[1:9], 1)], cols=4,
             example=f'{objs(ns[0], ic[0])} {EX(ns[0])}'),
         blk("Desenhe a quantidade de bolinhas pedida.", [(f'<span class="big">{n}</span><span class="draw"></span>', None) for n in pick(rng, [1, 2, 3, 4, 5], 4)], cols=4)]
    B = [blk("Cubra os números pontilhados.", [(trace_row(str(d), 9), None) for d in "12345"], cols=1),
         blk("Conte as bolinhas e escreva o número.", [(f'{dots(n)} {BX}', n) for n in pick(rng, [1, 2, 3, 4, 5], 8)], cols=4)]
    return [A, B]


@passo("contar-ate-10", "Contar até 10", "Contar objetos de 6 a 10 usando grupos de 5.")
def _(rng):
    ic = pick(rng, ICONES, 12)
    ns = pick(rng, [6, 7, 8, 9, 10], 9)
    A = [blk("Conte e escreva quantos há. Dica: cada linha cheia tem 5.", [(f'{objs(n, ic[i])} {BX}', n) for i, n in enumerate(ns[1:], 1)], cols=4,
             example=f'{objs(ns[0], ic[0])} {EX(ns[0])}'),
         blk("Desenhe a quantidade de bolinhas pedida.", [(f'<span class="big">{n}</span><span class="draw"></span>', None) for n in pick(rng, [6, 7, 8, 9, 10], 4)], cols=4)]
    B = [blk("Cubra os números pontilhados.", [(trace_row(d, 9), None) for d in ["6", "7", "8", "9", "0"]], cols=1),
         blk("Conte as bolinhas e escreva o número.", [(f'{dots(n)} {BX}', n) for n in pick(rng, range(1, 11), 8)], cols=4)]
    return [A, B]


@passo("escrever-0-a-10", "Escrever os números de 0 a 10", "Escrever os algarismos e completar a sequência de 0 a 10.")
def _(rng):
    A = [blk("Cubra os números pontilhados e continue.", [(trace_row(str(d), 9, 40), None) for d in range(10)], cols=1)]
    fw = []
    for _ in range(5):
        bl = sorted(rng.sample(range(1, 11), 4))
        fw.append((seq_row(list(range(11)), bl), ", ".join(str(i) for i in bl)))
    bw = []
    for _ in range(3):
        bl = sorted(rng.sample(range(1, 11), 4))
        nums = list(range(10, -1, -1))
        bw.append((seq_row(nums, bl), ", ".join(str(nums[i]) for i in bl)))
    B = [blk("Complete a sequência.", fw, cols=1), blk("Agora de trás para frente.", bw, cols=1)]
    return [A, B]


@passo("quadro-de-dez", "Quadro de dez", "Ler e representar quantidades até 10 no quadro de dez.")
def _(rng):
    ns = pick(rng, range(1, 11), 13)
    A = [blk("Quantas bolinhas há no quadro?", [(f'{tenframe(n)} {BX}', n) for n in ns[1:]], cols=3,
             example=f'{tenframe(ns[0])} {EX(ns[0])}')]
    B = [blk("Desenhe as bolinhas no quadro.", [(f'<span class="big">{n}</span> {tenframe(0)}', None) for n in pick(rng, range(2, 11), 6)], cols=2),
         blk("Quantos espaços vazios há no quadro?", [(f'{tenframe(n)} {BX}', 10 - n) for n in pick(rng, range(1, 10), 6)], cols=3)]
    return [A, B]


@passo("antes-depois-entre", "Antes, depois e entre", "Identificar o número que vem antes, depois e entre outros até 10.")
def _(rng):
    sup = numline(0, 10, width=520)
    aft = [(seq_row([n, n + 1], [1]), n + 1) for n in pick(rng, range(0, 10), 8)]
    bef = [(seq_row([n - 1, n], [0]), n - 1) for n in pick(rng, range(1, 11), 8)]
    A = [free("Use a reta para ajudar.", sup),
         blk("Escreva o número que vem <b>depois</b>.", aft, cols=4),
         blk("Escreva o número que vem <b>antes</b>.", bef, cols=4)]
    bet = [(seq_row([n - 1, n, n + 1], [1]), n) for n in pick(rng, range(1, 10), 12)]
    order = []
    for _ in range(4):
        t = sorted(rng.sample(range(0, 11), 3))
        s = shuffled(rng, t)
        order.append((f'{", ".join(map(str, s))} &nbsp;→&nbsp; {BX} {BX} {BX}', ", ".join(map(str, t))))
    B = [blk("Escreva o número que está <b>entre</b>.", bet, cols=4),
         blk("Escreva do <b>menor</b> para o <b>maior</b>.", order, cols=2)]
    return [A, B]


@passo("mais-menos-igual", "Mais, menos e igual", "Comparar quantidades e números até 10.")
def _(rng):
    items = []
    for _ in range(5):
        a, b = rng.sample(range(1, 11), 2)
        side = "esquerda" if a > b else "direita"
        items.append((f'<span class="pair">{dots(a)} {BX}</span><span class="pair">{dots(b)} {BX}</span>', f"{a} e {b}; mais: {side}"))
    A = [blk("Escreva quantas bolinhas há em cada grupo. Circule o grupo que tem <b>mais</b>.", items, cols=1)]
    big = []
    for _ in range(12):
        a, b = rng.sample(range(0, 11), 2)
        big.append((f'<span class="cmp">{a}</span><span class="cmp">{b}</span>', max(a, b)))
    small = []
    for _ in range(8):
        a, b = rng.sample(range(0, 11), 2)
        small.append((f'<span class="cmp">{a}</span><span class="cmp">{b}</span>', min(a, b)))
    B = [blk("Circule o número <b>maior</b>.", big, cols=4), blk("Circule o número <b>menor</b>.", small, cols=4)]
    return [A, B]


@passo("numeros-ordinais", "Números ordinais", "Usar números para indicar posição: 1º, 2º, 3º... até 10º.")
def _(rng):
    ords = ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º"]
    items = []
    for _ in range(6):
        row = pick(rng, ICONES, 8)
        k = rng.randint(2, 8)
        nm = NOMES[row[k - 1]][0]
        g = "".join(f'<span class="ordcell">{objs(1, ic)}</span>' for ic in row)
        items.append((f'<span class="ordlbl">Circule a figura em <b>{k}º</b> lugar.</span><span class="ordrow">← frente {g}</span>', f"a {k}ª figura ({nm})"))
    A = [blk("A fila começa pela esquerda (frente).", items, cols=1)]
    it2 = []
    for _ in range(6):
        row = pick(rng, ICONES, 8)
        k = rng.randint(1, 8)
        g = "".join(f'<span class="ordcell{" mark" if i == k - 1 else ""}">{objs(1, ic)}</span>' for i, ic in enumerate(row))
        it2.append((f'<span class="ordrow">← frente {g}</span> &nbsp; {BX}º', f"{k}º"))
    seq = [(seq_row(["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º", "10º"], [2, 5, 8]), "3º, 6º, 9º")]
    B = [blk("Em que lugar está a figura marcada?", it2, cols=1), blk("Complete.", seq, cols=1)]
    return [A, B]


# =====================================================================
unidade("Compor e decompor até 10", "EF01MA06, EF01MA07")


def gen_partes(rng, wholes):
    spl = [(w, a) for w in wholes for a in range(1, w)]
    ex = pick(rng, spl, 7)
    A1 = [(f'{dots(w, filled=a)} &nbsp; {w} = {BX} + {BX}', f"{a} + {w - a}") for w, a in ex[1:]]
    w0, a0 = ex[0]
    A = [blk("Conte as bolinhas pretas e as brancas.", A1, cols=2, example=f'{dots(w0, filled=a0)} &nbsp; {w0} = {EX(a0)} + {EX(w0 - a0)}')]
    bonds = []
    for w, a in pick(rng, [(w, a) for w in wholes for a in range(0, w + 1)], 6):
        if rng.random() < .5:
            bonds.append((bond(w, a, None), w - a))
        else:
            bonds.append((bond(w, None, w - a), a))
    A.append(blk("Complete a ligação de números.", bonds, cols=3))
    bb = []
    for w, a in pick(rng, [(w, a) for w in wholes for a in range(0, w + 1)], 8):
        bb.append((bond(w, a, None) if rng.random() < .5 else bond(w, None, a), w - a))
    eqs = []
    for w, a in pick(rng, [(w, a) for w in wholes for a in range(0, w + 1)], 12):
        eqs.append((f'{w} = {a} + {BX}', w - a))
    B = [blk("Complete a ligação de números.", bb, cols=4), blk("Complete.", eqs, cols=3)]
    return [A, B]


@passo("partes-do-5", "As partes do 5", "Decompor o 5 de todas as maneiras (ligações de números).")
def _(rng):
    return gen_partes(rng, [5])


@passo("partes-do-6-e-7", "As partes do 6 e do 7", "Decompor 6 e 7 em duas partes.")
def _(rng):
    return gen_partes(rng, [6, 7])


@passo("partes-do-8-e-9", "As partes do 8 e do 9", "Decompor 8 e 9 em duas partes.")
def _(rng):
    return gen_partes(rng, [8, 9])


@passo("amigos-do-10", "Amigos do 10", "Reconhecer os pares que formam 10.")
def _(rng):
    ns = pick(rng, range(1, 10), 9)
    A = [blk("Quantos faltam para completar 10?", [(f'{tenframe(n)} &nbsp; {n} + {BX} = 10', 10 - n) for n in ns[1:]], cols=2,
             example=f'{tenframe(ns[0])} &nbsp; {ns[0]} + {EX(10 - ns[0])} = 10')]
    bb = [(bond(10, a, None), 10 - a) for a in pick(rng, range(0, 11), 4)]
    eqs = []
    for a in pick(rng, range(0, 11), 16):
        if rng.random() < .5:
            eqs.append((f'{a} + {BX} = 10', 10 - a))
        else:
            eqs.append((f'{BX} + {a} = 10', 10 - a))
    B = [blk("Complete a ligação de números.", bb, cols=4), blk("Complete para dar 10.", eqs, cols=4)]
    return [A, B]


@passo("ligacoes-ate-10", "Ligações de números até 10", "Treinar todas as decomposições de 2 a 10.")
def _(rng):
    pool = [(w, a) for w in range(2, 11) for a in range(0, w + 1)]
    A = []
    bb = []
    for w, a in pick(rng, pool, 12):
        bb.append((bond(w, a, None) if rng.random() < .5 else bond(w, None, a), w - a))
    A.append(blk("Complete a ligação de números.", bb, cols=4))
    eqs = [(f'{w} = {a} + {BX}', w - a) for w, a in pick(rng, pool, 30)]
    B = [blk("Complete.", eqs, cols=3)]
    return [A, B]


# =====================================================================
unidade("Adição até 10", "EF01MA06, EF01MA08")


@passo("juntar-com-figuras", "Juntar com figuras", "Entender a adição como juntar duas quantidades.")
def _(rng):
    pairs = [(a, b) for a in range(1, 6) for b in range(1, 6) if a + b <= 10]
    ps = pick(rng, pairs, 7)
    ic = pick(rng, ICONES, 7)
    a0, b0 = ps[0]
    A = [blk("Junte e escreva quantos são ao todo.",
             [(f'{objs(a, ic[i])} <b>+</b> {objs(b, ic[i])}<br>{a} + {b} = {BX}', a + b) for i, (a, b) in enumerate(ps[1:], 1)], cols=2,
             example=f'{objs(a0, ic[0])} <b>+</b> {objs(b0, ic[0])}<br>{a0} + {b0} = {EX(a0 + b0)}')]
    p5 = [(a, b) for a in range(0, 6) for b in range(0, 6) if a + b <= 5]
    B = [blk("Junte as bolinhas.", [(f'{dots(a)} <b>+</b> {dots(b)} = {BX}', a + b) for a, b in pick(rng, [p for p in p5 if p[0] and p[1]], 6)], cols=2),
         blk("Calcule.", drill(rng, p5, 15), cols=3)]
    return [A, B]


def gen_somar(rng, ks):
    ex = pick(rng, [(n, k) for n in range(0, 11 - max(ks)) for k in ks], 7)
    n0, k0 = ex[0]
    A = [blk("Use a reta: pule para frente.", [(f'{numline(0, 10, n, k, width=250)}<br>{n} + {k} = {BX}', n + k) for n, k in ex[1:]], cols=2,
             example=f'{numline(0, 10, n0, k0, width=250)}<br>{n0} + {k0} = {EX(n0 + k0)}')]
    pairs = [(n, k) for n in range(0, 11 - max(ks)) for k in ks] + [(k, n) for n in range(0, 11 - max(ks)) for k in ks]
    A.append(blk("Calcule.", drill(rng, pairs, 6), cols=3))
    B = [blk("Calcule.", drill(rng, pairs, 30), cols=3)]
    return [A, B]


@passo("somar-1", "Somar 1", "Somar 1 é dizer o próximo número.")
def _(rng):
    return gen_somar(rng, [1])


@passo("somar-2", "Somar 2", "Somar 2 é pular dois números para frente.")
def _(rng):
    return gen_somar(rng, [2])


@passo("somar-0-e-3", "Somar 0 e somar 3", "Somar 0 não muda o número; somar 3 é pular três.")
def _(rng):
    return gen_somar(rng, [0, 3])


@passo("adicao-na-reta", "Adição na reta numérica", "Representar adições com pulos na reta.")
def _(rng):
    ps = pick(rng, [(a, b) for a in range(0, 9) for b in range(1, 6) if a + b <= 10], 6)
    A = [blk("Observe os pulos e escreva a conta.", [(f'{numline(0, 10, a, b, width=400)} &nbsp; {a} + {b} = {BX}', a + b) for a, b in ps], cols=1)]
    qs = pick(rng, [(a, b) for a in range(0, 9) for b in range(1, 6) if a + b <= 10], 6)
    B = [blk("Desenhe os pulos na reta e resolva.", [(f'{numline(0, 10, width=400)} &nbsp; {a} + {b} = {BX}', a + b) for a, b in qs], cols=1)]
    return [A, B]


def tempo():
    return '<div class="timer">Comecei às ______ &nbsp;&nbsp; Terminei às ______</div>'


@passo("treino-adicao-ate-10", "Treino: adição até 10", "Ganhar rapidez nos fatos de adição até 10.")
def _(rng):
    pairs = [(a, b) for a in range(0, 11) for b in range(0, 11) if a + b <= 10]
    A = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30), cols=3, note=tempo())]
    B = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30), cols=3, note=tempo())]
    return [A, B]


def prob(rng, kind, maxv=10):
    nm = rng.sample(NOMES_P, 2)
    ic = rng.choice(ICONES)
    q = quant(ic)
    if kind == "juntar":
        a, b = rng.randint(1, maxv - 1), 0
        b = rng.randint(1, maxv - a)
        t = f"{nm[0]} tem {a} {nome_obj(ic, a)}. {nm[1]} tem {b} {nome_obj(ic, b)}. {q} {NOMES[ic][1]} as duas crianças têm juntas?"
        return t, a, b, a + b, ic, "+"
    if kind == "acrescentar":
        a = rng.randint(1, maxv - 1)
        b = rng.randint(1, maxv - a)
        t = f"Havia {a} {nome_obj(ic, a)} na mesa. {nm[0]} colocou mais {b}. {q} {NOMES[ic][1]} há agora?"
        return t, a, b, a + b, ic, "+"
    if kind == "retirar":
        a = rng.randint(3, maxv)
        b = rng.randint(1, a - 1)
        t = f"{nm[0]} tinha {a} {nome_obj(ic, a)} e deu {b} para {nm[1]}. {q} {NOMES[ic][1]} sobraram?"
        return t, a, b, a - b, ic, "−"
    if kind == "separar":
        a = rng.randint(3, maxv)
        b = rng.randint(1, a - 1)
        s, p, g = NOMES[ic]
        f_ = g == "f"
        t = f"Há {a} {p} numa caixa. {b} são grandes e {'as outras' if f_ else 'os outros'} são pequen{'as' if f_ else 'os'}. {q} são pequen{'as' if f_ else 'os'}?"
        return t, a, b, a - b, ic, "−"
    if kind == "comparar":
        a = rng.randint(3, maxv)
        b = rng.randint(1, a - 1)
        t = f"{nm[0]} tem {a} {nome_obj(ic, a)}. {nm[1]} tem {b}. {q} {NOMES[ic][1]} {nm[0]} tem a mais que {nm[1]}?"
        return t, a, b, a - b, ic, "−", nm
    raise ValueError(kind)


def prob_item(rng, kind, maxv, visual):
    r = prob(rng, kind, maxv)
    t, a, b, res, ic, op = r[:6]
    if visual == "fig":
        if op == "+":
            fig = f'{objs(a, ic, s=20)} <b>+</b> {objs(b, ic, s=20)}'
        else:
            fig = objs(a, ic, s=20, crossed=b) if kind in ("retirar",) else objs(a, ic, s=20)
    else:
        if kind == "comparar":
            nm = r[6]
            fig = bar_compare(a, b, nm[0], nm[1], width=330)
        elif op == "+":
            fig = bar_model([(a, str(a)), (b, str(b))], "?", width=330)
        else:
            fig = bar_model([(b, str(b)), (a - b, "?")], str(a), width=330)
    html = (f'<p class="pt">{t}</p><div class="pf">{fig}</div>'
            f'<div class="pa">Conta: {BXW} {BX} {BXW} = {BX} &nbsp;&nbsp; Resposta: {BX} {NOMES[ic][1]}</div>')
    return html, f"{a} {op} {b} = {res}; {res} {nome_obj(ic, res)}"


@passo("problemas-de-adicao", "Problemas de juntar e acrescentar", "Resolver problemas de adição com figuras e com o modelo de barras.")
def _(rng):
    A = [blk("Leia (ou escute) o problema, observe o desenho e resolva.", [prob_item(rng, k, 10, "fig") for k in ["juntar", "acrescentar", "juntar"]], cols=1)]
    B = [blk("Use o modelo de barras para resolver.", [prob_item(rng, k, 10, "bar") for k in ["acrescentar", "juntar", "acrescentar"]], cols=1)]
    return [A, B]


# =====================================================================
unidade("Subtração até 10", "EF01MA06, EF01MA08")


@passo("tirar-com-figuras", "Tirar com figuras", "Entender a subtração como tirar.")
def _(rng):
    ps = pick(rng, [(a, b) for a in range(2, 11) for b in range(1, a)], 9)
    ic = pick(rng, ICONES, 9)
    a0, b0 = ps[0]
    A = [blk("Algumas figuras foram riscadas. Quantas sobraram?",
             [(f'{objs(a, ic[i], crossed=b)}<br>{a} − {b} = {BX}', a - b) for i, (a, b) in enumerate(ps[1:], 1)], cols=2,
             example=f'{objs(a0, ic[0], crossed=b0)}<br>{a0} − {b0} = {EX(a0 - b0)}')]
    B = [blk("Desenhe as bolinhas, risque e resolva.", [(f'<span class="draw wide"></span>{a} − {b} = {BX}', a - b) for a, b in pick(rng, [(a, b) for a in range(3, 8) for b in range(1, a)], 4)], cols=2),
         blk("Calcule.", drill(rng, [(a, b) for a in range(1, 6) for b in range(0, a + 1)], 15, "-"), cols=3)]
    return [A, B]


def gen_tirar(rng, ks):
    ex = pick(rng, [(n, k) for n in range(max(ks), 11) for k in ks], 7)
    n0, k0 = ex[0]
    A = [blk("Use a reta: pule para trás.", [(f'{numline(0, 10, n, -k, width=250)}<br>{n} − {k} = {BX}', n - k) for n, k in ex[1:]], cols=2,
             example=f'{numline(0, 10, n0, -k0, width=250)}<br>{n0} − {k0} = {EX(n0 - k0)}')]
    pairs = [(n, k) for n in range(max(ks), 11) for k in ks]
    A.append(blk("Calcule.", drill(rng, pairs, 6, "-"), cols=3))
    B = [blk("Calcule.", drill(rng, pairs, 30, "-"), cols=3)]
    return [A, B]


@passo("tirar-1", "Tirar 1", "Tirar 1 é dizer o número anterior.")
def _(rng):
    return gen_tirar(rng, [1])


@passo("tirar-2", "Tirar 2", "Tirar 2 é pular dois números para trás.")
def _(rng):
    return gen_tirar(rng, [2])


@passo("subtracao-na-reta", "Subtração na reta numérica", "Representar subtrações com pulos para trás.")
def _(rng):
    ps = pick(rng, [(a, b) for a in range(2, 11) for b in range(1, 6) if b < a], 6)
    A = [blk("Observe os pulos e escreva a conta.", [(f'{numline(0, 10, a, -b, width=400)} &nbsp; {a} − {b} = {BX}', a - b) for a, b in ps], cols=1)]
    qs = pick(rng, [(a, b) for a in range(2, 11) for b in range(1, 6) if b < a], 6)
    B = [blk("Desenhe os pulos para trás e resolva.", [(f'{numline(0, 10, width=400)} &nbsp; {a} − {b} = {BX}', a - b) for a, b in qs], cols=1)]
    return [A, B]


@passo("quanto-falta", "Quanto falta?", "Achar a parte que falta (ligação entre adição e subtração).")
def _(rng):
    ps = pick(rng, [(a, b) for b in range(3, 11) for a in range(1, b)], 9)
    a0, b0 = ps[0]
    A = [blk("As bolinhas pretas são as que já tenho. Quantas faltam?",
             [(f'{dots(a, empty_after=b - a)}<br>{a} + {BX} = {b}', b - a) for a, b in ps[1:]], cols=2,
             example=f'{dots(a0, empty_after=b0 - a0)}<br>{a0} + {EX(b0 - a0)} = {b0}')]
    pool = [(a, b) for b in range(2, 11) for a in range(0, b + 1)]
    eqs = []
    for a, b in pick(rng, pool, 24):
        eqs.append((f'{a} + {BX} = {b}', b - a) if rng.random() < .6 else (f'{BX} + {a} = {b}', b - a))
    B = [blk("Complete.", eqs, cols=3)]
    return [A, B]


@passo("treino-subtracao-ate-10", "Treino: subtração até 10", "Ganhar rapidez nos fatos de subtração até 10.")
def _(rng):
    pairs = [(a, b) for a in range(0, 11) for b in range(0, a + 1)]
    A = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30, "-"), cols=3, note=tempo())]
    B = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30, "-"), cols=3, note=tempo())]
    return [A, B]


def familia(w, a):
    b = w - a
    html = (f'{bond(w, a, b)}<div class="fam">{BX} + {BX} = {BX}<br>{BX} + {BX} = {BX}<br>'
            f'{BX} − {BX} = {BX}<br>{BX} − {BX} = {BX}</div>')
    ans = f"{a}+{b}={w}; {b}+{a}={w}; {w}−{a}={b}; {w}−{b}={a}"
    return html, ans


@passo("familias-de-fatos", "Famílias de fatos", "Com três números, escrever duas adições e duas subtrações.")
def _(rng):
    pool = [(w, a) for w in range(4, 11) for a in range(1, w) if a != w - a]
    ps = pick(rng, pool, 10)
    A = [blk("Escreva as quatro contas de cada família.", [familia(w, a) for w, a in ps[:4]], cols=2)]
    B = [blk("Escreva as quatro contas de cada família.", [familia(w, a) for w, a in ps[4:10]], cols=3)]
    return [A, B]


@passo("problemas-de-subtracao", "Problemas de tirar, separar e comparar", "Resolver problemas de subtração com figuras e com o modelo de barras.")
def _(rng):
    A = [blk("Leia (ou escute) o problema, observe o desenho e resolva.", [prob_item(rng, k, 10, "fig") for k in ["retirar", "separar", "retirar"]], cols=1)]
    B = [blk("Use o modelo de barras para resolver.", [prob_item(rng, k, 10, "bar") for k in ["comparar", "retirar", "comparar"]], cols=1)]
    return [A, B]


# =====================================================================
unidade("Números até 20", "EF01MA04, EF01MA05, EF01MA06, EF01MA07")


@passo("contar-ate-20", "Contar até 20", "Contar até 20 usando um quadro cheio (10) e mais.")
def _(rng):
    ns = pick(rng, range(11, 21), 9)
    A = [blk("Quantas bolinhas há nos dois quadros?", [(f'{tenframe(n, cell=18, frames=2)} {BX}', n) for n in ns[1:]], cols=2,
             example=f'{tenframe(ns[0], cell=18, frames=2)} {EX(ns[0])}')]
    rows = []
    for _ in range(4):
        bl = sorted(rng.sample(range(1, 11), 4))
        nums = list(range(10, 21))
        rows.append((seq_row(nums, bl), ", ".join(str(nums[i]) for i in bl)))
    B = [blk("Conte e escreva.", [(f'{objs(n, ic, per_row=10, s=18, gap=3)} {BX}', n) for n, ic in zip(pick(rng, range(11, 21), 4), pick(rng, ICONES, 4))], cols=1),
         blk("Complete a sequência.", rows, cols=1)]
    return [A, B]


@passo("dez-e-mais", "Dez e mais", "Entender 11 a 19 como 10 e mais algumas unidades.")
def _(rng):
    ns = pick(rng, range(1, 10), 9)
    A = [blk("Uma barra vale 10. Escreva a conta e o número.", [(f'{rods(1, n)} &nbsp; 10 + {n} = {BX}', 10 + n) for n in ns[1:]], cols=2,
             example=f'{rods(1, ns[0])} &nbsp; 10 + {ns[0]} = {EX(10 + ns[0])}')]
    B = [blk("Complete.", [(f'10 + {n} = {BX}', 10 + n) for n in pick(rng, range(0, 11), 12)], cols=3),
         blk("Separe em 10 e mais.", [(f'{10 + n} = 10 + {BX}', n) for n in pick(rng, range(0, 11), 12)], cols=3)]
    return [A, B]


@passo("comparar-ate-20", "Ordem e comparação até 20", "Antes, depois, entre e comparar números até 20.")
def _(rng):
    items = []
    for n in pick(rng, range(1, 20), 12):
        k = rng.choice([0, 1, 2])
        nums = [n - 1, n, n + 1]
        items.append((seq_row(nums, [k]), nums[k]))
    A = [free("Use a reta para ajudar.", numline(0, 20, width=560)), blk("Complete com o número que falta.", items, cols=4)]
    big = []
    for _ in range(8):
        a, b = rng.sample(range(0, 21), 2)
        big.append((f'<span class="cmp">{a}</span><span class="cmp">{b}</span>', max(a, b)))
    order = []
    for _ in range(4):
        t = sorted(rng.sample(range(0, 21), 3))
        s = shuffled(rng, t)
        order.append((f'{", ".join(map(str, s))} &nbsp;→&nbsp; {BX} {BX} {BX}', ", ".join(map(str, t))))
    B = [blk("Circule o número <b>maior</b>.", big, cols=4), blk("Escreva do <b>menor</b> para o <b>maior</b>.", order, cols=2)]
    return [A, B]


@passo("dobros", "Dobros", "Memorizar os dobros de 1 a 10.")
def _(rng):
    ns = pick(rng, range(1, 11), 7)
    A = [blk("Os dois lados são iguais. Quanto dá ao todo?", [(f'{dots(n)} <span class="mirror">|</span> {dots(n)}<br>{n} + {n} = {BX}', 2 * n) for n in ns[1:]], cols=2,
             example=f'{dots(ns[0])} <span class="mirror">|</span> {dots(ns[0])}<br>{ns[0]} + {ns[0]} = {EX(2 * ns[0])}')]
    pairs = [(n, n) for n in range(1, 11)]
    B = [blk("Calcule.", drill(rng, pairs, 20), cols=4),
         blk("Qual é o dobro?", [(f'dobro de {n} = {BX}', 2 * n) for n in pick(rng, range(1, 11), 8)], cols=4)]
    return [A, B]


@passo("fazer-10-para-somar", "Fazer 10 para somar", "Somar passando de 10: completar a dezena primeiro (método de Singapura).")
def _(rng):
    pool = [(a, b) for a in range(6, 10) for b in range(2, 10) if a + b > 10 and a + b <= 18]
    ps = pick(rng, pool, 13)
    a0, b0 = ps[0]
    def it(a, b, ex=False):
        f = (lambda v: EX(v)) if ex else (lambda v: BX)
        return (f'{tenframe(a, cell=16)}&nbsp;{dots(b, r=6, gap=3)}<br>{a} + {b}<br>{bond(b, 10 - a, None if not ex else b - 10 + a)}'
                f'<br>{a} + {f(10 - a)} = 10 &nbsp; 10 + {f(b - 10 + a)} = {f(a + b)}')
    A = [blk("Separe o segundo número para completar 10.", [(it(a, b), f"{10 - a} e {b - 10 + a}; {a + b}") for a, b in ps[1:5]], cols=2,
             example=it(a0, b0, True))]
    B = [blk("Complete 10 primeiro e depois some o resto.", [(f'{a} + {b} = {BX}<br>{bond(b, None, None)}', f"{b} = {10 - a} + {b - 10 + a}; {a + b}") for a, b in ps[5:13]], cols=4)]
    return [A, B]


@passo("treino-adicao-ate-20", "Treino: adição até 20", "Ganhar rapidez em adições com resultado até 20.")
def _(rng):
    pairs = [(a, b) for a in range(1, 11) for b in range(1, 11) if a + b <= 20] + [(10 + a, b) for a in range(0, 10) for b in range(0, 10) if a + b <= 9]
    A = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30), cols=3, note=tempo())]
    B = [blk("Calcule o mais rápido que conseguir, sem errar.", drill(rng, pairs, 30), cols=3, note=tempo())]
    return [A, B]


@passo("subtracao-ate-20", "Subtração até 20", "Subtrair até 20, tirando primeiro até chegar a 10.")
def _(rng):
    nc = pick(rng, [(10 + u, b) for u in range(1, 10) for b in range(1, u + 1)], 6)
    A = [blk("Risque os cubinhos e resolva.", [(f'{rods(1, a - 10)} &nbsp; {a} − {b} = {BX}', a - b) for a, b in nc], cols=2)]
    cr = pick(rng, [(a, b) for a in range(11, 19) for b in range(2, 10) if a - b < 10 and a - b >= 1], 8)
    A.append(blk("Passando pelo 10: tire primeiro as unidades, depois o resto.",
                 [(f'{a} − {b} = {BX} &nbsp; <small>({a} − {a - 10} = 10; 10 − {b - (a - 10)} = ?)</small>', a - b) for a, b in cr[:4]], cols=2))
    pairs = [(a, b) for a in range(10, 21) for b in range(0, 11) if 0 <= a - b <= 10]
    B = [blk("Calcule.", drill(rng, pairs, 30, "-"), cols=3, note=tempo())]
    return [A, B]


@passo("problemas-ate-20", "Problemas até 20", "Resolver problemas variados com números até 20.")
def _(rng):
    A = [blk("Leia (ou escute) o problema, observe o desenho e resolva.", [prob_item(rng, k, 20, "bar") for k in ["juntar", "retirar", "comparar"]], cols=1)]
    B = [blk("Desenhe o modelo de barras e resolva.", [prob_item(rng, k, 20, "bar") for k in ["acrescentar", "separar", "comparar"]], cols=1)]
    return [A, B]


# =====================================================================
unidade("Números até 100", "EF01MA04, EF01MA05, EF01MA07, EF01MA08, EF01MA10")


@passo("contar-de-10-em-10", "Contar de 10 em 10", "Contar dezenas inteiras até 100.")
def _(rng):
    ts = pick(rng, range(1, 10), 7)
    A = [blk("Cada barra vale 10. Quantos há?", [(f'{rods(t, 0)} &nbsp; {BX} dezenas = {BXW}', f"{t} dezenas = {10 * t}") for t in ts[1:]], cols=3,
             example=f'{rods(ts[0], 0)} &nbsp; {EX(ts[0])} dezenas = {EX(10 * ts[0])}')]
    rows = []
    for _ in range(3):
        bl = sorted(rng.sample(range(1, 10), 4))
        nums = list(range(10, 101, 10))
        rows.append((seq_row(nums, bl), ", ".join(str(nums[i]) for i in bl)))
    B = [blk("Complete contando de 10 em 10.", rows, cols=1),
         blk("Complete.", [(f'{10 * t} = {BX} dezenas', t) for t in pick(rng, range(1, 11), 8)] + [(f'{t} dezenas = {BXW}', 10 * t) for t in pick(rng, range(1, 11), 8)], cols=4)]
    return [A, B]


@passo("dezenas-e-unidades", "Dezenas e unidades", "Compor e decompor números de dois algarismos.")
def _(rng):
    ps = pick(rng, [(t, u) for t in range(1, 10) for u in range(1, 10)], 7)
    t0, u0 = ps[0]
    A = [blk("Quantas dezenas e unidades? Que número é?", [(f'{rods(t, u, u=7)}<br>{BX} dez. {BX} un. = {BXW}', f"{t} dez. {u} un. = {10 * t + u}") for t, u in ps[1:]], cols=3,
             example=f'{rods(t0, u0, u=7)}<br>{EX(t0)} dez. {EX(u0)} un. = {EX(10 * t0 + u0)}')]
    B = [blk("Separe em dezenas e unidades.", [(f'{n} = {BXW} + {BX}', f"{n // 10 * 10} + {n % 10}") for n in pick(rng, [n for n in range(21, 100) if n % 10], 12)], cols=2),
         blk("Escreva o número.", [(f'{t} dezena{"s" if t > 1 else ""} e {u} unidade{"s" if u != 1 else ""} = {BXW}', 10 * t + u) for t, u in pick(rng, [(t, u) for t in range(1, 10) for u in range(0, 10)], 8)], cols=2)]
    return [A, B]


def hundred(blanks):
    rows = []
    for r in range(10):
        cells = []
        for c in range(10):
            n = r * 10 + c + 1
            cells.append(f'<td class="{"hb" if n in blanks else ""}">{"" if n in blanks else n}</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return f'<table class="h100">{"".join(rows)}</table>'


def cross(n, show):
    """Pedaço do quadro de 100: n no centro, vizinhos acima/abaixo/esquerda/direita."""
    pos = {"c": n, "u": n - 10, "d": n + 10, "l": n - 1, "r": n + 1}
    def cell(k):
        return f'<td class="{"" if k in show else "hb"}">{pos[k] if k in show else ""}</td>'
    return (f'<table class="h100 x"><tr><td class="e"></td>{cell("u")}<td class="e"></td></tr>'
            f'<tr>{cell("l")}{cell("c")}{cell("r")}</tr><tr><td class="e"></td>{cell("d")}<td class="e"></td></tr></table>')


@passo("quadro-de-100", "Quadro de 100", "Perceber os padrões do quadro de 100 (mais 1, mais 10).")
def _(rng):
    bl = sorted(rng.sample(range(2, 101), 28))
    A = [blk("Complete o quadro de 100.", [(hundred(set(bl)), ", ".join(map(str, bl)))], cols=1)]
    items = []
    for n in pick(rng, [r * 10 + c for r in range(1, 9) for c in range(2, 10)], 8):
        items.append((cross(n, {"c"}), f"acima {n - 10}, abaixo {n + 10}, esquerda {n - 1}, direita {n + 1}"))
    B = [blk("Complete os pedaços do quadro de 100.", items, cols=4)]
    return [A, B]


@passo("contar-de-2-5-e-comparar", "Contar de 2 em 2, de 5 em 5 e comparar", "Contagens com saltos e comparação até 100.")
def _(rng):
    A = [blk("Conte de 2 em 2.", seq_items(rng, 0, 40, 2, 10, 3, 3), cols=1),
         blk("Conte de 5 em 5.", seq_items(rng, 0, 100, 5, 10, 3, 3), cols=1),
         blk("Conte de 10 em 10.", seq_items(rng, 1, 99, 10, 9, 3, 2), cols=1)]
    big = []
    for _ in range(12):
        a, b = rng.sample(range(10, 100), 2)
        big.append((f'<span class="cmp">{a}</span><span class="cmp">{b}</span>', max(a, b)))
    order = []
    for _ in range(4):
        t = sorted(rng.sample(range(10, 100), 3))
        order.append((f'{", ".join(map(str, shuffled(rng, t)))} &nbsp;→&nbsp; {BXW} {BXW} {BXW}', ", ".join(map(str, t))))
    B = [blk("Circule o número <b>maior</b>.", big, cols=4), blk("Escreva do <b>menor</b> para o <b>maior</b>.", order, cols=2)]
    return [A, B]


@passo("somar-e-tirar-dezenas", "Somar e tirar com dezenas", "Adições e subtrações com dois algarismos, sem reagrupar.")
def _(rng):
    ps = pick(rng, [(a, b) for a in range(1, 9) for b in range(1, 9) if a + b <= 9], 6)
    A = [blk("Junte as barras e escreva.", [(f'{rods(a, 0, u=7)} <b>+</b> {rods(b, 0, u=7)}<br>{10 * a} + {10 * b} = {BXW}', 10 * (a + b)) for a, b in ps], cols=3)]
    it = []
    for _ in range(8):
        t, u = rng.randint(1, 8), rng.randint(0, 7)
        b = rng.randint(1, 9 - u)
        it.append((f'{10 * t + u} + {b} = {BXW}', 10 * t + u + b))
    for _ in range(8):
        t, u = rng.randint(2, 9), rng.randint(2, 9)
        b = rng.randint(1, u)
        it.append((f'{10 * t + u} − {b} = {BXW}', 10 * t + u - b))
    for _ in range(8):
        a, b = rng.sample(range(1, 10), 2)
        a, b = max(a, b), min(a, b)
        it.append((f'{10 * a} − {10 * b} = {BXW}', 10 * (a - b)))
    rng.shuffle(it)
    B = [blk("Calcule.", it, cols=3)]
    return [A, B]


# =====================================================================
unidade("Geometria e localização", "EF01MA09, EF01MA10, EF01MA11, EF01MA12, EF01MA13, EF01MA14")


@passo("figuras-planas", "Figuras planas", "Reconhecer círculo, quadrado, triângulo e retângulo.")
def _(rng):
    kinds = ["circulo", "quadrado", "triangulo", "retangulo"]
    seq = pick(rng, kinds, 16)
    b = []
    for i, k in enumerate(seq):
        x = (i % 6) * 72 + rng.randint(0, 12)
        y = (i // 6) * 58 + rng.randint(0, 10)
        b.append(shape(k, x, y, 40, "#fff"))
    pic = svg(470, 180, "".join(b), label="figuras misturadas")
    cnt = {k: seq.count(k) for k in kinds}
    tab = "".join(f'<div class="cnt">{svg(64, 34, shape(k, 2, 1, 32))} {SHAPE_NOME[k]}s: {BX}</div>' for k in kinds)
    A = [blk("Conte cada tipo de figura.", [(f'{pic}<div class="cnts">{tab}</div>', ", ".join(f"{SHAPE_NOME[k]}s {cnt[k]}" for k in kinds))], cols=1)]
    rows = []
    for alvo in ["triangulo", "quadrado", "circulo", "retangulo"]:
        r = pick(rng, kinds, 8)
        rows.append((f'Circule os <b>{SHAPE_NOME[alvo]}s</b>: {shape_row(r, s=28)}', f"{r.count(alvo)} {SHAPE_NOME[alvo]}(s)"))
    A.append(blk("", rows, cols=1))
    lados = [(f'{svg(64, 40, shape(k, 2, 2, 36))} Quantos lados? {BX}', {"triangulo": 3, "quadrado": 4, "retangulo": 4}[k]) for k in ["triangulo", "quadrado", "retangulo"]]
    dot = "".join(f'<circle cx="{10 + c * 22}" cy="{10 + r * 22}" r="1.8" fill="{INK}"/>' for r in range(7) for c in range(22))
    B = [blk("Responda.", lados, cols=3),
         free("Ligue os pontos para desenhar um quadrado, um triângulo e um retângulo.", svg(480, 150, dot))]
    return [A, B]


@passo("solidos-geometricos", "Sólidos geométricos", "Relacionar objetos do dia a dia a cubo, esfera, cilindro, cone e bloco.")
def _(rng):
    sol = [("A", "cubo"), ("B", "esfera"), ("C", "cilindro"), ("D", "cone"), ("E", "bloco")]
    nomes = {"cubo": "cubo", "esfera": "esfera", "cilindro": "cilindro", "cone": "cone", "bloco": "bloco retangular"}
    ref = "".join(f'<div class="sol">{svg(64, 60, solid(k, 2, 0))}<b>{L}</b> {nomes[k]}</div>' for L, k in sol)
    objetos = [("um dado", "A"), ("uma bola de futebol", "B"), ("uma lata de milho", "C"), ("um chapéu de aniversário", "D"),
               ("uma caixa de sapato", "E"), ("uma laranja", "B"), ("um rolo de papel", "C"), ("uma casquinha de sorvete", "D"),
               ("um tijolo", "E"), ("um cubo mágico", "A")]
    objetos = shuffled(rng, objetos)
    A = [free("Observe os sólidos.", f'<div class="sols">{ref}</div>'),
         blk("Escreva a letra do sólido que cada objeto lembra.", [(f'{o} {BX}', L) for o, L in objetos], cols=2)]
    rola = [("cubo", "não"), ("esfera", "sim"), ("cilindro", "sim"), ("cone", "sim"), ("bloco", "não")]
    B = [blk("Esse sólido rola? Escreva S (sim) ou N (não).", [(f'{svg(64, 60, solid(k, 2, 0))} {BX}', "S" if r == "sim" else "N") for k, r in rola], cols=5),
         blk("Responda.", [(f'Quantas faces tem o cubo? {BX}', 6), (f'Quantas faces tem o bloco retangular? {BX}', 6),
                           (f'Qual sólido não tem nenhuma parte reta? {BXW}', "esfera")], cols=1)]
    return [A, B]


@passo("padroes-e-sequencias", "Padrões e sequências", "Descobrir a regra de uma sequência e continuar.")
def _(rng):
    kinds = ["circulo", "quadrado", "triangulo"]
    pats = [["circulo", "quadrado"], ["triangulo", "triangulo", "circulo"], ["quadrado", "circulo", "triangulo"],
            ["circulo", "circulo", "quadrado", "quadrado"], ["triangulo", "quadrado"], ["quadrado", "triangulo", "triangulo"]]
    items = []
    for p in pats:
        full = (p * 6)[:9]
        bl = [7, 8]
        items.append((shape_row(full, s=28, blanks=bl), ", ".join(SHAPE_NOME[full[i]] for i in bl)))
    A = [blk("Descubra o padrão e desenhe as figuras que faltam.", items, cols=1)]
    num = [([2, 4, 6, 8, 10, 12], 2), ([5, 10, 15, 20, 25, 30], 5), ([1, 3, 5, 7, 9, 11], 2), ([20, 18, 16, 14, 12, 10], -2),
           ([10, 20, 30, 40, 50, 60], 10), ([3, 6, 9, 12, 15, 18], 3), ([15, 14, 13, 12, 11, 10], -1), ([0, 4, 8, 12, 16, 20], 4)]
    it = []
    for seq, step in num:
        it.append((seq_row(seq + [seq[-1] + step, seq[-1] + 2 * step], [6, 7]) + f' &nbsp; regra: {BXW}',
                   f"{seq[-1] + step}, {seq[-1] + 2 * step}; regra {'+' if step > 0 else '−'}{abs(step)}"))
    B = [blk("Continue a sequência e escreva a regra (ex.: +2).", it, cols=1)]
    return [A, B]


def grid_pic(cells, n=4, s=46):
    b = []
    for r in range(n + 1):
        b.append(f'<line x1="1" y1="{1 + r * s}" x2="{1 + n * s}" y2="{1 + r * s}" stroke="{INK}" stroke-width="1.4"/>')
        b.append(f'<line x1="{1 + r * s}" y1="1" x2="{1 + r * s}" y2="{1 + n * s}" stroke="{INK}" stroke-width="1.4"/>')
    from figuras import _icon
    for (r, c), ic in cells.items():
        b.append(_icon(ic, 1 + c * s + 7, 1 + r * s + 7, 32))
    return svg(n * s + 2, n * s + 2, "".join(b), label="quadriculado")


@passo("posicao-e-localizacao", "Posição e localização", "Usar direita, esquerda, acima e abaixo.")
def _(rng):
    def make():
        pos = rng.sample([(r, c) for r in range(4) for c in range(4)], 6)
        ics = rng.sample(ICONES, 6)
        return dict(zip(pos, ics))
    def questions(cells, k):
        inv = {v: p for p, v in cells.items()}
        qs = []
        dirs = [("à direita", (0, 1)), ("à esquerda", (0, -1)), ("acima", (-1, 0)), ("abaixo", (1, 0))]
        for ic, (r, c) in inv.items():
            for nm, (dr, dc) in dirs:
                t = (r + dr, c + dc)
                if t in cells:
                    qs.append((f'O que está {nm} {"da" if NOMES[ic][2] == "f" else "do"} {NOMES[ic][0]}? {BXW}', NOMES[cells[t]][0]))
        return pick(rng, qs, k) if qs else []
    for _ in range(50):
        c1 = make()
        q1 = questions(c1, 6)
        if len(set(h for h, _ in q1)) >= 5:
            break
    A = [blk("Observe o quadriculado.", [(grid_pic(c1), None)], cols=1), blk("Responda (escreva ou desenhe).", q1, cols=1)]
    B = [free("Desenhe no quadriculado: uma <b>bola</b> no canto de cima à esquerda; uma <b>estrela</b> à direita da bola; "
              "uma <b>flor</b> abaixo da estrela; um <b>coração</b> no canto de baixo à direita.", grid_pic({}, s=58)),
         blk("Responda olhando para a sala de aula.", [(f'O que está à sua direita? {BXW}', None), (f'O que está acima do quadro? {BXW}', None)], cols=1)]
    return [A, B]


# =====================================================================
unidade("Medidas, tempo, dinheiro e dados", "EF01MA15, EF01MA16, EF01MA17, EF01MA18, EF01MA19, EF01MA20, EF01MA21")


def ruler_bar(n, label, unit=24):
    b = [f'<text x="0" y="19" font-size="15" font-weight="600">{label}</text>']
    for i in range(12):
        b.append(f'<rect x="{30 + i * unit}" y="2" width="{unit}" height="24" fill="none" stroke="#bbb" stroke-width="1"/>')
    b.append(f'<rect x="30" y="6" width="{n * unit}" height="16" fill="{FILL}" stroke="{INK}" stroke-width="1.8"/>')
    return svg(30 + 12 * unit + 2, 28, "".join(b), label=f"fita de {n}")


@passo("comparar-comprimentos", "Comparar comprimentos", "Medir com quadradinhos e comparar maior e menor.")
def _(rng):
    ns = rng.sample(range(2, 12), 5)
    labs = "ABCDE"
    it = [(f'{ruler_bar(n, L)} {BX}', n) for n, L in zip(ns, labs)]
    mx = labs[ns.index(max(ns))]
    mn = labs[ns.index(min(ns))]
    A = [blk("Quantos quadradinhos mede cada fita?", it, cols=1),
         blk("Responda.", [(f'Qual é a fita mais comprida? {BX}', mx), (f'Qual é a fita mais curta? {BX}', mn)], cols=2)]
    hs = rng.sample(range(2, 10), 4)
    names = rng.sample(NOMES_P, 4)
    b = []
    for i, (h, nm) in enumerate(zip(hs, names)):
        x = 20 + i * 90
        for k in range(h):
            b.append(f'<rect x="{x}" y="{200 - (k + 1) * 20}" width="40" height="20" fill="#fff" stroke="{INK}" stroke-width="1.5"/>')
        b.append(f'<text x="{x + 20}" y="218" text-anchor="middle" font-size="14">{nm}</text>')
    torres = svg(380, 224, "".join(b), label="torres de blocos")
    ordem = [n for _, n in sorted(zip(hs, names))]
    B = [free("Cada criança montou uma torre de blocos.", torres),
         blk("Responda.", [(f'Quantos blocos tem a torre de {names[0]}? {BX}', hs[0]),
                           (f'Quem fez a torre mais alta? {BXW}', names[hs.index(max(hs))]),
                           (f'Quantos blocos a mais tem a torre de {names[hs.index(max(hs))]} do que a de {names[hs.index(min(hs))]}? {BX}', max(hs) - min(hs)),
                           (f'Escreva os nomes da torre mais baixa para a mais alta: {BXW} {BXW} {BXW} {BXW}', ", ".join(ordem))], cols=1)]
    return [A, B]


DIAS = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def calendario(start, ndays, mes):
    head = "".join(f"<th>{d[:3]}</th>" for d in DIAS)
    cells = [""] * start + [str(d) for d in range(1, ndays + 1)]
    while len(cells) % 7:
        cells.append("")
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in cells[i:i + 7]) + "</tr>" for i in range(0, len(cells), 7))
    return f'<table class="cal"><caption>{mes.capitalize()}</caption><tr>{head}</tr>{rows}</table>'


@passo("calendario", "Calendário", "Dias da semana, meses e leitura de um calendário.")
def _(rng):
    start, nd, mes = 3, 31, "março"  # mês fictício: começa numa quarta-feira
    def dow(d):
        return DIAS[(start + d - 1) % 7]
    seg = sum(1 for d in range(1, nd + 1) if dow(d) == "segunda-feira")
    A = [free("Observe o calendário.", calendario(start, nd, mes)),
         blk("Responda.", [(f'Quantos dias tem este mês? {BX}', nd), (f'Em que dia da semana é o dia 1º? {BXW}', dow(1)),
                           (f'Em que dia da semana é o dia 15? {BXW}', dow(15)), (f'Quantas segundas-feiras há neste mês? {BX}', seg),
                           (f'Que dia vem logo depois do dia 19? {BX}', 20), (f'Se hoje é dia 10, que dia será daqui a uma semana? {BX}', 17)], cols=1)]
    d7 = [(seq_row(DIAS, bl), ", ".join(DIAS[i] for i in bl)) for bl in [[2, 5]]]
    m12 = [(seq_row(MESES[:6], [1, 4]), "fevereiro, maio"), (seq_row(MESES[6:], [2, 4]), "setembro, novembro")]
    B = [blk("Complete os dias da semana.", d7, cols=1, size="sm"), blk("Complete os meses do ano.", m12, cols=1, size="sm"),
         blk("Responda.", [(f'Hoje é terça-feira. Amanhã será {BXW}', "quarta-feira"), (f'Ontem foi sexta-feira. Hoje é {BXW}', "sábado"),
                           (f'Quantos dias tem uma semana? {BX}', 7), (f'Quantos meses tem um ano? {BX}', 12),
                           (f'Em que mês é o seu aniversário? {BXW}', None)], cols=1)]
    return [A, B]


@passo("dinheiro", "Dinheiro: cédulas e moedas", "Reconhecer cédulas e moedas e contar quantias até R$ 20.")
def _(rng):
    combos = []
    for _ in range(40):
        k = rng.randint(2, 4)
        it = sorted([rng.choice([1, 1, 2, 2, 5, 10]) for _ in range(k)], reverse=True)
        if sum(it) <= 20:
            combos.append(tuple(it))
    combos = list(dict.fromkeys(combos))[:7]
    c0 = combos[0]
    A = [blk("Quanto dinheiro há?", [(f'{money(c)} &nbsp; R$ {BXW}', sum(c)) for c in combos[1:7]], cols=2,
             example=f'{money(c0)} &nbsp; R$ {EX(sum(c0))}')]
    precos = [("um caderno", 8), ("uma bola", 10), ("um suco", 3), ("um pão", 1), ("um lápis", 2), ("uma borracha", 2)]
    it = []
    for _ in range(4):
        (a, pa), (b, pb) = rng.sample(precos, 2)
        it.append((f'{a.capitalize()} custa R$ {pa} e {b} custa R$ {pb}. Quanto custam juntos? R$ {BXW}', pa + pb))
    pairs = []
    for _ in range(3):
        x = sorted([rng.choice([1, 2, 5, 10]) for _ in range(3)], reverse=True)
        y = sorted([rng.choice([1, 2, 5, 10]) for _ in range(3)], reverse=True)
        if sum(x) == sum(y):
            y = y[:-1] + [y[-1] + 1] if y[-1] != 1 else y[:-1] + [2]
        n1, n2 = rng.sample(NOMES_P, 2)
        pairs.append((f'{n1}: {money(x)}<br>{n2}: {money(y)}<br>Quem tem mais dinheiro? {BXW}', n1 if sum(x) > sum(y) else n2))
    B = [blk("Resolva.", it, cols=1), blk("Compare.", pairs, cols=3)]
    return [A, B]


@passo("certo-talvez-impossivel", "Certo, talvez ou impossível", "Classificar acontecimentos do dia a dia.")
def _(rng):
    fr = [("Amanhã o sol vai nascer.", "C"), ("Vai chover amanhã.", "T"), ("Um gato vai falar com você.", "I"),
          ("Depois de segunda-feira vem terça-feira.", "C"), ("Você vai ganhar um presente hoje.", "T"),
          ("Um elefante vai caber na sua mochila.", "I"), ("Ao jogar um dado, vai sair o número 6.", "T"),
          ("Ao jogar um dado, vai sair o número 9.", "I"), ("O ano tem 12 meses.", "C"), ("Vai ter macarrão no almoço.", "T")]
    fr = shuffled(rng, fr)
    A = [blk("Escreva <b>C</b> (com certeza vai acontecer), <b>T</b> (talvez aconteça) ou <b>I</b> (impossível).",
             [(f'{t} {BX}', a) for t, a in fr], cols=1)]
    b = []
    for i in range(6):
        b.append(f'<circle cx="{40 + (i % 3) * 36}" cy="{40 + (i // 3) * 36}" r="15" fill="{INK if i < 4 else "#fff"}" stroke="{INK}" stroke-width="2"/>')
    saco = svg(150, 100, f'<path d="M10 10 Q0 95 75 95 Q150 95 140 10" fill="none" stroke="{INK}" stroke-width="2"/>' + "".join(b), label="saco com bolas")
    B = [free("No saco há 4 bolas pretas e 2 bolas brancas. Sem olhar, você tira uma bola.", saco),
         blk("Escreva C, T ou I.", [(f'Tirar uma bola preta. {BX}', "T"), (f'Tirar uma bola branca. {BX}', "T"),
                                    (f'Tirar uma bola verde. {BX}', "I"), (f'Tirar uma bola preta ou branca. {BX}', "C")], cols=1),
         blk("Responda.", [(f'Que cor é mais fácil de sair? {BXW}', "preta")], cols=1)]
    return [A, B]


@passo("tabelas-e-graficos", "Tabelas e gráficos", "Ler pictogramas, tabelas e gráficos de colunas.")
def _(rng):
    frutas = ["maca", "estrela", "flor", "coracao"]
    rot = {"maca": "maçã", "estrela": "estrela", "flor": "flor", "coracao": "coração"}
    vals = rng.sample(range(2, 9), 4)
    rows = "".join(f'<tr><td>{rot[f]}</td><td>{objs(v, f, per_row=10, s=20, gap=3)}</td></tr>' for f, v in zip(frutas, vals))
    picto = f'<table class="picto"><caption>Figurinha preferida da turma</caption>{rows}</table>'
    mx = rot[frutas[vals.index(max(vals))]]
    mn = rot[frutas[vals.index(min(vals))]]
    A = [free("Cada desenho é um aluno.", picto),
         blk("Responda.", [(f'Quantos alunos escolheram {rot[frutas[0]]}? {BX}', vals[0]), (f'Qual figurinha foi a mais escolhida? {BXW}', mx),
                           (f'Qual foi a menos escolhida? {BXW}', mn), (f'Quantos alunos votaram ao todo? {BX}', sum(vals)),
                           (f'Quantos alunos a mais escolheram {mx} do que {mn}? {BX}', max(vals) - min(vals))], cols=1)]
    br = ["futebol", "pega-pega", "amarelinha", "esconde-esconde"]
    v2 = rng.sample(range(1, 9), 4)
    b = []
    for i in range(9):
        y = 190 - i * 20
        b.append(f'<line x1="40" y1="{y}" x2="430" y2="{y}" stroke="#ccc" stroke-width="1"/><text x="30" y="{y + 5}" text-anchor="end" font-size="13">{i}</text>')
    for i, (n, v) in enumerate(zip(br, v2)):
        x = 70 + i * 95
        b.append(f'<rect x="{x}" y="{190 - v * 20}" width="50" height="{v * 20}" fill="{FILL}" stroke="{INK}" stroke-width="1.6"/>')
        b.append(f'<text x="{x + 25}" y="208" text-anchor="middle" font-size="13">{n}</text>')
    graf = svg(440, 214, "".join(b), label="gráfico de colunas")
    tab = "".join(f'<tr><td>{n}</td><td>{BX}</td></tr>' for n in br)
    B = [free("Brincadeira preferida da turma.", graf),
         blk("Complete a tabela com os números do gráfico.", [(f'<table class="tb"><tr><th>Brincadeira</th><th>Votos</th></tr>{tab}</table>',
                                                               ", ".join(f"{n} {v}" for n, v in zip(br, v2)))], cols=1),
         blk("Responda.", [(f'Qual brincadeira teve mais votos? {BXW}', br[v2.index(max(v2))]), (f'Quantos votos tiveram juntos futebol e amarelinha? {BX}', v2[0] + v2[2])], cols=1)]
    return [A, B]
