# -*- coding: utf-8 -*-
import html, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import LISTAS
from primeiro_ano import PASSOS, UNIDADES
from render1 import CSS1, passo_html
from concurrent.futures import ThreadPoolExecutor

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
TMP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_tmp")
os.makedirs(TMP, exist_ok=True)
os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
LET = "abcdefghij"

SHEET_CSS = r"""
.sheet{--ink:#1b1d1f;--rule:#b9bec4;--soft:#5d646b;
  width:210mm;min-height:297mm;box-sizing:border-box;padding:13mm 15mm 12mm;background:#fff;color:var(--ink);
  font-family:"Fira Sans","DejaVu Sans",Arial,sans-serif;font-size:11.5pt;line-height:1.4;position:relative}
.sheet *{box-sizing:border-box}
.sh-top{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2pt solid var(--ink);padding-bottom:2.5mm}
.sh-kicker{font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);font-weight:600}
.sh-title{font-family:"Bitter","DejaVu Serif",Georgia,serif;font-weight:700;font-size:19pt;line-height:1.15;margin:1mm 0 0}
.sh-ano{font-family:"Bitter","DejaVu Serif",Georgia,serif;font-weight:700;font-size:13pt;border:1.5pt solid var(--ink);padding:1mm 3mm;white-space:nowrap}
.sh-fields{display:grid;grid-template-columns:1fr 1fr;gap:2.2mm 6mm;margin:4mm 0 2mm;font-size:10pt}
.sh-fields div{display:flex;gap:2mm;align-items:flex-end}
.sh-fields span.l{flex:1;border-bottom:.8pt solid var(--ink);height:5mm}
.sh-fields .wide{grid-column:1/-1}
.sh-meta{font-size:8.5pt;color:var(--soft);margin-bottom:4mm}
.q{display:grid;grid-template-columns:7mm 1fr;break-inside:avoid;page-break-inside:avoid;margin-bottom:3.2mm}
.q-n{font-weight:700}
.q-t{margin:0}
.q-items{display:grid;grid-template-columns:repeat(auto-fill,minmax(40mm,1fr));gap:1.5mm 6mm;margin-top:1.6mm}
.q-items.wide{grid-template-columns:repeat(auto-fill,minmax(80mm,1fr))}
.q-items b{font-weight:600;margin-right:1.5mm}
.space{border-bottom:.6pt dashed var(--rule)}
.sp-s{height:6mm}.sp-m{height:20mm}.sp-l{height:34mm}
.fig{display:block;margin:2mm 0 1mm}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1.05;font-size:.92em;margin:0 .1em}
.fr>span:first-child{border-bottom:.9pt solid currentColor;padding:0 .2em}
.fr>span:last-child{padding:0 .2em}
.sh-foot{position:absolute;left:15mm;right:15mm;bottom:7mm;font-size:7.5pt;color:var(--soft);display:flex;justify-content:space-between}
.gab .g{display:grid;grid-template-columns:8mm 1fr;padding:1.8mm 0;border-bottom:.6pt solid #e2e4e7}
.gab .g b{font-weight:700}
.gab-note{font-size:9pt;color:var(--soft);margin:3mm 0 4mm}
"""


def esc(s):
    return html.escape(s, quote=True)


