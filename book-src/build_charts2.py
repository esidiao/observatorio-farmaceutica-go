# -*- coding: utf-8 -*-
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = json.load(open('current_data.json', encoding='utf-8'))

NAVY = '#16304F'
GOLD = '#B8893B'
MUTE = '#5A6675'
INK = '#2A2F36'
LINE = '#D8DDE3'
RED = '#B0413E'
GREEN = '#3F7D5C'

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11, 'text.color': INK,
    'axes.edgecolor': LINE, 'axes.labelcolor': INK, 'xtick.color': MUTE, 'ytick.color': MUTE,
    'axes.facecolor': 'white', 'figure.facecolor': 'white', 'savefig.facecolor': 'white',
})

def style_ax(ax, grid_axis='x'):
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(LINE)
    ax.tick_params(length=0)
    if grid_axis:
        ax.grid(axis=grid_axis, color=LINE, linewidth=0.7, alpha=0.8, zorder=0)
        ax.set_axisbelow(True)

def savefig(fig, name, w, h):
    fig.set_size_inches(w, h)
    fig.tight_layout(pad=0.6)
    fig.savefig(f'fig_{name}.png', dpi=300, bbox_inches='tight', pad_inches=0.08)
    plt.close(fig)
    print('wrote fig_%s.png' % name)

def donut_external(ax, labels, values, colors):
    total = sum(values)
    wedges, _ = ax.pie(values, colors=colors, startangle=90, counterclock=False,
                        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2))
    for w, v, lab in zip(wedges, values, labels):
        ang = (w.theta1 + w.theta2) / 2
        x, y = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pct = v / total * 100
        ha = 'left' if x >= 0 else 'right'
        lx, ly = x * 1.22, y * 1.22
        ax.plot([x * 1.01, x * 1.14], [y * 1.01, y * 1.14], color=MUTE, linewidth=0.9, zorder=2)
        ax.text(lx, ly, f'{pct:.1f}% {lab}', ha=ha, va='center', fontsize=11.5, fontweight='bold', color=INK)
    ax.set_aspect('equal')
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.35, 1.35)
    return total

# 1. Situação cadastral (donut: Ativos/Em extinção/Extintos)
def fig_situacao():
    d = D['situacao']
    fig, ax = plt.subplots()
    donut_external(ax, d['labels'], d['valores'], [GREEN, GOLD, RED])
    savefig(fig, 'situacao', 4.9, 3.1)

# 2. Avaliação (donut: Sem ciclo x Com ciclo)
def fig_avaliacao():
    d = D['avaliacao']
    fig, ax = plt.subplots()
    donut_external(ax, d['labels'], d['valores'], [RED, GREEN])
    savefig(fig, 'avaliacao', 4.9, 3.1)

# 3. Centro-Oeste x Brasil x Sudeste (bar)
def fig_centro_oeste():
    d = D['centro_oeste']
    labels = d['labels']
    vals = d['valores']
    colors = [GOLD, MUTE, NAVY]
    fig, ax = plt.subplots()
    bars = ax.bar(labels, vals, color=colors, width=0.55, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 4, f'{v:.1f}', ha='center',
                 fontsize=11, fontweight='bold', color=INK)
    ax.set_ylim(0, max(vals) * 1.2)
    ax.set_ylabel('Vagas / 100 mil hab.', fontsize=9, color=MUTE)
    style_ax(ax, grid_axis='y')
    savefig(fig, 'centro_oeste', 4.6, 3.0)

# 4. Cenários 2024-2050 (multi-line)
def fig_cenarios():
    d = D['cenarios']
    anos = d['anos']
    fig, ax = plt.subplots()
    series = [('contido', 'Contido (~3%/ano)', MUTE, ':'),
              ('tendencial', 'Tendencial (~5%/ano)', GOLD, '--'),
              ('expansionista', 'Expansionista (~7%/ano)', NAVY, '-')]
    for key, label, color, ls in series:
        vals = d[key]
        ax.plot(anos, vals, color=color, linewidth=2.3, linestyle=ls, marker='o', markersize=5.5, label=label, zorder=3)
        ax.annotate(f'{vals[-1]:,}'.replace(',', '.'), (anos[-1], vals[-1]), textcoords='offset points',
                     xytext=(6, 2), fontsize=9, fontweight='bold', color=color, ha='left')
    ax.set_xticks(anos)
    ax.set_xlim(anos[0] - 1, anos[-1] + 5)
    style_ax(ax, grid_axis='y')
    ax.legend(loc='upper left', frameon=False, fontsize=9)
    ax.set_ylabel('Vagas anuais projetadas', fontsize=9, color=MUTE)
    savefig(fig, 'cenarios', 6.2, 3.2)

fig_situacao()
fig_avaliacao()
fig_centro_oeste()
fig_cenarios()
print('ALL DONE 2')
