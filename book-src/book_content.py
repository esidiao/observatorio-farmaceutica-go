# -*- coding: utf-8 -*-
"""Structured content for the revised book (pages 2-N), Censo INEP 2024 basis.
Block types: part, chap, h2, p, li, table(+title+note), stat4, hr
"""

B = []

def PART(title, desc):
    B.append(('part', title, desc))

def CHAP(num, title):
    B.append(('chap', num, title))

def H2(t):
    B.append(('h2', t))

def P(t):
    B.append(('p', t))

def LI(t):
    B.append(('li', t))

def STAT4(items):
    B.append(('stat4', items))

def TABLE(title, rows, note=None):
    B.append(('table', title, rows, note))

def QUOTE(t):
    B.append(('quote', t))

def FIGURE(path, caption, width_mm=140):
    B.append(('figure', path, caption, width_mm))

# ================= FICHA TÉCNICA =================
CHAP(None, 'Ficha técnica')
P('Título: Formação Farmacêutica em Goiás — diagnóstico situacional, evidências e proposições para a nova DCN.')
P('Autoria institucional: Grupo Técnico de Ensino do Conselho Regional de Farmácia do Estado de Goiás (CRF-GO).')
P('Autor: Farmacêutico Dr. Edson Sidião de Souza Júnior — GT de Ensino do CRF-GO.')
P('Natureza: estudo técnico-científico de base documental e quantitativa, com auditoria metodológica integrada.')
P('Base de dados primária (edição revisada, 09/07/2026): Censo da Educação Superior 2024 e microdados ENADE/CPC 2023 (INEP/MEC), consolidados pelo Observatório Nacional da Formação Farmacêutica — extração de 27/06/2026: 67 instituições de ensino superior (IES) com curso de Farmácia em Goiás e 1.281 IES no Brasil.')
P('Fontes secundárias: e-MEC (situação cadastral e recorte setorial, jun/2026), IBGE, INEP, IPEA, CFF, CRF-GO, SES-GO/CIB-GO, ANS, Ministério da Saúde, SBVC/Cognatis, FIP, ACPE/AACP e literatura indexada.')
P('Princípio metodológico: nenhum dado foi fabricado. Distinguem-se, em todo o texto, fato observado, estimativa, projeção e recomendação. Lacunas são assinaladas com o método de obtenção.')
P('Cidade / ano: Goiânia, Goiás — 2026. Edição original fechada em 25/06/2026 (base e-MEC); revisão de 09/07/2026 substitui a base primária pelo Censo da Educação Superior 2024, unificando a metodologia com a leitura interestadual do Observatório Nacional da Formação Farmacêutica.')
QUOTE('"Sob o novo marco, a Farmácia deixa de admitir oferta integralmente a distância. A questão não é a modalidade em si, mas assegurar qualidade prática verificável, núcleo clínico forte e compromisso com o SUS — no presencial e no semipresencial."')

# ================= SUMÁRIO EXECUTIVO =================
CHAP(None, 'Sumário executivo')
P('Este resumo reúne, em duas páginas, os números e as conclusões essenciais do estudo, para leitura prévia por gestores e participantes do XII ENCCF.')
P('Goiás dispõe de uma oferta expressiva de cursos de farmácia, concentrada na capital e majoritariamente privada, mas — ao contrário do que uma leitura administrativa isolada sugeria — de predominância presencial. A comparação com o Brasil, agora construída sobre a mesma base do Censo da Educação Superior usada nas 27 unidades da federação, mostra um estado que forma abaixo da densidade proporcional média do país, com concentração territorial moderada e uma lacuna de verificação de qualidade que atinge a maior parte das vagas.')
STAT4(['67', 'IES com curso de Farmácia', '8.887', 'vagas anuais autorizadas'])
STAT4(['47,7%', 'das vagas presenciais em Goiânia', '90,6%', 'das vagas sem ciclo ENADE 2023'])
H2('Principais achados')
LI('A oferta é predominantemente presencial. Das 8.887 vagas anuais, 7.247 (81,5%) são presenciais e 1.640 (18,5%) a distância — o inverso da tendência nacional, em que a EaD responde por 68,8% da capacidade do país (Cap. 4 e 5).')
LI('A concentração geográfica é real, porém moderada. A oferta presencial existe em 75 dos 246 municípios; Goiânia detém 47,7% das vagas presenciais. Os outros 171 municípios são desertos formativos (Cap. 8).')
LI('O vácuo avaliativo é o maior risco regulatório do estado. Das 8.887 vagas, apenas 831 (9,4%) foram avaliadas no ciclo ENADE 2023 — 90,6% da oferta ainda não passou por verificação externa de qualidade (Cap. 6).')
LI('Forma-se abaixo da média nacional, com qualidade aferida também abaixo da média. No recorte comparável às 27 UFs, Goiás tem 119,7 vagas por 100 mil habitantes contra a média nacional de 195,4 (13º lugar), com CC/ENADE médio de 2,48 (Brasil: 2,95) e IDD de 2,01 (Brasil: 2,21) — Cap. 10.')
LI('Há descompasso com o SUS, ainda que menos acentuado que a leitura setorial sugeria. A assistência farmacêutica pública é capilarizada (a Farmácia Popular alcança 205 dos 246 municípios), enquanto a formação, apesar de já presente em 75 municípios, segue concentrada nas regiões de saúde Central e Entorno Sul (Cap. 11).')
P('Recomendação central. Sob o novo marco regulatório, a Farmácia já não admite oferta integralmente a distância: resta o presencial e o semipresencial. O encaminhamento, portanto, não está em vetar modalidades, e sim em assegurar, em qualquer formato, três condições: carga prática verificável, núcleo clínico consistente e vínculo efetivo com o SUS — com prioridade regulatória para fechar o vácuo avaliativo de 90,6% das vagas. Em paralelo, recomenda-se que o CRF-GO assuma o monitoramento permanente da formação no estado, com painel de indicadores atualizado anualmente. As proposições correspondentes, em linguagem de minuta, constam do Anexo I.')
P('Reservas de método. As vagas referem-se a capacidade autorizada apurada pelo Censo da Educação Superior 2024, não a matrículas: em Goiás, 8.887 vagas autorizadas corresponderam a 9.276 matrículas e 1.065 concluintes no ciclo medido (taxa pontual de 11,5%). A densidade municipal de farmacêuticos em atividade (CNES) por estabelecimento e a empregabilidade dos egressos (RAIS) permanecem pendentes de extração; o total estadual em atividade consta do Cap. 9 (CNES, mai/2026: 3.408 profissionais; 0,48 por mil habitantes). Uma nota de proveniência completa consta do Capítulo 2.')

