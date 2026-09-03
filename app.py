import streamlit as st

# Configuração da página para ocupar mais espaço na tela (layout "wide")
st.set_page_config(page_title="FIAP Mega Simulado", page_icon="🚀", layout="wide")

# ==========================================
# BANCO DE QUESTÕES 
# ==========================================
fase1_pandas = [
    {"q": "O que a função `describe()` faz em um DataFrame do Pandas?", "opts": ["Lista os tipos de dados de cada coluna.", "Gera um resumo estatístico das colunas numéricas.", "Descreve as 5 primeiras linhas.", "Remove os valores nulos."], "ans": "Gera um resumo estatístico das colunas numéricas."},
    {"q": "Para verificar rapidamente se existem valores nulos e quais são os tipos de dados, qual método é indicado?", "opts": ["df.shape()", "df.describe()", "df.info()", "df.head()"], "ans": "df.info()"},
    {"q": "Você quer apagar a coluna 'Salário'. Qual é o comando correto?", "opts": ["df.drop('Salário', axis=1)", "df.drop('Salário', axis=0)", "df.delete('Salário')", "df.remove('Salário', axis=1)"], "ans": "df.drop('Salário', axis=1)"},
    {"q": "Qual a diferença entre loc e iloc no Pandas?", "opts": ["loc filtra texto; iloc números.", "loc usa rótulos (nomes); iloc usa índices numéricos (posições).", "Não há diferença.", "loc é só para Machine Learning."], "ans": "loc usa rótulos (nomes); iloc usa índices numéricos (posições)."},
    {"q": "Como preencher valores nulos (NaN) com o número 0?", "opts": ["df.drop_na(0)", "df.replace_null(0)", "df.fillna(0)", "df.zeros()"], "ans": "df.fillna(0)"},
    {"q": "O método `groupby()` é usado junto com qual tipo de função?", "opts": ["Visualização (ex: plot).", "Agregação (ex: sum, mean).", "Machine learning.", "Exclusão de dados."], "ans": "Agregação (ex: sum, mean)."},
    {"q": "O que o atributo `df.shape` retorna?", "opts": ["Tamanho em bytes.", "Tupla com quantidade de (linhas, colunas).", "As 5 primeiras linhas.", "Formato geométrico."], "ans": "Tupla com quantidade de (linhas, colunas)."},
    {"q": "Para juntar dois DataFrames usando uma coluna em comum (estilo PROCV), usamos:", "opts": ["df.concat()", "df.append()", "df.merge()", "df.group()"], "ans": "df.merge()"},
    {"q": "Para contar quantas vezes cada valor único aparece em uma coluna, usamos:", "opts": ["value_counts()", "count_values()", "unique()", "sum()"], "ans": "value_counts()"},
    {"q": "O que acontece se aplicarmos o método `dropna()` sem parâmetros?", "opts": ["Apaga colunas numéricas.", "Apaga todas as linhas com pelo menos um valor nulo.", "Substitui por zero.", "Apaga a tabela inteira."], "ans": "Apaga todas as linhas com pelo menos um valor nulo."}
]

