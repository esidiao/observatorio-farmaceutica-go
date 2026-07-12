# -*- coding: utf-8 -*-
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch

D = json.load(open('current_data.json', encoding='utf-8'))

NAVY = '#16304F'
GOLD = '#B8893B'
MUTE = '#5A6675'
INK = '#2A2F36'
LINE = '#D8DDE3'
SOFT = '#F5F7FA'
RED = '#B0413E'
GREEN = '#3F7D5C'
PALETTE = [NAVY, GOLD, '#6E8CA0', '#D9B36C', MUTE]

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'text.color': INK,
    'axes.edgecolor': LINE,
    'axes.labelcolor': INK,
    'xtick.color': MUTE,
    'ytick.color': MUTE,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'savefig.facecolor': 'white',
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

# 1. Modalidade — Presencial vs EaD (donut, external labels)
def fig_modalidade():
    d = D['modalidade_vagas']
    fig, ax = plt.subplots()
    colors = [NAVY, GOLD]
    wedges, _ = ax.pie(d['valores'], colors=colors, startangle=90, counterclock=False,
                        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2))
    total = sum(d['valores'])
    import math
    for w, v, lab in zip(wedges, d['valores'], d['labels']):
        ang = (w.theta1 + w.theta2) / 2
        x, y = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pct = v / total * 100
        ha = 'left' if x >= 0 else 'right'
        lx, ly = x * 1.22, y * 1.22
        ax.plot([x * 1.01, x * 1.14], [y * 1.01, y * 1.14], color=MUTE, linewidth=0.9, zorder=2)
        ax.text(lx, ly, f'{pct:.1f}% {lab}', ha=ha, va='center', fontsize=12,
                 fontweight='bold', color=INK)
    ax.text(0, 0, f'{total:,}'.replace(',', '.') + '\nvagas', ha='center', va='center',
             fontsize=13, fontweight='bold', color=NAVY)
    ax.set_aspect('equal')
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.35, 1.35)
    savefig(fig, 'modalidade', 4.6, 3.1)

# 2. Setor — Privado vs Público (donut, external labels)
def fig_setor():
    d = D['setor']
    fig, ax = plt.subplots()
    colors = [GOLD, '#6E8CA0']
    wedges, _ = ax.pie(d['valores'], colors=colors, startangle=90, counterclock=False,
                        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2))
    total = sum(d['valores'])
    import math
    for w, v, lab in zip(wedges, d['valores'], d['labels']):
        ang = (w.theta1 + w.theta2) / 2
        x, y = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pct = v / total * 100
        ha = 'left' if x >= 0 else 'right'
        lx, ly = x * 1.22, y * 1.22
        ax.plot([x * 1.01, x * 1.14], [y * 1.01, y * 1.14], color=MUTE, linewidth=0.9, zorder=2)
        ax.text(lx, ly, f'{pct:.1f}% {lab}', ha=ha, va='center', fontsize=12,
                 fontweight='bold', color=INK)
    ax.set_aspect('equal')
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.35, 1.35)
    savefig(fig, 'setor', 4.6, 3.1)

# 3. Ranking IES — top 10 horizontal bar
def fig_ranking_ies():
    rk = D['ranking_ies'][:10]
    rk = list(reversed(rk))

    def fit_name(n):
        n = n.title().replace('De ', 'de ').replace('Da ', 'da ').replace('Do ', 'do ')
        if len(n) <= 40:
            return n
        cut = n.rfind(' ', 0, 40)
        return n[:cut] + '…' if cut > 0 else n[:40] + '…'

    names = [fit_name(r['nome']) for r in rk]
    vals = [r['vagas'] for r in rk]
    cats = [r['categoria'] for r in rk]
    colors = [NAVY if 'Priv' in c else GOLD for c in cats]
    fig, ax = plt.subplots()
    bars = ax.barh(names, vals, color=colors, height=0.62, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_width() + max(vals) * 0.015, b.get_y() + b.get_height() / 2, f'{v:,}'.replace(',', '.'),
                 va='center', fontsize=9, color=INK)
    ax.set_xlim(0, max(vals) * 1.14)
    style_ax(ax, grid_axis='x')
    ax.tick_params(axis='y', labelsize=8.8)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=NAVY, label='Privada'), Patch(color=GOLD, label='Pública')],
               loc='lower right', frameon=False, fontsize=8.5)
    savefig(fig, 'ranking_ies', 7.0, 3.6)