# ================= APRESENTAÇÃO =================
CHAP(None, 'Apresentação')
P('A formação de farmacêuticos em Goiás está dimensionada e orientada para as necessidades de saúde do estado? Foi essa a pergunta que orientou o trabalho do Grupo Técnico de Ensino do CRF-GO.')
P('A primeira edição deste estudo (fechada em 25/06/2026) respondeu a essa pergunta com base na Consulta Pública Avançada do e-MEC — um cadastro regulatório em tempo real, cuja unidade de análise é o curso e sua situação cadastral. Entre o fechamento daquela edição e a apresentação no XII ENCCF, o Observatório Nacional da Formação Farmacêutica — mesma equipe técnica, mesmo autor — consolidou uma leitura de Goiás construída sobre o Censo da Educação Superior 2024 e o ENADE/CPC 2023, agora estritamente comparável às demais 26 unidades da federação. Esta edição revisada substitui a base e-MEC pela base censitária em todo o diagnóstico quantitativo, preservando da edição original apenas os dados que não dependem dessa escolha metodológica: o contexto territorial e demográfico (Cap. 3), a demografia profissional via CNES/CRF-GO (Cap. 9, 13), o debate internacional (Cap. 12) e o marco legal (Cap. 14).')
P('O documento parte de um diagnóstico da oferta — quantas instituições existem, com quantas vagas, em que modalidade e com qual qualidade aferida — e avança para a comparação com o Brasil, a distribuição geográfica por região de saúde, a demografia da categoria e o cruzamento com a rede de assistência farmacêutica do SUS. Os indicadores oficiais de qualidade, inclusive o valor agregado dos cursos (IDD) e o Conceito Preliminar de Curso (CPC), foram extraídos diretamente das bases do INEP.')
P('O momento da publicação não é casual. O país revê as Diretrizes Curriculares Nacionais do curso de Farmácia e reconstrói o marco da educação a distância, e Goiás, por combinar oferta expressiva e forte dependência do SUS, reúne condições para contribuir com esse debate a partir de evidências. Soma-se a isso a atribuição legal do conselho de zelar pela qualidade do exercício profissional, que começa na formação.')
P('O estudo não emite juízo sobre instituições individuais: os números são tratados de forma agregada, com o objetivo de identificar padrões estaduais úteis à decisão pública. Onde faltou informação, registramos a lacuna e indicamos a fonte e o método para obtê-la, em vez de preenchê-la por suposição. É esse cuidado que sustenta o uso do documento como base técnica.')

PART('Parte I — A questão e o método', 'Antes de medir, é preciso enunciar o problema e declarar como ele será medido. Esta parte fixa a pergunta que organiza o livro e expõe, sem reservas, as fontes, as escolhas e os limites do método.')

CHAP('1', 'Introdução: a formação como política de saúde')
P('A formação de profissionais de saúde é, antes de tudo, uma política de saúde. Essa afirmação, que pode soar óbvia, costuma ser esquecida quando se discute ensino superior apenas pela ótica da expansão do acesso. O número, a distribuição geográfica e a qualificação dos farmacêuticos formados hoje determinam, anos depois, a capacidade concreta de um território de garantir o uso seguro e racional de medicamentos — na farmácia comunitária, no hospital, na atenção primária, na vigilância sanitária e na gestão pública.')
P('Quando a oferta formadora cresce em sintonia com a necessidade assistencial e sob controle de qualidade, o resultado é mais saúde: profissionais bem preparados, distribuídos onde a população precisa deles. Quando cresce desacoplada da necessidade e da verificação de qualidade, o resultado é outro — desperdício de recursos públicos e privados, frustração de expectativas de milhares de jovens e, no limite, risco à população que recebe um cuidado farmacêutico aquém do exigível.')
P('O estado oferece um caso particularmente instrutivo. É um território interiorizado, de dimensões continentais em escala regional, fortemente dependente do Sistema Único de Saúde. A leitura mais recente — construída sobre o Censo da Educação Superior 2024 — mostra uma oferta que, ao contrário do que a fotografia cadastral do e-MEC sugeria, permanece majoritariamente presencial, ainda concentrada na capital, com qualidade aferida abaixo da média nacional e um vácuo avaliativo que atinge nove em cada dez vagas.')
P('A oferta de cursos em Goiás é expressiva. O que está em questão é a sua concentração na capital, a verificação de qualidade — ainda incompleta para a maior parte das vagas — e a distância entre o que se forma e o que o SUS demanda.')
P('Cada capítulo submete essa leitura ao teste dos dados. A correção mais relevante desta edição em relação à original diz respeito exatamente à magnitude e à direção de um dos achados centrais — a composição por modalidade —, tema do Capítulo 4. Essa correção não enfraquece o argumento: o que sobrevive ao confronto com o dado oficial mais comparável é o que pode, de fato, orientar política pública.')

