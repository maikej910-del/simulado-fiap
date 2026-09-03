import streamlit as st

st.set_page_config(page_title="FIAP Arcade Data", page_icon="🕹️", layout="wide")

# ==========================================
# FUNÇÕES DE RENDERIZAÇÃO DOS CARDS
# ==========================================
def renderizar_questoes(lista_questoes, prefixo):
    pontos = 0
    # Duas colunas para os cards ficarem lado a lado e a página não ficar infinita
    col1, col2 = st.columns(2)
    
    for i, q in enumerate(lista_questoes):
        coluna_atual = col1 if i % 2 == 0 else col2
        
        with coluna_atual:
            with st.container(border=True):
                st.markdown(f"### 🎴 Questão {i+1}")
                st.markdown(f"**{q['q']}**")
                
                chave = f"{prefixo}_{i}"
                if chave not in st.session_state:
                    st.session_state[chave] = None
                
                resposta = st.radio(
                    "Sua resposta:", 
                    q['opts'], 
                    key=f"rad_{chave}", 
                    index=None,
                    label_visibility="collapsed"
                )
                
                if resposta:
                    if resposta == q['ans']:
                        st.success("✅ **Correto!** " + q.get('exp', ''))
                        pontos += 1
                    else:
                        st.error(f"❌ **Errou.** A resposta certa é: **{q['ans']}**")
    return pontos

# ==========================================
# AS 30 QUESTÕES COMPLETAS
# ==========================================
fase1_pandas = [
    {"q": "O que a função `describe()` faz em um DataFrame do Pandas?", "opts": ["Lista os tipos de dados de cada coluna.", "Gera um resumo estatístico das colunas numéricas.", "Descreve as 5 primeiras linhas.", "Remove os valores nulos."], "ans": "Gera um resumo estatístico das colunas numéricas.", "exp": "Calcula média, quartis, mínimo e máximo."},
    {"q": "Para verificar rapidamente se existem valores nulos e quais são os tipos de dados, qual método é indicado?", "opts": ["df.shape", "df.describe()", "df.info()", "df.head()"], "ans": "df.info()", "exp": "O info() é o raio-x estrutural da tabela."},
    {"q": "Você quer apagar a coluna 'Salário'. Qual é o comando correto?", "opts": ["df.drop('Salário', axis=1)", "df.drop('Salário', axis=0)", "df.delete('Salário')", "df.remove('Salário', axis=1)"], "ans": "df.drop('Salário', axis=1)", "exp": "axis=1 foca nas colunas. axis=0 nas linhas."},
    {"q": "Qual a diferença entre loc e iloc no Pandas?", "opts": ["loc filtra texto; iloc números.", "loc usa rótulos (nomes); iloc usa índices numéricos (posições).", "Não há diferença.", "loc é só para Machine Learning."], "ans": "loc usa rótulos (nomes); iloc usa índices numéricos (posições).", "exp": "iloc significa 'index location'."},
    {"q": "Como você preenche valores nulos (NaN) com o número 0?", "opts": ["df.drop_na(0)", "df.replace_null(0)", "df.fillna(0)", "df.zeros()"], "ans": "df.fillna(0)", "exp": "fillna preenche os 'Not a Number'."},
    {"q": "O método `groupby()` é usado junto com qual tipo de função?", "opts": ["Visualização (ex: plot).", "Agregação (ex: sum, mean).", "Machine learning.", "Exclusão de dados."], "ans": "Agregação (ex: sum, mean).", "exp": "Sempre agregamos após agrupar."},
    {"q": "O que o atributo `df.shape` retorna?", "opts": ["Tamanho em bytes do arquivo.", "Tupla com quantidade de (linhas, colunas).", "As 5 primeiras linhas.", "Formato geométrico."], "ans": "Tupla com quantidade de (linhas, colunas).", "exp": "Retorna o formato da matriz."},
    {"q": "Para juntar dois DataFrames usando uma coluna em comum (estilo PROCV), usamos:", "opts": ["df.concat()", "df.append()", "df.merge()", "df.group()"], "ans": "df.merge()", "exp": "Equivalente ao JOIN em banco de dados."},
    {"q": "Para contar quantas vezes cada valor único aparece em uma coluna, usamos:", "opts": ["value_counts()", "count_values()", "unique()", "sum()"], "ans": "value_counts()", "exp": "Gera a frequência absoluta de categorias."},
    {"q": "O que acontece se aplicarmos o método `dropna()` sem parâmetros?", "opts": ["Apaga colunas numéricas.", "Apaga todas as linhas com pelo menos um valor nulo.", "Substitui por zero.", "Apaga a tabela inteira."], "ans": "Apaga todas as linhas com pelo menos um valor nulo.", "exp": "Usa axis=0 e 'how=any' por padrão."}
]

