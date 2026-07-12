# -*- coding: utf-8 -*-
"""Part VI (appendices) + back matter. Imported and appended to book_content.B by the build script."""
from book_content import B, PART, CHAP, H2, P, LI, STAT4, TABLE, QUOTE

PART('Parte VI — Aparato analítico e benchmark internacional', 'Os índices próprios do Observatório, o benchmark interestadual, o modelo causal e a comparação com quatro referências regulatórias internacionais.')

CHAP('A1', 'Sistema Integrado de Índices (SII)')
P('Esta edição substitui o Sistema Integrado de Índices da versão original (apoiado no e-MEC, com IVQ, ICT, RGA e ISF de fórmula própria) pelo conjunto de treze índices do Observatório da Formação Farmacêutica em Goiás, construído sobre o Censo INEP 2024 e já publicado no painel interativo do CRF-GO — o que assegura que o número citado neste livro seja, em qualquer data de consulta, idêntico ao do instrumento vivo.')
TABLE('Tabela A1.1 — Os treze índices do Observatório, Goiás (2026)', [
 ['Índice', 'Valor', 'Leitura'],
 ['ICT — Concentração Territorial', '0,586', '15º de 27 UFs; mediana nacional 0,548'],
 ['IIR — Interiorização Real', '30,5%', '75 de 246 municípios com oferta'],
 ['IVA — Vácuo Avaliativo', '0,906', '90,6% das vagas sem ciclo ENADE 2023'],
 ['IDP — Dependência Privada', '93,1%', '6,9% das vagas em rede pública'],
 ['IAS — Alinhamento com o SUS (IAPI)', '0,60', 'vedação da EaD plena; verificação ainda frágil'],
 ['IRR — Risco Regulatório', '0,62', 'moderado-alto; pendente de recalibração'],
 ['IPR — Prioridade Regional', 'Dado a integrar', 'requer CNES por município + malha SES-GO'],
 ['ISO — Sustentabilidade da Oferta', '0,77', 'melhora frente à base e-MEC (0,35); a confirmar'],
 ['IAF — Adequação Formativa', '30,0', '18º de 27 UFs; mediana nacional 33,3'],
 ['ICON — Cobertura Assistencial', '2,7', '8º de 27 UFs; mediana nacional 1,9'],
 ['HHI — Concentração de Mercado', '0,062', 'mercado pulverizado (67 IES / 35 mantenedoras)'],
 ['E — Equidade Territorial', '0,414', '= 1 − ICT; moderada-baixa'],
 ['ICON-deserto', '0,76', '76% dos desertos já têm Farmácia Popular'],
], note='Fonte: Observatório da Formação Farmacêutica em Goiás / Observatório Nacional da Formação Farmacêutica, Censo INEP 2024/ENADE-CPC 2023, extração 27/06/2026. Fórmulas e limitações de cada índice no painel interativo (seção "Índices próprios").')
P('Leitura do conjunto. O índice mais crítico é o IVA (0,906): nove em cada dez vagas ainda não passaram por verificação externa de qualidade. É também o único componente do IRR (Risco Regulatório) com dado atualizado nesta base — o IRR permanece registrado em 0,62 porque seus outros dois componentes (fragilidade de verificação da prática, defasagem de avaliação) são qualitativos e não foram recalculados nesta revisão. O ICT (0,586) e a IIR (30,5%) mostram um retrato de concentração territorial moderada — nem o extremo que a leitura e-MEC sugeria, nem uma distribuição equitativa. O ISO (0,77), lido com cautela, indica menor pressão de saturação de mercado do que a base e-MEC original apontava, mas a melhora decorre da mudança de base de vagas (8.887, ante 19.589), não de nova coleta de dados assistenciais — por isso permanece classificado como sinal "a confirmar".')

