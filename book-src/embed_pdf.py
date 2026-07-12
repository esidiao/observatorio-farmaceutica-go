# -*- coding: utf-8 -*-
import base64

html_path = r'C:\Users\User\OneDrive\Área de Trabalho\CRF-GO_Observatorio_Formacao_Farmaceutica_GO.html'
pdf_path = 'CRF-GO_Livro_Formacao_Farmaceutica_GO_atualizado.pdf'

html = open(html_path, encoding='utf-8').read()
pdf_bytes = open(pdf_path, 'rb').read()
b64 = base64.b64encode(pdf_bytes).decode('ascii')

marker = 'window.PDF_B64="'
i = html.index(marker) + len(marker)
j = html.index('"', i)
old_len = j - i
print('old base64 length:', old_len, '-> new:', len(b64))

new_html = html[:i] + b64 + html[j:]
open(html_path, 'w', encoding='utf-8').write(new_html)
print('done. new html size:', len(new_html))