fase2_ml = [
    {"q": "Qual a principal diferença do DBSCAN para o K-Means?", "opts": ["DBSCAN precisa do número de clusters (k).", "DBSCAN não acha outliers.", "DBSCAN agrupa por densidade e acha outliers sozinho.", "DBSCAN só funciona para textos."], "ans": "DBSCAN agrupa por densidade e acha outliers sozinho."},
    {"q": "O que é a técnica de Bag of Words (BoW)?", "opts": ["Tradutor de textos.", "Conta a frequência das palavras, ignorando a ordem gramatical.", "Corretor ortográfico.", "Rede neural geradora de texto."], "ans": "Conta a frequência das palavras, ignorando a ordem gramatical."},
    {"q": "Em NLP, o que são 'Stop Words'?", "opts": ["Palavras ofensivas.", "Palavras de pausa no código.", "Palavras muito comuns (e, de, o) que são removidas.", "Pontuações."], "ans": "Palavras muito comuns (e, de, o) que são removidas."},
    {"q": "Se o modelo acerta 100% no treino e erra tudo no teste, aconteceu:", "opts": ["Underfitting", "Overfitting (Superajuste)", "Acurácia Perfeita", "Validação Cruzada"], "ans": "Overfitting (Superajuste)"},
    {"q": "Qual é a função do hiperparâmetro `eps` no DBSCAN?", "opts": ["Distância máxima entre dois pontos para serem vizinhos.", "Quantidade de clusters.", "Taxa de aprendizado.", "Apagar outliers."], "ans": "Distância máxima entre dois pontos para serem vizinhos."},
    {"q": "Qual algoritmo é baseado em múltiplas Árvores de Decisão?", "opts": ["K-Means", "DBSCAN", "Random Forest", "Bag of Words"], "ans": "Random Forest"},
    {"q": "Para que dividimos os dados em 'Treino' e 'Teste'?", "opts": ["Para rodar mais rápido.", "Para treinar em uma parte e testar a generalização em dados inéditos.", "Para dividir a equipe.", "Para apagar nulos no teste."], "ans": "Para treinar em uma parte e testar a generalização em dados inéditos."},
    {"q": "O que é Tokenização em NLP?", "opts": ["Senhas de segurança.", "Dividir um texto em pedaços menores (ex: palavras).", "O mesmo que Bag of Words.", "Apagar Stop Words."], "ans": "Dividir um texto em pedaços menores (ex: palavras)."},
    {"q": "Qual problema seria resolvido com Clusterização?", "opts": ["Prever valor de venda.", "Segmentar clientes com perfis parecidos.", "Classificar spam.", "Prever chuva."], "ans": "Segmentar clientes com perfis parecidos."},
    {"q": "Prever um valor numérico contínuo (ex: faturamento) é:", "opts": ["Classificação", "Clusterização", "Regressão", "NLP"], "ans": "Regressão"}
]

fase3_story = [
    {"q": "Qual o principal objetivo ao se criar uma visualização de dados?", "opts": ["Usar o máximo de cores.", "Mostrar todo o código.", "Comunicar uma mensagem clara para direcionar uma decisão.", "Ocultar dados."], "ans": "Comunicar uma mensagem clara para direcionar uma decisão."},
    {"q": "O que é 'Carga Cognitiva' em um dashboard?", "opts": ["Esforço mental exigido do público para entender a informação.", "Tempo de carregamento.", "Gigabytes do arquivo.", "Custo do projeto."], "ans": "Esforço mental exigido do público para entender a informação."},
    {"q": "Qual gráfico é ruim para comparar mais de 5 categorias?", "opts": ["Barras Horizontais", "Linhas", "Dispersão", "Pizza (Setores)"], "ans": "Pizza (Setores)"},
    {"q": "A 'Limpeza de Dados' serve para:", "opts": ["Apagar dados do servidor.", "Tratar nulos, duplicados e inconsistências antes de criar modelos.", "Fazer gráficos bonitos.", "Instalar o Python."], "ans": "Tratar nulos, duplicados e inconsistências antes de criar modelos."},
    {"q": "O que significa 'Conhecer sua Audiência'?", "opts": ["Ajustar o nível técnico dependendo de quem vai assistir.", "Perguntar o nome de todos.", "Só falar de lucros.", "Usar o mesmo gráfico para todos."], "ans": "Ajustar o nível técnico dependendo de quem vai assistir."},
    {"q": "Qual a melhor prática ao usar cores?", "opts": ["Cores aleatórias.", "Uso estratégico para destacar a informação principal.", "Sempre vermelho e verde.", "Preto e branco."], "ans": "Uso estratégico para destacar a informação principal."},
    {"q": "O que significa 'Declutter'?", "opts": ["Colocar sombras 3D.", "Remover a 'sujeira' visual que não agrega valor aos dados.", "Aumentar a fonte para 50.", "Ocultar legenda."], "ans": "Remover a 'sujeira' visual que não agrega valor aos dados."},
    {"q": "A variável que queremos prever em um modelo é a:", "opts": ["Feature", "Variável Alvo (Target)", "Outlier", "Stop Word"], "ans": "Variável Alvo (Target)"},
    {"q": "O que é 'Stemming'?", "opts": ["Adicionar palavras.", "Reduzir palavras ao radical (correndo -> corr).", "Mudar a cor da palavra.", "Texto em áudio."], "ans": "Reduzir palavras ao radical (correndo -> corr)."},
    {"q": "Gráfico adequado para mostrar evolução no tempo:", "opts": ["Pizza", "Linhas", "Dispersão", "Boxplot"], "ans": "Linhas"}
]

