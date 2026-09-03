import streamlit as st
import time

st.set_page_config(page_title="FIAP Arcade Data", page_icon="🕹️", layout="wide")

# ==========================================
# FUNÇÕES DE RENDERIZAÇÃO DOS CARDS
# ==========================================
def renderizar_questoes(lista_questoes, prefixo):
    pontos = 0
    # Duas colunas para os cards não ficarem gigantes na tela
    col1, col2 = st.columns(2)
    
    for i, q in enumerate(lista_questoes):
        coluna_atual = col1 if i % 2 == 0 else col2
        
        with coluna_atual:
            # UM CARD PARA CADA QUESTÃO (Usando container e sombra)
            with st.container(border=True):
                st.markdown(f"### 🎴 Questão {i+1}")
                st.markdown(f"**{q['q']}**")
                
                chave = f"{prefixo}_{i}"
                if chave not in st.session_state:
                    st.session_state[chave] = None
                
                # Radio buttons como opções do card
                resposta = st.radio(
                    "Sua resposta:", 
                    q['opts'], 
                    key=f"rad_{chave}", 
                    index=None,
                    label_visibility="collapsed"
                )
                
                # Feedback interativo no próprio card
                if resposta:
                    if resposta == q['ans']:
                        st.success("✅ **Correto!** " + q.get('exp', ''))
                        pontos += 1
                    else:
                        st.error(f"❌ **Errou.** A certa é: **{q['ans']}**")
    return pontos

# ==========================================
# BANCO DE DADOS (15 Múltipla Escolha p/ UI ficar limpa + Jogos)
# ==========================================
fase1_pandas = [
    {"q": "O que a função `describe()` faz em um DataFrame?", "opts": ["Lista tipos de dados.", "Gera um resumo estatístico das colunas numéricas.", "Apaga dados nulos."], "ans": "Gera um resumo estatístico das colunas numéricas.", "exp": "Calcula média, quartis, min e max na hora!"},
    {"q": "Para verificar rapidamente se existem valores nulos e quais são os tipos de dados:", "opts": ["df.shape()", "df.describe()", "df.info()"], "ans": "df.info()", "exp": "O info() é o raio-x estrutural da tabela."},
    {"q": "Você quer apagar a coluna 'Salário'. Qual comando?", "opts": ["df.drop('Salário', axis=1)", "df.drop('Salário', axis=0)", "df.delete('Salário')"], "ans": "df.drop('Salário', axis=1)", "exp": "Lembre-se: axis=1 é para colunas, axis=0 para linhas."},
    {"q": "Qual a diferença entre loc e iloc?", "opts": ["loc usa rótulos (nomes); iloc usa índices numéricos.", "loc filtra texto; iloc números.", "Não há diferença."], "ans": "loc usa rótulos (nomes); iloc usa índices numéricos.", "exp": "i-loc = index location (posição numérica)."}
]

fase2_ml = [
    {"q": "Qual a principal diferença do DBSCAN para o K-Means?", "opts": ["DBSCAN precisa de 'k'.", "DBSCAN agrupa por densidade e acha outliers sozinho.", "K-Means lida melhor com ruídos."], "ans": "DBSCAN agrupa por densidade e acha outliers sozinho."},
    {"q": "O que é Bag of Words (BoW)?", "opts": ["Tradutor.", "Conta a frequência das palavras ignorando a ordem gramatical.", "Rede neural profunda."], "ans": "Conta a frequência das palavras ignorando a ordem gramatical."},
    {"q": "Se o modelo acerta 100% no treino e erra no teste, aconteceu:", "opts": ["Underfitting", "Overfitting", "Validação perfeita"], "ans": "Overfitting", "exp": "O modelo decorou os dados, mas não aprendeu a regra."},
    {"q": "O que são 'Stop Words' em NLP?", "opts": ["Palavras ofensivas.", "Palavras muito comuns (e, de, o) que são removidas.", "Pontuações isoladas."], "ans": "Palavras muito comuns (e, de, o) que são removidas."}
]

fase3_story = [
    {"q": "Qual o principal objetivo do Data Storytelling?", "opts": ["Usar o máximo de cores.", "Comunicar uma mensagem clara para direcionar uma decisão.", "Ocultar dados ruins."], "ans": "Comunicar uma mensagem clara para direcionar uma decisão."},
    {"q": "O que é 'Carga Cognitiva' em um dashboard?", "opts": ["Esforço mental exigido para entender a informação.", "Tempo de carregamento.", "Gigabytes do arquivo."], "ans": "Esforço mental exigido para entender a informação."},
    {"q": "Qual gráfico é ruim para comparar mais de 5 categorias?", "opts": ["Barras", "Dispersão", "Pizza (Setores)"], "ans": "Pizza (Setores)", "exp": "O cérebro humano é péssimo avaliando pequenos ângulos em fatias."},
    {"q": "O que significa 'Declutter'?", "opts": ["Sombras 3D.", "Remover a 'sujeira' visual (linhas e bordas excessivas).", "Ocultar legenda."], "ans": "Remover a 'sujeira' visual (linhas e bordas excessivas)."}
]

# ==========================================
# INTERFACE PRINCIPAL
# ==========================================
st.title("🕹️ Arcade de Revisão: FIAP Data Analytics")
st.markdown("Bem-vindo ao fliperama de dados! Teste seus reflexos nos **Minigames** e resolva os **Cards de Questões**.")

aba1, aba2, aba3 = st.tabs(["🐼 Nível 1: Pandas", "🤖 Nível 2: ML & NLP", "📊 Nível 3: Storytelling"])

