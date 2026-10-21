import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="Rolês do Grupo",
    page_icon="🎯",
    layout="centered",
)

DATA_DIR = Path("dados")
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "respostas_grupo.csv"

st.markdown("""
<style>
    .block-container {max-width: 850px; padding-top: 2rem; padding-bottom: 3rem;}
    .hero {
        padding: 1.5rem; border-radius: 18px; margin-bottom: 1rem;
        background: linear-gradient(135deg, #e9e4ff 0%, #f7f3ff 100%);
        color: #21164d;
    }
    .hero h1 {margin-bottom: .35rem;}
    div[data-testid="stForm"] {
        border: 1px solid rgba(128,128,128,.25);
        padding: 1.2rem; border-radius: 16px;
    }
</style>
<div class="hero">
    <h1>🎯 Rolês do Grupo</h1>
    <p>Conta pra gente o que você curte, quanto pretende gastar e quais rolês toparia fazer.</p>
</div>
""", unsafe_allow_html=True)

st.caption("Leva cerca de 3–5 minutos. As respostas ajudam a escolher programas que funcionem para todo mundo.")

atividades = [
    "Praia e piscina", "Trilhas e natureza", "Parques de diversão",
    "Museus e exposições", "Cinema", "Shows e festivais", "Bares e baladas",
    "Restaurantes e cafés", "Churrasco e encontros em casa",
    "Jogos de tabuleiro ou videogame", "Boliche, kart ou fliperama",
    "Escape room", "Compras e feirinhas", "Esportes e atividades físicas",
    "Viagens e passeios bate-volta", "Artesanato, oficinas e experiências criativas",
    "Eventos gratuitos", "Não tenho preferência"
]
dias = ["Durante a semana", "Sexta à noite", "Sábado", "Domingo", "Feriados", "Depende da ocasião"]
transportes = ["Carro próprio ou carona", "Aplicativo (Uber/99)", "Transporte público",
               "Ônibus de viagem", "Trem ou metrô", "Prefiro passeios próximos"]

with st.form("form_preferencias", clear_on_submit=True):
    st.subheader("1. Sobre você")
    nome = st.text_input("Qual é o seu nome?", placeholder="Seu nome")
    disponibilidade = st.multiselect("Quando você costuma estar disponível?", dias)

    st.divider()
    st.subheader("2. Que tipo de rolê você curte?")
    gostos = st.multiselect("Quais atividades você mais gosta? (pode marcar várias)", atividades)
    estilo = st.radio(
        "Qual estilo combina mais com você?",
        ["Tranquilo e para conversar", "Divertido e movimentado", "Aventura e adrenalina",
         "Cultural e para conhecer coisas novas", "Comida e experiências gastronômicas",
         "Festa e vida noturna", "Um pouco de tudo"],
        index=6
    )
    ambiente = st.radio("Você prefere atividades em qual ambiente?",
                        ["Ao ar livre", "Em lugares fechados", "Tanto faz"], horizontal=True)
    novidade = st.radio("Você toparia experimentar algo novo?",
                        ["Sim, adoro experiências diferentes", "Depende da atividade",
                         "Prefiro programas que já conheço"])

    st.divider()
    st.subheader("3. Orçamento 💸")
    orcamento = st.radio(
        "Quanto pretende gastar por pessoa em um rolê de um dia?",
        ["Até R$ 30", "R$ 31 a R$ 60", "R$ 61 a R$ 100",
         "R$ 101 a R$ 150", "R$ 151 a R$ 250",
         "Mais de R$ 250, dependendo do passeio"],
        index=1
    )
    bate_volta = st.radio(
        "Quanto gastaria em um passeio especial ou bate-volta?",
        ["Até R$ 50", "R$ 51 a R$ 100", "R$ 101 a R$ 200",
         "R$ 201 a R$ 350", "Mais de R$ 350", "Depende do planejamento"],
        index=1
    )
    alimentacao = st.radio(
        "Qual faixa de preço prefere para alimentação?",
        ["Econômica: até R$ 30", "Intermediária: R$ 31 a R$ 60",
         "Mais elaborada: R$ 61 a R$ 100", "Sem preferência"],
        index=1
    )
    custo_beneficio = st.radio(
        "Você prefere economizar ou pagar mais por uma experiência melhor?",
        ["Prioridade total para economizar", "Bom custo-benefício",
         "Pago mais se valer a pena", "Depende da ocasião"],
        index=1
    )

    st.divider()
    st.subheader("4. Transporte e distância")
    deslocamento = st.radio(
        "Quanto tempo aceitaria gastar no deslocamento?",
        ["Até 30 minutos", "De 30 minutos a 1 hora",
         "De 1 a 2 horas", "Mais de 2 horas se o passeio valer a pena"],
        index=1
    )
    transporte = st.multiselect("Quais meios de transporte toparia usar?", transportes)
    dividir = st.radio("Toparia dividir os custos de transporte com o grupo?",
                       ["Sim", "Depende do valor", "Prefiro ir por conta própria"],
                       horizontal=True)

    st.divider()
    st.subheader("5. Organização")
    frequencia = st.radio(
        "Com que frequência gostaria de fazer atividades com o grupo?",
        ["Toda semana", "A cada 15 dias", "Uma vez por mês",
         "A cada 2 ou 3 meses", "Quando surgir uma oportunidade"],
        index=2
    )
    antecedencia = st.radio(
        "Como prefere organizar os rolês?",
        ["Com bastante antecedência", "Alguns dias antes", "Decidir em cima da hora"],
        index=1
    )
    pernoite = st.radio("Toparia viagens com pernoite?",
                        ["Sim, tranquilamente", "Sim, se o custo for acessível",
                         "Só viagens curtas", "Prefiro passeios de um dia"])
    nao_gosta = st.text_area("Tem algo que não gosta ou não faria de jeito nenhum? (opcional)")
    quer_fazer = st.text_area("Tem algum rolê que quer muito fazer com o grupo? (opcional)")
    extras = st.text_area("Outra preferência, restrição ou sugestão? (opcional)")

    enviado = st.form_submit_button("Enviar minhas respostas 🎉", type="primary", use_container_width=True)