CHAP('2', 'Metodologia e fontes')
P('Esta edição revisada combina duas camadas de apuração. A primeira, herdada da edição original (fechada em 25/06/2026), extraiu e limpou os 101 registros de cursos de Farmácia de Goiás e os 1.592 registros nacionais da Consulta Pública Avançada do e-MEC, organizados por situação cadastral, modalidade, setor administrativo e conceitos oficiais. A segunda camada, incorporada nesta revisão, substitui a base primária de vagas, modalidade, concentração e qualidade pelo Censo da Educação Superior 2024 e pelos microdados ENADE/CPC 2023 (INEP/MEC), consolidados pelo Observatório Nacional da Formação Farmacêutica — mesma metodologia aplicada às 27 unidades da federação, com extração em 27/06/2026.')
P('A opção pela base censitária como referência principal desta edição decorre de três razões declaradas: (i) permite comparação direta e homogênea com as demais 26 UFs, o que o e-MEC, por si só, não assegura; (ii) mede a vaga efetivamente ofertada por instituição no ano-base, e não o registro cadastral de um curso — inclusive os ainda sem turma iniciada; (iii) é a mesma base sobre a qual o INEP calcula os indicadores oficiais de qualidade (CC, ENADE, IDD, CPC), o que permite cruzá-los sem transposição de fonte. A situação cadastral (ativo/em extinção/extinto) e o recorte setorial fino permanecem apoiados no e-MEC, por não terem equivalente direto no Censo, e são identificados como tais em cada figura.')
H2('Princípios e escolhas')
P('Quatro escolhas metodológicas estruturam o trabalho. A primeira é a rastreabilidade: toda afirmação quantitativa tem fonte declarada, e nenhuma estatística é apresentada sem que se saiba de onde vem e a que ano se refere. A segunda é a disciplina diante da lacuna: sempre que uma medida exige um dado não disponível, ele é assinalado como "a extrair" ou "Dado a integrar", com a base e o método indicados. A terceira é a distinção conceitual rigorosa — em especial entre o farmacêutico inscrito no conselho, o farmacêutico em atividade (CNES) e a vaga autorizada (capacidade, não matrícula). A quarta é a natureza declarada das projeções: cenários futuros são extrapolações de premissas explícitas, jamais previsões.')
H2('O que mudou entre as duas edições')
P('A tabela seguinte resume a mudança de base e por que ela altera a magnitude — e, em um ponto, a direção — dos achados centrais.')
TABLE('Quadro 2.1 — Duas leituras de Goiás', [
 ['Indicador', 'e-MEC jun/2026 (edição original)', 'Censo INEP 2024 (esta edição)'],
 ['Vagas autorizadas', '19.589', '8.887 (7.247 presencial + 1.640 EaD)'],
 ['Unidade de oferta', '53 cursos ativos (101 registros)', '67 IES / 35 mantenedoras'],
 ['Municípios com oferta', '15 de 246', '75 de 246'],
 ['Concentração em Goiânia', '82,8% do total de vagas', '47,7% da oferta presencial'],
 ['Modalidade dominante', 'Semipresencial (67,4%)', 'Presencial (81,5%)'],
 ['Vagas sem avaliação', '76%', '90,6%'],
], note='Fonte: e-MEC (Consulta Pública Avançada, 25/06/2026) e Censo da Educação Superior 2024/ENADE-CPC 2023 (Observatório Nacional da Formação Farmacêutica, extração 27/06/2026).')
P('Limites de fonte, declarados de saída. O Censo atribui a vaga a distância ao estado-sede da mantenedora, não ao polo de entrega — a densidade e a concentração aqui medidas descrevem a capacidade sediada, não necessariamente onde a EaD chega fisicamente. A ocupação real das vagas (matrícula) é inferior à capacidade autorizada: em Goiás, 9.276 matrículas para 8.887 vagas do ciclo mais recente. A confirmação de detalhes adicionais (polos, egressos) depende de extrações dirigidas, listadas no Apêndice A7.')

PART('Parte II — O diagnóstico', 'A fotografia da oferta: quantas instituições formam, onde, em que modalidade, com quantas vagas e com qual qualidade verificada.')

CHAP('3', 'Goiás: território, população e saúde')
P('Nenhum diagnóstico sobre formação faz sentido fora do território que ele serve. Goiás tem cerca de 7,42 milhões de habitantes (estimativa IBGE, 2025) distribuídos em 246 municípios, organizados pela Secretaria de Estado da Saúde (SES-GO) em 18 regiões de saúde, agrupadas em 5 macrorregiões: Centro-Oeste, Centro Norte, Centro Sudeste, Nordeste e Sudoeste. É um estado de povoamento relativamente disperso, com uma capital que polariza fortemente a economia, os serviços e — como se verá — a oferta de ensino superior.')
P('O traço estrutural mais decisivo para este estudo é a relação da população com o sistema de saúde. Em Goiás, cerca de 74% da população depende exclusivamente do SUS. A assistência pública organiza-se nas 18 regiões de saúde citadas, arranjo que define como o cuidado deve, idealmente, distribuir-se pelo território — e que esta edição passa a usar como camada territorial de análise (Cap. 8 e 11), substituindo a estimativa por geocodificação da edição original.')
STAT4(['7,42 mi', 'habitantes (IBGE, 2025)', '246', 'municípios em 18 regiões de saúde'])
P('Dessas características decorrem duas orientações que reaparecem ao longo da análise. A primeira: por ser fortemente SUS-dependente e interiorizado, Goiás demanda uma formação voltada ao cuidado clínico, à assistência farmacêutica e à atenção primária, e capilarizada para além da capital. A segunda: por já dispor de um mercado profissional volumoso — mais de 14 mil farmacêuticos inscritos no CRF-GO —, o diferencial do egresso goiano desloca-se da quantidade para a qualificação clínica e tecnológica.')
P('Há, ainda, um dado de saúde pública que antecipa o Capítulo 11: a rede de assistência farmacêutica goiana é ampla, com a Farmácia Popular presente em 205 dos 246 municípios — bem mais capilarizada do que a oferta formadora, hoje presente em 75. O contraste entre essa capilaridade assistencial e a concentração da formação será um dos eixos analíticos do estudo.')

CHAP('4', 'A oferta de formação')
P('O Censo da Educação Superior 2024 identifica 67 instituições de ensino superior (IES), sob 35 mantenedoras distintas, ofertando o curso de Farmácia em Goiás — um mercado pulverizado e competitivo (HHI de 0,062 por IES, muito abaixo do limiar de concentração de 0,25). Esse número de IES é superior aos 53 "cursos ativos" da leitura cadastral e-MEC, porque a unidade de contagem difere: o Censo conta instituições ofertantes no ano-base, ao passo que o e-MEC conta registros de curso, que podem estar duplicados por campus ou por habilitação. A situação cadastral (ativo/em extinção/extinto) permanece um dado e-MEC sem equivalente direto no Censo: dos 101 registros, 53 seguem ativos, 34 em extinção e 14 extintos — mortalidade cadastral concentrada nos cursos integralmente a distância, cuja oferta migrou de rótulo após a Portaria MEC nº 2.041/2023 (Cap. 7).')
FIGURE('fig_situacao.png', 'Figura 4.0 — Situação cadastral dos registros e-MEC (101 registros). Fonte: e-MEC, jun/2026.', width_mm=110)
P('Quanto à modalidade, a leitura censitária inverte o quadro que a fotografia cadastral sugeria: das 8.887 vagas anuais, 7.247 (81,5%) são presenciais e apenas 1.640 (18,5%) são a distância — 38 cursos presenciais contra 5 cursos EaD sediados no estado. É o oposto da tendência nacional, em que a EaD responde por 68,8% da capacidade do país. Essa aparente contradição com a leitura cadastral (que apontava 67,4% das vagas em cursos "semipresenciais") tem explicação metodológica: o e-MEC registra a criação de cursos recentes majoritariamente sob o rótulo semipresencial, mas o Censo, ao medir a vaga efetivamente ofertada no ano-base 2024, ainda não capturou plenamente esse movimento — sinal de que a próxima edição do Censo deve aproximar as duas leituras (ver Quadro 2.1).')
STAT4(['67', 'IES / 35 mantenedoras', '81,5%', 'da oferta é presencial'])
FIGURE('fig_modalidade.png', 'Figura 4.1 — Vagas autorizadas por modalidade de ensino. Fonte: Censo INEP 2024.', width_mm=95)
P('Quanto ao setor administrativo, a oferta segue majoritariamente privada: 93,1% das vagas estão em IES privadas, contra 6,9% em instituições públicas (Censo INEP 2024) — recorte mais preciso do que a estimativa e-MEC anterior (98,3%/1,7%), que superestimava a dependência privada por não decompor o setor administrativo por vaga. Em um estado em que três de cada quatro habitantes dependem do SUS, a parcela pública seguir minoritária é, ainda assim, um achado de política digno de registro.')
FIGURE('fig_setor.png', 'Figura 4.2 — Vagas autorizadas por dependência administrativa. Fonte: Censo INEP 2024.', width_mm=95)
P('O predomínio privado não é, em si, um problema — boa parte da formação em saúde no Brasil é privada e de qualidade. O ponto relevante é outro: quando a oferta pública é mínima, o controle de qualidade externo (CC, ENADE, IDD, CPC) torna-se a principal salvaguarda do interesse público — e é justamente essa salvaguarda que, como se verá no Capítulo 6, ainda não alcançou a maior parte da oferta.')