CHAP('A2', 'Benchmark interestadual e posição relativa')
P('Medir Goiás contra si mesmo não basta para uma obra de referência nacional. Sobre a base do Censo INEP 2024 — agora estritamente comparável entre as 27 unidades da federação —, a densidade formativa das UFs permite situar o estado em distribuição, e não apenas em ranking ordinal.')
TABLE('Quadro A2.1 — Densidade formativa (vagas/100 mil hab.), cinco maiores e Goiás', [
 ['UF', 'Vagas/100 mil hab.', 'Posição'],
 ['Distrito Federal', '502,2', '1º'],
 ['Rio de Janeiro', '380,4', '2º'],
 ['Pernambuco', '363,3', '3º'],
 ['Mato Grosso do Sul', '358,3', '4º'],
 ['Paraná', '304,4', '5º'],
 ['Goiás', '119,7', '13º'],
], note='Fonte: Censo INEP 2024/IBGE 2025, Observatório Nacional da Formação Farmacêutica, 27 UFs.')
P('A densidade média simples das 27 unidades é de 164,2 vagas por 100 mil habitantes, com desvio-padrão de 125,0. Goiás, com 119,7, situa-se a 0,36 desvio-padrão abaixo da média — 13º lugar, próximo ao centro da distribuição. É uma revisão substancial frente à leitura e-MEC original, que posicionava o estado 1,16 desvio-padrão acima da média (3º lugar) usando uma métrica distinta (cursos por milhão de habitantes, e não vagas por 100 mil habitantes) e uma base de vagas 2,2 vezes maior. As duas métricas — cursos por milhão e vagas por 100 mil habitantes — respondem a perguntas diferentes; nesta edição, adota-se a segunda por ser a que o Observatório Nacional aplica de forma uniforme às 27 UFs.')
QUOTE('Achado revisado. A "saturação de Goiás por densidade formativa", afirmada na edição original como desvio estatístico extremo (z = +1,16, 3º lugar), não se sustenta na base censitária comparável: Goiás está discretamente abaixo da média nacional (z = −0,36, 13º lugar). O sinal de saturação mais robusto deste estudo é outro — a razão entre vagas anuais e farmacêuticos em atividade no CNES (2,6×, Cap. 9), não a densidade formativa por habitante.')
P('Em concentração territorial (ICT) e adequação formativa (IAF), Goiás permanece em posição intermediária a discretamente abaixo da mediana nacional (Cap. 10, Quadro 10.1) — quadro mais nuançado do que um único indicador de densidade seria capaz de expressar.')

CHAP('A3', 'Modelo causal: por que aconteceu')
P('Um diagnóstico de referência precisa explicar mecanismos, não apenas registrar resultados. A recomposição modal identificada no cadastro e-MEC (Cap. 7) — da educação a distância para o rótulo "semipresencial" — não foi um fenômeno de mercado espontâneo: foi a resposta de um setor majoritariamente privado a uma sucessão de incentivos regulatórios. A cadeia causal permanece válida como explicação do movimento cadastral; o que esta edição revê é a magnitude do seu reflexo no estoque de vagas medido pelo Censo 2024.')
TABLE('Tabela A3.1 — Cadeia causal da recomposição modal (2017–2026)', [
 ['Elo', 'Fator', 'Mecanismo'],
 ['Causa estrutural 1', 'Economia de escala da EaD', 'Custo marginal baixo por vaga incentiva oferta de grande porte'],
 ['Causa estrutural 2', 'Oferta pública mínima (6,9% das vagas)', 'Ausência de contrapeso público desloca o controle para a avaliação externa'],
 ['Causa estrutural 3', 'Defasagem da verificação', 'Cursos novos não completam ciclo avaliativo antes de operar em escala'],
 ['Gatilho', 'Portaria MEC nº 2.041/2023', 'Suspende credenciamento de EaD em saúde; inflexão da série cadastral em 2023'],
 ['Transmissão', 'Reetiquetagem modal', 'Registro cadastral migra de EaD para "semipresencial", preservando a escala'],
 ['Efeito concentrado', 'Vácuo avaliativo (90,6% das vagas)', 'Maior parcela de vagas sem verificação, justamente onde a oferta mais se expande'],
], note='Cadeia causal preservada da edição original (explica o movimento cadastral e-MEC); efeito final (vácuo avaliativo) atualizado para a métrica desta edição.')
P('Implicação causal. Como o gatilho foi normativo, a correção também o é. Instrumentos regulatórios que condicionem a operação à verificação prévia de qualidade atingem a raiz do problema; intervenções de mercado (concorrência, preço), não. É a base lógica das proposições priorizadas em A5.')

