import streamlit as st
import time

st.set_page_config(page_title="FIAP Mega Simulado", page_icon="🎮", layout="centered")

# ==========================================
# BANCO DE QUESTÕES (Dividido por Fases)
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
# FUNÇÃO PARA RENDERIZAR QUESTÕES COM CARDS
# ==========================================
def renderizar_questoes(lista_questoes, prefixo_chave):
    pontos_fase = 0
    for i, q in enumerate(lista_questoes):
        # Cria um "card" visual para cada pergunta usando container
        with st.container(border=True):
            st.markdown(f"**Questão {i+1}:** {q['q']}")
            
            # Gerencia o estado de resposta desta pergunta específica
            chave = f"{prefixo_chave}_{i}"
            if chave not in st.session_state:
                st.session_state[chave] = None
                
            resposta = st.radio("Escolha:", q['opts'], key=f"radio_{chave}", index=None, label_visibility="collapsed")
            
            if resposta:
                if resposta == q['ans']:
                    st.success("✅ **Correto!** Mandou bem.")
                    pontos_fase += 1
                else:
                    st.error(f"❌ **Errou.** A correta era: **{q['ans']}**")
    return pontos_fase

# ==========================================
# INTERFACE PRINCIPAL
# ==========================================
st.title("🎮 FIAP: Mega Simulado")
st.write("Navegue pelas abas abaixo como se fossem Fases de um jogo. Leia os cards de teoria e detone nas questões!")

# Criando as 3 Fases (Abas)
fase1, fase2, fase3 = st.tabs(["🐼 FASE 1: Pandas", "🤖 FASE 2: ML & NLP", "📊 FASE 3: Storytelling"])

# ----------------- FASE 1 -----------------
with fase1:
    st.header("O Território do Pandas")
    st.write("Abra os cards abaixo para relembrar a prática antes de responder:")
    
    # Cards Dinâmicos de Teoria (Expanders)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🔍 O que faz o `info()`?", expanded=False):
            st.info("**O Raio-X Estrutural:**\nMostra o 'esqueleto' da sua tabela: quantas colunas existem, o tipo de cada dado (texto, número) e se há dados nulos faltando.")
    with col2:
        with st.expander("🧮 O que faz o `describe()`?", expanded=False):
            st.warning("**O Raio-X Matemático:**\nPega as colunas numéricas e cospe a estatística de uma vez: média, valor mínimo, valor máximo e quartis (25%, 50%, 75%).")
            
    with st.expander("🧭 O temido 'axis' (Eixos)", expanded=False):
        st.error("**0 = Linhas | 1 = Colunas**\nAo usar `df.drop('Idade', axis=1)`, o Pandas olha para o horizonte (colunas) e deleta a coluna inteira. Se usasse `axis=0`, ele procuraria uma linha chamada 'Idade' e daria erro.")

    st.divider()
    st.subheader("📝 Desafio da Fase 1")
    pts1 = renderizar_questoes(fase1_pandas, "f1")

# ----------------- FASE 2 -----------------
with fase2:
    st.header("Machine Learning e NLP")
    
    with st.expander("🎯 Entendendo o DBSCAN", expanded=False):
        st.success("**Como ele pensa?**\nEle acha padrões por proximidade (densidade). Pontos muito próximos viram um Cluster (grupo). Um ponto isolado lá longe é marcado como Ruído (Outlier). Não precisa dizer a ele quantos grupos formar!")
        
    with st.expander("🎒 Bag of Words & Stop Words", expanded=False):
        st.info("**Bag of Words:** Joga a frase num saco e devolve a contagem: `{'prova': 2, 'boa': 1}`. A ordem não importa.\n\n**Stop Words:** Joga no lixo palavras como 'a', 'o', 'de', porque elas não ajudam a entender o sentimento do texto.")

    st.divider()
    st.subheader("📝 Desafio da Fase 2")
    pts2 = renderizar_questoes(fase2_ml, "f2")

# ----------------- FASE 3 -----------------
with fase3:
    st.header("Visualização e Jogo Final")
    
    st.markdown("### 🎮 Mini-game: Ligue as Colunas")
    st.write("Antes das perguntas, prove que seu reflexo está bom!")
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**1.** `axis=1`\n\n**2.** Storytelling\n\n**3.** `describe()`")
        with c2:
            r1 = st.selectbox("O que faz o axis=1?", ["Selecione...", "Mira nas colunas", "Conta historinha", "Traz a média"], label_visibility="collapsed")
            r2 = st.selectbox("O que é Storytelling?", ["Selecione...", "Mira nas colunas", "Conta historinha", "Traz a média"], label_visibility="collapsed")
            r3 = st.selectbox("O que faz o describe()?", ["Selecione...", "Mira nas colunas", "Conta historinha", "Traz a média"], label_visibility="collapsed")
            
            if r1 == "Mira nas colunas" and r2 == "Conta historinha" and r3 == "Traz a média":
                st.success("✨ Triplo Acerto no Minigame!")
    
    st.divider()
    st.subheader("📝 Desafio da Fase 3")
    pts3 = renderizar_questoes(fase3_story, "f3")

# ==========================================
# PAINEL DE PONTUAÇÃO GERAL (Na barra lateral)
# ==========================================
total_pontos = pts1 + pts2 + pts3
with st.sidebar:
    st.header("🏆 Seu Placar")
    st.metric(label="Fase 1 (Pandas)", value=f"{pts1}/10")
    st.metric(label="Fase 2 (ML & NLP)", value=f"{pts2}/10")
    st.metric(label="Fase 3 (Story)", value=f"{pts3}/10")
    st.divider()
    st.metric(label="PONTUAÇÃO TOTAL", value=f"{total_pontos}/30")
    
    if total_pontos == 30:
        st.success("PERFEITO! Você "gabaritou" o simulado! 🎉")
        st.balloons()
    elif total_pontos > 20:
        st.info("Mandou muito bem! Quase lá.")
