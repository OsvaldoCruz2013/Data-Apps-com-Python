import streamlit as st

st.markdown("# Data Salary")

salarios_pos = {
    "Junior": 4000,
    "Pleno": 7500,
    "Senior": 11000,
    }

col1, col2 = st.columns(2)

with col1:
    select_box_posicao = st.selectbox("Selecione a posição", options=salarios_pos.keys())


with col2:
    input_tempo_experiencia = st.number_input("Digite o tempo de experiência (em anos)", min_value=0, max_value=35, help="Seu tempo de mercado em anos ")

salario = salarios_pos[select_box_posicao] + (input_tempo_experiencia * 500)

st.markdown(f"#### O salário médio para a posição de {select_box_posicao} é de R$ {salario:.2f}")


