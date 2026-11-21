# -*- coding: utf-8 -*-
"""Figuras SVG para as folhas do 1º ano (impressão em preto e branco)."""
import math

INK = "#222"
GRAY = "#9a9a9a"
FILL = "#cfcfcf"


SCALE = 1.4


def svg(w, h, body, width_mm=None, label="", scale=None):
    k = SCALE if scale is None else scale
    wm = f' style="width:{width_mm}mm;height:auto"' if width_mm else ""
    return (f'<svg class="fg" viewBox="0 0 {w:g} {h:g}" width="{w * k:.0f}" height="{h * k:.0f}"{wm} role="img" '
            f'aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{body}</svg>')


# ---------- ícones (caixa 24x24, origem no canto) ----------
def _icon(name, x, y, s=24):
    k = s / 24
    t = f'transform="translate({x:g},{y:g}) scale({k:g})"'
    if name == "bola":
        return (f'<g {t} fill="none" stroke="{INK}" stroke-width="1.6"><circle cx="12" cy="12" r="9"/>'
                f'<path d="M3.5 9.5 Q12 14 20.5 9.5 M5 17 Q12 11 19 17"/></g>')
    if name == "estrela":
        pts = []
        for i in range(10):
            r = 10.5 if i % 2 == 0 else 4.5
            a = -math.pi / 2 + i * math.pi / 5
            pts.append(f"{12 + r * math.cos(a):.2f},{12.8 + r * math.sin(a):.2f}")
        return f'<g {t}><polygon points="{" ".join(pts)}" fill="{FILL}" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/></g>'
    if name == "maca":
        return (f'<g {t} stroke="{INK}" stroke-width="1.5"><path d="M12 7 C6 3 1.5 9 3.5 15 C5 20 9 22.5 12 20.5 C15 22.5 19 20 20.5 15 C22.5 9 18 3 12 7 Z" fill="{FILL}"/>'
                f'<path d="M12 7 L13 2.5" fill="none"/><path d="M13.2 4 C15.5 2 18 2.5 18.5 3.5 C16.5 5 14.5 5 13.2 4 Z" fill="#fff"/></g>')
    if name == "peixe":
        return (f'<g {t} stroke="{INK}" stroke-width="1.5" fill="#fff"><path d="M2.5 12 C6 5 15 5 18.5 12 C15 19 6 19 2.5 12 Z"/>'
                f'<path d="M18.5 12 L23 7.5 L23 16.5 Z"/><circle cx="7" cy="11" r="1.1" fill="{INK}"/></g>')
    if name == "flor":
        pet = "".join(f'<circle cx="{12 + 5.2 * math.cos(i * 2 * math.pi / 5 - math.pi / 2):.2f}" cy="{12 + 5.2 * math.sin(i * 2 * math.pi / 5 - math.pi / 2):.2f}" r="4" fill="#fff"/>' for i in range(5))
        return f'<g {t} stroke="{INK}" stroke-width="1.4">{pet}<circle cx="12" cy="12" r="3" fill="{FILL}"/></g>'
    if name == "coracao":
        return f'<g {t}><path d="M12 21 C3 14 1.5 9.5 4 6 C6.5 3 10.5 4 12 7.5 C13.5 4 17.5 3 20 6 C22.5 9.5 21 14 12 21 Z" fill="{FILL}" stroke="{INK}" stroke-width="1.4"/></g>'
    if name == "lapis":
        return (f'<g {t} stroke="{INK}" stroke-width="1.4" fill="#fff"><path d="M4 20 L5.5 15 L16.5 4 L20 7.5 L9 18.5 Z"/>'
                f'<path d="M4 20 L5.5 15 L9 18.5 Z" fill="{FILL}"/></g>')
    raise ValueError(name)


ICONES = ["maca", "estrela", "bola", "peixe", "flor", "coracao"]
NOMES = {"maca": ("maçã", "maçãs", "f"), "estrela": ("estrela", "estrelas", "f"), "bola": ("bola", "bolas", "f"),
         "peixe": ("peixe", "peixes", "m"), "flor": ("flor", "flores", "f"), "coracao": ("coração", "corações", "m"),
         "lapis": ("lápis", "lápis", "m")}


