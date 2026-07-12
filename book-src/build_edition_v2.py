# -*- coding: utf-8 -*-
from reportlab.lib.units import mm, cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
                                 KeepTogether, Image, HRFlowable, Flowable)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

import book_content
import book_content_part2  # noqa: F401 (appends to book_content.B on import)
from logo_reportlab import draw_logo

FONTS_DIR = r'C:\Windows\Fonts'
pdfmetrics.registerFont(TTFont('Georgia', FONTS_DIR + r'\georgia.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Bold', FONTS_DIR + r'\georgiab.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Italic', FONTS_DIR + r'\georgiai.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-BoldItalic', FONTS_DIR + r'\georgiaz.ttf'))
pdfmetrics.registerFontFamily('Georgia', normal='Georgia', bold='Georgia-Bold',
                               italic='Georgia-Italic', boldItalic='Georgia-BoldItalic')

NAVY = colors.HexColor('#16304F')
GOLD = colors.HexColor('#B8893B')
MUTE = colors.HexColor('#5A6675')
INK = colors.HexColor('#2A2F36')
LINE = colors.HexColor('#CCCCCC')
SOFT = colors.HexColor('#F5F7FA')

PAGE = (17 * cm, 24 * cm)
LM = RM = 18 * mm
TM = 20 * mm
BM = 18 * mm
CONTENT_W = PAGE[0] - LM - RM
CONTENT_W_MM = CONTENT_W / mm

BOOK_TITLE_SHORT = 'Formação Farmacêutica em Goiás'

styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitlePage', fontName='Helvetica-Bold', fontSize=22, leading=27, textColor=NAVY, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('SubtitlePage', fontName='Helvetica-Oblique', fontSize=12.5, leading=17, textColor=MUTE, alignment=TA_CENTER)
author_style = ParagraphStyle('AuthorPage', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=INK, alignment=TA_CENTER)
meta_style = ParagraphStyle('MetaPage', fontName='Helvetica', fontSize=9.5, leading=13, textColor=MUTE, alignment=TA_CENTER)
part_title_style = ParagraphStyle('PartTitle', fontName='Helvetica-Bold', fontSize=17, leading=21, textColor=NAVY, alignment=TA_CENTER, spaceAfter=10)
part_toc_style = ParagraphStyle('PartTOC', parent=part_title_style, fontSize=17, alignment=TA_CENTER)
part_desc_style = ParagraphStyle('PartDesc', fontName='Helvetica-Oblique', fontSize=10, leading=14, textColor=MUTE, alignment=TA_CENTER, spaceAfter=6)
chap_num_style = ParagraphStyle('ChapNum', fontName='Helvetica-Bold', fontSize=10.5, textColor=GOLD, spaceBefore=4, spaceAfter=2)
chap_title_style = ParagraphStyle('ChapTitle', fontName='Helvetica-Bold', fontSize=15.5, leading=19, textColor=NAVY, spaceBefore=2, spaceAfter=4)
chap_toc_style = ParagraphStyle('ChapTOC', parent=chap_title_style, fontSize=15.5)
h2_style = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=13, spaceAfter=6)
body_style = ParagraphStyle('Body', fontName='Georgia', fontSize=9.3, leading=14.2, textColor=INK, spaceAfter=7, alignment=4, firstLineIndent=10)
bullet_style = ParagraphStyle('Bullet', parent=body_style, leftIndent=14, firstLineIndent=0, spaceAfter=6)
tabletitle_style = ParagraphStyle('TableTitle', fontName='Helvetica-Bold', fontSize=9.5, textColor=NAVY, spaceBefore=9, spaceAfter=5)
tabletitle_toc_style = ParagraphStyle('FigTOC', parent=tabletitle_style, fontSize=9.5)
note_style = ParagraphStyle('Note', fontName='Helvetica-Oblique', fontSize=7.3, leading=9.6, textColor=MUTE, spaceBefore=4, spaceAfter=8)
cell_style = ParagraphStyle('Cell', fontName='Helvetica', fontSize=7.2, leading=9.1, textColor=INK)
cell_head_style = ParagraphStyle('CellHead', parent=cell_style, fontName='Helvetica-Bold', textColor=colors.white)
quote_style = ParagraphStyle('Quote', fontName='Georgia-Italic', fontSize=9.6, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=11, leftIndent=15, rightIndent=15)
caption_style = ParagraphStyle('Caption', fontName='Helvetica-Oblique', fontSize=7.9, leading=10.2, textColor=MUTE, alignment=TA_CENTER, spaceBefore=5, spaceAfter=12)
label_style = ParagraphStyle('Label', fontName='Helvetica-Bold', fontSize=9, leading=13, textColor=NAVY)
ficha_style = ParagraphStyle('Ficha', fontName='Helvetica', fontSize=8.6, leading=13, textColor=INK)
ficha_pending_style = ParagraphStyle('FichaPending', parent=ficha_style, fontName='Helvetica-Oblique', textColor=GOLD)
ref_style = ParagraphStyle('Ref', fontName='Helvetica', fontSize=8.4, leading=12.5, textColor=INK, spaceAfter=7, leftIndent=12, firstLineIndent=-12)

