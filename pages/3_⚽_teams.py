import streamlit as st

st.set_page_config(
  page_title="Teams",
  page_icon="⚽",
  layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

col1, col2, col3, col4 = st.columns(4)


col1.image(df_filtered.iloc[0]["Club Logo"])
col2.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Joined',
          'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
          column_config={
              "Overall": st.column_config.ProgressColumn(
                "Overall", format="%d", min_value=0, max_value=100
              ),
              "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
              "Photo": st.column_config.ImageColumn(),
              "Flag": st.column_config.ImageColumn("Country"),

          }

)