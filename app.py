import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a pontuação final
def calculate_final_score(scores):
    max_score = len(scores) * 3  # pontuação máxima se todas as variáveis tiverem nota 3
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100
    return percentage_score

# Função para plotar o gráfico radar com um tamanho maior
def plot_radar_chart(scores, categories):
    # Certifique-se de que 'scores' e 'categories' têm o mesmo tamanho
    if len(scores) != len(categories):
        st.error("O número de pontuações e categorias não coincide.")
        return None
    
    values = scores + scores[:1]  # Repete o primeiro valor para fechar o círculo
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    angles += angles[:1]  # Repete o primeiro ângulo para fechar o gráfico

    # Aumentando o tamanho da figura
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    return fig

# Definir variáveis agrupadas por ODS com prefixos

variables = {
    "ODS 7": [
        {"name": "7.1 Número de programas de conscientização em uso racional de energia", "options": [
            "0: Nenhum programa em operação.",
            "1: Até 2 programas em operação, atingindo até 100 pessoas.",
            "2: 3-5 programas em operação, atingindo 101-500 pessoas.",
            "3: Mais de 5 programas em operação, atingindo mais de 500 pessoas."
        ]},
        {"name": "7.2 Número de programas de gestão de eficiência energética", "options": [
            "0: Nenhum programa em operação.",
            "1: Pelo menos um programa, resultando em até 5% de redução no consumo de energia.",
            "2: Pelo menos um programa, resultando em uma redução maior que 5% e menor ou igual a 10% no consumo de energia.",
            "3: Pelo menos um programa com reduções no consumo de energia superiores a 10%."
        ]},
        {"name": "7.3 Número de iniciativas de inovação tecnológica em eficiência energética", "options": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas tecnológicas implementadas.",
            "2: 3-5 iniciativas tecnológicas implementadas.",
            "3: Mais de 5 iniciativas implementadas."
        ]},
        {"name": "7.4 Percentual de energia renovável contratada e produzida em instalações portuárias", "options": [
            "0: Nenhum uso de energia renovável.",
            "1: Até 10% da energia utilizada é renovável.",
            "2: Mais de 10% até 50% da energia usada é renovável.",
            "3: Mais de 50% da energia usada é renovável."
        ]},
        {"name": "7.5 Percentual de biocombustíveis em cargas elétricas e mecânicas", "options": [
            "0: Nenhum uso de biocombustíveis.",
            "1: Menos de 5% das cargas são operadas com biocombustíveis.",
            "2: 5% a 20% das cargas são operadas com biocombustíveis.",
            "3: Mais de 20% das cargas são operadas com biocombustíveis."
        ]},
        {"name": "7.6 Número de iniciativas de inovação tecnológica em energia renovável", "options": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas na fase de planejamento ou piloto.",
            "2: 3-5 iniciativas na fase de implementação com resultados preliminares.",
            "3: Mais de 5 iniciativas em plena operação com resultados comprovados."
        ]},
        {"name": "7.7. Diversidade de fontes de energia renovável em instalações portuárias", "options": [
            "0: Nenhum uso de fontes renováveis.",
            "1: Uso de 1 tipo diferente de energia renovável.",
            "2: Uso de 2 tipos diferentes de energia renovável.",
            "3: Uso de 3 ou mais tipos diferentes de energia renovável."
        ]},
        {"name": "7.8 Quantidade de parcerias para promoção de energia limpa", "options": [
            "0: Nenhuma parceria estabelecida.",
            "1: Até 2 parcerias estabelecidas com foco em energia limpa.",
            "2: 3-5 parcerias estabelecidas com foco em energia limpa.",
            "3: Mais de 5 parcerias estabelecidas com foco em energia limpa."
        ]},
        {"name": "7.9 Quantidade de estações de carregamento para veículos elétricos", "options": [
            "0: Nenhuma estação de carregamento disponível.",
            "1: Até 5 estações de carregamento disponíveis.",
            "2: 6-15 estações de carregamento disponíveis.",
            "3: Mais de 15 estações de carregamento disponíveis."
        ]},
        {"name": "7.10 Percentual de fornecimento de energia renovável para navios", "options": [
            "0: Nenhum fornecimento de energia renovável para navios.",
            "1: Menos de 10% do fornecimento de energia para navios vem de fontes renováveis.",
            "2: Entre 10% e 30% do fornecimento de energia para navios vem de fontes renováveis.",
            "3: Mais de 30% do fornecimento de energia para navios vem de fontes renováveis."
        ]},
        {"name": "7.11 Percentual de abastecimento com GNL", "options": [
            "0: Nenhum abastecimento de GNL.",
            "1: Menos de 5% do fornecimento total de combustível é com GNL.",
            "2: Entre 5% e 20% do fornecimento total de combustível é com GNL.",
            "3: Mais de 20% do fornecimento total de combustível é com GNL."
        ]},
        {"name": "7.12 Número de iniciativas de inovação tecnológica em atendimento elétrico e energético para navios", "options": [
            "0: Nenhuma iniciativa.",
            "1: Até 2 iniciativas de inovação tecnológica em fase de planejamento ou piloto.",
            "2: 3-5 iniciativas em fase de implementação ou avaliação de eficácia.",
            "3: Mais de 5 iniciativas em plena operação, com resultados de eficácia comprovados."
        ]},
        {"name": "7.13 Quantidade de navios usando energia renovável no porto", "options": [
            "0: Nenhum navio utiliza energia renovável.",
            "1: Até 5% dos navios no porto utilizam energia renovável.",
            "2: 5% a 15% dos navios no porto utilizam energia renovável.",
            "3: Mais de 15% dos navios no porto utilizam energia renovável."
        ]},
        {"name": "7.14 Tarifas diferenciadas para navios com desempenho acima dos padrões ambientais", "options": [
            "0: Nenhuma aplicação de tarifas diferenciadas.",
            "1: Até 5% de desconto nas tarifas portuárias.",
            "2: 5% a 15% de desconto nas tarifas portuárias.",
            "3: Mais de 15% de desconto nas tarifas portuárias."
        ]}
        ],

    "ODS 9": [
    {"name": "9.1 Número de patentes depositadas e concedidas no INPI (Instituto Nacional da Propriedade Industrial)", "options": [
        "0: Nenhuma patente depositada no ano.",
        "1: Até 2 patentes depositadas no ano, com patentes concedidas.",
        "2: De 3 a 5 patentes depositadas no ano, com patentes concedidas.",
        "3: Mais de 5 patentes depositadas no ano, com patentes concedidas."
    ]},
    {"name": "9.2 Número de publicações em periódicos de alto impacto financiadas pelo porto", "options": [
        "0: Nenhuma iniciativa ou resultado significativo.",
        "1: Até 2 publicações em periódicos de alto impacto.",
        "2: De 3 a 5 publicações em periódicos de alto impacto.",
        "3: Mais de 5 publicações em periódicos de alto impacto."
    ]},
    {"name": "9.3 Número de prêmios e selos de qualidade relacionados à Inovação", "options": [
        "0: Nenhuma iniciativa ou resultado significativo.",
        "1: Recebimento de até 2 prêmios ou selos de qualidade em inovação.",
        "2: Recebimento de 3 a 5 prêmios ou selos de qualidade em inovação.",
        "3: Recebimento de mais de 5 prêmios ou selos de qualidade em inovação."
    ]},
    {"name": "9.4 Posição no ranking de inovação do setor portuário", "options": [
        "0: Posição no quarto quartil no ranking de inovação.",
        "1: Posição no terceiro quartil no ranking de inovação.",
        "2: Posição no segundo quartil no ranking de inovação.",
        "3: Posição no primeiro quartil no ranking de inovação."
    ]},
    {"name": "9.5 Nível médio de maturação de inovação por projeto", "options": [
        "0: Nenhum projeto.",
        "1: Projetos em fase de conceito inicial ou desenvolvimento com baixo nível de maturação.",
        "2: Projetos em fase de protótipo ou piloto com nível médio de maturação.",
        "3: Projetos com produtos finais ou soluções implementadas com alto nível de maturidade tecnológica (Technology Readiness Levels)."
    ]},
    {"name": "9.6 Diversidade de áreas de conhecimento em projetos de pesquisa aplicada", "options": [
        "0: Nenhuma área de conhecimento envolvida nos projetos.",
        "1: Até 2 áreas de conhecimento envolvidas nos projetos.",
        "2: De 3 a 5 áreas de conhecimento diferentes envolvidas nos projetos.",
        "3: Mais de 5 áreas de conhecimento diferentes envolvidas nos projetos."
    ]},
    {"name": "9.7 Percentual de operações automatizadas no porto", "options": [
        "0: Nenhuma operação automatizada.",
        "1: Até 25% das operações automatizadas.",
        "2: De 25% a 50% das operações automatizadas.",
        "3: Mais de 50% das operações automatizadas."
    ]},
    {"name": "9.8 Número de acordos com universidades e centros de pesquisa ou projetos financiados", "options": [
        "0: Nenhum acordo ou projeto.",
        "1: Até 2 acordos ou projetos.",
        "2: De 3 a 5 acordos ou projetos estabelecidos.",
        "3: Mais de 5 acordos ou projetos."
    ]},
    {"name": "9.9 Número de pesquisadores externos da instituição portuária ou universidade vinculados a projetos de inovação", "options": [
        "0: Nenhum pesquisador externo vinculado.",
        "1: Até 3 pesquisadores externos vinculados.",
        "2: De 4 a 6 pesquisadores externos vinculados.",
        "3: Mais de 6 pesquisadores externos vinculados."
    ]},
    {"name": "9.10 Número de empresas parceiras em projetos de inovação", "options": [
        "0: Nenhuma empresa parceira.",
        "1: Até 2 empresas parceiras envolvidas.",
        "2: De 3 a 5 empresas parceiras envolvidas.",
        "3: Mais de 5 empresas parceiras com colaboração efetiva e contribuições significativas."
    ]},
    {"name": "9.11 Número de startups apoiadas focadas em soluções inovadoras", "options": [
        "0: Nenhuma startup.",
        "1: Apoio a até 2 startups.",
        "2: Apoio a 3-5 startups.",
        "3: Apoio a mais de 5 startups."
    ]},
    {"name": "9.12 Número de acordos com outros portos ou terminais para a promoção da inovação", "options": [
        "0: Nenhum acordo.",
        "1: Até 2 acordos.",
        "2: De 3 a 5 acordos.",
        "3: Mais de 5 acordos."
    ]}
],

        "ODS 13": [
    {"name": "13.1 Status do Plano de Estratégia para Mudança Climática", "options": [
        "0: Nenhuma estratégia.",
        "1: Plano estratégico em desenvolvimento, sem ações implementadas.",
        "2: Plano estratégico implementado, com algumas ações em prática.",
        "3: Plano estratégico totalmente operacional, com revisão e atualizações regulares."
    ]},
    {"name": "13.2 Inventário de Emissões", "options": [
        "0: Inventário de emissões não realizado.",
        "1: Inventário de emissões realizado, mas desatualizado.",
        "2: Inventário de emissões realizado, atualizado há mais de um ano.",
        "3: Inventário de emissões atualizado anualmente e ativamente utilizado para gestão de emissões."
    ]},
    {"name": "13.3 Programa de Gestão de Créditos de Carbono", "options": [
        "0: Nenhum programa de créditos de carbono.",
        "1: Programa em fase inicial, sem créditos gerados ou adquiridos.",
        "2: Programa ativo, com créditos de carbono sendo gerados ou adquiridos.",
        "3: Programa bem estabelecido, com créditos de carbono sendo ativamente geridos."
    ]},
    {"name": "13.4 Programa de Monitoramento Climático", "options": [
        "0: Programa inexistente.",
        "1: Programa em fase de implementação.",
        "2: Programa implementado, mas dados usados de forma limitada.",
        "3: Programa implementado e integrado a um sistema de resposta e planejamento climático."
    ]},
    {"name": "13.5 Número de Colaborações e Parcerias para Ação Climática", "options": [
        "0: Nenhuma colaboração ou parceria estabelecida.",
        "1: Até 2 colaborações ou parcerias estabelecidas.",
        "2: 3-5 colaborações ou parcerias com resultados iniciais.",
        "3: Mais de 5 colaborações ou parcerias com impacto significativo e mensurável na ação climática."
    ]},
    {"name": "13.6 Infraestrutura Resiliente ao Clima", "options": [
        "0: Nenhuma infraestrutura avaliada como resiliente ao clima.",
        "1: Menos de 25% da infraestrutura avaliada como resiliente ao clima.",
        "2: De 25-50% da infraestrutura avaliada como resiliente ao clima.",
        "3: Mais de 50% da infraestrutura avaliada como resiliente ao clima e adaptada."
    ]},
    {"name": "13.7 Índice de Eficiência do Tráfego de Carga", "options": [
        "0: Índice não calculado.",
        "1: Índice de eficiência abaixo da média do setor.",
        "2: Índice de eficiência na média do setor.",
        "3: Índice de eficiência acima da média do setor, com melhorias contínuas."
    ]},
    {"name": "13.8 Percentual de Redução de Emissões por Meio da Implementação de Novas Tecnologias", "options": [
        "0: Nenhum programa de redução de emissões.",
        "1: Redução de emissões inferior a 5% por meio de novas tecnologias.",
        "2: Redução de 5-10% das emissões por meio de novas tecnologias.",
        "3: Redução de mais de 10% das emissões por meio de novas tecnologias."
    ]}
],

    "ODS 14": [
    {"name": "14.1 Número de espécies exóticas invasoras registradas", "options": [
        "0: Nenhum programa de identificação de espécies.",
        "1: Identificação de um número de espécies invasoras na região maior que no período anterior.",
        "2: Identificação de um número de espécies invasoras na região igual ao do período anterior.",
        "3: Identificação de um número de espécies invasoras na região menor que no período anterior."
    ]},
    {"name": "14.2 Concentração média de poluentes na água costeira, conforme legislação regional", "options": [
        "0: Sem medições de poluentes na água.",
        "1: Concentrações de poluentes mais de 10% acima dos padrões estabelecidos.",
        "2: Concentrações de poluentes dentro dos padrões estabelecidos.",
        "3: Concentrações de poluentes 10% abaixo dos padrões estabelecidos."
    ]},
    {"name": "14.3 Qualidade dos sedimentos marinhos, conforme legislação regional", "options": [
        "0: Nenhuma avaliação da qualidade dos sedimentos.",
        "1: Qualidade dos sedimentos abaixo dos padrões aceitáveis, com presença de contaminantes.",
        "2: Qualidade dos sedimentos dentro dos padrões aceitáveis.",
        "3: Qualidade dos sedimentos acima dos padrões, com baixos níveis de contaminantes."
    ]},
    {"name": "14.4 Número de eventos ambientais registrados na costa da região", "options": [
        "0: Nenhum monitoramento de eventos.",
        "1: Mais de 5 eventos ambientais registrados no ano.",
        "2: De 2 a 5 eventos ambientais registrados no ano.",
        "3: 0 a 1 evento ambiental registrado no ano, com respostas rápidas e eficazes."
    ]},
    {"name": "14.5 Monitoramento da água de lastro", "options": [
        "0: Sem monitoramento em vigor.",
        "1: Monitoramento inconsistente.",
        "2: Monitoramento regular.",
        "3: Monitoramento sistemático."
    ]},
    {"name": "14.6 Área total de habitats marinhos protegidos na área de operação do porto", "options": [
        "0: Nenhum programa de proteção em vigor.",
        "1: Menos de 10% dos habitats marinhos estão sob proteção.",
        "2: 10-25% dos habitats marinhos estão sob proteção.",
        "3: Mais de 25% dos habitats marinhos estão sob proteção, com programas de conservação ativos."
    ]},
    {"name": "14.7 Valor total investido em pesquisa de recursos marinhos sustentáveis", "options": [
        "0: Sem investimentos.",
        "1: Investimento inferior a 5% do orçamento total de pesquisa.",
        "2: Investimento de 5-10% do orçamento total de pesquisa.",
        "3: Investimento superior a 10% do orçamento total de pesquisa."
    ]},
    {"name": "14.8 Número de projetos de pesquisa marinha financiados pelo porto", "options": [
        "0: Nenhum projeto.",
        "1: Até 2 projetos financiados no ano.",
        "2: De 3 a 5 projetos financiados no ano.",
        "3: Mais de 5 projetos financiados no ano, com colaborações de IES ou centros de pesquisa."
    ]}
 ],
    "ODS 17": [
    {"name": "17.1 Status como signatário do Pacto Global da ONU", "options": [
        "0: Não é signatário.",
        "1: Signatário, sem relatório de progresso.",
        "2: Signatário ativo.",
        "3: Signatário ativo, com relatório anual de progresso e metas para melhoria contínua."
    ]},
    {"name": "17.2 Alinhamento dos ODS com indicadores IDA e GRI", "options": [
        "0: Nenhum alinhamento documentado.",
        "1: Alinhamento parcial com os ODS.",
        "2: Alinhamento parcial e relatórios regulares sobre o progresso dos ODS.",
        "3: Alinhamento completo e relatórios regulares sobre o progresso dos ODS."
    ]},
    {"name": "17.3 Existência de certificação ECOPORTS", "options": [
        "0: Não certificado.",
        "1: Em processo de certificação.",
        "2: Certificado, sem renovação regular.",
        "3: Certificado, com renovação regular e cumprimento de todos os critérios."
    ]},
    {"name": "17.4 Publicação do relatório de sustentabilidade", "options": [
        "0: Relatório não publicado.",
        "1: Relatório em fase de implementação.",
        "2: Relatório publicado, mas não em conformidade com os padrões GRI ou equivalente.",
        "3: Relatório publicado e em conformidade com os padrões GRI ou equivalente."
    ]},
    {"name": "17.5 Divulgação da posição no IDA", "options": [
        "0: Posição no IDA não divulgada.",
        "1: Posição no IDA divulgada publicamente sem planos de ação para melhoria.",
        "2: Posição no IDA divulgada publicamente.",
        "3: Posição no IDA divulgada publicamente com planos de ação para melhoria."
    ]},
    {"name": "17.6 Publicação de indicadores de sustentabilidade", "options": [
        "0: Indicadores não publicados.",
        "1: Indicadores em fase de implementação.",
        "2: Indicadores publicados, mas sem detalhes ou contexto.",
        "3: Indicadores publicados com detalhes, contexto e comparações de desempenho."
    ]},
    {"name": "17.7 Registro e comunicação de incidentes ambientais", "options": [
        "0: Sem acompanhamento de registros.",
        "1: Registro e comunicação não sistemáticos.",
        "2: Registro sistemático e comunicação interna.",
        "3: Registro e comunicação sistemáticos, públicos e com ações de resposta."
    ]},
    {"name": "17.8 Número de membros independentes no conselho de administração", "options": [
        "0: Nenhum membro independente.",
        "1: Menos de 25% dos membros são independentes.",
        "2: 25-50% dos membros são independentes.",
        "3: Mais de 50% dos membros são independentes."
    ]},
    {"name": "17.9 Número de parcerias estabelecidas com ONGs e outras entidades para iniciativas de sustentabilidade", "options": [
        "0: Nenhuma parceria estabelecida.",
        "1: Até 2 parcerias estabelecidas.",
        "2: De 3 a 5 parcerias estabelecidas.",
        "3: Mais de 5 parcerias estabelecidas com projetos em andamento."
    ]},
    {"name": "17.10 Listagem de canais de comunicação ativos com stakeholders", "options": [
        "0: Nenhum canal de comunicação.",
        "1: Canais de comunicação limitados ou ineficazes.",
        "2: Alguns canais de comunicação estabelecidos e ativos.",
        "3: Diversos canais de comunicação estabelecidos, ativos e com feedback regular."
    ]}
    
 ]}