CHAP('A4', 'Consequências e análise preditiva')
P('O futuro da força de trabalho não está determinado; é resultado de escolhas presentes. Esta edição substitui a estimativa de ingressos por proxy nacional (21% de ocupação sobre a base e-MEC) pelo dado direto do Censo: 9.276 matrículas e 1.065 concluintes sobre 8.887 vagas autorizadas — uma taxa de ocupação efetiva de 104% (mais matrículas do que vagas do ciclo, refletindo o acúmulo de coortes em curso) e uma taxa de conclusão pontual de 11,5%.')
P('O Índice de Sustentabilidade da Oferta (ISO = 0,77, Apêndice A1) resume a relação entre o contingente em atividade no CNES (3.408) e o fluxo anual de vagas (8.887): a razão melhora frente à leitura e-MEC (0,35) porque a base de vagas é 2,2 vezes menor, não porque a absorção assistencial tenha mudado. O risco identificado na edição original — descolamento entre quem se forma e quem efetivamente atua — permanece presente, ainda que com magnitude revista: as 8.887 vagas anuais equivalem a 2,6 vezes o contingente em atividade (Cap. 9), ante 5,7 vezes na leitura original. A alavanca de política permanece dupla: ampliar papéis clínicos e digitais que absorvam o contingente formado, e conter a expansão de vagas sem verificação de qualidade.')

CHAP('A5', 'Priorização de intervenções')
P('Diagnóstico e causa convergem para a ação. As proposições do estudo, somadas ao instrumento de monitoramento (A6), são ordenadas por impacto esperado e viabilidade de implementação, segundo avaliação qualitativa do grupo técnico. O produto é uma matriz de decisão, não um ranking definitivo.')
P('Três intervenções ocupam o quadrante de prioridade alta — impacto e viabilidade elevados: a garantia de qualidade prévia no semipresencial (P3), que ataca diretamente o IVA de 0,906; o piso de prática verificável em toda modalidade (P1), que protege o núcleo profissional; e o painel de monitoramento por índices (M1), que torna o diagnóstico permanente — e que esta própria revisão demonstra ser necessário: a diferença entre as duas edições deste livro é, ela mesma, o argumento a favor de um painel vivo em vez de um retrato estático. A avaliação por competências (P6) e a extensão territorial (P5) têm alto impacto, porém viabilidade menor, e demandam construção institucional de médio prazo.')

CHAP('A6', 'Painel de monitoramento contínuo')
P('Uma obra de referência não se encerra no diagnóstico: institui o instrumento que o mantém vivo. O painel a seguir opera diretamente sobre os treze índices do Observatório (A1), com linha de base nesta revisão, meta, fonte e cadência — de modo que o CRF-GO, e qualquer Conselho Regional, possa acompanhar a trajetória ano a ano no mesmo painel interativo que sustenta este livro.')
TABLE('Tabela A6.1 — Painel de indicadores (linha de base 09/07/2026)', [
 ['Indicador', 'Base (GO)', 'Meta', 'Fonte', 'Cadência'],
 ['IVA — vácuo avaliativo', '0,906', '≤ 0,50', 'Censo INEP/ENADE', 'anual/trienal'],
 ['IDD médio', '2,01', '≥ 2,21 (Brasil)', 'ENADE (ciclo)', 'trienal'],
 ['ICT — concentração territorial', '0,586', '↓ tendência', 'Censo INEP', 'anual'],
 ['IIR — interiorização real', '30,5%', '↑ tendência', 'Censo INEP', 'anual'],
 ['Densidade em atividade (CNES)', '0,48/mil', 'série histórica', 'CNES/TABNET', 'anual'],
 ['IAF — adequação formativa', '30,0', '≥ 33,3 (mediana)', 'Observatório Nacional', 'anual'],
], note='Fonte: painel interativo do Observatório da Formação Farmacêutica em Goiás (CRF-GO/GT de Ensino).')
P('Do dado à decisão, e da decisão à medida: o índice que não se atualiza envelhece; o que se atualiza cobra resultado. Esta revisão do livro — motivada pela divergência entre a leitura e-MEC original e a base censitária comparável — é, em si, a demonstração prática desse princípio.')