# 4. Concentração — Goiânia vs resto do estado (bar) + CR2/CR10 inset-like second panel
def fig_concentracao():
    c = D['concentracao']
    fig, axes = plt.subplots(1, 2)
    ax = axes[0]
    vals = [c['goiania'], 100 - c['goiania']]
    labels = ['Goiânia', 'Demais 74\nmunicípios']
    bars = ax.bar(labels, vals, color=[GOLD, NAVY], width=0.56, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f'{v:.1f}%', ha='center',
                 fontsize=11, fontweight='bold', color=INK)
    ax.set_ylim(0, max(vals) * 1.22)
    style_ax(ax, grid_axis='y')
    ax.set_title('Concentração da oferta\npresencial', fontsize=9.5, color=MUTE, loc='left')

    ax2 = axes[1]
    labels2 = ['CR2', 'CR10']
    vals2 = [c['cr2'], c['cr10']]
    bars2 = ax2.bar(labels2, vals2, color=[NAVY, '#6E8CA0'], width=0.5, zorder=3)
    for b, v in zip(bars2, vals2):
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f'{v:.1f}%', ha='center',
                  fontsize=11, fontweight='bold', color=INK)
    ax2.set_ylim(0, 100)
    style_ax(ax2, grid_axis='y')
    ax2.set_title('Razão de concentração\n(% das vagas nas N maiores IES)', fontsize=9.5, color=MUTE, loc='left')
    savefig(fig, 'concentracao', 6.5, 2.9)

# 5. Qualidade GO vs BR (grouped bar)
def fig_qualidade():
    q = D['qualidade']
    labels = q['labels']
    go = q['go']
    br = q['br']
    import numpy as np
    x = np.arange(len(labels))
    w = 0.34
    fig, ax = plt.subplots()
    b1 = ax.bar(x - w / 2, go, w, label='Goiás', color=GOLD, zorder=3)
    b2 = ax.bar(x + w / 2, br, w, label='Brasil', color=NAVY, zorder=3)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05, f'{b.get_height():.2f}',
                     ha='center', fontsize=9, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9.5)
    ax.set_ylim(0, max(go + br) * 1.25)
    style_ax(ax, grid_axis='y')
    ax.legend(loc='upper right', frameon=False, fontsize=9.5)
    savefig(fig, 'qualidade', 6.0, 3.1)

# 6. Docente + Infraestrutura (2 panels)
def fig_docente_infra():
    doc = D['docente']
    infra = D['infraestrutura']
    fig, axes = plt.subplots(1, 2)
    ax = axes[0]
    labels = [l.replace('Regime integral/parcial', 'Regime\nintegral/parcial') for l in doc['labels']]
    vals = doc['valores']
    bars = ax.barh(labels, vals, color=NAVY, height=0.5, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_width() + 1.5, b.get_y() + b.get_height() / 2, f'{v:.1f}%', va='center', fontsize=9)
    ax.set_xlim(0, 108)
    style_ax(ax, grid_axis='x')
    ax.set_title('Corpo docente (% dos cursos avaliados)', fontsize=9.3, color=MUTE, loc='left')

    ax2 = axes[1]
    labels2 = [l.replace('Organização didático-pedagógica', 'Organização\ndidático-pedagógica')
                 .replace('Infraestrutura física', 'Infraestrutura\nfísica')
                 .replace('Oportunidade de ampliação', 'Oportunidade de\nampliação de formação')
               for l in infra['labels']]
    vals2 = infra['valores']
    bars2 = ax2.barh(labels2, vals2, color=GOLD, height=0.5, zorder=3)
    for b, v in zip(bars2, vals2):
        ax2.text(b.get_width() + 0.06, b.get_y() + b.get_height() / 2, f'{v:.2f}', va='center', fontsize=9)
    ax2.set_xlim(0, 6.6)
    style_ax(ax2, grid_axis='x')
    ax2.set_title('Infraestrutura — dimensões do CPC (escala 1–6)', fontsize=9.3, color=MUTE, loc='left')
    savefig(fig, 'docente_infra', 6.6, 2.7)

