import streamlit as st
import time

# Configuração da página para ficar mais limpa e com cara de app
st.set_page_config(page_title="Duolingo: FIAP Data", page_icon="🦉", layout="centered")

# ==========================================
# BANCO DE QUESTÕES (AS 30 DA PROVA)
# ==========================================
questoes = [
    {"q": "O que a função `describe()` faz em um DataFrame Pandas?", "opts": ["Lista os tipos de dados", "Gera um resumo estatístico das colunas numéricas", "Mostra as 5 primeiras linhas", "Remove os valores nulos"], "ans": "Gera um resumo estatístico das colunas numéricas", "exp": "O describe() calcula média, desvio padrão, min, max e quartis automaticamente."},
    {"q": "Qual método verifica rapidamente valores nulos e tipos de dados?", "opts": ["df.shape", "df.describe()", "df.info()", "df.head()"], "ans": "df.info()", "exp": "O info() é o 'raio-x estrutural' da sua tabela."},
    {"q": "Para excluir a coluna 'Salário', qual parâmetro usamos no drop()?", "opts": ["axis=1", "axis=0", "axis='col'", "axis=None"], "ans": "axis=1", "exp": "axis=1 aponta para as colunas. axis=0 apontaria para as linhas."},
    {"q": "Qual a diferença entre loc e iloc?", "opts": ["loc filtra texto; iloc número", "loc usa rótulos (nomes); iloc usa índices numéricos", "Não há diferença", "iloc apaga linhas"], "ans": "loc usa rótulos (nomes); iloc usa índices numéricos", "exp": "i-loc = index location (posição 0, 1, 2...). loc = nome da linha/coluna."},
    {"q": "Como preencher valores nulos (NaN) com o número 0?", "opts": ["df.drop_na(0)", "df.replace_null(0)", "df.fillna(0)", "df.zeros()"], "ans": "df.fillna(0)", "exp": "fillna() é a função nativa do Pandas para preencher 'Not a Number' (NaN)."},
    {"q": "O método `groupby()` é usado em conjunto com qual tipo de função?", "opts": ["Agregação (sum, mean)", "Visualização (plot)", "Machine Learning", "Exclusão"], "ans": "Agregação (sum, mean)", "exp": "Quando você agrupa (ex: por estado), precisa agregar o resultado (ex: somar as vendas)."},
    {"q": "O que `df.shape` retorna?", "opts": ["Tamanho em bytes", "Tupla com (linhas, colunas)", "As 5 primeiras linhas", "Os tipos de dados"], "ans": "Tupla com (linhas, colunas)", "exp": "Shape mostra o formato da matriz (ex: 1000 linhas, 5 colunas)."},
    {"q": "Para juntar dois DataFrames usando uma coluna em comum (estilo PROCV), usamos:", "opts": ["df.concat()", "df.append()", "df.merge()", "df.group()"], "ans": "df.merge()", "exp": "Merge é o equivalente ao JOIN do SQL ou PROCV do Excel."},
    {"q": "Para contar quantas vezes cada valor único aparece em uma coluna, usamos:", "opts": ["value_counts()", "count_values()", "unique()", "sum()"], "ans": "value_counts()", "exp": "Retorna a frequência absoluta de cada categoria na coluna."},
    {"q": "O que faz o `dropna()` sem parâmetros?", "opts": ["Apaga colunas numéricas", "Apaga todas as linhas com pelo menos um valor nulo", "Substitui nulos por zero", "Apaga a tabela inteira"], "ans": "Apaga todas as linhas com pelo menos um valor nulo", "exp": "Por padrão, ele atua no axis=0 (linhas) e tem a tolerância 'any' (qualquer nulo)."},
    {"q": "O que diferencia o DBSCAN do K-Means?", "opts": ["DBSCAN precisa do número de clusters", "DBSCAN não acha outliers", "DBSCAN agrupa por densidade e acha outliers sozinho", "K-Means é para textos"], "ans": "DBSCAN agrupa por densidade e acha outliers sozinho", "exp": "DBSCAN não precisa que você adivinhe o número de grupos antes!"},
    {"q": "O que é Bag of Words (BoW)?", "opts": ["Tradutor de textos", "Conta a frequência das palavras, ignorando a ordem", "Corretor ortográfico", "Rede neural profunda"], "ans": "Conta a frequência das palavras, ignorando a ordem", "exp": "Transforma texto em vetor numérico contando as aparições de cada palavra."},
    {"q": "O que são Stop Words em NLP?", "opts": ["Palavras ofensivas", "Palavras que pausam o código", "Palavras muito comuns (e, de, o) removidas por não agregarem sentido", "Pontuações"], "ans": "Palavras muito comuns (e, de, o) removidas por não agregarem sentido", "exp": "Remover stop words diminui o 'ruído' e o tamanho dos dados."},
    {"q": "Se o modelo acerta 100% no treino e erra no teste, ocorreu:", "opts": ["Underfitting", "Overfitting (Superajuste)", "Acurácia Perfeita", "Validação Cruzada"], "ans": "Overfitting (Superajuste)", "exp": "O modelo 'decorou' os dados de treino, mas não aprendeu a regra geral."},
    {"q": "Qual a função do hiperparâmetro `eps` no DBSCAN?", "opts": ["Distância máxima entre dois pontos para serem vizinhos", "Quantidade de clusters", "Taxa de erro", "Apagar outliers"], "ans": "Distância máxima entre dois pontos para serem vizinhos", "exp": "O epsilon (eps) define o raio de alcance para procurar vizinhos."},
    {"q": "Qual algoritmo é baseado em múltiplas Árvores de Decisão?", "opts": ["K-Means", "DBSCAN", "Random Forest", "Bag of Words"], "ans": "Random Forest", "exp": "Random Forest (Floresta Aleatória) cria várias árvores e junta o resultado delas."},
    {"q": "Para que dividimos os dados em Treino e Teste?", "opts": ["Para o código rodar rápido", "Para testar a capacidade do modelo em dados inéditos", "Para apagar nulos", "Para criar gráficos"], "ans": "Para testar a capacidade do modelo em dados inéditos", "exp": "Sem os dados de teste, você não sabe se o modelo aprendeu ou só decorou as respostas."},
    {"q": "O que é Tokenização?", "opts": ["Criar senhas", "Dividir texto em pedaços menores (ex: palavras)", "Bag of Words", "Apagar números"], "ans": "Dividir texto em pedaços menores (ex: palavras)", "exp": "É o primeiro passo de NLP: quebrar uma frase inteira em tokens (palavras)."},
    {"q": "Qual problema seria resolvido com Clusterização (DBSCAN)?", "opts": ["Prever valor de casa", "Segmentar clientes com perfis parecidos", "Identificar spam", "Prever chuva"], "ans": "Segmentar clientes com perfis parecidos", "exp": "Clusterização é aprendizado não supervisionado para achar grupos ocultos."},
    {"q": "Prever um valor numérico contínuo (ex: faturamento) é um problema de:", "opts": ["Classificação", "Clusterização", "Regressão", "NLP"], "ans": "Regressão", "exp": "Regressão prevê números contínuos. Classificação prevê categorias (sim/não, gato/cachorro)."},
    {"q": "Qual o principal objetivo do Data Storytelling?", "opts": ["Usar muitas cores", "Mostrar o código feito", "Comunicar mensagem clara para tomada de decisão", "Ocultar dados ruins"], "ans": "Comunicar mensagem clara para tomada de decisão", "exp": "O foco é gerar ação e não apenas mostrar gráficos bonitos."},
    {"q": "O que é 'Carga Cognitiva' em um dashboard?", "opts": ["Esforço mental exigido para entender a informação", "Tempo de carregamento", "Tamanho em GB", "Custo financeiro"], "ans": "Esforço mental exigido para entender a informação", "exp": "Bons dashboards diminuem a carga cognitiva (são fáceis e rápidos de entender)."},
    {"q": "Qual gráfico é ruim para comparar mais de 5 categorias?", "opts": ["Barras", "Linhas", "Dispersão", "Pizza (Setores)"], "ans": "Pizza (Setores)", "exp": "O cérebro humano é péssimo em comparar áreas e ângulos parecidos."},
    {"q": "A Limpeza de Dados (Data Cleaning) serve para:", "opts": ["Apagar o servidor", "Tratar nulos, duplicados e inconsistências", "Fazer gráficos", "Instalar Python"], "ans": "Tratar nulos, duplicados e inconsistências", "exp": "Garbage in, garbage out. Dados sujos geram modelos ruins."},
    {"q": "O que significa 'Conhecer sua Audiência'?", "opts": ["Ajustar o foco e o nível técnico dependendo de quem assiste", "Saber o nome de todos", "Só falar de lucros", "Usar o mesmo gráfico sempre"], "ans": "Ajustar o foco e o nível técnico dependendo de quem assiste", "exp": "A diretoria quer ver o impacto financeiro; os analistas querem ver a precisão do modelo."},
    {"q": "Qual a melhor prática com cores no Storytelling?", "opts": ["Cores aleatórias", "Uso estratégico para destacar a informação principal", "Sempre vermelho e verde", "Preto e branco"], "ans": "Uso estratégico para destacar a informação principal", "exp": "Cores devem ser usadas para guiar o olhar para o insight principal."},
    {"q": "O que é 'Declutter'?", "opts": ["Por bordas 3D", "Remover sujeira visual (linhas, bordas) que não agrega valor", "Aumentar a fonte", "Tirar a legenda"], "ans": "Remover sujeira visual (linhas, bordas) que não agrega valor", "exp": "Menos é mais. Tire tudo que distrai do dado principal."},
    {"q": "A variável que queremos prever em um modelo é chamada de:", "opts": ["Feature", "Variável Alvo (Target)", "Outlier", "Stop Word"], "ans": "Variável Alvo (Target)", "exp": "Target é o que você quer descobrir. Features são as variáveis que você usa para prever o target."},
    {"q": "O que é 'Stemming' em NLP?", "opts": ["Adicionar palavras", "Reduzir palavras ao radical (correndo -> corr)", "Colorir texto", "Audio para texto"], "ans": "Reduzir palavras ao radical (correndo -> corr)", "exp": "Ajuda o modelo a entender que 'casamento', 'casar' e 'casado' falam da mesma coisa."},
    {"q": "Qual o melhor gráfico para mostrar evolução ao longo do tempo?", "opts": ["Pizza", "Linhas", "Dispersão", "Boxplot"], "ans": "Linhas", "exp": "O gráfico de linhas é o padrão universal para séries temporais e evolução."}
]