story = []


class Bookmark(Flowable):
    def __init__(self, title, key, level=0):
        Flowable.__init__(self)
        self.title, self.key, self.level = title, key, level

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, self.level, False)


class FigureIndex(TableOfContents):
    def notify(self, kind, stuff):
        if kind == 'FigEntry':
            self.addEntry(*stuff)


def add_figure(path, caption, width_mm):
    w_mm = min(width_mm, CONTENT_W_MM)
    w_pt = w_mm * mm
    with PILImage.open(path) as im:
        iw, ih = im.size
    h_pt = w_pt * (ih / iw)
    img = Image(path, width=w_pt, height=h_pt)
    img.hAlign = 'CENTER'
    story.append(Spacer(1, 6))
    story.append(KeepTogether([img, Paragraph(caption, caption_style)]))


def add_table(title, rows, note, ncols_first_pct=0.32):
    if title:
        story.append(Paragraph(title, tabletitle_style))
    header = rows[0]
    data = [[Paragraph(f'<b>{h}</b>', cell_head_style) for h in header]]
    for r in rows[1:]:
        data.append([Paragraph(c, cell_style) for c in r])
    ncols = len(header)
    first_w = CONTENT_W * ncols_first_pct
    rest_w = (CONTENT_W - first_w) / (ncols - 1)
    col_widths = [first_w] + [rest_w] * (ncols - 1)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, SOFT]),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    if note:
        story.append(Paragraph(note, note_style))


def add_stat4(items):
    cells = []
    for i in range(0, len(items), 2):
        n, l = items[i], items[i + 1]
        html = f'<para alignment="center"><font name="Helvetica-Bold" size="15" color="#B8893B">{n}</font><br/><font name="Helvetica" size="7.6" color="#FFFFFF">{l}</font></para>'
        cells.append(Paragraph(html, styles['Normal']))
    ncols = len(cells)
    t = Table([cells], colWidths=[CONTENT_W / ncols] * ncols)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAVY), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('TOPPADDING', (0, 0), (-1, -1), 11), ('BOTTOMPADDING', (0, 0), (-1, -1), 11)]))
    story.append(Spacer(1, 4)); story.append(t); story.append(Spacer(1, 8))


# ============================================================ 1. FOLHA DE ROSTO
story.append(Bookmark('Folha de rosto', 'bm-rosto', 0))
story.append(Spacer(1, 42 * mm))
story.append(Paragraph('FORMAÇÃO FARMACÊUTICA EM GOIÁS', title_style))
story.append(Spacer(1, 6))
story.append(Paragraph('Diagnóstico situacional, evidências e proposições<br/>para a nova Diretriz Curricular Nacional', subtitle_style))
story.append(Spacer(1, 22 * mm))
story.append(Paragraph('Farm. Dr. Edson Sidião de Souza Júnior', author_style))
story.append(Paragraph('Grupo Técnico de Ensino — Conselho Regional de Farmácia do Estado de Goiás (CRF-GO)', meta_style))
story.append(Spacer(1, 30 * mm))
story.append(Paragraph('Edição revisada · Censo da Educação Superior 2024', meta_style))
story.append(Paragraph('Goiânia, Goiás — 2026', meta_style))
story.append(PageBreak())

# ============================================================ 2. VERSO / DIREITOS AUTORAIS
story.append(Bookmark('Direitos autorais', 'bm-direitos', 0))
story.append(Spacer(1, 60 * mm))
story.append(Paragraph('© 2026 Edson Sidião de Souza Júnior.', ficha_style))
story.append(Paragraph('Todos os direitos reservados.', ficha_style))
story.append(Spacer(1, 8))
story.append(Paragraph('Dados primários de fontes oficiais públicas (INEP, IBGE, e-MEC, SES-GO e demais fontes citadas nas referências). O tratamento estatístico, os índices próprios, as interpretações e as proposições contidas nesta obra são produção autoral original.', ficha_style))
story.append(Spacer(1, 8))
story.append(Paragraph('Permitida a reprodução para fins educacionais e de pesquisa, mediante citação da fonte. Vedado o uso comercial sem autorização expressa do autor e do CRF-GO.', ficha_style))
story.append(Spacer(1, 10))
story.append(Paragraph('Forma recomendada de citação:', label_style))
story.append(Paragraph('SOUZA JÚNIOR, Edson Sidião de. <i>Formação Farmacêutica em Goiás: diagnóstico situacional, evidências e proposições para a nova Diretriz Curricular Nacional</i>. Goiânia: CRF-GO, 2026.', ficha_style))
story.append(PageBreak())