# 7. Perfil discente (bar)
def fig_perfil_discente():
    p = D['perfil_discente']
    labels = [l.replace('Negros/pardos/indígenas', 'Negros, pardos\nou indígenas')
                .replace('Financiamento (FIES/PROUNI)', 'Financiamento\n(FIES/PROUNI)') for l in p['labels']]
    vals = p['valores']
    fig, ax = plt.subplots()
    bars = ax.bar(labels, vals, color=[NAVY, GOLD, '#6E8CA0', '#D9B36C'], width=0.56, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f'{v:.1f}%', ha='center',
                 fontsize=10.5, fontweight='bold', color=INK)
    ax.set_ylim(0, 100)
    style_ax(ax, grid_axis='y')
    ax.tick_params(axis='x', labelsize=9)
    savefig(fig, 'perfil_discente', 6.3, 2.9)

# 8. Série histórica (line, with projection segment dashed)
def fig_serie():
    s = D['serie']
    anos = s['anos']
    vals = s['inscritos']
    tipos = s['tipos']
    fig, ax = plt.subplots()
    obs_x = [a for a, t in zip(anos, tipos) if t == 'observado']
    obs_y = [v for v, t in zip(vals, tipos) if t == 'observado']
    ax.plot(obs_x, obs_y, color=NAVY, marker='o', markersize=7, linewidth=2.4, zorder=3, label='Observado')
    proj_x = anos[len(obs_x) - 1:]
    proj_y = vals[len(obs_x) - 1:]
    ax.plot(proj_x, proj_y, color=GOLD, marker='o', markersize=7, linewidth=2.4, linestyle='--', zorder=3, label='Projeção (~7,5%/ano)')
    for a, v in zip(anos, vals):
        ax.annotate(f'{v:,}'.replace(',', '.'), (a, v), textcoords='offset points', xytext=(0, 10),
                     ha='center', fontsize=10, fontweight='bold', color=INK)
    ax.set_xticks(anos)
    ax.set_xlim(anos[0] - 0.6, anos[-1] + 0.6)
    ax.set_ylim(0, max(vals) * 1.2)
    style_ax(ax, grid_axis='y')
    ax.legend(loc='upper left', frameon=False, fontsize=9.5)
    ax.set_ylabel('Inscritos no CRF-GO', fontsize=9.5, color=MUTE)
    savefig(fig, 'serie', 6.0, 3.0)

# 9. Regiões de saúde — top regiões por vagas (bar), destacando zero-oferta
def fig_regioes_saude():
    rs = D['regioes_saude']['por_regiao']
    items = sorted(rs.items(), key=lambda kv: kv[1]['vagas'], reverse=True)
    names = [k for k, v in items]
    vals = [v['vagas'] for k, v in items]
    colors = [GOLD if v > 0 else '#C9CFD6' for v in vals]
    fig, ax = plt.subplots()
    bars = ax.barh(list(reversed(names)), list(reversed(vals)), color=list(reversed(colors)), height=0.62, zorder=3)
    for b, v in zip(bars, reversed(vals)):
        lab = f'{v:,}'.replace(',', '.') if v > 0 else 'sem oferta'
        ax.text(b.get_width() + max(vals) * 0.012, b.get_y() + b.get_height() / 2, lab,
                 va='center', fontsize=8, color=INK if v > 0 else MUTE)
    ax.set_xlim(0, max(vals) * 1.16)
    style_ax(ax, grid_axis='x')
    ax.tick_params(axis='y', labelsize=8.3)
    savefig(fig, 'regioes_saude', 6.5, 4.6)

# 10. Densidade UF — 27 UFs ranked, GO destacado
def fig_densidade_uf():
    d = D['densidade_uf']
    labels = d['labels']
    vals = d['valores']
    colors = [GOLD if l == 'GO' else NAVY for l in labels]
    fig, ax = plt.subplots()
    bars = ax.bar(labels, vals, color=colors, width=0.66, zorder=3)
    ax.axhline(d['media'], color=MUTE, linewidth=1.1, linestyle='--', zorder=2)
    ax.text(len(labels) - 1, d['media'] + 6, f"Média BR: {d['media']:.1f}", ha='right', fontsize=8.5, color=MUTE)
    style_ax(ax, grid_axis='y')
    ax.tick_params(axis='x', labelsize=7.6, rotation=0)
    ax.set_ylabel('Vagas / 100 mil hab.', fontsize=9, color=MUTE)
    savefig(fig, 'densidade_uf', 6.6, 2.9)

fig_modalidade()
fig_setor()
fig_ranking_ies()
fig_concentracao()
fig_qualidade()
fig_docente_infra()
fig_perfil_discente()
fig_serie()
fig_regioes_saude()
fig_densidade_uf()
print('ALL DONE')
