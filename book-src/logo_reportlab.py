# -*- coding: utf-8 -*-
"""Shared helper: draw the CRF-GO logo (badge + wordmark) on a reportlab canvas."""
import re
from reportlab.lib import colors
from reportlab.pdfgen import canvas as rl_canvas

TOKEN_RE = re.compile(r'([MLCZ])|(-?\d*\.?\d+(?:[eE]-?\d+)?)')
TEAL = colors.HexColor('#A4C4C5')
GRAY = colors.HexColor('#636266')

_svg = open('icon_traced3.svg', encoding='utf-8').read()
_paths = re.findall(r'<path d="([^"]+)" fill="(#[0-9A-Fa-f]+)" transform="translate\(([^)]+)\)"', _svg)
SYMBOL_D, _, _SYMBOL_TR = max(_paths, key=lambda p: len(p[0]))
_TX, _TY = [float(v) for v in _SYMBOL_TR.split(',')]
# symbol path coordinates are in an 8x-upscaled 552x616 space, offset by (_TX,_TY) within that space,
# and that whole space maps to a 69x77 badge via scale(0.125). So symbol-space -> badge-space: (x+_TX)*0.125, (y+_TY)*0.125


def _draw_symbol_path(c, ox, oy, scale):
    """ox,oy = badge origin (bottom-left) in canvas pt; scale = badge_width_pt / 69."""
    tokens = []
    for a, b in TOKEN_RE.findall(SYMBOL_D):
        tokens.append(a if a else float(b))
    i = 0
    cmd = None
    p = c.beginPath()
    while i < len(tokens):
        tok = tokens[i]
        if tok in ('M', 'L', 'C', 'Z'):
            cmd = tok
            i += 1
            if cmd == 'Z':
                p.close()
                continue
            if cmd in ('M', 'L'):
                x, y = tokens[i], tokens[i + 1]
                i += 2
                bx, by = (x + _TX) * 0.125, (y + _TY) * 0.125
                # badge viewBox y grows downward (svg), canvas y grows upward -> flip within badge height 77
                px, py = ox + bx * scale, oy + (77 - by) * scale
                if cmd == 'M':
                    p.moveTo(px, py)
                else:
                    p.lineTo(px, py)
            elif cmd == 'C':
                pass
        elif cmd == 'C':
            x1, y1, x2, y2, x3, y3 = tokens[i:i + 6]
            i += 6

            def conv(x, y):
                bx, by = (x + _TX) * 0.125, (y + _TY) * 0.125
                return ox + bx * scale, oy + (77 - by) * scale
            p1 = conv(x1, y1); p2 = conv(x2, y2); p3 = conv(x3, y3)
            p.curveTo(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
        else:
            i += 1
    c.setFillColor(colors.white)
    c.drawPath(p, fill=1, stroke=0)


def draw_logo(c, x, y, badge_h=60, light=False, wordmark=True):
    """Draw badge (bottom-left at x,y) with height badge_h pt; optionally the CRF-GO wordmark to its right.
    light=True -> white text (for dark backgrounds)."""
    scale = badge_h / 77.0
    badge_w = 69 * scale
    rx = 9 * scale
    c.saveState()
    c.setFillColor(TEAL)
    c.roundRect(x, y, badge_w, badge_h, rx, fill=1, stroke=0)
    _draw_symbol_path(c, x, y, scale)
    if wordmark:
        text_color = colors.white if light else GRAY
        tag_color = colors.HexColor('#EAF1F1') if light else GRAY
        tx0 = x + badge_w + 0.22 * badge_h
        c.setFillColor(text_color)
        c.setFont('Helvetica-Bold', badge_h * 0.62)
        title_baseline = y + badge_h * 0.40
        c.drawString(tx0, title_baseline, 'CRF-GO')
        c.setFillColor(tag_color)
        c.setFont('Helvetica-Bold', badge_h * 0.135)
        c.drawString(tx0 + 0.01 * badge_h, y + badge_h * 0.12, 'CONSELHO REGIONAL DE FARMÁCIA DO ESTADO DE GOIÁS')
    c.restoreState()
