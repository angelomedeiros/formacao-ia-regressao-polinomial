from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe com dados de entrada que virão no request body com os tipos esperados
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar o modelo treinado
model_polynomial = joblib.load('models/model_salario.pkl')

# Criar função para fazer a predição
def predict(data: request_body):
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame([input_features], index=[1])

    y_pred = model_polynomial.predict(pred_df)[0].astype(float)

    return {
        'salario_em_reais': y_pred.tolist()
    }

# Criar rota para a API
@app.post('/predict_salario')
def predict_salario(data: request_body):
    return predict(data)