fase2_ml = [
    {"q": "Qual a principal diferença do DBSCAN para o K-Means?", "opts": ["DBSCAN precisa do número de clusters (k).", "DBSCAN não acha outliers.", "DBSCAN agrupa por densidade e acha outliers sozinho.", "DBSCAN só funciona para textos."], "ans": "DBSCAN agrupa por densidade e acha outliers sozinho.", "exp": "Não exige declarar a quantidade de grupos antes."},
    {"q": "O que é a técnica de Bag of Words (BoW)?", "opts": ["Tradutor de textos.", "Conta a frequência das palavras, ignorando a ordem gramatical.", "Corretor ortográfico.", "Rede neural geradora de texto."], "ans": "Conta a frequência das palavras, ignorando a ordem gramatical.", "exp": "Transforma palavras em vetores numéricos."},
    {"q": "Em NLP, o que são 'Stop Words'?", "opts": ["Palavras ofensivas.", "Palavras de pausa no código.", "Palavras muito comuns (e, de, o) que são removidas.", "Pontuações."], "ans": "Palavras muito comuns (e, de, o) que são removidas.", "exp": "Removidas para diminuir o ruído dos dados."},
    {"q": "Se o modelo acerta 100% no treino e erra tudo no teste, aconteceu:", "opts": ["Underfitting", "Overfitting (Superajuste)", "Acurácia Perfeita", "Validação Cruzada"], "ans": "Overfitting (Superajuste)", "exp": "O modelo apenas 'decorou' a resposta."},
    {"q": "Qual é a função do hiperparâmetro `eps` no DBSCAN?", "opts": ["Distância máxima entre dois pontos para serem vizinhos.", "Quantidade de clusters.", "Taxa de aprendizado.", "Apagar outliers."], "ans": "Distância máxima entre dois pontos para serem vizinhos.", "exp": "Define o raio do 'círculo' de densidade."},
    {"q": "Qual algoritmo é baseado em múltiplas Árvores de Decisão?", "opts": ["K-Means", "DBSCAN", "Random Forest", "Bag of Words"], "ans": "Random Forest", "exp": "Várias árvores tomam decisões juntas e ocorre uma votação (Ensemble)."},
    {"q": "Para que dividimos os dados em 'Treino' e 'Teste'?", "opts": ["Para rodar mais rápido.", "Para treinar em uma parte e testar a generalização em dados inéditos.", "Para dividir a equipe.", "Para apagar nulos no teste."], "ans": "Para treinar em uma parte e testar a generalização em dados inéditos.", "exp": "Para evitar que o modelo decore os dados (Overfitting)."},
    {"q": "O que é Tokenização em NLP?", "opts": ["Senhas de segurança.", "Dividir um texto em pedaços menores (ex: palavras).", "O mesmo que Bag of Words.", "Apagar Stop Words."], "ans": "Dividir um texto em pedaços menores (ex: palavras).", "exp": "Uma frase vira uma lista de palavras (tokens)."},
    {"q": "Qual problema seria resolvido com Clusterização?", "opts": ["Prever valor de venda.", "Segmentar clientes com perfis parecidos.", "Classificar spam.", "Prever chuva."], "ans": "Segmentar clientes com perfis parecidos.", "exp": "Clusterização agrupa dados semelhantes, sem alvo pré-definido."},
    {"q": "Prever um valor numérico contínuo (ex: faturamento) é problema de:", "opts": ["Classificação", "Clusterização", "Regressão", "NLP"], "ans": "Regressão", "exp": "Regressão prevê números contínuos, classificação prevê categorias."}
]