CHAP('A7', 'Registro de lacunas e agenda de dados')
P('A credibilidade de uma referência mede-se também pelo que ela declara não saber. Quatro extrações dirigidas completariam o aparato e fechariam os índices hoje parciais ou pendentes.')
TABLE('Tabela A7.1 — Registro de lacunas', [
 ['Lacuna', 'Extração necessária', 'Índice/capítulo afetado'],
 ['A — Orientação clínica dos PPC', 'Análise de conteúdo dos projetos pedagógicos', 'Componente do IAS (IAPI)'],
 ['B — Necessidade assistencial por território', 'CNES por estabelecimento, cruzado com as 18 regiões de saúde', 'IPR — ainda "Dado a integrar"'],
 ['C — Fluxo de egressos', 'RAIS/Novo CAGED (CBO 2234-05)', 'Calibração do ISO e empregabilidade'],
 ['D — Ano de autorização por curso', 'Extração e-MEC dirigida ou nova consulta bulk', 'Filtro "Ano de autorização" do painel — ainda "Dado a integrar"'],
], note='As lacunas B e D foram objeto de tentativa de extração nesta revisão (09/07/2026): a malha de 18 regiões de saúde da SES-GO foi incorporada (Cap. 8 e 11), mas o CNES por estabelecimento e a API e-MEC de autorização por curso permanecem indisponíveis sem credencial de acesso — ver nota de proveniência no painel interativo.')
P('Próximos módulos da obra. Este volume, em sua segunda edição, mantém o plano original: (II) aparato analítico — entregue; (III) benchmark internacional de modelos regulatórios — entregue (A8-A9); (IV) mapa municipal de convergência oferta–necessidade — parcialmente entregue nesta revisão via regiões de saúde (Cap. 8), pendente o detalhamento por estabelecimento CNES; (V) manual de replicação do Observatório para os 27 Conselhos Regionais.')

CHAP('A8', 'Benchmark internacional de modelos regulatórios')
P('A pergunta que organiza este capítulo não é pedagógica, e sim regulatória: como os sistemas maduros disciplinam a educação a distância e híbrida em Farmácia? Este capítulo não depende da base e-MEC/Censo e permanece integralmente válido da edição original.')
P('Nos Estados Unidos, a agência acreditadora (ACPE) reconhece programas de Doctor of Pharmacy ofertados por educação a distância, com reconhecimento federal renovado até 2031 — mas condicionado: o componente experiencial deve ocorrer presencialmente em locais de prática supervisionados, chegando a um terço do currículo. No Reino Unido, o GPhC admite modalidades a distância em determinadas trilhas, sempre com piso de dias presenciais e horas de prática supervisionada. No plano global, a FIP consolidou, desde 2016, uma educação baseada em necessidades e competências, articulada à Estratégia Global da OMS para a força de trabalho até 2030 — que projeta déficit de 18 milhões de trabalhadores de saúde, concentrado em países de renda baixa e média.')
TABLE('Tabela A8.1 — Modelos regulatórios: comparação internacional', [
 ['Dimensão', 'EUA (ACPE)', 'Reino Unido (GPhC)', 'Norma global (FIP/OMS)', 'Brasil (Decreto 12.456/2025)'],
 ['EaD plena permitida?', 'Não', 'Não', 'Não recomendada', 'Não (vedada)'],
 ['Prática presencial obrigatória?', 'Sim (IPPE/APPE)', 'Sim (horas mínimas)', 'Sim (baseada em necessidades)', 'Sim em norma; verificação frágil'],
 ['Avaliação externa prévia?', 'Sim (acreditação)', 'Sim (acreditação prévia)', 'Recomendada', 'Defasada (90,6% sem ENADE)'],
], note='Fonte: ACPE Standards 2025; GPhC; FIP Development Goals 2020; OMS Global Strategy on HRH 2030; Decreto nº 12.456/2025. Coluna Brasil atualizada com o achado revisado (IVA = 0,906).')
P('Achado-síntese. Nenhuma das referências admite curso de Farmácia integralmente a distância. A convergência internacional não recai sobre a modalidade de entrega do ensino teórico — que pode ser remota —, e sim sobre dois invariantes: a prática experiencial presencial e supervisionada, e a avaliação externa prévia à operação em escala.')