CHAP('5', 'Vagas e concentração')
P('Contar instituições é necessário, mas insuficiente: uma IES de 30 vagas e outra de 1.360 pesam de modo radicalmente diferente sobre o mercado. As 67 IES de Goiás somam 8.887 vagas anuais autorizadas — e a distribuição dessas vagas é desigual, ainda que menos extrema do que a leitura cadastral original sugeria.')
TABLE('Quadro 5.1 — As 15 maiores IES por vagas (Censo INEP 2024)', [
 ['IES', 'Vagas', 'Categoria'],
 ['Centro Universitário Estácio de Goiás', '1.360', 'Privada'],
 ['Centro Universitário Goyazes', '443', 'Privada'],
 ['Faculdade Logos', '420', 'Privada'],
 ['Universidade Estadual de Goiás', '409', 'Pública Estadual'],
 ['Centro Universitário Universo Goiânia', '403', 'Privada'],
 ['Universidade Evangélica de Goiás', '325', 'Privada'],
 ['Centro Universitário Alfredo Nasser', '257', 'Privada'],
 ['Universidade Paulista', '250', 'Privada'],
 ['Centro Universitário Cambury', '213', 'Privada'],
 ['Centro Universitário Facunicamps Goiânia', '200', 'Privada'],
 ['Faculdade Quirinópolis', '200', 'Privada'],
 ['Centro Universitário Facunicamps', '170', 'Privada'],
 ['Faculdade Anhanguera de Anápolis', '160', 'Privada'],
 ['Pontifícia Universidade Católica de Goiás', '160', 'Privada'],
 ['Faculdade Evangélica de Valparaíso', '160', 'Privada'],
], note='Fonte: Censo INEP 2024, agregado estadual por IES (Observatório Nacional). As 15 IES listadas (maior ranking disponível) somam 5.130 vagas (57,7% do total); as 52 IES restantes, de menor porte individual, respondem pelas demais 3.757 vagas (42,3%) e estão detalhadas no painel interativo.')
FIGURE('fig_ranking_ies.png', 'Figura 5.1 — As 10 maiores IES por vagas autorizadas. Fonte: Censo INEP 2024.', width_mm=155)
P('A maior IES isolada (Estácio de Goiás, 1.360 vagas) responde por 15,3% do total estadual — concentração relevante, mas muito distante do quadro da leitura e-MEC original, que apontava dois cursos, ainda sem turma iniciada, de 5.000 vagas cada. A medida formal de concentração confirma o novo quadro: o índice Herfindahl-Hirschman (HHI) por IES é de 0,062 (620 na escala 0–10.000) — mercado pulverizado —, e as razões de concentração mostram que as 2 maiores IES detêm 24,9% das vagas (CR2) e as 10 maiores, 59,1% (CR10). Todos os três indicadores são substancialmente menores do que os da leitura e-MEC (HHI 1.387; CR2 51%; CR10 72%), porque medem por instituição ofertante no Censo, e não por registro de curso no e-MEC — entre os quais os dois cursos ainda não iniciados distorciam desproporcionalmente a leitura cadastral.')
STAT4(['0,062', 'HHI por IES (mercado pulverizado)', '24,9% / 59,1%', 'CR2 / CR10'])
FIGURE('fig_concentracao.png', 'Figura 5.2 — Concentração da oferta presencial: Goiânia × demais municípios, e razões de concentração CR2/CR10. Fonte: Censo INEP 2024.', width_mm=155)
P('Vaga autorizada não é vaga preenchida. Em Goiás, o próprio Censo permite a comparação direta: as 8.887 vagas anuais corresponderam a 9.276 matrículas e 1.065 concluintes no ciclo medido — uma taxa pontual de conclusão de 11,5%, coerente com a referência nacional (10,6%). A distinção entre capacidade instalada e matrícula efetiva permanece central: ao longo do livro, "oferta" designa capacidade — um teto, não um fluxo.')

