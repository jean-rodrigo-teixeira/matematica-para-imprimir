# -*- coding: utf-8 -*-
"""Renderização das folhas da trilha do 1º ano."""
import html

CSS1 = r"""
.sheet.s1{font-size:15pt;line-height:1.35}
.s1 .sh-title{font-size:21pt}
.s1 .folha,.gab1 .folha{font-family:"Bitter","DejaVu Serif",Georgia,serif;font-weight:700;font-size:13pt;border:1.5pt solid var(--ink);padding:1mm 3mm;white-space:nowrap;text-align:center;line-height:1.1}
.s1 .folha small,.gab1 .folha small{display:block;font-family:"Fira Sans","DejaVu Sans",sans-serif;font-weight:500;font-size:7.5pt;letter-spacing:.04em}
.s1 .f1{display:grid;grid-template-columns:1.6fr 1fr .9fr .9fr;gap:5mm;margin:3.5mm 0 4.5mm;font-size:10pt;align-items:end}
.s1 .f1 div{display:flex;gap:2mm;align-items:flex-end;white-space:nowrap}
.s1 .f1 span.l{flex:1;border-bottom:.8pt solid var(--ink);height:5mm;min-width:8mm}
.blk{margin-bottom:5mm;break-inside:avoid}
.ins{margin:0 0 2.5mm;font-weight:500;display:flex;gap:2.5mm;align-items:baseline}
.ins .n{display:inline-grid;place-items:center;min-width:6.5mm;height:6.5mm;border-radius:50%;background:#222;color:#fff;font-size:10pt;font-weight:700;flex:none}
.g1{display:grid;gap:5mm 5mm;align-items:center}
.g1.c1{grid-template-columns:1fr}.g1.c2{grid-template-columns:1fr 1fr}.g1.c3{grid-template-columns:repeat(3,1fr)}
.g1.c4{grid-template-columns:repeat(4,1fr)}.g1.c5{grid-template-columns:repeat(5,1fr)}
.it{position:relative;line-height:1.9;min-width:0}
.it svg{vertical-align:middle;max-width:100%;height:auto}
.it .in{font-size:7.5pt;color:#777;margin-right:1.2mm;vertical-align:top}
.it.ex{border:1pt dashed #999;border-radius:2mm;padding:1mm 2mm}
.it.ex::before{content:"Exemplo";position:absolute;top:-2.6mm;left:2mm;background:#fff;padding:0 1mm;font-size:7pt;color:#666;letter-spacing:.05em;text-transform:uppercase;line-height:1}
.bx{display:inline-block;width:12mm;height:10.5mm;border:1.1pt solid #222;border-radius:1mm;vertical-align:middle;text-align:center;line-height:10.5mm;background:#fff}
.bx.w{width:24mm}
.bx.exv{color:#6b6b6b;font-style:italic;font-weight:600}
.big{display:inline-block;font-family:"Bitter","DejaVu Serif",serif;font-weight:700;font-size:20pt;min-width:9mm;vertical-align:middle}
.draw{display:inline-block;width:32mm;height:26mm;border:.8pt dashed #888;border-radius:2mm;vertical-align:middle;margin-left:1mm}
.draw.wide{width:62mm;height:24mm;display:block;margin:0 0 1.5mm}
.seq{display:inline-flex;gap:1.2mm;flex-wrap:wrap;vertical-align:middle}
.seq .cell,.seq .bx{min-width:11.5mm;width:auto;height:10mm;line-height:10mm;padding:0 1mm;text-align:center;border:1.1pt solid #222;border-radius:1mm}
.seq .cell{background:#f0f0f0}
.size-sm .seq .cell,.size-sm .seq .bx{font-size:9.5pt;min-width:22mm}
.cmp{display:inline-block;min-width:12mm;text-align:center;font-size:16pt;font-weight:600;margin-right:3mm}
.pair{display:inline-flex;align-items:center;gap:2mm;margin-right:12mm}
.mirror{display:inline-block;width:0;border-left:1.2pt dashed #888;height:9mm;vertical-align:middle;margin:0 2mm;color:transparent}
.ordrow{display:inline-flex;align-items:center;gap:1.5mm;font-size:9pt;color:#555}
.ordcell{display:inline-grid;place-items:center;width:13mm;height:13mm;border:.6pt solid #ccc;border-radius:1mm}
.ordcell.mark{border:2pt solid #222}
.ordcell svg{width:10mm;height:auto}
.ordlbl{display:block;line-height:1.4}
.fam{display:inline-block;vertical-align:middle;line-height:2.15;margin-left:2mm;font-size:12pt}
.fam .bx{width:8mm;height:7.5mm;line-height:7.5mm}
.pt{margin:0 0 1.5mm;line-height:1.4}
.pf{margin:0 0 1.5mm}
.pa{font-size:12pt}
.timer{font-size:10pt;margin:-1mm 0 3mm;color:#333}
.h100{border-collapse:collapse;margin:0 auto}
.h100 td{width:14mm;height:9.5mm;border:1pt solid #222;text-align:center;font-size:12pt;padding:0}
.h100 td.hb{background:#fff}
.h100 td:not(.hb){background:#f2f2f2}
.h100.x td{width:11mm;height:9mm}
.h100.x td.e{border:none;background:none}
.cnts{display:grid;grid-template-columns:1fr 1fr;gap:2mm 6mm;margin-top:2mm}
.cnt{display:flex;align-items:center;gap:2mm}
.sols{display:flex;gap:4mm;flex-wrap:wrap}
.sol{display:flex;flex-direction:column;align-items:center;font-size:10pt;gap:1mm}
.cal{border-collapse:collapse;margin:0 auto}
.cal caption{font-family:"Bitter","DejaVu Serif",serif;font-weight:700;font-size:15pt;margin-bottom:1.5mm}
.cal th,.cal td{border:1pt solid #222;width:17mm;height:10mm;text-align:center;font-size:12pt}
.cal th{background:#eee;font-size:10pt;text-transform:capitalize}
.picto{border-collapse:collapse}
.picto caption{font-weight:700;text-align:left;margin-bottom:1.5mm}
.picto td{border:1pt solid #222;padding:1.5mm 3mm}
.picto td:first-child{width:28mm;font-weight:600}
.tb{border-collapse:collapse}
.tb th,.tb td{border:1pt solid #222;padding:1.5mm 4mm;text-align:left}
.tb th{background:#eee}
.gab1 h3{font-family:"Bitter","DejaVu Serif",serif;font-size:13pt;margin:4mm 0 1.5mm}
.gab1 .gl{display:grid;grid-template-columns:7mm 1fr;padding:1.2mm 0;border-bottom:.6pt solid #e2e4e7;font-size:9.5pt;line-height:1.45}
.gab1 .gl b{font-weight:700}
.gab1 .gi{display:inline-block;margin-right:3.2mm;white-space:nowrap}
.gab1 .gi i{font-style:normal;color:#888;font-size:8pt}
.gab1 .coach{border:1pt solid #222;border-radius:2mm;padding:3mm 4mm;margin:3mm 0;font-size:10pt;line-height:1.45}
.gab1 .coach p{margin:0 0 1.5mm}
"""