fase3_story = [
    {"q": "Qual o principal objetivo ao se criar uma visualização de dados?", "opts": ["Usar o máximo de cores.", "Mostrar todo o código.", "Comunicar uma mensagem clara para direcionar uma decisão.", "Ocultar dados."], "ans": "Comunicar uma mensagem clara para direcionar uma decisão.", "exp": "Gráfico bonito sem ação não serve de nada."},
    {"q": "O que é 'Carga Cognitiva' em um dashboard?", "opts": ["Esforço mental exigido do público para entender a informação.", "Tempo de carregamento.", "Gigabytes do arquivo.", "Custo do projeto."], "ans": "Esforço mental exigido do público para entender a informação.", "exp": "Bons gráficos diminuem a carga cognitiva."},
    {"q": "Qual gráfico é ruim para comparar mais de 5 categorias?", "opts": ["Barras Horizontais", "Linhas", "Dispersão", "Pizza (Setores)"], "ans": "Pizza (Setores)", "exp": "O cérebro tem dificuldade em comparar áreas e ângulos pequenos."},
    {"q": "A 'Limpeza de Dados' serve para:", "opts": ["Apagar dados do servidor.", "Tratar nulos, duplicados e inconsistências antes de criar modelos.", "Fazer gráficos bonitos.", "Instalar o Python."], "ans": "Tratar nulos, duplicados e inconsistências antes de criar modelos.", "exp": "Lixo entra, lixo sai. A base do bom modelo é um bom dado."},
    {"q": "O que significa 'Conhecer sua Audiência'?", "opts": ["Ajustar o nível técnico dependendo de quem vai assistir.", "Perguntar o nome de todos.", "Só falar de lucros.", "Usar o mesmo gráfico para todos."], "ans": "Ajustar o nível técnico dependendo de quem vai assistir.", "exp": "Diretoria quer números de negócio, Engenheiros querem métricas técnicas."},
    {"q": "Qual a melhor prática ao usar cores?", "opts": ["Cores aleatórias.", "Uso estratégico para destacar a informação principal.", "Sempre vermelho e verde.", "Preto e branco."], "ans": "Uso estratégico para destacar a informação principal.", "exp": "Chama-se 'Preattentive Attributes' (Atributos Pré-atentivos)."},
    {"q": "O que significa 'Declutter'?", "opts": ["Colocar sombras 3D.", "Remover a 'sujeira' visual que não agrega valor aos dados.", "Aumentar a fonte para 50.", "Ocultar legenda."], "ans": "Remover a 'sujeira' visual que não agrega valor aos dados.", "exp": "Eliminar linhas de grade excessivas, bordas marcadas, etc."},
    {"q": "A variável que queremos prever em um modelo é chamada de:", "opts": ["Feature", "Variável Alvo (Target)", "Outlier", "Stop Word"], "ans": "Variável Alvo (Target)", "exp": "A coluna que será prevista pelo modelo (y)."},
    {"q": "O que é 'Stemming'?", "opts": ["Adicionar palavras.", "Reduzir palavras ao radical (correndo -> corr).", "Mudar a cor da palavra.", "Texto em áudio."], "ans": "Reduzir palavras ao radical (correndo -> corr).", "exp": "Ajuda o modelo a entender que correr, correndo e corrida tratam do mesmo tema."},
    {"q": "Gráfico mais adequado para mostrar evolução ao longo do tempo:", "opts": ["Pizza", "Linhas", "Dispersão", "Boxplot"], "ans": "Linhas", "exp": "O eixo X com tempo e a linha mostrando as variações (séries temporais)."}
]

# ==========================================
# INTERFACE PRINCIPAL DO APP
# ==========================================
st.title("🕹️ Arcade de Revisão: FIAP Data Analytics")
st.markdown("Bem-vindo ao fliperama de dados! Teste seus reflexos nos **Minigames** e resolva os **Cards de Prova** (30 questões no total).")

aba1, aba2, aba3 = st.tabs(["🐼 Nível 1: Pandas", "🤖 Nível 2: ML & NLP", "📊 Nível 3: Storytelling"])

