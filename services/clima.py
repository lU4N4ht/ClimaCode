import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

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


def get_historical_temperatures(cidade):
    matriz = [[], []]
    hoje = datetime.now()

    for semana in range(2):
        for dia in range(5):
            data = (hoje - timedelta(days=7 * semana + dia + 1)).strftime('%Y-%m-%d')
            url = f'http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={cidade}&dt={data}'
            resposta = requests.get(url)

            if resposta.status_code == 200:
                dados = resposta.json()
                temperatura = dados['forecast']['forecastday'][0]['day']['avgtemp_c']
                matriz[semana].append(temperatura)
            else:
                matriz[semana].append(None)

    estatisticas = []
    for semana in matriz:
        temps_validas = [t for t in semana if t is not None]
        if temps_validas:
            maior = max(temps_validas)
            menor = min(temps_validas)
        else:
            maior = menor = None
        estatisticas.append({'maior': maior, 'menor': menor})

    return matriz, estatisticas