def sheet_html(L, n_total):
    q_html = []
    for i, q in enumerate(L["q"], 1):
        parts = [f'<p class="q-t">{q["t"]}</p>']
        if q.get("fig"):
            parts.append(q["fig"])
        if q.get("items"):
            wide = any(len(x) > 60 and "fr" not in x for x in q["items"]) or len(q["items"]) == 2 and any(len(x) > 22 for x in q["items"])
            its = "".join(f'<div><b>{LET[k]})</b>{x}</div>' for k, x in enumerate(q["items"]))
            parts.append(f'<div class="q-items{" wide" if wide else ""}">{its}</div>')
        parts.append(f'<div class="space sp-{q.get("space","m")}"></div>')
        q_html.append(f'<section class="q"><span class="q-n">{i}.</span><div>{"".join(parts)}</div></section>')

    top = f'''<header class="sh-top"><div><div class="sh-kicker">Lista de exercícios · Matemática · {esc(L["tema"])}</div>
<h2 class="sh-title">{esc(L["titulo"])}</h2></div><div class="sh-ano">{L["ano"]}º ano</div></header>'''
    fields = '''<div class="sh-fields"><div class="wide">Escola:<span class="l"></span></div>
<div>Nome:<span class="l"></span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div style="display:flex;gap:2mm;align-items:flex-end">Turma:<span class="l"></span></div><div style="display:flex;gap:2mm;align-items:flex-end">Data:<span class="l"></span></div></div></div>'''
    meta = f'<div class="sh-meta">Habilidades BNCC: {esc(L["bncc"])} · {len(L["q"])} questões</div>'
    foot = f'<footer class="sh-foot"><span>Acervo de Listas de Matemática</span><span>{L["ano"]}º ano · {esc(L["titulo"])}</span></footer>'
    main = f'<article class="sheet">{top}{fields}{meta}{"".join(q_html)}</article>'

    g = "".join(f'<div class="g"><b>{i}.</b><span>{q["ans"]}</span></div>' for i, q in enumerate(L["q"], 1))
    gab = f'''<article class="sheet gab">{top.replace("Lista de exercícios", "Gabarito do professor")}
<p class="gab-note">Respostas finais. Destaque esta página antes de entregar a lista aos alunos.</p>{g}{foot}</article>'''
    return main, gab


# ---------- PDFs ----------
PDF_PAGE = """<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title>
<style>@page{{size:A4;margin:12mm 14mm 11mm}}html,body{{margin:0;padding:0}}{css}
.sheet{{width:auto;min-height:0;height:auto;padding:0}}
.sheet + .sheet{{break-before:page;page-break-before:always}}
.sh-foot{{position:static;margin-top:5mm}}</style></head><body>{body}</body></html>"""
ALL_CSS = SHEET_CSS + CSS1
JOBS = []


def pdf_job(name, title, body):
    hp = os.path.abspath(os.path.join(TMP, f"{name}.html"))
    with open(hp, "w") as f:
        f.write(PDF_PAGE.format(title=esc(title), css=ALL_CSS, body=body))
    JOBS.append((hp, os.path.join(OUT, "pdf", f"{name}.pdf")))


def to_pdf(job):
    hp, pdf = job
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--user-data-dir=/tmp/chr-{os.path.basename(hp)}", f"--print-to-pdf={pdf}", "file://" + hp],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


rendered = []
all_bodies = []
for L in LISTAS:
    main, gab = sheet_html(L, len(LISTAS))
    rendered.append((L, main, gab))
    body = main + gab
    all_bodies.append(body)
    pdf_job(L["slug"], L["titulo"], body)
pdf_job("todas-as-listas", "Todas as listas", "".join(all_bodies))

passos_r = []
for p in PASSOS:
    pages, gab = passo_html(p)
    passos_r.append((p, pages, gab))
    pdf_job(p["slug"], f'Passo {p["n"]} · {p["titulo"]}', "".join(pages) + gab)
for u in UNIDADES:
    body = "".join("".join(pg) + gb for p, pg, gb in passos_r if p["unidade"] == u["n"])
    pdf_job(f'1ano-unidade-{u["n"]}', f'1º ano · Unidade {u["n"]}', body)
pdf_job("1ano-trilha-completa", "Trilha do 1º ano", "".join("".join(pg) + gb for _, pg, gb in passos_r))

if os.environ.get("SKIP_PDF") != "1":
    with ThreadPoolExecutor(6) as ex:
        list(ex.map(to_pdf, JOBS))