CHAP('6', 'Qualidade e avaliação')
P('Aqui o diagnóstico encontra seu ponto mais sensível. A expansão da oferta só é defensável se acompanhada de verificação de qualidade — e é precisamente nesse ponto que os dados revelam a lacuna mais severa do estudo, agora medida com maior precisão pelo Censo/ENADE do que pela leitura cadastral original.')
P('Das 8.887 vagas autorizadas em Goiás, apenas 831 (9,4%) foram efetivamente avaliadas no ciclo ENADE 2023 — ou seja, 90,6% da oferta (8.056 vagas) opera sem ciclo avaliativo concluído. É uma lacuna maior do que a estimativa da edição original (76%), porque a base de vagas do Censo é mais ampla do que o recorte de cursos ativos do e-MEC, ao passo que o número de vagas efetivamente avaliadas pelo ENADE 2023 é o mesmo em ambas as leituras.')
STAT4(['90,6%', 'das vagas sem ciclo ENADE 2023', '831', 'vagas efetivamente avaliadas'])
FIGURE('fig_avaliacao.png', 'Figura 6.0 — Vagas com e sem ciclo avaliativo ENADE concluído. Fonte: INEP/ENADE 2023.', width_mm=110)
P('Onde há medida, Goiás fica abaixo da média nacional: o Conceito de Curso médio, apurado a partir do ciclo ENADE 2023, é 2,48 em Goiás contra 2,95 no Brasil; o IDD (indicador de valor agregado, calculado sobre 28 cursos com ciclo avaliativo suficiente) é 2,01 em Goiás contra 2,21 no Brasil; e o CPC contínuo é 2,69 em Goiás contra 2,76 no Brasil. Nenhum desses três indicadores estava disponível na edição original, que registrava CC/ENADE/IDD como consulta direta ao INEP com cobertura distinta de cursos (3,64/2,40/2,59) — números que não são diretamente comparáveis aos desta edição por usarem outro critério de inclusão de cursos.')
FIGURE('fig_qualidade.png', 'Figura 6.1 — Indicadores de qualidade aferida: Goiás × Brasil. Fonte: INEP/ENADE 2023.', width_mm=140)
P('O achado precisa ser lido com cuidado. A ausência de ciclo avaliativo não autoriza a conclusão de que a oferta tem má qualidade: o que os dados mostram é que essa qualidade, na maior parte dos casos, ainda não foi verificada. Em um sistema majoritariamente privado (93,1% das vagas), a avaliação externa é a principal garantia do interesse público, e sua ausência sobre 90,6% das vagas constitui, por si, o principal risco regulatório identificado neste estudo — tema que retoma o Capítulo 15 (SWOT) e orienta a Proposição 1 do Capítulo 16.')
H2('Corpo docente, infraestrutura e perfil discente')
P('O ciclo avaliativo, onde ocorre, também permite abrir a "caixa-preta" da qualidade em três dimensões que a leitura cadastral original não alcançava. O corpo docente dos cursos avaliados é predominantemente qualificado — 93,2% dos docentes têm mestrado ou doutorado, 95,2% atuam em regime integral ou parcial (não horista) e 62,6% são doutores —, o que indica que o vácuo avaliativo (Cap. 6) não decorre de precariedade docente, mas da ausência de ciclo ENADE/CPC concluído para a maior parte da oferta.')
FIGURE('fig_docente_infra.png', 'Figura 6.2 — Corpo docente (% dos cursos avaliados) e dimensões de infraestrutura do CPC (escala 1–6). Fonte: Censo INEP 2024 / ENADE-CPC 2023.', width_mm=160)
P('Nas dimensões de infraestrutura do Conceito Preliminar de Curso, a organização didático-pedagógica (5,46) e a infraestrutura física (5,19) pontuam bem acima da mediana da escala 1–6; a oportunidade de ampliação da formação profissional (4,67) é a dimensão relativamente mais fraca, ainda que também positiva. O perfil discente, apurado pelo questionário do estudante do ENADE 2023, mostra um corpo discente majoritariamente feminino (70,7%), com presença relevante de estudantes negros, pardos ou indígenas (53,8%) e concentração expressiva no turno noturno (61,0%) — compatível com um público que concilia trabalho e estudo. O financiamento estudantil (FIES/PROUNI) alcança apenas 5,6% dos concluintes, indicando que a expansão privada da oferta (Cap. 4) se sustenta majoritariamente em mensalidade plena, não em crédito ou bolsa federal.')
FIGURE('fig_perfil_discente.png', 'Figura 6.3 — Perfil do corpo discente dos cursos avaliados. Fonte: ENADE 2023, questionário do estudante.', width_mm=140)

PART('Parte III — As dimensões analíticas', 'A fotografia ganha profundidade quando se acrescentam o tempo, o espaço, a demografia e a comparação interestadual.')

CHAP('7', 'A dimensão temporal: série histórica')
P('O diagnóstico cadastral é uma fotografia; a política pública, porém, precisa do filme. Reconstruindo as datas de criação contidas no e-MEC, a edição original recompôs a trajetória da oferta ao longo de duas décadas: uma onda de expansão concentrada entre 2017 e 2024, majoritariamente por educação a distância, seguida de um refluxo regulatório — a Portaria MEC nº 2.041/2023 suspendeu o credenciamento de EaD em cursos de saúde, e o repique de 2025 correspondeu a uma nova geração de cursos rotulados "semipresenciais".')
FIGURE('fig_serie.png', 'Figura 7.1 — Série histórica de inscritos ativos no CRF-GO, com projeção 2030. Fonte: CRF-GO.', width_mm=140)
P('Essa leitura temporal, apoiada no cadastro e-MEC (que registra a data de criação por curso), permanece válida como retrato do movimento regulatório e cadastral — não é substituída pelo Censo, que é uma fotografia anual sem série própria de datas de autorização. O que a comparação com o Censo 2024 acrescenta é uma advertência de leitura: a "recomposição para semipresencial" identificada no cadastro ainda não se traduz, no ano-base do Censo, em predominância de vagas EaD — a oferta efetivamente medida em 2024 seguia 81,5% presencial (Cap. 4). As duas leituras não se contradizem: descrevem, uma, o fluxo de novos registros cadastrais (onde a semipresencialidade cresce), e outra, o estoque de vagas efetivamente ofertadas no ano-base (onde o presencial ainda domina). A convergência entre elas é, ela própria, uma variável a monitorar nas próximas edições.')
P('Essa leitura temporal tem uma consequência analítica importante: o estoque de vagas "presenciais" predominante em 2024 é, em grande parte, anterior à onda EaD/semipresencial mais recente — o que ajuda a explicar por que a qualidade aferida (Cap. 6) ainda reflete um perfil majoritariamente presencial, mesmo com o vácuo avaliativo elevado. Qualquer política que se baseie apenas na fotografia cadastral mais recente, sem a base censitária, arrisca superestimar a magnitude da migração para EaD já concluída.')