# ============================================================ 3. FICHA CATALOGRÁFICA
story.append(Bookmark('Ficha catalográfica', 'bm-ficha', 0))
story.append(Paragraph('FICHA CATALOGRÁFICA', chap_title_style))
story.append(HRFlowable(width='100%', thickness=0.8, color=LINE, spaceAfter=10))
ficha_rows = [
    ('Autor', 'Souza Júnior, Edson Sidião de'),
    ('Título', 'Formação Farmacêutica em Goiás : diagnóstico situacional, evidências e proposições para a nova Diretriz Curricular Nacional'),
    ('Edição', 'Edição revisada (base Censo da Educação Superior 2024)'),
    ('Local', 'Goiânia, GO'),
    ('Editora/Instituição', 'Conselho Regional de Farmácia do Estado de Goiás (CRF-GO)'),
    ('Ano', '2026'),
    ('Páginas', '[a confirmar na versão final diagramada]'),
    ('Formato', '17 × 24 cm ; PDF digital'),
    ('ISBN', '[ISBN a ser solicitado junto à Agência Brasileira do ISBN]'),
    ('Assuntos', 'Educação farmacêutica — Goiás. 2. Ensino superior — avaliação. 3. Política educacional — saúde. [a validar por bibliotecário]'),
    ('CDD', '[a validar por bibliotecário habilitado]'),
    ('CDU', '[a validar por bibliotecário habilitado]'),
    ('Bibliotecário responsável', '[nome e nº de registro a incluir]'),
]
_data = [[Paragraph(f'<b>{k}</b>', ficha_style), Paragraph(v, ficha_pending_style if v.strip().startswith('[') else ficha_style)] for k, v in ficha_rows]
_t = Table(_data, colWidths=[38 * mm, CONTENT_W - 38 * mm])
_t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                         ('LINEBELOW', (0, 0), (-1, -1), 0.3, LINE)]))
story.append(_t)
story.append(Spacer(1, 10))
story.append(Paragraph('Campos em itálico dourado aguardam validação de bibliotecário(a) habilitado(a) antes da publicação final. Nenhum dado catalográfico foi presumido ou inventado nesta reedição.', note_style))
story.append(PageBreak())

# ============================================================ 4. EXPEDIENTE
story.append(Bookmark('Expediente', 'bm-expediente', 0))
story.append(Paragraph('EXPEDIENTE', chap_title_style))
story.append(HRFlowable(width='100%', thickness=0.8, color=LINE, spaceAfter=10))
exp_rows = [
    ('Instituição', 'Conselho Regional de Farmácia do Estado de Goiás — CRF-GO'),
    ('Grupo responsável', 'Grupo Técnico de Ensino (GT de Ensino)'),
    ('Autoria', 'Farm. Dr. Edson Sidião de Souza Júnior'),
    ('Presidência do CRF-GO', 'Luciana Calil'),
    ('Coordenação editorial', 'Farm. Dr. Edson Sidião de Souza Júnior (pelo próprio autor)'),
    ('Revisão técnica', '[a designar]'),
    ('Revisão linguística', '[a designar]'),
    ('Projeto gráfico e diagramação', 'Reedição editorial 2026'),
    ('Produção de gráficos, mapas e infográficos', 'Elaboração própria a partir das fontes citadas'),
    ('Fontes de dados', 'INEP, IBGE, e-MEC, SES-GO, CFF, CRF-GO e Observatório Nacional da Formação Farmacêutica (ver Referências)'),
    ('Contato do autor', '(62) 99804-4822 · sidiao@i9educar.com'),
]
_data = [[Paragraph(f'<b>{k}</b>', ficha_style), Paragraph(v, ficha_pending_style if v.strip().startswith('[') else ficha_style)] for k, v in exp_rows]
_t = Table(_data, colWidths=[48 * mm, CONTENT_W - 48 * mm])
_t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                         ('LINEBELOW', (0, 0), (-1, -1), 0.3, LINE)]))
story.append(_t)
story.append(Spacer(1, 8))
story.append(Paragraph('Campos em itálico dourado identificam informações não presentes no arquivo original e que dependem de confirmação do CRF-GO antes da publicação.', note_style))
story.append(PageBreak())