# Título da aplicação Streamlit com cor verde escuro
st.markdown("<h1 style='color: darkgreen;'>Atributos ODS - ODS 7, 9, 13, 14 e 17</h1>", unsafe_allow_html=True)

# Criação de abas para cada ODS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["ODS 7", "ODS 9", "ODS 13", "ODS 14", "ODS 17"])

# Função para exibir conteúdo de cada aba
def display_ods_tab(ods_group):
    st.header(f"Avaliação - {ods_group}")
    scores = []
    categories = []
    for variable in variables[ods_group]:
        option = st.selectbox(variable["name"], options=variable["options"])
        scores.append(int(option[0]))  # Converte o primeiro caractere da opção selecionada em inteiro
        
        # Extrai apenas o prefixo numérico (exemplo: "7.1") para o gráfico radar
        prefix = variable["name"].split(" ")[0]
        categories.append(prefix)

    # Verifique se 'scores' e 'categories' têm o mesmo comprimento antes de prosseguir
    if len(scores) != len(categories):
        st.error("Erro: O número de pontuações e categorias não coincide.")
        return

    # Calcula a pontuação final
    percentage_score = calculate_final_score(scores)
    st.write(f"Pontuação Final para {ods_group}: {percentage_score:.2f}%")

    # Exibe o gráfico radar
    st.subheader("Gráfico Radar")
    radar_chart = plot_radar_chart(scores, categories)
    if radar_chart:
        st.pyplot(radar_chart)

# Exibe as variáveis e resultados para cada aba
with tab1:
    display_ods_tab("ODS 7")

with tab2:
    display_ods_tab("ODS 9")

with tab3:
    display_ods_tab("ODS 13")

with tab4:
    display_ods_tab("ODS 14")

with tab5:
    display_ods_tab("ODS 17")

# Informações finais do projeto
st.write("""
Os idealizadores do modelo são Darliane Cunha, Clóvis Oliveira e Markus Carneiro Costa.
""")