def esc(s):
    return html.escape(str(s), quote=True)


def n_answerable(blocos):
    return sum(1 for b in blocos for _, a in b["items"] if a is not None)


def render_blocos(blocos):
    out = []
    num = 0
    for b in blocos:
        if b.get("instr"):
            num += 1
        cols = b["cols"]
        cells = []
        if b.get("example"):
            cells.append(f'<div class="it ex">{b["example"]}</div>')
        show_n = len(b["items"]) > 3
        for i, (h, _) in enumerate(b["items"], 1):
            lab = f'<span class="in">({i})</span>' if show_n and not b.get("free") else ""
            cells.append(f'<div class="it">{lab}{h}</div>')
        ins = f'<p class="ins"><span class="n">{num}</span><span>{b["instr"]}</span></p>' if b.get("instr") else ""
        size = f' size-{b["size"]}' if b.get("size") else ""
        out.append(f'<section class="blk{size}">{ins}{b.get("note", "")}<div class="g1 c{cols}">{"".join(cells)}</div></section>')
    return "".join(out)


def gab_blocos(blocos):
    out = []
    num = 0
    for b in blocos:
        if b.get("instr"):
            num += 1
        ans = [(i, a) for i, (_, a) in enumerate(b["items"], 1)]
        if all(a is None for _, a in ans):
            txt = "Resposta pessoal / traçado livre."
        elif len(ans) == 1:
            txt = esc(ans[0][1])
        else:
            txt = "".join(f'<span class="gi"><i>({i})</i> {esc("—" if a is None else a)}</span>' for i, a in ans)
        out.append(f'<div class="gl"><b>{num}.</b><span>{txt}</span></div>')
    return "".join(out)


def passo_html(p):
    letters = "AB"
    top = lambda kicker, folha: (
        f'<header class="sh-top"><div><div class="sh-kicker">{kicker}</div>'
        f'<h2 class="sh-title">Passo {p["n"]} · {esc(p["titulo"])}</h2></div>{folha}</header>')
    kick = f'Matemática · 1º ano · Unidade {p["unidade"]}: {esc(p["unidade_titulo"])}'
    pages = []
    for i, blocos in enumerate(p["folhas"]):
        L = letters[i]
        sub = "com apoio" if L == "A" else "treino"
        tot = n_answerable(blocos)
        fields = (f'<div class="f1"><div>Nome:<span class="l"></span></div><div>Data:<span class="l"></span></div>' +
                  (f'<div>Acertos:<span class="l"></span>/ {tot}</div>' if tot else '<div></div>') + '<div>Tempo:<span class="l"></span>min</div></div>')
        pages.append(f'<article class="sheet s1">{top(kick, f"<div class=folha>Folha {L}<small>{sub}</small></div>")}{fields}'
                     f'{render_blocos(blocos)}'
                     f'<footer class="sh-foot"><span>Matemática para Imprimir · Trilha do 1º ano</span><span>Passo {p["n"]} · Folha {L}</span></footer></article>')
    totB = n_answerable(p["folhas"][-1])
    meta = max(1, int(totB * 0.9 + 0.999)) if totB else 0
    crit = (f"Avance para o próximo passo quando a criança acertar pelo menos <b>{meta} de {totB}</b> itens da Folha B (90%). "
            "Se não chegar lá, repita a Folha B em outro dia, sem pressa." if totB else
            "Avance quando a criança fizer as atividades com segurança e explicar como pensou.")
    if "Treino" in p["titulo"]:
        crit += " Nas folhas de treino, anote o tempo: a meta é acertar tudo e ir ficando mais rápido a cada repetição."
    body = "".join(f'<h3>Folha {letters[i]}</h3>{gab_blocos(b)}' for i, b in enumerate(p["folhas"]))
    gab = (f'<article class="sheet gab gab1">{top(kick.replace("Matemática", "Gabarito do professor"), "<div class=folha>Gabarito</div>")}'
           f'<div class="coach"><p><b>Objetivo:</b> {esc(p["objetivo"])}</p><p><b>Critério de avanço:</b> {crit}</p>'
           f'<p><b>BNCC:</b> {esc(p["bncc"])}</p></div>{body}'
           f'<footer class="sh-foot"><span>Matemática para Imprimir · Trilha do 1º ano</span><span>Passo {p["n"]} · Gabarito</span></footer></article>')
    return pages, gab