def objs(n, icon, per_row=5, s=24, gap=4, crossed=0, label=None):
    """n ícones em linhas de 5 (agrupamento que favorece a subitização)."""
    rows = max(1, math.ceil(n / per_row))
    w = min(n, per_row) * (s + gap) - gap if n else s
    h = rows * (s + gap) - gap
    b = []
    for i in range(n):
        x = (i % per_row) * (s + gap)
        y = (i // per_row) * (s + gap)
        b.append(_icon(icon, x, y, s))
        if i >= n - crossed:
            b.append(f'<path d="M{x + 1} {y + 1} L{x + s - 1} {y + s - 1} M{x + s - 1} {y + 1} L{x + 1} {y + s - 1}" stroke="{INK}" stroke-width="2.2"/>')
    return svg(w, h, "".join(b), label=label or f"{n} figuras")


def dots(n, per_row=5, r=8, gap=5, filled=None, crossed=0, empty_after=0):
    """filled: quantas pintadas (o resto vazado). empty_after: círculos vazios extras."""
    total = n + empty_after
    filled = n if filled is None else filled
    rows = max(1, math.ceil(total / per_row))
    d = 2 * r
    w = min(total, per_row) * (d + gap) - gap if total else d
    h = rows * (d + gap) - gap
    b = []
    for i in range(total):
        cx = (i % per_row) * (d + gap) + r
        cy = (i // per_row) * (d + gap) + r
        f = INK if i < filled else "#fff"
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 1}" fill="{f}" stroke="{INK}" stroke-width="1.6"/>')
        if n - crossed <= i < n:
            b.append(f'<path d="M{cx - r} {cy - r} L{cx + r} {cy + r} M{cx + r} {cy - r} L{cx - r} {cy + r}" stroke="{INK}" stroke-width="2.2"/>')
    return svg(w, h, "".join(b), label=f"{n} bolinhas")


def tenframe(n, cell=22, frames=1, mark="dot"):
    """Quadro de dez (ou dois quadros lado a lado para até 20)."""
    b = []
    fw = 5 * cell
    for f in range(frames):
        ox = f * (fw + 10)
        b.append(f'<rect x="{ox + 1}" y="1" width="{fw}" height="{2 * cell}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        for i in range(1, 5):
            b.append(f'<line x1="{ox + 1 + i * cell}" y1="1" x2="{ox + 1 + i * cell}" y2="{1 + 2 * cell}" stroke="{INK}" stroke-width="1.2"/>')
        b.append(f'<line x1="{ox + 1}" y1="{1 + cell}" x2="{ox + 1 + fw}" y2="{1 + cell}" stroke="{INK}" stroke-width="1.2"/>')
        k = max(0, min(10, n - 10 * f))
        for i in range(k):
            cx = ox + 1 + (i % 5) * cell + cell / 2
            cy = 1 + (i // 5) * cell + cell / 2
            b.append(f'<circle cx="{cx}" cy="{cy}" r="{cell * .34:.1f}" fill="{INK}"/>')
    W = frames * fw + (frames - 1) * 10 + 2
    return svg(W, 2 * cell + 2, "".join(b), label=f"quadro de dez com {n}")


def bond(whole, a, b, r=17, box=False):
    """Ligação de números (método de Singapura): todo em cima, partes embaixo. None = vazio."""
    W, H = 120, 92
    def node(cx, cy, v):
        t = "" if v is None else f'<text x="{cx}" y="{cy + 6.5}" text-anchor="middle" font-size="19" font-weight="600">{v}</text>'
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>{t}'
    body = (f'<line x1="60" y1="{r + 2}" x2="24" y2="{H - r - 2}" stroke="{INK}" stroke-width="2"/>'
            f'<line x1="60" y1="{r + 2}" x2="96" y2="{H - r - 2}" stroke="{INK}" stroke-width="2"/>'
            + node(60, r + 2, whole) + node(22, H - r - 2, a) + node(98, H - r - 2, b))
    return svg(W, H, body, label="ligação de números")


def numline(lo=0, hi=10, start=None, jumps=0, unit=None, width=300, labels=True):
    """Reta numérica; jumps>0 pulos para frente, <0 para trás, a partir de start."""
    n = hi - lo
    unit = unit or (width - 20) / n
    W = 20 + n * unit
    y = 46
    b = [f'<line x1="4" y1="{y}" x2="{W - 4}" y2="{y}" stroke="{INK}" stroke-width="1.8"/>',
         f'<path d="M{W - 4} {y} l-7 -4 v8 z" fill="{INK}"/>']
    for i in range(n + 1):
        x = 10 + i * unit
        b.append(f'<line x1="{x:.1f}" y1="{y - 6}" x2="{x:.1f}" y2="{y + 6}" stroke="{INK}" stroke-width="1.5"/>')
        if labels:
            b.append(f'<text x="{x:.1f}" y="{y + 22}" text-anchor="middle" font-size="14">{lo + i}</text>')
    if start is not None and jumps:
        step = 1 if jumps > 0 else -1
        for j in range(abs(jumps)):
            a = start + j * step
            x1 = 10 + (a - lo) * unit
            x2 = x1 + step * unit
            mx = (x1 + x2) / 2
            b.append(f'<path d="M{x1:.1f} {y - 7} Q{mx:.1f} {y - 34} {x2:.1f} {y - 7}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
            b.append(f'<path d="M{x2:.1f} {y - 7} l{-step * 6:.1f} -5 l{step * 1:.1f} 6 z" fill="{INK}"/>')
        xs = 10 + (start - lo) * unit
        b.append(f'<circle cx="{xs:.1f}" cy="{y}" r="4.5" fill="{INK}"/>')
    return svg(W, y + 28, "".join(b), label="reta numérica", scale=1.25)


def rods(tens, ones, u=9):
    """Material dourado simplificado: barras de 10 e cubinhos."""
    b = []
    x = 0
    for t in range(tens):
        b.append(f'<rect x="{x + 1}" y="1" width="{u}" height="{10 * u}" fill="{FILL}" stroke="{INK}" stroke-width="1.5"/>')
        for k in range(1, 10):
            b.append(f'<line x1="{x + 1}" y1="{1 + k * u}" x2="{x + 1 + u}" y2="{1 + k * u}" stroke="{INK}" stroke-width=".8"/>')
        x += u + 5
    if ones:
        x += 6
        for i in range(ones):
            cx = x + (i % 2) * (u + 3)
            cy = 10 * u - (i // 2) * (u + 3) - u + 1
            b.append(f'<rect x="{cx + 1}" y="{cy}" width="{u}" height="{u}" fill="#fff" stroke="{INK}" stroke-width="1.5"/>')
        x += 2 * (u + 3)
    return svg(max(x, u + 2), 10 * u + 2, "".join(b), label=f"{tens} dezenas e {ones} unidades")


def bar_model(parts, total="?", width=300, unit=None):
    """Modelo de barras de Singapura. parts: lista de (valor_num, rótulo)."""
    tot = sum(p[0] for p in parts)
    unit = unit or (width - 4) / tot
    x = 2
    b = []
    for v, lab in parts:
        w = v * unit
        b.append(f'<rect x="{x:.1f}" y="26" width="{w:.1f}" height="30" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        b.append(f'<text x="{x + w / 2:.1f}" y="47" text-anchor="middle" font-size="16">{lab}</text>')
        x += w
    b.append(f'<path d="M2 18 V12 H{x:.1f} V18" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    b.append(f'<text x="{(x + 2) / 2:.1f}" y="9" text-anchor="middle" font-size="15" font-weight="600">{total}</text>')
    return svg(x + 2, 60, "".join(b), label="modelo de barras")


def bar_compare(a, b_, la, lb, width=300):
    """Modelo de barras de comparação: duas barras, diferença com '?'."""
    m = max(a, b_)
    unit = (width - 70) / m
    out = []
    for i, (v, lab) in enumerate([(a, la), (b_, lb)]):
        y = 6 + i * 38
        out.append(f'<text x="0" y="{y + 20}" font-size="14">{lab}</text>')
        out.append(f'<rect x="64" y="{y}" width="{v * unit:.1f}" height="28" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        out.append(f'<text x="{64 + v * unit / 2:.1f}" y="{y + 20}" text-anchor="middle" font-size="15">{v}</text>')
    s, l = min(a, b_), m
    y = 6 + (0 if a < b_ else 1) * 38
    out.append(f'<rect x="{64 + s * unit:.1f}" y="{y}" width="{(l - s) * unit:.1f}" height="28" fill="none" stroke="{INK}" stroke-width="1.6" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{64 + (s + l) / 2 * unit:.1f}" y="{y + 20}" text-anchor="middle" font-size="16" font-weight="600">?</text>')
    return svg(width, 82, "".join(out), label="barras de comparação")


def trace_row(ch, n=6, size=46):
    """Linha de números pontilhados para cobrir."""
    gap = size * 0.95
    b = [f'<line x1="0" y1="{size + 4}" x2="{n * gap + 6}" y2="{size + 4}" stroke="{GRAY}" stroke-width="1"/>']
    for i in range(n):
        x = 6 + i * gap
        if i == 0:
            b.append(f'<text x="{x}" y="{size}" font-size="{size}" font-family="Fira Sans, DejaVu Sans, sans-serif" fill="{INK}">{ch}</text>')
        else:
            b.append(f'<text x="{x}" y="{size}" font-size="{size}" font-family="Fira Sans, DejaVu Sans, sans-serif" fill="none" stroke="{GRAY}" stroke-width="1.3" stroke-dasharray="3 2.5">{ch}</text>')
    return svg(n * gap + 8, size + 8, "".join(b), label=f"cobrir o número {ch}")


def shape(kind, x, y, s=30, fill="#fff"):
    if kind == "circulo":
        return f'<circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s / 2 - 1}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    if kind == "quadrado":
        return f'<rect x="{x + 1}" y="{y + 1}" width="{s - 2}" height="{s - 2}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    if kind == "triangulo":
        return f'<polygon points="{x + s / 2},{y + 1} {x + s - 1},{y + s - 1} {x + 1},{y + s - 1}" fill="{fill}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'
    if kind == "retangulo":
        return f'<rect x="{x + 1}" y="{y + s * .22}" width="{s * 1.5 - 2}" height="{s * .56}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    raise ValueError(kind)


SHAPE_W = {"circulo": 1, "quadrado": 1, "triangulo": 1, "retangulo": 1.5}
SHAPE_NOME = {"circulo": "círculo", "quadrado": "quadrado", "triangulo": "triângulo", "retangulo": "retângulo"}


def shape_row(kinds, s=30, gap=10, blanks=()):
    b = []
    x = 0
    for i, k in enumerate(kinds):
        if i in blanks:
            b.append(f'<rect x="{x + 1}" y="1" width="{s - 2}" height="{s - 2}" fill="none" stroke="{GRAY}" stroke-width="1.2" stroke-dasharray="4 3"/>')
            x += s + gap
        else:
            b.append(shape(k, x, 0, s, FILL if k in ("triangulo", "circulo") else "#fff"))
            x += s * SHAPE_W[k] + gap
    return svg(x, s + 2, "".join(b), label="sequência de figuras")


def solid(kind, x=0, y=0, s=60):
    k = s / 60
    t = f'transform="translate({x},{y}) scale({k:g})"'
    st = f'stroke="{INK}" stroke-width="2" fill="#fff"'
    if kind == "cubo":
        return (f'<g {t}><path d="M8 20 L38 20 L38 52 L8 52 Z" {st}/><path d="M8 20 L20 8 L50 8 L38 20 Z" {st}/>'
                f'<path d="M38 20 L50 8 L50 40 L38 52 Z" {st}/></g>')
    if kind == "esfera":
        return (f'<g {t}><circle cx="30" cy="30" r="24" {st}/><ellipse cx="30" cy="30" rx="24" ry="7" fill="none" stroke="{INK}" stroke-width="1.2" stroke-dasharray="3 3"/></g>')
    if kind == "cilindro":
        return (f'<g {t}><path d="M10 12 L10 48 A20 6 0 0 0 50 48 L50 12" {st}/><ellipse cx="30" cy="12" rx="20" ry="6" {st}/></g>')
    if kind == "cone":
        return (f'<g {t}><path d="M30 4 L50 48 A20 6 0 0 1 10 48 Z" {st}/><path d="M10 48 A20 6 0 0 1 50 48" fill="none" stroke="{INK}" stroke-width="1.2" stroke-dasharray="3 3"/></g>')
    if kind == "bloco":
        return (f'<g {t}><path d="M4 26 L42 26 L42 52 L4 52 Z" {st}/><path d="M4 26 L16 16 L54 16 L42 26 Z" {st}/>'
                f'<path d="M42 26 L54 16 L54 42 L42 52 Z" {st}/></g>')
    if kind == "piramide":
        return (f'<g {t}><path d="M30 4 L8 44 L36 54 Z" {st}/><path d="M30 4 L36 54 L54 42 Z" {st}/></g>')
    raise ValueError(kind)


def coin(v, x, y):
    lab = f"{v}" if v >= 1 else f"{int(v * 100)}¢"
    r = 15 if v >= 1 else 12
    return (f'<circle cx="{x + r}" cy="{y + 16}" r="{r}" fill="{FILL}" stroke="{INK}" stroke-width="1.8"/>'
            f'<circle cx="{x + r}" cy="{y + 16}" r="{r - 3.5}" fill="none" stroke="{INK}" stroke-width=".8"/>'
            f'<text x="{x + r}" y="{y + 21}" text-anchor="middle" font-size="{13 if v >= 1 else 10}" font-weight="700">{lab}</text>'), 2 * r + 6


def note(v, x, y):
    return (f'<rect x="{x + 1}" y="{y + 1}" width="62" height="32" rx="3" fill="#fff" stroke="{INK}" stroke-width="1.8"/>'
            f'<rect x="{x + 5}" y="{y + 5}" width="54" height="24" rx="2" fill="none" stroke="{INK}" stroke-width=".8"/>'
            f'<text x="{x + 32}" y="{y + 23}" text-anchor="middle" font-size="15" font-weight="700">R$ {v}</text>'), 68


def money(items):
    """items: lista de valores; >=2 vira cédula, 1 vira moeda."""
    b = []
    x = 0
    for v in items:
        g, w = note(v, x, 0) if v >= 2 else coin(v, x, 1)
        b.append(g)
        x += w
    return svg(x, 36, "".join(b), label="dinheiro")