# ==========================================
# FUNÇÃO: RENDERIZAR QUESTÕES
# ==========================================
def renderizar_questoes(lista_questoes, prefixo_chave):
    pontos_fase = 0
    # Criamos 2 colunas para as perguntas não ficarem tão "esticadas" na tela larga
    col1, col2 = st.columns(2)
    
    for i, q in enumerate(lista_questoes):
        # Alterna as perguntas entre a coluna 1 e 2
        coluna_atual = col1 if i % 2 == 0 else col2
        
        with coluna_atual:
            with st.container(border=True):
                st.markdown(f"**{i+1}.** {q['q']}")
                
                chave = f"{prefixo_chave}_{i}"
                if chave not in st.session_state:
                    st.session_state[chave] = None
                    
                resposta = st.radio("Escolha:", q['opts'], key=f"radio_{chave}", index=None, label_visibility="collapsed")
                
                if resposta:
                    if resposta == q['ans']:
                        st.success("✅ Acertou!")
                        pontos_fase += 1
                    else:
                        st.error(f"❌ Errou. Correta: **{q['ans']}**")
    return pontos_fase

# ==========================================
# INTERFACE PRINCIPAL
# ==========================================
st.title("🚀 Hub de Revisão FIAP: Data Analytics")
st.markdown("Bem-vindo(a)! Revise os **exemplos práticos** nos cards coloridos e depois desça para testar seus conhecimentos.")

fase1, fase2, fase3 = st.tabs(["🐼 FASE 1: Pandas", "🤖 FASE 2: ML & NLP", "📊 FASE 3: Storytelling"])

# ----------------- FASE 1: PANDAS -----------------
with fase1:
    st.header("1. O Território do Pandas")
    
    # Linha 1 de Cards Teóricos
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            st.info("🔍 **O Raio-X (`info` vs `describe`)**")
            st.markdown("`info()` mostra colunas, nulos e se é texto/número. `describe()` faz a matemática (média, max).")
            st.code("# Traz tipos de dados e nulos\ndf.info()\n\n# Traz média, min, max, quartis\ndf.describe()", language="python")
            
    with c2:
        with st.container(border=True):
            st.warning("🧭 **Eixos (`axis`)**")
            st.markdown("O maior motivo de erros! **0 = Linhas**, **1 = Colunas**.")
            st.code("# Deleta a COLUNA inteira 'Salario'\ndf.drop('Salario', axis=1)\n\n# Deleta a LINHA de índice 0\ndf.drop(0, axis=0)", language="python")

    with c3:
        with st.container(border=True):
            st.error("🎯 **Filtros (`loc` vs `iloc`)**")
            st.markdown("`loc` busca pelo **Nome** (rótulo). `iloc` busca pela **Posição** (número do índice).")
            st.code("# Pega a linha que se chama 'Brasil'\ndf.loc['Brasil']\n\n# Pega a linha na posição número 0\ndf.iloc[0]", language="python")

    # Linha 2 de Cards Teóricos
    with st.container(border=True):
        st.success("🤝 **Agrupamentos (`groupby`) na prática**")
        st.markdown("Sempre que usar groupby, você precisa de uma função matemática depois (sum, mean, count) para agregar os dados.")
        st.code("# Exemplo prático: Qual estado comprou mais?\ndf.groupby('Estado')['Vendas'].sum()\n\n# Resultado imaginário:\n# SP    50000\n# RJ    35000", language="python")

    st.divider()
    st.subheader("📝 Questões da Fase 1")
    pts1 = renderizar_questoes(fase1_pandas, "f1")

