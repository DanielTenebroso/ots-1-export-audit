import streamlit as st
import pandas as pd

st.set_page_config(page_title="OTS Export Audit", layout="wide")

st.title("📦 OTS Export Audit")

st.write("Sube un archivo CSV para revisar los datos de exportación:")

uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Archivo cargado correctamente ✅")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Descargar CSV",
        data=csv,
        file_name="export_audit.csv",
        mime="text/csv",
    )
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")

