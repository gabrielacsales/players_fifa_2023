import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import kagglehub
import requests

# import os
# import re
# import time
# import pandas as pd
# import requests
# from urllib.parse import urlparse

# CSV_PATH = "datasets/CLEAN_FIFA23_official_data.csv"  # ajuste se sua pasta tiver outro nome
# PHOTO_COL = "Photo"
# OUT_DIR = "assets/photos"
# SLEEP = 0.05  # 50ms entre requests pra não martelar o CDN

# os.makedirs(OUT_DIR, exist_ok=True)

# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Referer": "https://sofifa.com/",
#     "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
# }


# def clean_url(u: str) -> str:
#     u = str(u).replace("\u00a0", " ").strip()
#     u = re.sub(r"\s+", "", u)  # remove qualquer whitespace
#     return u


# def make_filename(url: str) -> str:
#     # cria nome estável: players_192_119_23_60.png
#     p = urlparse(url).path.strip("/")
#     return p.replace("/", "_")


# def main():
#     df = pd.read_csv(CSV_PATH)

#     urls = (
#         df[PHOTO_COL]
#         .dropna()
#         .astype(str)
#         .map(clean_url)
#         .unique()
#         .tolist()
#     )

#     print(f"Total de URLs únicas: {len(urls)}")

#     s = requests.Session()

#     ok = 0
#     fail = 0

#     for i, url in enumerate(urls, start=1):
#         if not url.startswith("http"):
#             fail += 1
#             continue

#         fname = make_filename(url)
#         out_path = os.path.join(OUT_DIR, fname)

#         if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
#             ok += 1
#             continue  # já baixou

#         try:
#             r = s.get(url, headers=headers, timeout=20, allow_redirects=True)

#             if r.status_code == 200 and r.headers.get("Content-Type", "").lower().startswith("image/"):
#                 with open(out_path, "wb") as f:
#                     f.write(r.content)
#                 ok += 1
#             else:
#                 fail += 1

#         except Exception:
#             fail += 1

#         if i % 200 == 0:
#             print(f"{i}/{len(urls)} | ok={ok} fail={fail}")

#         time.sleep(SLEEP)

#     print("Final:", f"ok={ok}", f"fail={fail}")


# if __name__ == "__main__":
#     main()

# Download latest version Dataset
# path = kagglehub.dataset_download("kevwesophia/fifa23-official-datasetclean-data")
# print("Path to dataset files:", path)

## Já pegando os dados tanto para o projeto como para previsualizar na pag home
if "data" not in st.session_state:
  df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)

  # df_data["Photo"] = df_data["Photo"].astype(str).str.strip()
  # df_data["Flag"] = df_data["Flag"].astype(str).str.strip()
  # df_data["Club Logo"] = df_data["Club Logo"].astype(str).str.strip()

  df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
  df_data = df_data[df_data["Value(£)"] > 0]
  df_data = df_data.sort_values(by="Overall", ascending=False)

  st.session_state["data"] = df_data


# ajustes textos do sidebar
st.sidebar.success("Navegue pelas seções acima 👆")
st.sidebar.markdown("Desenvolvido por Gabriela Sales com apoio das aulas [Asimov Academy](https://asimov.academy)")

# Incio do Site em si 
st.title("FIFA23 OFFICIAL DATASET ⚽")
st.write("**Explorando o mundo do futebol com dados**")

tab1, tab2 = st.tabs(["📌 Sobre o projeto", "📊 Sobre os dados"])

with tab1:
  st.markdown("""
  Este projeto é uma **aplicação web de análise de dados** desenvolvida com **Python, Pandas e Streamlit**, utilizando dados do **FIFA 23**. A solução transforma uma base tabular em um **dashboard interativo**, facilitando a exploração de informações sobre **jogadores, clubes, desempenho, valores de mercado, salários e contratos**.

  """)

  with st.expander("**📌 que dor esse projeto Resolve?**"):
      st.markdown("""
      O projeto resolve a dor de analisar dados extensos apenas em planilhas, oferecendo uma experiência mais **visual, filtrável e intuitiva**. 

      <br/> Mesmo sendo um **projeto curto**, ele demonstra habilidades aplicáveis a cenários reais, como **tratamento de dados**, **criação de dashboards**, **organização de informações relevantes** e construção de soluções orientadas à **tomada de decisão**.

      """)

with tab2:
  st.markdown("### Prévia dos dados:")
  st.write("""
  Abaixo está uma amostra dos primeiros registros do dataset já tratado e ordenado pelos jogadores com maior pontuação geral.
  """)

  st.dataframe(df_data.head(5), use_container_width=True)
  st.info("Esse conjunto de dados reúne informações dos jogadores entre 2017 e 2023, incluindo estatísticas, características físicas e detalhes de contrato.")
  with st.expander("O que você encontra neste dataset"):
    st.markdown("""
      - 👤 Dados demográficos  
      - ⚽ Estatísticas de jogo  
      - 💪 Características físicas  
      - 📑 Detalhes de contrato  
      - 🏟️ Histórico de clubes 
    """)

  btn = st.button("Acesse os dados no Kaggle 📁")
  if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