CHAP('8', 'A dimensão espacial: atlas geoespacial')
P('Geocodificando as 67 IES sobre a malha municipal oficial do IBGE e cruzando com as 18 regiões de saúde da SES-GO, obtém-se um mapa mais fino do que a estimativa por geocodificação de nomes de instituição usada na edição original.')
FIGURE('fig_mapa_oferta.png', 'Mapa 8.1 — Vagas autorizadas por município, Goiás (246 municípios). Fonte: Censo INEP 2024/IBGE.', width_mm=130)
QUOTE('A oferta chegou a mais território do que o cadastro sugeria: 75 municípios têm oferta presencial (30,5% dos 246), ante 15 na leitura e-MEC — mas 171 (69,5%) seguem como desertos formativos, e a capital ainda concentra quase metade da oferta presencial.')
P('Goiânia responde por 3.456 das 7.247 vagas presenciais do estado (47,7%). É concentração real, mas bem menor do que os 82,8% da leitura cadastral original — que somava vagas EaD atribuídas à capital como se fossem presenciais e ignorava as instituições fora do recorte "curso ativo". Os cinco municípios seguintes por volume de vagas — Anápolis (790), Trindade (443), Novo Gama (420), Valparaíso de Goiás (316) e Aparecida de Goiânia (257) — somam 2.226 vagas, ou 30,7% da oferta presencial fora da capital.')
TABLE('Quadro 8.1 — Cobertura formadora por região de saúde (SES-GO)', [
 ['Região de saúde', 'Macrorregião', 'Municípios c/ oferta', 'Vagas'],
 ['Central', 'Centro-Oeste', '7 de 26', '4.002'],
 ['Entorno Sul', 'Nordeste', '7 de 7', '838'],
 ['Pireneus', 'Centro Norte', '4 de 10', '790'],
 ['Centro Sul', 'Centro Sudeste', '8 de 25', '257'],
 ['Sul', 'Centro Sudeste', '3 de 12', '245'],
 ['Rio Vermelho', 'Centro-Oeste', '7 de 17', '0*'],
], note='*Rio Vermelho tem 7 municípios com curso/matrícula ativa, mas nenhuma vaga nova autorizada no ciclo 2024. Fonte: Censo INEP 2024 cruzado com o Plano Diretor de Regionalização da SES-GO (18 regiões de saúde), Observatório Nacional. Quadro completo (18 regiões) no painel interativo.')
FIGURE('fig_regioes_saude.png', 'Figura 8.1 — Vagas autorizadas por região de saúde (SES-GO), 18 regiões. Fonte: Censo INEP 2024 / SES-GO.', width_mm=155)
P('Um achado central: a região de saúde Entorno Sul (7 municípios, na divisa com o Distrito Federal) tem cobertura formadora completa — todos os seus municípios ofertam o curso —, enquanto regiões inteiras do Centro Norte e do Nordeste goiano (Norte, São Patrício II, Nordeste I) têm oferta pontual ou nula. A oferta segue, portanto, a lógica de mercado — proximidade da metrópole de Brasília e da capital estadual —, não a distribuição da necessidade assistencial, tema retomado no Capítulo 11.')
P('Um achado que a leitura anterior não podia captar: 56 municípios são atendidos exclusivamente por polos de EaD, sem qualquer curso presencial — situação que exige atenção redobrada à verificação da prática presencial exigida por essa modalidade.')
TABLE('Quadro 8.2 — Os 75 municípios com curso e/ou matrícula ativa (Censo INEP 2024)', [
 ['Município', 'Vagas', 'Cursos', 'IES', 'Matrículas'],
 ['Goiânia', '3.456', '39', '34', '2.972'],
 ['Anápolis', '790', '17', '17', '1.903'],
 ['Trindade', '443', '7', '7', '228'],
 ['Novo Gama', '420', '6', '6', '78'],
 ['Valparaíso de Goiás', '316', '14', '13', '576'],
 ['Aparecida de Goiânia', '257', '11', '11', '509'],
 ['Itumbiara', '245', '7', '7', '286'],
 ['Quirinópolis', '200', '4', '4', '31'],
 ['Porangatu', '165', '5', '5', '151'],
 ['Rio Verde', '150', '8', '8', '173'],
 ['Caldas Novas', '120', '7', '7', '176'],
 ['São Luís de Montes Belos', '120', '3', '3', '139'],
 ['Ceres', '110', '4', '4', '112'],
 ['Mineiros', '105', '3', '3', '76'],
 ['Inhumas', '103', '6', '6', '119'],
 ['Luziânia', '102', '7', '7', '137'],
 ['Formosa', '50', '7', '7', '166'],
 ['Iporá', '50', '2', '2', '61'],
 ['Uruaçu', '45', '5', '5', '85'],
 ['Águas Lindas de Goiás', '0*', '7', '7', '83'],
 ['Acreúna', '0*', '1', '1', '10'],
 ['Alexânia', '0*', '3', '3', '13'],
 ['Alto Paraíso de Goiás', '0*', '1', '1', '13'],
 ['Anicuns', '0*', '1', '1', '5'],
 ['Aruanã', '0*', '1', '1', '4'],
 ['Barro Alto', '0*', '1', '1', '0'],
 ['Bela Vista de Goiás', '0*', '2', '2', '10'],
 ['Campinorte', '0*', '1', '1', '0'],
 ['Campos Belos', '0*', '2', '2', '27'],
 ['Catalão', '0*', '6', '6', '107'],
 ['Cavalcante', '0*', '1', '1', '0'],
 ['Caçu', '0*', '1', '1', '0'],
 ['Cidade Ocidental', '0*', '5', '5', '18'],
 ['Cristalina', '0*', '3', '3', '23'],
 ['Crixás', '0*', '1', '1', '3'],
 ['Damianópolis', '0*', '1', '1', '1'],
 ['Edéia', '0*', '1', '1', '12'],
 ['Flores de Goiás', '0*', '1', '1', '2'],
 ['Goianira', '0*', '3', '3', '4'],
 ['Goianápolis', '0*', '1', '1', '1'],
 ['Goianésia', '0*', '4', '4', '65'],
 ['Goiatuba', '0*', '2', '2', '9'],
 ['Goiás', '0*', '2', '2', '13'],
 ['Guapó', '0*', '1', '1', '2'],
 ['Hidrolândia', '0*', '1', '1', '2'],
 ['Ipameri', '0*', '1', '1', '5'],
 ['Itaberaí', '0*', '4', '4', '28'],
 ['Itapaci', '0*', '1', '1', '1'],
 ['Itapuranga', '0*', '1', '1', '111'],
 ['Jaraguá', '0*', '1', '1', '5'],
 ['Jataí', '0*', '5', '5', '40'],
 ['Jussara', '0*', '1', '1', '9'],
 ['Mambaí', '0*', '1', '1', '1'],
 ['Minaçu', '0*', '2', '2', '5'],
 ['Morrinhos', '0*', '3', '3', '109'],
 ['Mozarlândia', '0*', '1', '1', '1'],
 ['Nerópolis', '0*', '2', '2', '6'],
 ['Niquelândia', '0*', '1', '1', '12'],
 ['Nova Crixás', '0*', '1', '1', '25'],
 ['Orizona', '0*', '1', '1', '1'],
 ['Padre Bernardo', '0*', '2', '2', '10'],
 ['Palmeiras de Goiás', '0*', '1', '1', '5'],
 ['Piracanjuba', '0*', '1', '1', '0'],
 ['Pirenópolis', '0*', '1', '1', '1'],
 ['Pires do Rio', '0*', '2', '2', '8'],
 ['Planaltina', '0*', '8', '8', '116'],
 ['Posse', '0*', '3', '3', '86'],
 ['Santa Helena de Goiás', '0*', '3', '3', '12'],
 ['Santa Terezinha de Goiás', '0*', '2', '2', '145'],
 ['Santo Antônio do Descoberto', '0*', '3', '3', '22'],
 ['Senador Canedo', '0*', '5', '5', '64'],
 ['Simolândia', '0*', '1', '1', '11'],
 ['São Domingos', '0*', '1', '1', '1'],
 ['São Miguel do Araguaia', '0*', '1', '1', '17'],
 ['Vianópolis', '0*', '1', '1', '14'],
], note='*Município com curso e/ou matrícula ativa, mas sem vaga nova autorizada no ciclo Censo 2024 (mesma leitura da nota do Quadro 8.1). Fonte: Censo INEP 2024, Observatório Nacional da Formação Farmacêutica. Ordenado por vagas decrescente. Os 171 municípios remanescentes (69,5% do estado) não têm nenhum registro de curso ou matrícula — desertos formativos completos.')