CHAP('A9', 'Alinhamento do marco brasileiro e implicação para a DCN')
P('Posto o marco brasileiro contra o padrão internacional, o diagnóstico ganha precisão estratégica. A vedação da EaD plena em saúde, instituída em 2025, coloca o Brasil em linha com a norma global. O ponto de divergência não é a modalidade — é a verificação.')
P('O Índice de Alinhamento Regulatório (IAS/IAPI) situa o marco brasileiro em 0,60 numa escala de 0 a 1 — inalterado desta para a edição original, por ser uma construção qualitativa sobre a norma, não sobre o estoque de vagas. A nota é puxada para cima pela vedação da EaD plena e pela exigência formal de núcleo clínico, e para baixo por duas lacunas: a avaliação externa prévia, comprometida quando 90,6% das vagas operam sem ciclo avaliativo concluído (IVA, Apêndice A1) — lacuna maior nesta edição do que a estimativa original (76%) —, e a verificação da prática presencial no formato semipresencial, hoje frágil.')
P('Implicação para a nova DCN. A revisão das Diretrizes Curriculares Nacionais não precisa reabrir o debate de modalidade — esse já está resolvido em linha com o mundo. Precisa fechar o flanco da verificação, hoje mais amplo do que o diagnóstico original media. Três dispositivos elevam simultaneamente o IAS e reduzem o IVA: exigir prática presencial supervisionada com carga e registro auditáveis em todas as modalidades; condicionar a operação em escala à avaliação externa prévia, e não posterior; e tornar o núcleo clínico-experiencial um requisito aferível por competências, não apenas declarado.')
QUOTE('O mundo não discute mais se a Farmácia pode ser totalmente a distância. Discute como garantir prática verificável e qualidade aferida — e é nesse ponto que o Brasil, e Goiás em particular, têm o que avançar.')

CHAP(None, 'Referências')
LI('BRASIL. Ministério da Educação. Sistema e-MEC — Consulta Pública Avançada. Brasília: MEC, extração de 25/06/2026 (Goiás e nacional).')
LI('INEP. Censo da Educação Superior 2024 e microdados ENADE/CPC 2023. Brasília: INEP/MEC. Consolidado pelo Observatório Nacional da Formação Farmacêutica, extração de 27/06/2026.')
LI('IBGE. Estimativas da população dos municípios (2025) e Censo Demográfico 2022 — Goiás e Brasil.')
LI('SECRETARIA DE ESTADO DA SAÚDE DE GOIÁS (SES-GO). Plano Diretor de Regionalização — 18 regiões de saúde, 5 macrorregiões. Disponível em goias.gov.br/saude/regionais-de-saude. Consultado em 09/07/2026.')
LI('CONSELHO FEDERAL DE FARMÁCIA (CFF). Dados demográficos e profissionais da categoria. Brasília: CFF, 2010–2024.')
LI('CRF-GO. Registros de inscritos. Goiânia, 2020; 2024.')
LI('BRASIL. Ministério da Saúde. Programa Farmácia Popular do Brasil — cobertura municipal, 2024–2026; CNES/DATASUS, mai/2026.')
LI('IPEA; CFF. Mercado de trabalho do farmacêutico no Brasil, 2021–2023.')
LI('FIP. Global Competency Framework (GbCFv2). Haia: International Pharmaceutical Federation, 2020.')
LI('AACP/ACPE. CAPE Educational Outcomes; ACPE Standards 2025; COEPA, 2022.')
LI('BRASIL. Portaria MEC nº 2.041/2023; Portaria MEC nº 158/2024; Decreto nº 12.456/2025; Leis nº 3.820/1960, 5.991/1973 e 13.021/2014; Res. CNE/CES nº 2/2002, 6/2017 e 7/2018.')
LI('OBSERVATÓRIO NACIONAL DA FORMAÇÃO FARMACÊUTICA. Formação Farmacêutica no Brasil: diagnóstico nacional, análise por unidade federativa. Goiânia, 2026.')