if enviado:
    if not nome.strip():
        st.error("Preencha seu nome antes de enviar.")
    else:
        row = {
            "data_resposta": datetime.now().isoformat(timespec="seconds"),
            "nome": nome.strip(),
            "disponibilidade": "; ".join(disponibilidade),
            "atividades": "; ".join(gostos),
            "estilo": estilo,
            "ambiente": ambiente,
            "novidade": novidade,
            "orcamento_dia": orcamento,
            "orcamento_bate_volta": bate_volta,
            "orcamento_alimentacao": alimentacao,
            "prioridade_gastos": custo_beneficio,
            "tempo_deslocamento": deslocamento,
            "transportes": "; ".join(transporte),
            "dividir_transporte": dividir,
            "frequencia": frequencia,
            "antecedencia": antecedencia,
            "pernoite": pernoite,
            "nao_gosta": nao_gosta.strip(),
            "quer_fazer": quer_fazer.strip(),
            "outras_sugestoes": extras.strip(),
        }
        if DATA_FILE.exists():
            df = pd.read_csv(DATA_FILE)
            # Atualiza a resposta anterior da mesma pessoa, evitando duplicidade por nome.
            df = df[df["nome"].astype(str).str.casefold() != nome.strip().casefold()]
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])
        df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
        st.success("Resposta salva! Valeu por participar 🎉")
        st.info("A resposta fica salva no arquivo CSV na pasta `dados` do computador/servidor em que o app está rodando.")

st.divider()
with st.expander("🔒 Ver respostas e baixar CSV (organizador)"):
    st.warning("Esta área não tem senha. Se publicar o app, remova esta seção ou adicione autenticação antes de compartilhar.")
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE)
        st.metric("Pessoas com resposta registrada", len(df))
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button(
            "Baixar respostas em CSV",
            data=df.to_csv(index=False).encode("utf-8-sig"),
            file_name="respostas_preferencias_grupo.csv",
            mime="text/csv",
            use_container_width=True,
        )
    else:
        st.caption("Ainda não há respostas salvas neste ambiente.")
