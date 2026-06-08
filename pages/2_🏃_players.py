import streamlit as st
# import os
# from urllib.parse import urlparse
import requests 
import base64
# from io import BytesIO

@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()
# @st.cache_data
# def carregar_imagem(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0",
#         "Referer": "https://sofifa.com/"
#     }

#     resposta = requests.get(url, headers=headers, timeout=10)
#     resposta.raise_for_status()

#     return resposta.content

st.set_page_config(
  page_title="Players",
  page_icon="🏃",
  layout="wide"
)

df_data = st.session_state["data"]

# PHOTO_DIR = "assets\photos"

# 1) Padroniza a coluna Photo (se ainda estiver como URL)
# Só faz se parecer URL; senão, deixa como está (já nome de arquivo).
# if df_data["Photo"].astype(str).str.startswith("http").any():
#  df_data["Photo"] = (
#  df_data["Photo"]
#  .astype(str)
#  .apply(lambda u: urlparse(u).path.strip("/").replace("/", "_"))
#  )

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"]== player].iloc[0]

# photo_url = str(player_stats["Photo"]).strip()

# try:
#     imagem = carregar_imagem(photo_url)
#     st.image(imagem, width=180)
# except Exception as erro:
#     st.warning("Não foi possível carregar a imagem do jogador.")
#     st.write(photo_url)
#     st.error(erro)

# photo_name = str(player_stats["Photo"]).strip()
# photo_path = os.path.join(PHOTO_DIR, photo_name)

# if os.path.exists(photo_path):
#  st.image(photo_path, width=60)
# else:
#  st.warning(f"Foto não encontrada: {photo_path}")

st.image(load_image_64(player_stats["Photo"]))
#st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor do Mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Clásula de Recisão", value=f"£ {player_stats['Release Clause(£)']:,}")