CHAP(None, 'Apêndice metodológico')
P('Em cumprimento ao princípio de não fabricação, este apêndice registra, com transparência, o que permanece sem evidência direta e o método para obtê-lo nesta edição revisada (09/07/2026).')
TABLE('Tabela A.1 — Registro de dados: incorporados e pendentes (revisão 09/07/2026)', [
 ['Dado', 'Situação'],
 ['Vagas, IES, modalidade, concentração', 'Incorporado — Censo INEP 2024 (Cap. 4, 5, 8)'],
 ['Qualidade (CC, ENADE, IDD, CPC)', 'Incorporado — ENADE/CPC 2023 (Cap. 6, 10)'],
 ['Município-sede de cada IES', 'Incorporado — microdado municipal do Censo (Cap. 8)'],
 ['Matrículas, ingressos, concluintes', 'Incorporado — Censo da Educação Superior 2024 (Cap. 5)'],
 ['Região/macrorregião de saúde (SES-GO)', 'Incorporado nesta revisão — 246 municípios, 18 regiões (Cap. 8, 11)'],
 ['Benchmark Goiás × Brasil × 27 UFs', 'Incorporado — Observatório Nacional (Cap. 10, Apêndice A2)'],
 ['Densidade de farmacêuticos em atividade (GO)', 'Incorporado (estadual): CNES/TABNET, mai/2026 = 3.408 (0,48/mil). Detalhamento por estabelecimento pendente.'],
 ['Necessidade assistencial por região de saúde', 'Parcialmente incorporado (oferta por região, Cap. 8); necessidade (CNES por estabelecimento) pendente'],
 ['Ano de autorização por curso', 'Pendente — e-MEC não publica base aberta em lote (Apêndice A7)'],
 ['Empregabilidade e renda dos egressos', 'Pendente — RAIS e Novo CAGED (CBO 2234-05)'],
], note=None)
P('Nota de encerramento. Esta edição revisada substitui a base primária de vagas, modalidade, concentração e qualidade — antes apoiada no e-MEC — pelo Censo da Educação Superior 2024 e pelo ENADE/CPC 2023, na mesma metodologia aplicada pelo Observatório Nacional da Formação Farmacêutica às 27 unidades da federação. A mudança alterou a magnitude de praticamente todos os indicadores e, num ponto — a composição por modalidade —, também a direção do achado. Os capítulos não afetados pela escolha de base (território, demografia via CNES/CRF-GO, cenários, debate internacional e marco legal) permanecem os mesmos da edição original. O painel interativo do CRF-GO e o Observatório Nacional da Formação Farmacêutica são as referências vivas desta obra; em caso de divergência entre este texto e o painel em uma data futura, prevalece o painel, por refletir o ciclo de dados mais recente.')
P('GT de Ensino — Conselho Regional de Farmácia do Estado de Goiás (CRF-GO). Autor: Farmacêutico Dr. Edson Sidião de Souza Júnior. Edição original: 25/06/2026. Revisão com base Censo INEP 2024: 09/07/2026.')