# ============================================================ 5. SUMÁRIO (real page numbers via multiBuild)
story.append(Bookmark('Sumário', 'bm-sumario', 0))
story.append(Paragraph('SUMÁRIO', chap_title_style))
story.append(HRFlowable(width='100%', thickness=0.8, color=LINE, spaceAfter=8))
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle('TOCPart', fontName='Helvetica-Bold', fontSize=10, leading=16, textColor=NAVY, spaceBefore=10),
    ParagraphStyle('TOCChap', fontName='Helvetica', fontSize=9.2, leading=14.5, textColor=INK, leftIndent=10),
]
story.append(toc)
story.append(PageBreak())

# ============================================================ 6. LISTA DE FIGURAS, GRÁFICOS, MAPAS E TABELAS
story.append(Bookmark('Lista de figuras, gráficos, mapas e tabelas', 'bm-listas', 0))
story.append(Paragraph('LISTA DE FIGURAS, GRÁFICOS, MAPAS E TABELAS', chap_title_style))
story.append(HRFlowable(width='100%', thickness=0.8, color=LINE, spaceAfter=8))
figtoc = FigureIndex()
figtoc.levelStyles = [ParagraphStyle('FigTOCEntry', fontName='Helvetica', fontSize=8.8, leading=13.5, textColor=INK)]
story.append(figtoc)
story.append(PageBreak())

# ============================================================ 7. LISTA DE SIGLAS E ABREVIATURAS
story.append(Bookmark('Lista de siglas e abreviaturas', 'bm-siglas', 0))
story.append(Paragraph('LISTA DE SIGLAS E ABREVIATURAS', chap_title_style))
story.append(HRFlowable(width='100%', thickness=0.8, color=LINE, spaceAfter=8))
siglas = [
    ('CRF-GO', 'Conselho Regional de Farmácia do Estado de Goiás'),
    ('CFF', 'Conselho Federal de Farmácia'),
    ('INEP', 'Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira'),
    ('e-MEC', 'Sistema Eletrônico de Acompanhamento de Processos (Ministério da Educação)'),
    ('ENADE', 'Exame Nacional de Desempenho dos Estudantes'),
    ('CPC', 'Conceito Preliminar de Curso'),
    ('CC', 'Conceito de Curso'),
    ('IDD', 'Indicador de Diferença entre os Desempenhos Observado e Esperado'),
    ('IES', 'Instituição de Ensino Superior'),
    ('EaD', 'Educação a Distância'),
    ('SES-GO', 'Secretaria de Estado da Saúde de Goiás'),
    ('SUS', 'Sistema Único de Saúde'),
    ('IBGE', 'Instituto Brasileiro de Geografia e Estatística'),
    ('DCN', 'Diretriz Curricular Nacional'),
    ('HHI', 'Índice Herfindahl-Hirschman'),
    ('CR2 / CR10', 'Razão de Concentração das 2 / 10 maiores IES'),
    ('SII', 'Sistema Integrado de Índices (Observatório)'),
]
for sig, ext in siglas:
    story.append(Paragraph(f'<b>{sig}</b> — {ext}', ref_style))
story.append(PageBreak())

# ============================================================ 8. CORPO DA OBRA (real content)
first_chap = True
for block in book_content.B:
    kind = block[0]
    if kind == 'part':
        _, ptitle, pdesc = block
        story.append(PageBreak())
        story.append(Bookmark(ptitle, 'bm-part-%d' % len(story), 0))
        story.append(Spacer(1, 38 * mm))
        story.append(Paragraph(ptitle, part_toc_style))
        story.append(Paragraph(pdesc, part_desc_style))
        first_chap = True
    elif kind == 'chap':
        _, num, ctitle = block
        if not first_chap:
            story.append(PageBreak())
        first_chap = False
        full_title = (f'{num} — {ctitle}' if num else ctitle)
        story.append(Bookmark(full_title, 'bm-chap-%d' % len(story), 1))
        if num:
            story.append(Paragraph(num, chap_num_style))
        story.append(Paragraph(ctitle, chap_toc_style))
        story.append(HRFlowable(width='18%', thickness=1.6, color=GOLD, spaceAfter=11, hAlign='LEFT'))
    elif kind == 'h2':
        story.append(Paragraph(block[1], h2_style))
    elif kind == 'p':
        story.append(Paragraph(block[1], body_style))
    elif kind == 'li':
        story.append(Paragraph('&#8226;&nbsp; ' + block[1], bullet_style))
    elif kind == 'quote':
        story.append(Paragraph(block[1], quote_style))
    elif kind == 'stat4':
        add_stat4(block[1])
    elif kind == 'table':
        _, ttitle, rows, note = block
        add_table(ttitle, rows, note)
    elif kind == 'figure':
        _, path, caption, width_mm = block
        add_figure(path, caption, width_mm)