CHAP('9', 'Demografia farmacêutica')
P('Este capítulo permanece apoiado no CNES e no cadastro do CRF-GO, fontes não afetadas pela mudança de base do Censo INEP. Em maio de 2026, o CNES registrava 3.408 farmacêuticos em atividade no estado — 0,48 por mil habitantes (base populacional do Censo IBGE 2022). O CRF-GO, por sua vez, tinha 14.000 farmacêuticos inscritos em 2024, ante 10.484 em 2020 (~7,5% ao ano).')
STAT4(['3.408', 'farmacêuticos em atividade (CNES)', '14.000', 'inscritos no CRF-GO (2024)'])
P('O cruzamento com a nova base de vagas (Cap. 5) suaviza, mas não elimina, o sinal de saturação: as 8.887 vagas anuais equivalem a 2,6 vezes o contingente em atividade registrado no CNES — abaixo das 5,7 vezes da leitura e-MEC original (19.589 vagas), mas ainda um múltiplo expressivo para um fluxo anual sobre um estoque profissional. A distinção entre farmacêutico inscrito (todos os registrados, incluindo inativos) e farmacêutico em atividade (força de trabalho efetiva) permanece essencial: o mercado goiano já é volumoso, e o desafio se desloca da quantidade para a qualificação clínica e a distribuição territorial dos novos formados.')

CHAP('10', 'Benchmark nacional')
P('O Observatório Nacional da Formação Farmacêutica aplica, às 27 unidades da federação, o mesmo método consolidado neste diagnóstico estadual — o que permite, nesta edição, posicionar Goiás com precisão que a leitura e-MEC (comparável apenas de forma aproximada) não assegurava.')
FIGURE('fig_centro_oeste.png', 'Figura 10.0 — Densidade formativa regional: Centro-Oeste × Brasil × Sudeste. Fonte: Censo INEP 2024/IBGE 2025.', width_mm=105)
TABLE('Quadro 10.1 — Posição de Goiás entre as 27 UFs', [
 ['Indicador', 'Valor (GO)', 'Posição', 'Mediana/média nacional'],
 ['Densidade (vagas/100 mil hab.)', '119,7', '13º', '195,4 (média)'],
 ['ICT — concentração territorial', '0,586', '15º', '0,548 (mediana)'],
 ['IAF — adequação formativa', '30,0', '18º', '33,3 (mediana)'],
 ['ICON — cobertura assistencial', '2,7', '8º', '1,9 (mediana)'],
 ['CC/ENADE 2023', '2,48', '17º', '2,95 (Brasil, ponderado)'],
], note='Fonte: Observatório Nacional da Formação Farmacêutica, Censo INEP 2024/ENADE-CPC 2023, extração 27/06/2026.')
FIGURE('fig_densidade_uf.png', 'Figura 10.1 — Vagas por 100 mil habitantes, 27 UFs (Goiás em destaque). Fonte: Censo INEP 2024/IBGE 2025.', width_mm=155)
P('Goiás é o 13º estado em densidade formativa (119,7 vagas por 100 mil habitantes), abaixo da média nacional (195,4) — posição consideravelmente mais modesta do que o "3º lugar" da leitura e-MEC original, que media cursos por milhão de habitantes (métrica distinta, não comparável ao ranking de vagas por habitante usado nas 27 UFs). Em concentração territorial (ICT), Goiás ocupa posição intermediária (15º, praticamente na mediana nacional de 0,548); em adequação formativa (IAF), fica abaixo da mediana (18º); em cobertura assistencial (ICON), tem desempenho relativamente melhor (8º), puxado pela capilaridade da Farmácia Popular frente ao número ainda modesto de municípios com curso.')
P('Em qualidade aferida, Goiás permanece abaixo da média nacional em todos os indicadores disponíveis: CC/ENADE 2,48 contra 2,95 no Brasil (17º lugar); IDD 2,01 contra 2,21; CPC contínuo 2,69 contra 2,76. A leitura interestadual confirma, portanto, o achado qualitativo da edição original — Goiás forma com qualidade aferida abaixo da média nacional —, ainda que a magnitude precisa e o ranking de densidade tenham sido revistos por completo.')

CHAP('11', 'Formação e necessidade de saúde')
P('O ICON mediano nacional (1,9) já situava Goiás em posição relativamente favorável (ICON = 2,7, 8º lugar); esta edição pode, agora, decompor esse indicador por região de saúde, algo que a estimativa por geocodificação da versão original não permitia.')
P('A Farmácia Popular alcança 205 dos 246 municípios goianos — rede assistencial capilarizada, presente em 2,7 municípios para cada município com curso de Farmácia. Entre os 171 desertos formativos, 76% já contam com Farmácia Popular — potencial concreto de ancoragem para estágios e para uma futura estratégia de interiorização da formação, sem esperar a abertura de novos cursos.')
STAT4(['205/246', 'municípios com Farmácia Popular', '76%', 'dos desertos já têm Farmácia Popular'])
P('O cruzamento por região de saúde (Quadro 8.1) mostra que a formação segue a lógica de mercado — proximidade da capital e da metrópole de Brasília —, e não a distribuição da necessidade assistencial pelas 18 regiões. A região Entorno Sul, com cobertura formadora completa, é também uma das mais próximas do Distrito Federal; regiões mais distantes e mais dependentes do SUS, como Norte e Nordeste II, têm oferta pontual ou nula. Detalhar essa necessidade por estabelecimento de saúde (CNES por município) permanece como extração pendente, registrada no Apêndice A7.')

PART('Parte IV — O horizonte', 'Da fotografia territorial à comparação internacional e à extrapolação de cenários — o que esperar adiante.')