# ---------- Site ----------
cards = {"I": [], "II": []}
views = []
for L, main, gab in rendered:
    seg = "I" if L["ano"] <= 5 else "II"
    cards[seg].append(f'''<li class="card" data-ano="{L['ano']}">
<div class="card-top"><span class="tag">{L['ano']}º ano</span><span class="tema">{esc(L['tema'])}</span></div>
<h3><a href="#lista-{L['slug']}">{esc(L['titulo'])}</a></h3>
<p class="card-meta">{len(L['q'])} questões · gabarito incluso<br><span class="bncc">BNCC {esc(L['bncc'])}</span></p>
<div class="card-actions"><a class="btn" href="#lista-{L['slug']}">Ver lista</a>
<button class="btn ghost dl" type="button" data-slug="{L['slug']}" data-name="{L['ano']}ano-{L['slug'].split('-',1)[1]}.pdf">Baixar PDF</button></div></li>''')
    views.append(f'''<section class="view" id="v-{L['slug']}" hidden>
<div class="toolbar"><a class="btn ghost" href="#catalogo">← Catálogo</a>
<span class="tb-title">{L['ano']}º ano · {esc(L['titulo'])}</span>
<label class="tgl"><input type="checkbox" class="gab-toggle" id="gab-{L['slug']}" checked> Mostrar gabarito</label>
<button class="btn dl" type="button" data-slug="{L['slug']}" data-name="{L['ano']}ano-{L['slug'].split('-',1)[1]}.pdf">Baixar PDF para imprimir</button></div>
<div class="paper-wrap"><div class="paper">{main}<div class="gab-wrap">{gab}</div></div></div></section>''')

trilha = []
for u in UNIDADES:
    rows = "".join(f'''<li><a href="#lista-{p['slug']}"><span class="pn">{p['n']}</span>{esc(p['titulo'])}</a>
<button class="ico dl" type="button" data-slug="{p['slug']}" data-name="{p['slug']}.pdf" aria-label="Baixar PDF do passo {p['n']}" title="Baixar PDF">PDF</button></li>''' for p in u["passos"])
    trilha.append(f'''<section class="unit"><div class="unit-h"><span class="un">Unidade {u['n']}</span><h3>{esc(u['titulo'])}</h3>
<p class="bncc">BNCC {esc(u['bncc'])}</p></div><ol class="steps">{rows}</ol>
<button class="btn ghost dl unit-dl" type="button" data-slug="1ano-unidade-{u['n']}" data-name="1ano-unidade-{u['n']}.pdf">Baixar unidade inteira (PDF)</button></section>''')
for p, pages, gab in passos_r:
    nxt = PASSOS[p["n"]] if p["n"] < len(PASSOS) else None
    prv = PASSOS[p["n"] - 2] if p["n"] > 1 else None
    nav = (f'<a class="btn ghost" href="#lista-{prv["slug"]}">← Passo {prv["n"]}</a>' if prv else "") + \
          (f'<a class="btn ghost" href="#lista-{nxt["slug"]}">Passo {nxt["n"]} →</a>' if nxt else "")
    views.append(f'''<section class="view" id="v-{p['slug']}" hidden>
<div class="toolbar"><a class="btn ghost" href="#catalogo">← Catálogo</a>
<span class="tb-title">1º ano · Passo {p['n']} · {esc(p['titulo'])}</span>{nav}
<label class="tgl"><input type="checkbox" class="gab-toggle" id="gab-{p['slug']}" checked> Mostrar gabarito</label>
<button class="btn dl" type="button" data-slug="{p['slug']}" data-name="{p['slug']}.pdf">Baixar PDF para imprimir</button></div>
<div class="paper-wrap"><div class="paper">{"".join(pages)}<div class="gab-wrap">{gab}</div></div></div></section>''')

chips = '<button type="button" class="chip on" data-f="all">Todos</button>' + "".join(
    f'<button type="button" class="chip" data-f="{a}">{a}º ano</button>' for a in range(1, 10))

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_template.html")) as f:
    tpl = f.read()
nfolhas = len(LISTAS) + sum(len(p["folhas"]) for p in PASSOS)
nitens = sum(len(L["q"]) for L in LISTAS) + sum(len(b["items"]) for p in PASSOS for fl in p["folhas"] for b in fl)
page = (tpl.replace("{{SHEET_CSS}}", ALL_CSS)
        .replace("{{CHIPS}}", chips)
        .replace("{{TRILHA}}", "".join(trilha))
        .replace("{{NPASSOS}}", str(len(PASSOS)))
        .replace("{{CARDS_I}}", "".join(cards["I"]))
        .replace("{{CARDS_II}}", "".join(cards["II"]))
        .replace("{{VIEWS}}", "".join(views))
        .replace("{{N}}", str(len(LISTAS) + len(PASSOS)))
        .replace("{{NQ}}", str(nitens)))
with open(os.path.join(OUT, "index.html"), "w") as f:
    f.write(page)
print("ok", len(LISTAS), "listas +", len(PASSOS), "passos;", len(JOBS), "PDFs")
