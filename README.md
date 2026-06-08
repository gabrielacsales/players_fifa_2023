# FIFA 23 Official Dataset Analysis ⚽

Este é um projeto de **Dashboard Interativo de Análise de Dados** desenvolvido com **Python**, **Streamlit** e **Pandas**. Ele transforma o conjunto de dados oficial do FIFA 23 (e edições anteriores) em uma aplicação web visual, intuitiva e interativa para a tomada de decisões e exploração de estatísticas de futebol.

---

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### 2. Instalação das Dependências
Instale as bibliotecas necessárias utilizando o `pip`:
```bash
pip install streamlit pandas requests
```

### 3. Executando a Aplicação
Inicie o servidor do Streamlit a partir do arquivo principal do projeto:
```bash
streamlit run 1_🏠_home.py
```
A aplicação será aberta automaticamente no seu navegador padrão (geralmente no endereço `http://localhost:8501`).

---

## 📂 Estrutura do Projeto

A organização dos arquivos no repositório segue a estrutura padrão de projetos multipáginas do Streamlit:

*   **`1_🏠_home.py`**: A página principal da aplicação. Apresenta o escopo do projeto, a utilidade da ferramenta e exibe uma amostra dos dados tratados.
*   **`pages/`**: Contém as páginas adicionais da aplicação:
    *   `2_🏃_players.py`: Análise detalhada dos atributos de jogadores individuais (Idade, Altura, Peso, Overall, Valor de Mercado, Salário, Cláusula de Rescisão, etc.).
    *   `3_⚽_teams.py`: Visualização do elenco completo de cada clube, incluindo gráficos de progresso dos atributos e filtros rápidos.
*   **`datasets/`**: Diretório contendo os arquivos CSV históricos com os dados oficiais extraídos do FIFA (do ano de 2017 a 2023). O arquivo principal utilizado é o `CLEAN_FIFA23_official_data.csv`.
*   **`ajustes.md`**: Lista de pendências, melhorias planejadas e tarefas de refatoração para o dashboard.
*   **`aprendi.md`**: Anotações de aprendizado sobre Markdown e componentes visuais do Streamlit.

---

## ✨ Funcionalidades do Dashboard

### 🏠 Página Inicial (Home)
*   **Visão Geral**: Introdução sobre o objetivo do dashboard e a dor de negócio que ele resolve (facilitar a análise de planilhas extensas de forma visual).
*   **Prévia dos Dados**: Um componente de tabela dinâmico que exibe os primeiros registros ordenados pelos melhores jogadores gerais.

### 🏃 Análise de Jogadores (Players)
*   **Perfil Completo**: Foto do jogador selecionado e principais informações (clube atual, posição de jogo, idade, altura e peso).
*   **Visualização de Overall**: Uma barra de progresso interativa para destacar graficamente o nível geral (Overall) do atleta.
*   **Métricas Financeiras**: Cards informativos com o valor de mercado estimado, salário semanal e multa rescisória.

### ⚽ Análise de Clubes (Teams)
*   **Elenco do Clube**: Filtro por clube que exibe todos os jogadores cadastrados, suas fotos e nacionalidades.
*   **Visualização Progressiva**: Exibição da nota Overall de cada jogador de forma visual diretamente na tabela (ProgressColumn).

---

## 🛠️ Tecnologias Utilizadas

*   [**Python**](https://www.python.org/) - Linguagem de programação base.
*   [**Streamlit**](https://streamlit.io/) - Framework para criação de aplicativos web para Ciência de Dados de forma rápida e bonita.
*   [**Pandas**](https://pandas.pydata.org/) - Biblioteca para manipulação e análise de dados estruturados.

---

## 📌 Melhorias Futuras (Backlog)
Conforme documentado no arquivo `ajustes.md`, as seguintes melhorias estão planejadas para o projeto:
1.  Otimizar o carregamento de dados em cache (`st.session_state`) para evitar erros ao navegar diretamente para a página de Jogadores.
2.  Melhorar o design do perfil do jogador, alinhando a imagem ao lado dos dados demográficos.
3.  Adicionar uma tag dinâmica ou classificação colorida para o valor do Overall.
4.  Integrar uma API de LLM pública para gerar resumos de performance histórica de cada jogador.