# ----------------- FASE 2: ML & NLP -----------------
with fase2:
    st.header("2. Machine Learning e Linguagem (NLP)")
    
    c1, c2 = st.columns(2)
    
    with c1:
        with st.container(border=True):
            st.info("🧩 **DBSCAN (Agrupamento por Densidade)**")
            st.markdown("Diferente do K-Means, ele acha **outliers sozinho** e não precisa que você diga quantos grupos criar.")
            st.code("# eps = distância máxima para ser vizinho\nfrom sklearn.cluster import DBSCAN\nmodelo = DBSCAN(eps=0.5, min_samples=5)", language="python")
            
        with st.container(border=True):
            st.warning("⚖️ **Treino vs Teste (Overfitting)**")
            st.markdown("Se um aluno decora o gabarito (Treino) ele tira 10. Mas se a prova tiver questões novas (Teste), ele tira 0. Isso é o **Overfitting**.")
            st.code("X_train, X_test, y_train, y_test = \\\ntrain_test_split(X, y, test_size=0.2)", language="python")

    with c2:
        with st.container(border=True):
            st.success("🎒 **A Jornada do Texto (NLP)**")
            st.markdown("Como o computador lê a frase: *'A prova da FIAP é muito justa'*")
            st.code(
                "1. Tokenização: \n['A', 'prova', 'da', 'FIAP', 'é', ...]\n\n"
                "2. Stop Words (jogar o lixo fora): \nRemove 'A', 'da', 'é'.\n\n"
                "3. Bag of Words: \nConta o que sobrou: {'prova':1, 'FIAP':1}", 
                language="python"
            )

    st.divider()
    st.subheader("📝 Questões da Fase 2")
    pts2 = renderizar_questoes(fase2_ml, "f2")

# ----------------- FASE 3: STORYTELLING -----------------
with fase3:
    st.header("3. Data Storytelling e Negócios")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.info("🗑️ **Declutter (Menos é Mais)**")
            st.markdown("Remova fundos coloridos, bordas grossas e dezenas de linhas de grade. Deixe o **dado** respirar e brilhar.")
    with c2:
        with st.container(border=True):
            st.warning("🧠 **Carga Cognitiva**")
            st.markdown("Se o diretor precisa de 5 minutos para entender seu gráfico, a carga cognitiva está muito alta. Gráficos de pizza com 20 fatias são o maior exemplo disso.")
    with c3:
        with st.container(border=True):
            st.success("🎨 **Uso da Cor**")
            st.markdown("Não faça um 'arco-íris'. Use cores neutras (cinza) para o contexto geral e **uma cor forte** para destacar a informação principal.")

    st.divider()
    st.subheader("📝 Questões da Fase 3")
    pts3 = renderizar_questoes(fase3_story, "f3")

# ==========================================
# PAINEL DE PONTUAÇÃO (BARRA LATERAL)
# ==========================================
total_pontos = pts1 + pts2 + pts3
with st.sidebar:
    st.header("🏆 Seu Desempenho")
    
    # Estilizando os placares na lateral
    st.metric(label="🐼 Pandas", value=f"{pts1}/10")
    st.metric(label="🤖 ML & NLP", value=f"{pts2}/10")
    st.metric(label="📊 Storytelling", value=f"{pts3}/10")
    
    st.divider()
    st.markdown(f"### Pontuação Final: **{total_pontos}/30**")
    
    if total_pontos == 30:
        st.success("PERFEITO! Você 'gabaritou' o simulado! 🎉")
        st.balloons()
    elif total_pontos > 20:
        st.info("Mandou muito bem! Quase lá. Continue revisando as dicas.")
    elif total_pontos > 0:
        st.warning("Você está no caminho! Leia os exemplos práticos antes de responder.")
