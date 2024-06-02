import streamlit as st
import json
import requests

# Título da aplicação
st.title('API de Predição de Salário')

# Inputs para o usuário
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider('Tempo na empresa (meses)', min_value=0, max_value=120, value=60, step=1)

st.write("Qual o nível do profissional na empresa?")
nivel_na_empresa = st.slider('Nível na empresa', min_value=1, max_value=10, value=5, step=1)

# Preparar dados para API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# Criar botão para fazer a predição
if st.button('Prever salário'):
    # Enviar dados para a API
    response = requests.post('http://localhost:8000/predict_salario', json=input_features)
    response_json = json.loads(response.text)
    salario_em_reais = round(response_json['salario_em_reais'], 2)
    st.subheader(f'Salário previsto: R$ {salario_em_reais}')
