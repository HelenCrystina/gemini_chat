import streamlit as st
import os
from gemini_client import GeminiClient

# Configuração da página
st.set_page_config(page_title="Chat IA com Gemini", layout="wide")
st.title("🤖 Chat da Helen com IA - Google Gemini")

# Obtém a chave da API do ambiente ou define diretamente (menos seguro)
API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyDoI726I60xUULjMfIcTqN2ojZBhBNcn60"

# Verificação de chave
if not API_KEY or API_KEY == "AIzaSyDoI726I60xUULjMfIcTqN2ojZBhBNcn60":
    st.error("⚠️ Insira sua chave da API Gemini no código ou configure a variável de ambiente GEMINI_API_KEY.")
    st.stop()

# Inicializa cliente
client = GeminiClient(api_key=API_KEY)

# Armazena mensagens na sessão
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Mensagem inicial
if not st.session_state.mensagens:
    with st.chat_message("assistant"):
        st.markdown("Olá! Sou uma IA da Google. Faça sua pergunta abaixo 👇")

# Entrada do usuário
prompt = st.chat_input("Digite sua pergunta...")

# Se o usuário enviar algo
if prompt:
    st.session_state.mensagens.append({"role": "user", "text": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Geração de resposta
    resposta = client.ask(prompt)
    st.session_state.mensagens.append({"role": "assistant", "text": resposta})

    with st.chat_message("assistant"):
        st.markdown(resposta)

# Exibe histórico anterior se houver
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
