import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
    if pH < 6.0 or temperatura > 30.0: # (Ejemplo de condicion)
        resultadio = "Rechazado"
    else:
        resultado = "Aprobado"

    st.write(f"Resultado: {resultado}")