# ----------------- NÍVEL 1: PANDAS -----------------
with aba1:
    st.header("Nível 1: O Mestre do Pandas")
    
    st.markdown("### 🎮 Minigame 1: Verdadeiro ou Falso")
    st.write("Teste seu instinto! Selecione V ou F:")
    
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**1. O `dropna()` por padrão apaga a linha inteira se achar algum nulo.**")
            vf1 = st.radio("Q1", ["V", "F"], horizontal=True, key="vf1", index=None, label_visibility="collapsed")
            if vf1 == "V": st.success("Correto! Ele apaga no axis=0.")
            elif vf1 == "F": st.error("Errou! A afirmação é verdadeira.")
            
        with c2:
            st.markdown("**2. Para preencher nulos com zero, usamos `df.zero()`**")
            vf2 = st.radio("Q2", ["V", "F"], horizontal=True, key="vf2", index=None, label_visibility="collapsed")
            if vf2 == "F": st.success("Correto! Usamos `df.fillna(0)`.")
            elif vf2 == "V": st.error("Errou! A função certa é fillna.")
            
        with c3:
            st.markdown("**3. `axis=0` diz para o Pandas olhar para as Colunas.**")
            vf3 = st.radio("Q3", ["V", "F"], horizontal=True, key="vf3", index=None, label_visibility="collapsed")
            if vf3 == "F": st.success("Correto! axis=0 = Linhas, axis=1 = Colunas.")
            elif vf3 == "V": st.error("Errou! axis=0 é para Linhas.")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (10 Questões)")
    pts_f1 = renderizar_questoes(fase1_pandas, "p")

# ----------------- NÍVEL 2: ML & NLP -----------------
with aba2:
    st.header("Nível 2: Inteligência Artificial")
    
    st.markdown("### 🎮 Minigame 2: Complete o Código (Drag & Drop)")
    st.write("Qual palavra preenche a lacuna do código Python?")
    
    with st.container(border=True):
        st.code("from sklearn.cluster import DBSCAN\n\n# Criando o modelo\nmodelo = DBSCAN(________=0.5, min_samples=5)", language="python")
        lacuna1 = st.selectbox("Qual é a lacuna?", ["Selecione...", "k", "eps", "target"])
        if lacuna1 == "eps": 
            st.success("✅ Boa! 'eps' (epsilon) define o limite de distância para formar grupos.")
        elif lacuna1 != "Selecione...": 
            st.error("❌ Errou. O DBSCAN usa 'eps'.")
                
    with st.container(border=True):
        st.code("# Dividindo os dados para evitar Overfitting\nX_train, X_test, y_train, y_test = ________(X, y, test_size=0.2)", language="python")
        lacuna2 = st.selectbox("Qual função divide os dados?", ["Selecione...", "train_test_split", "groupby", "merge"])
        if lacuna2 == "train_test_split": 
            st.success("✅ Perfeito!")
        elif lacuna2 != "Selecione...": 
            st.error("❌ Errou. É o train_test_split do pacote sklearn.")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (10 Questões)")
    pts_f2 = renderizar_questoes(fase2_ml, "m")

# ----------------- NÍVEL 3: STORYTELLING -----------------
with aba3:
    st.header("Nível 3: Data Storytelling")
    
    st.markdown("### 🎮 Minigame 3: Ligue as Colunas")
    st.write("Ligue os termos com as suas definições corretas. Ao acertar todas, celebre!")
    
    with st.container(border=True):
        col_esq, col_dir = st.columns(2)
        
        with col_esq:
            st.info("💡 **A. Carga Cognitiva**")
            st.warning("💡 **B. Declutter**")
            st.error("💡 **C. Target**")
            
        with col_dir:
            res1 = st.selectbox("1. A variável que queremos prever no Machine Learning:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            res2 = st.selectbox("2. Limpar o gráfico de linhas e cores desnecessárias:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            res3 = st.selectbox("3. O esforço mental para entender a informação:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            
            if res1 == "C. Target" and res2 == "B. Declutter" and res3 == "A. Carga Cognitiva":
                st.balloons()
                st.success("🏆 Você ligou tudo perfeitamente!")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (10 Questões)")
    pts_f3 = renderizar_questoes(fase3_story, "s")

# ==========================================
# PAINEL LATERAL DE PROGRESSO (O "HUD" do Jogador)
# ==========================================
total = pts_f1 + pts_f2 + pts_f3
max_pts = len(fase1_pandas) + len(fase2_ml) + len(fase3_story)

with st.sidebar:
    st.header("📊 Seu Placar")
    st.write("Resolva os cards nas abas para pontuar!")
    
    # Barra animada de progresso
    st.progress(total / max_pts if max_pts > 0 else 0)
    
    st.metric(label="🐼 Cards Pandas", value=f"{pts_f1}/10")
    st.metric(label="🤖 Cards ML/NLP", value=f"{pts_f2}/10")
    st.metric(label="📊 Cards Storytelling", value=f"{pts_f3}/10")
    
    st.divider()
    st.subheader(f"Total: {total}/30")
    
    if total == 30:
        st.success("Você gabaritou tudo! Pronto para a prova. 🚀")
