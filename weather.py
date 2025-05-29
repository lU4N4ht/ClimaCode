import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(cidade): 
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={cidade}&lang=pt'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            'temperatura': dados['current']['temp_c'],
            'umidade': dados['current']['humidity'],
            'descricao': dados['current']['condition']['text'],
            'pressao': dados['current']['pressure_mb'],
            'vento': dados['current']['wind_kph'],
            'precipitacao': dados['current']['precip_mm']  
        }
        return clima
    else:
        return {"erro": "Cidade não encontrada"}