# ==========================================
# GERENCIAMENTO DE ESTADO (A memória do app)
# ==========================================
if 'pergunta_atual' not in st.session_state:
    st.session_state.pergunta_atual = 0
    st.session_state.pontos = 0
    st.session_state.respondido = False
    st.session_state.opcao_selecionada = None
    st.session_state.acertou = False

# ==========================================
# UI DO APLICATIVO
# ==========================================
st.title("🦉 FIAP Duolingo: Data Analytics")

# Menu de Abas
aba_quiz, aba_pratica = st.tabs(["🎮 Jogar Simulado", "🎬 Resumo Animado"])

with aba_quiz:
    # Verifica se já terminou as 30 perguntas
    if st.session_state.pergunta_atual < len(questoes):
        
        questao_atual = questoes[st.session_state.pergunta_atual]
        progresso = (st.session_state.pergunta_atual) / len(questoes)
        
        # Barra de Progresso
        st.progress(progresso)
        st.caption(f"Questão {st.session_state.pergunta_atual + 1} de {len(questoes)} | Pontuação: {st.session_state.pontos}")
        
        st.divider()
        
        # Mostra a pergunta gigante tipo Duolingo
        st.header(questao_atual['q'])
        
        # Opções de resposta
        if not st.session_state.respondido:
            # Se ainda não respondeu, mostra as opções para selecionar
            opcao = st.radio("Selecione sua resposta:", questao_atual['opts'], index=None)
            
            if st.button("Verificar ✅", use_container_width=True):
                if opcao:
                    st.session_state.opcao_selecionada = opcao
                    st.session_state.respondido = True
                    if opcao == questao_atual['ans']:
                        st.session_state.pontos += 1
                        st.session_state.acertou = True
                        if st.session_state.pontos % 5 == 0:
                            st.balloons() # Balões a cada 5 acertos!
                    else:
                        st.session_state.acertou = False
                    st.rerun() # Recarrega a tela para mostrar o resultado
                else:
                    st.warning("Selecione uma opção antes de verificar!")
                    
        else:
            # Se já respondeu, trava as opções e mostra o resultado
            st.radio("Sua resposta:", questao_atual['opts'], index=questao_atual['opts'].index(st.session_state.opcao_selecionada), disabled=True)
            
            if st.session_state.acertou:
                st.success(f"**🎉 Correto!** {questao_atual['exp']}")
            else:
                st.error(f"**❌ Incorreto.** A resposta certa é: '{questao_atual['ans']}'.\n\n*Explicação:* {questao_atual['exp']}")
            
            # Botão para ir para a próxima
            if st.button("Continuar ➡️", use_container_width=True):
                st.session_state.pergunta_atual += 1
                st.session_state.respondido = False
                st.session_state.opcao_selecionada = None
                st.rerun()

    else:
        # TELA FINAL
        st.balloons()
        st.header("🏆 Fim de Jogo!")
        st.write(f"Você acertou **{st.session_state.pontos}** de {len(questoes)} perguntas!")
        
        nota = (st.session_state.pontos / len(questoes)) * 10
        st.metric(label="Sua Nota Final", value=f"{nota:.1f}")
        
        if nota >= 7:
            st.success("Você está mais do que aprovado(a)! Excelente trabalho.")
        else:
            st.warning("Foi um bom treino, mas vale revisar um pouco mais a aba de Resumo Animado!")
            
        if st.button("Jogar Novamente 🔄"):
            st.session_state.pergunta_atual = 0
            st.session_state.pontos = 0
            st.session_state.respondido = False
            st.rerun()

# Aba de bônus para manter aquele visual prático que conversamos
with aba_pratica:
    st.subheader("Para não esquecer mais:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**O Eixo (Axis)**\n\n`axis=0` -> Linhas (⬇️)\n\n`axis=1` -> Colunas (➡️)")
    with col2:
        st.warning("**Os Resumos**\n\n`info()` -> Esqueleto (tipos/nulos)\n\n`describe()` -> Matemática (média/min/max)")
        
    st.divider()
    
    if st.button("▶️ Animar DBSCAN na prática"):
        st.write("Procurando pessoas perto umas das outras (Densidade)...")
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            bar.progress(i+1)
        st.success("**Grupos formados:** 🔵🔵 (Cluster 1) ... 🔴 (Outlier sozinho) ... 🟢🟢 (Cluster 2)")