CHAP(None, 'Anexo I — Minuta de proposições para a DCN')
P('As seis proposições do Capítulo 16 são reapresentadas a seguir em linguagem de minuta, redigidas como dispositivos passíveis de incorporação à futura Resolução do Conselho Nacional de Educação que instituir as novas Diretrizes Curriculares Nacionais do curso de Farmácia. A numeração dos artigos é meramente indicativa. Cada dispositivo é acompanhado de breve justificativa, com remissão ao capítulo de evidência correspondente — atualizada nesta revisão onde a evidência mudou de magnitude.')
H2('Proposição 1 — Carga horária prática em todas as modalidades')
P('Art. 1º O projeto pedagógico do curso de Farmácia assegurará, em qualquer modalidade de oferta, percentual mínimo de carga horária destinada a atividades práticas presenciais e de ensino em serviço, vedada a sua substituição integral por atividades a distância.')
P('§ 1º Consideram-se atividades práticas, para os fins deste artigo, os estágios supervisionados, as práticas laboratoriais, a farmácia-escola e as atividades desenvolvidas em estabelecimentos de saúde sob supervisão de farmacêutico.')
P('§ 2º A instituição comprovará, antes do início de funcionamento de cada turma, a infraestrutura e os campos de prática necessários ao cumprimento do percentual mínimo.')
P('Justificativa. O estudo demonstrou que 90,6% das vagas do estado operam sem ciclo avaliativo concluído (Cap. 6), risco concentrado sobretudo nos cursos mais recentes e nos rotulados semipresenciais (Cap. 7). Um piso de prática verificável protege o núcleo profissional da formação independentemente da modalidade.')
H2('Proposição 2 — Núcleo de competências clínicas')
P('Art. 2º A formação contemplará núcleo obrigatório de competências voltadas ao cuidado em saúde, compreendendo, no mínimo, o raciocínio clínico, o acompanhamento farmacoterapêutico, a assistência farmacêutica e a atuação no Sistema Único de Saúde.')
P('Parágrafo único. As competências de que trata o caput serão descritas em termos de resultados de aprendizagem observáveis e progressivamente confiáveis ao longo do curso.')
P('Justificativa. Goiás é fortemente dependente do SUS (74% da população) e possui rede de assistência farmacêutica capilarizada — a Farmácia Popular alcança 205 dos 246 municípios (Cap. 3 e 11); a formação deve orientar-se ao cuidado clínico e à inserção no sistema público.')
H2('Proposição 3 — Garantia de qualidade na educação a distância')
P('Art. 3º Vedada a oferta de Farmácia integralmente a distância, o credenciamento e a autorização de cursos no formato semipresencial condicionam-se à comprovação prévia de infraestrutura de prática, corpo docente qualificado e processos de avaliação verificáveis.')
P('Parágrafo único. A oferta de que trata o caput submeter-se-á a avaliação externa em prazo não superior ao do primeiro ciclo avaliativo subsequente ao início de funcionamento.')
P('Justificativa. Sob o Decreto nº 12.456/2025, a Farmácia não pode mais ser ofertada integralmente a distância; o único formato não presencial admitido é o semipresencial. É exatamente sobre a fração da oferta ainda sem ciclo avaliativo concluído — 90,6% das vagas nesta edição (Cap. 6 e 10) — que devem recair as exigências de qualidade prévia, convertendo a expansão de aposta em qualidade verificada.')
H2('Proposição 4 — Tecnologia, dados e inovação')
P('Art. 4º O currículo incorporará competências relativas às tecnologias de informação e comunicação aplicadas à saúde, à telefarmácia, à análise de dados, à inteligência artificial e à farmacogenômica, na perspectiva do uso seguro e ético dessas ferramentas no cuidado farmacêutico.')
P('Justificativa. A revisão internacional aponta a literacia digital e de dados como fronteira da formação farmacêutica (Cap. 12), competência ainda incipiente na oferta goiana.')
H2('Proposição 5 — Extensão e integração territorial com o SUS')
P('Art. 5º A extensão curricularizada será desenvolvida preferencialmente em articulação com a rede de atenção à saúde, contemplando territórios de menor oferta formadora e assistencial.')
P('Parágrafo único. As instituições buscarão formalizar, com os gestores do SUS, campos de estágio, projetos de extensão e iniciativas de telefarmácia supervisionada que ampliem a presença da formação para além dos grandes centros.')
P('Justificativa. A oferta presencial concentra-se em 75 dos 246 municípios, com 47,7% das vagas na capital, enquanto a rede assistencial da Farmácia Popular já alcança 205 municípios — incluindo 76% dos 171 desertos formativos (Cap. 8 e 11), candidatos naturais a campos de prática.')
H2('Proposição 6 — Avaliação por competências')
P('Art. 6º A avaliação do estudante adotará, progressivamente, instrumentos de aferição de desempenho por competências, tais como exames clínicos objetivos estruturados (OSCE/OSPE) e portfólios reflexivos, complementando os instrumentos tradicionais de avaliação cognitiva.')
P('Justificativa. A qualidade aferida dos cursos goianos situa-se abaixo da média nacional em todos os indicadores disponíveis — CC/ENADE, IDD e CPC (Cap. 10); a avaliação por desempenho, consolidada internacionalmente (Cap. 12), eleva a confiabilidade da formação clínica.')
P('Nota de encaminhamento. Sugere-se que esta minuta seja submetida, pela presidência do CRF-GO, ao Conselho Federal de Farmácia e à Secretaria de Educação Superior do MEC, como contribuição formal do estado de Goiás ao processo de revisão das Diretrizes Curriculares Nacionais.')
P('Minuta elaborada pelo GT de Ensino do CRF-GO (2026), de autoria do Farmacêutico Dr. Edson Sidião de Souza Júnior, com base nas evidências revisadas do presente estudo (base Censo INEP 2024, 09/07/2026). Texto sujeito a revisão jurídica antes de protocolo.')