# ============================================================ 9. COLOFÃO
story.append(PageBreak())
story.append(Bookmark('Colofão', 'bm-colofao', 0))
story.append(Spacer(1, 70 * mm))
colofao_style = ParagraphStyle('Colofao', fontName='Helvetica', fontSize=8.6, leading=13.5, textColor=MUTE, alignment=TA_CENTER)
story.append(Paragraph('Esta edição foi produzida em formato 17 × 24 cm,<br/>tipografia Georgia (corpo) e Helvetica (títulos e tabelas),<br/>a partir de dados do Censo da Educação Superior 2024/INEP<br/>e do Observatório Nacional da Formação Farmacêutica.', colofao_style))
story.append(Spacer(1, 10))
story.append(Paragraph('Goiânia, GO — 2026', colofao_style))


# ============================================================ DOC TEMPLATE (TOC-aware, odd/even headers)
class EditionDocTemplate(SimpleDocTemplate):
    current_part_title = ''
    current_chap_title = ''

    def build(self, flowables, **kwargs):
        # multiBuild() calls build() once per pass; these are plain instance
        # attributes (not tracked by BaseDocTemplate._reset()), so without
        # resetting them here a later pass' early pages would still show the
        # previous pass' final chapter title in the running header.
        self.current_part_title = ''
        self.current_chap_title = ''
        # onPage fires at the START of each page, before that page's own
        # flowables (incl. its chapter-title paragraph) are drawn, so live
        # current_chap_title is always one page stale on a chapter's opening
        # page. Fix: read the PREVIOUS pass' finished TOC entries and
        # forward-fill a page->title map keyed by the entry's own page.
        # multiBuild() calls toc.beforeBuild() (which moves _entries into
        # _lastEntries and clears _entries) BEFORE calling this build(), so
        # _lastEntries -- not _entries -- holds the previous pass' data here.
        self._chap_by_page = {}
        entries = sorted(getattr(toc, '_lastEntries', []), key=lambda e: e[2])
        if entries:
            cur_part = cur_chap = ''
            idx = 0
            max_page = max(e[2] for e in entries) + 3
            for pg in range(1, max_page + 1):
                while idx < len(entries) and entries[idx][2] <= pg:
                    lvl, text = entries[idx][0], entries[idx][1]
                    if lvl == 0:
                        cur_part = text
                    else:
                        cur_chap = text
                    idx += 1
                self._chap_by_page[pg] = cur_chap or cur_part
        SimpleDocTemplate.build(self, flowables, **kwargs)

    def afterFlowable(self, flowable):
        style_name = getattr(getattr(flowable, 'style', None), 'name', None)
        if style_name == 'PartTOC':
            text = flowable.getPlainText()
            self.current_part_title = text
            self.notify('TOCEntry', (0, text, self.page))
        elif style_name == 'ChapTOC':
            text = flowable.getPlainText()
            self.current_chap_title = text
            self.notify('TOCEntry', (1, text, self.page))
        elif style_name in ('TableTitle', 'Caption'):
            text = flowable.getPlainText() if hasattr(flowable, 'getPlainText') else ''
            if text:
                self.notify('FigEntry', (0, text, self.page))


def header_footer(canvas, doc):
    canvas.saveState()
    draw_logo(canvas, LM, PAGE[1] - 15.5 * mm, badge_h=11, light=False, wordmark=True)
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(MUTE)
    page_no = canvas.getPageNumber()
    is_even = page_no % 2 == 0
    chap_for_page = getattr(doc, '_chap_by_page', {}).get(page_no, '')
    right_text = BOOK_TITLE_SHORT if is_even else (chap_for_page or BOOK_TITLE_SHORT)
    canvas.drawRightString(PAGE[0] - RM, PAGE[1] - 12 * mm, right_text)
    canvas.drawCentredString(PAGE[0] / 2, 11 * mm, str(page_no))
    canvas.restoreState()


doc = EditionDocTemplate('edition_body_17x24.pdf', pagesize=PAGE,
                          leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                          title='Formação Farmacêutica em Goiás — Edição Revisada',
                          author='Edson Sidião de Souza Júnior',
                          subject='Formação farmacêutica em Goiás — diagnóstico situacional, evidências e proposições',
                          creator='CRF-GO / GT de Ensino')
doc.multiBuild(story, onFirstPage=header_footer, onLaterPages=header_footer)
print('wrote edition_body_17x24.pdf')