# ----------------- NÍVEL 1: PANDAS -----------------
with aba1:
    st.header("Nível 1: O Mestre do Pandas")
    
    st.markdown("### 🎮 Minigame 1: Verdadeiro ou Falso")
    st.write("Teste seu instinto! Selecione V ou F:")
    
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**1. O comando `dropna()` por padrão apaga qualquer linha que tenha pelo menos um valor nulo.**")
            vf1 = st.radio("Q1", ["V", "F"], horizontal=True, key="vf1", index=None, label_visibility="collapsed")
            if vf1 == "V": st.success("Correto! Ele usa tolerância 'any' no axis 0.")
            elif vf1 == "F": st.error("Errou! A afirmação é verdadeira.")
            
        with c2:
            st.markdown("**2. Se eu quiser preencher valores nulos com zero, uso o comando `df.zero()`**")
            vf2 = st.radio("Q2", ["V", "F"], horizontal=True, key="vf2", index=None, label_visibility="collapsed")
            if vf2 == "F": st.success("Correto! O certo é `df.fillna(0)`.")
            elif vf2 == "V": st.error("Errou! A função é `fillna()`.")
            
        with c3:
            st.markdown("**3. `axis=0` significa que o Pandas vai olhar para as Colunas.**")
            vf3 = st.radio("Q3", ["V", "F"], horizontal=True, key="vf3", index=None, label_visibility="collapsed")
            if vf3 == "F": st.success("Correto! axis=0 = Linhas, axis=1 = Colunas.")
            elif vf3 == "V": st.error("Errou! axis=0 olha para as Linhas.")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (Pandas)")
    pts_f1 = renderizar_questoes(fase1_pandas, "p")

# ----------------- NÍVEL 2: ML & NLP -----------------
with aba2:
    st.header("Nível 2: Inteligência Artificial")
    
    st.markdown("### 🎮 Minigame 2: Complete o Código (Drag & Drop Mental)")
    st.write("Complete as lacunas do código Python com a palavra certa:")
    
    with st.container(border=True):
        st.code("from sklearn.cluster import DBSCAN\n\n# Criando o modelo\nmodelo = DBSCAN(________=0.5, min_samples=5)", language="python")
        c1, c2 = st.columns(2)
        with c1:
            lacuna1 = st.selectbox("Qual é a lacuna?", ["Selecione...", "k", "eps", "target"])
            if lacuna1 == "eps": 
                st.success("✅ Boa! 'eps' (epsilon) define a distância para formar grupos.")
            elif lacuna1 != "Selecione...": 
                st.error("❌ Errou. O DBSCAN usa 'eps' (raio de busca).")
                
    with st.container(border=True):
        st.code("# Dividindo os dados para evitar Overfitting\nX_train, X_test, y_train, y_test = ________(X, y, test_size=0.2)", language="python")
        c1, c2 = st.columns(2)
        with c1:
            lacuna2 = st.selectbox("Qual função divide os dados?", ["Selecione...", "train_test_split", "groupby", "merge"])
            if lacuna2 == "train_test_split": 
                st.success("✅ Perfeito!")
            elif lacuna2 != "Selecione...": 
                st.error("❌ Errou. Usamos o train_test_split do Sklearn.")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (ML & NLP)")
    pts_f2 = renderizar_questoes(fase2_ml, "m")

# ----------------- NÍVEL 3: STORYTELLING -----------------
with aba3:
    st.header("Nível 3: Data Storytelling")
    
    st.markdown("### 🎮 Minigame 3: Ligue as Colunas")
    st.write("Ache a correspondência exata de ferramentas e conceitos:")
    
    with st.container(border=True):
        col_esq, col_dir = st.columns(2)
        
        with col_esq:
            st.info("💡 **A. Carga Cognitiva**")
            st.warning("💡 **B. Declutter**")
            st.error("💡 **C. Target**")
            
        with col_dir:
            res1 = st.selectbox("1. A variável que queremos prever em ML:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            res2 = st.selectbox("2. Limpar tudo que não é dado no gráfico:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            res3 = st.selectbox("3. O esforço mental do usuário ao ver o painel:", ["Selecione...", "A. Carga Cognitiva", "B. Declutter", "C. Target"])
            
            if res1 == "C. Target" and res2 == "B. Declutter" and res3 == "A. Carga Cognitiva":
                st.balloons()
                st.success("🏆 Você ligou tudo perfeitamente!")

    st.divider()
    st.markdown("### 🎴 Cards de Prova (Storytelling)")
    pts_f3 = renderizar_questoes(fase3_story, "s")

# ==========================================
# PAINEL LATERAL DE PROGRESSO
# ==========================================
total = pts_f1 + pts_f2 + pts_f3
max_pts = len(fase1_pandas) + len(fase2_ml) + len(fase3_story)

with st.sidebar:
    st.header("📊 Seu Desempenho")
    st.write("Acerte os Cards de Prova para pontuar:")
    st.progress(total / max_pts if max_pts > 0 else 0)
    
    st.metric(label="🐼 Cards Pandas", value=f"{pts_f1}/{len(fase1_pandas)}")
    st.metric(label="🤖 Cards ML/NLP", value=f"{pts_f2}/{len(fase2_ml)}")
    st.metric(label="📊 Cards Storytelling", value=f"{pts_f3}/{len(fase3_story)}")
    
    st.divider()
    if total == max_pts:
        st.success("Você gabaritou os cards da prova! 🚀")