CHAP('12', 'O debate internacional')
P('Este capítulo, apoiado em literatura regulatória internacional (ACPE, GPhC, FIP/OMS) e não em dados estaduais, permanece integralmente válido nesta edição. Nenhum grande regulador de referência internacional admite formação em Farmácia integralmente a distância: todos exigem prática presencial supervisionada, verificável e vinculada a campos de estágio credenciados. O Índice de Alinhamento com o Padrão Internacional (IAPI) de Goiás é 0,60 — alinhamento moderado, puxado pela vedação normativa recente (Decreto nº 12.456/2025), mas ainda limitado pela fragilidade da verificação da prática.')

CHAP('13', 'Cenários 2024–2050')
P('As projeções de inscritos no CRF-GO permanecem inalteradas nesta edição, por serem construídas sobre a série histórica de registro profissional (CRF-GO), não sobre a base e-MEC/Censo de vagas autorizadas. Partindo de 14.000 inscritos em 2024, três cenários de crescimento anual (3%, 5% e 7%) projetam, respectivamente, 16.700, 20.100 e 21.000 inscritos em 2030 — chegando, em 2050, a um intervalo entre 30.100 (cenário contido) e 81.300 (cenário expansionista).')
FIGURE('fig_cenarios.png', 'Figura 13.1 — Cenários de crescimento de inscritos no CRF-GO, 2024–2050. Fonte: CRF-GO (projeção).', width_mm=150)
P('São projeções (cenário), não dados observados: extrapolações de premissas explícitas sobre a base de 2024, não previsões. O leitor deve tomá-las como referência de ordem de grandeza para o planejamento, não como meta.')

CHAP('14', 'Marco legal')
P('Sob o Decreto nº 12.456/2025, a Farmácia não pode mais ser ofertada integralmente a distância; o único formato não presencial admitido é o semipresencial, com piso de presencialidade obrigatório. É exatamente sobre a fração da oferta que ainda não foi submetida a ciclo avaliativo — 90,6% das vagas nesta edição — que devem recair as exigências de qualidade prévia, convertendo a expansão recente de aposta regulatória em qualidade verificada. O antecedente histórico permanece o mesmo da edição original: a proposta original das Diretrizes Curriculares de 2017 chegou a esboçar restrições à EaD em Farmácia, retiradas do texto final; o país levou quase uma década para retomar essa restrição, agora pelo Decreto de 2025.')

PART('Parte V — Síntese e proposições', 'Do diagnóstico revisado às recomendações — o que fazer com o que os dados, agora comparáveis nacionalmente, mostram.')

CHAP('15', 'Síntese: SWOT e achados')
H2('Forças')
LI('Mercado pulverizado e competitivo (HHI 0,062; 67 IES sob 35 mantenedoras) — baixo risco de dependência de poucos grandes players.')
LI('Predominância presencial (81,5% das vagas) — favorece a verificação de prática exigida pelo novo marco regulatório.')
LI('Cobertura assistencial relativamente boa (ICON 2,7, 8º lugar entre 27 UFs) — Farmácia Popular presente em 205 municípios.')
H2('Fraquezas')
LI('Vácuo avaliativo severo: 90,6% das vagas sem ciclo ENADE 2023 concluído.')
LI('Qualidade aferida abaixo da média nacional em todos os indicadores disponíveis (CC/ENADE, IDD, CPC).')
LI('Adequação formativa (IAF) abaixo da mediana nacional (18º lugar de 27).')
H2('Oportunidades')
LI('171 desertos formativos, dos quais 76% já têm Farmácia Popular — campo de prática e interiorização sem esperar novos cursos.')
LI('Decreto nº 12.456/2025 cria janela regulatória para exigir qualidade prévia da oferta semipresencial ainda em expansão.')
H2('Ameaças')
LI('Recomposição cadastral para semipresencial (Cap. 7) pode repetir, na próxima leitura censitária, o padrão de baixa verificação hoje concentrado nos cursos mais novos.')
LI('Concentração ainda relevante em Goiânia (47,7% da oferta presencial) mantém pressão sobre infraestrutura de estágio na capital.')
STAT4(['90,6%', 'Vácuo avaliativo — achado central', '47,7%', 'Concentração em Goiânia'])

CHAP('16', 'Proposições para a nova DCN')
P('Seis proposições, detalhadas em linguagem de minuta no Anexo I, derivam diretamente do diagnóstico revisado:')
LI('Carga horária prática em todas as modalidades — vedada substituição integral por atividades a distância.')
LI('Núcleo de competências clínicas obrigatório, orientado ao SUS (74% da população goiana é SUS-dependente).')
LI('Garantia de qualidade prévia na oferta semipresencial — condicionar autorização à infraestrutura de prática e a processos de avaliação verificáveis, já que 90,6% das vagas atuais seguem sem ciclo ENADE concluído.')
LI('Competências em tecnologia, dados e inovação no currículo.')
LI('Extensão e integração territorial com o SUS, priorizando os 171 municípios sem curso — 76% dos quais já contam com Farmácia Popular como ponto de ancoragem.')
LI('Avaliação por competências (OSCE/OSPE, portfólios), complementando os instrumentos cognitivos tradicionais.')

CHAP('17', 'Plano estratégico do CRF-GO')
LI('Monitorar. Painel público de vagas, modalidade e avaliação por território (município e região de saúde), com cadência semestral, usando esta mesma base Censo INEP/ENADE como referência.')
LI('Incidir. Levar as evidências revisadas à revisão da DCN e às audiências do CNE/MEC, com o quadro comparativo interestadual (Cap. 10) como argumento de posicionamento nacional.')
LI('Verificar. Articular com a SES-GO a integração dos microdados municipais de saúde (CNES por estabelecimento) às 18 regiões de saúde já incorporadas a este estudo (Cap. 8 e 11).')

CHAP('18', 'Conclusão')
P('A formação farmacêutica em Goiás, lida agora sobre a mesma base censitária aplicada às 27 unidades da federação, confirma o essencial do diagnóstico original — concentração territorial relevante na capital e um vácuo avaliativo que atinge a maior parte da oferta —, mas revê substancialmente sua magnitude e, num ponto decisivo, sua direção: a oferta é predominantemente presencial, não semipresencial, no ano-base do Censo 2024. Essa correção não enfraquece a agenda de qualificação proposta neste estudo; ao contrário, a torna mais urgente, porque mostra que mesmo a oferta presencial estabelecida ainda carece, em 90,6% das vagas, de verificação externa de qualidade. O convite permanece o mesmo: tratar a formação farmacêutica como infraestrutura do sistema de saúde, medi-la com o rigor que essa função exige, e atualizar a leitura a cada novo ciclo de dados — no painel interativo do CRF-GO e no Observatório Nacional da Formação Farmacêutica.')
