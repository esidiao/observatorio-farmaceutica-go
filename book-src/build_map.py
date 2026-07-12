# -*- coding: utf-8 -*-
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.collections import PatchCollection

NAVY = '#16304F'
GOLD = '#B8893B'
MUTE = '#5A6675'
INK = '#2A2F36'
DESERT = '#D7DCE2'
CAPITAL = '#B0413E'

geo = json.load(open('go_geo.json', encoding='utf-8'))
D = json.load(open('current_data.json', encoding='utf-8'))
mun = D['municipios_detalhe']

def polys_from_geom(geom):
    t = geom['type']
    if t == 'Polygon':
        return [geom['coordinates'][0]]
    elif t == 'MultiPolygon':
        return [poly[0] for poly in geom['coordinates']]
    return []

fig, ax = plt.subplots(figsize=(6.4, 6.9))
patches_desert = []
patches_oferta = []
vagas_max = max((v['vagas'] for v in mun.values()), default=1) or 1

patches_ativo_sem_vaga = []
for feat in geo['features']:
    code = str(feat['properties']['id'])
    rings = polys_from_geom(feat['geometry'])
    info = mun.get(code)
    for ring in rings:
        xy = [(pt[0], pt[1]) for pt in ring]
        p = MplPolygon(xy, closed=True)
        if info is None:
            patches_desert.append(p)
        elif info.get('vagas', 0) > 0:
            patches_oferta.append((p, info['vagas']))
        else:
            patches_ativo_sem_vaga.append(p)

# desert municipalities (flat color)
pc_desert = PatchCollection(patches_desert, facecolor=DESERT, edgecolor='white', linewidth=0.35, zorder=1)
ax.add_collection(pc_desert)

# municipalities with active course/matrícula but no NEW vaga authorized this cycle
ATIVO_SEM_VAGA = '#B7C4A8'
pc_ativo = PatchCollection(patches_ativo_sem_vaga, facecolor=ATIVO_SEM_VAGA, edgecolor='white', linewidth=0.35, zorder=1.5)
ax.add_collection(pc_ativo)

# municipalities with oferta, shaded by discrete vagas bins (clearer than a continuous ramp)
BIN_COLORS = ['#E9CE9C', '#D3A94F', GOLD, '#8C6420', NAVY]

def bin_color(v):
    if v >= 1000:
        return NAVY
    if v >= 400:
        return '#8C6420'
    if v >= 150:
        return GOLD
    if v >= 40:
        return '#D3A94F'
    return '#E9CE9C'

polys = [p for p, v in patches_oferta]
vals = [v for p, v in patches_oferta]
colors_list = [bin_color(v) for v in vals]
pc_oferta = PatchCollection(polys, facecolor=colors_list, edgecolor='white', linewidth=0.4, zorder=2)
ax.add_collection(pc_oferta)

ax.autoscale_view()
ax.set_aspect('equal')
ax.axis('off')

# legend
from matplotlib.patches import Patch as LegPatch
legend_elems = [
    LegPatch(facecolor=DESERT, edgecolor='white', label='Sem oferta (deserto formativo) — 171 municípios'),
    LegPatch(facecolor=ATIVO_SEM_VAGA, edgecolor='white', label='Curso/matrícula ativa, sem vaga nova no ciclo'),
    LegPatch(facecolor='#E9CE9C', edgecolor='white', label='1–39 vagas'),
    LegPatch(facecolor='#D3A94F', edgecolor='white', label='40–149 vagas'),
    LegPatch(facecolor=GOLD, edgecolor='white', label='150–399 vagas'),
    LegPatch(facecolor='#8C6420', edgecolor='white', label='400–999 vagas'),
    LegPatch(facecolor=NAVY, edgecolor='white', label='1.000+ vagas (Goiânia)'),
]
ax.legend(handles=legend_elems, loc='upper left', frameon=False, fontsize=8.0, labelcolor=INK, title='Vagas autorizadas por município', title_fontsize=8.6)

fig.tight_layout(pad=0.3)
fig.savefig('fig_mapa_oferta.png', dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close(fig)
print('wrote fig_mapa_oferta.png')
