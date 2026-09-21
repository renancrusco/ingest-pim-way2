# %%
import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

url = os.getenv('API_BASE_URL','https://pim.way2.com.br:183')
endpoint = os.getenv('API_ENDPOINT','api/v3/dados-de-medicao/pontos')
token = os.getenv('API_TOKEN')

if not token:
    raise ValueError('API_TOKEN nao encontrado, verificar arquivo .env')

#tira a barra do final, evitando o caminho ficar errado
url_completa = f'{url.rstrip("/")}/{endpoint.lstrip("/")}'

headers ={'PIM-Auth': token}

# %%
data_ref = datetime(2020, 1, 1, 0, 0, 0)
data_txt = data_ref.strftime('%Y-%m-%dT%H:%M:%S')

params = {
    'ids': '4149,6122',
    'grandezas': 'EneatDel,EneatRec',
    'intervalo': 'UmaHora',
    'medicao-datainicio': data_txt,
    'medicao-datafim': data_txt,
}

resposta = requests.get(url_completa, headers=headers, params=params, timeout=60)
print(resposta.status_code, resposta.url)
resposta.raise_for_status()
# %%
dados = resposta.json()
#print(list(dados.keys()))
#print(json.dumps(dados, indent=2, ensure_ascii=False)[:2000])
# %%
import pandas as pd
df = pd.json_normalize(
    dados['dados'],
    record_path='valores',
    meta=['pontoId', 'ultimaColeta', 'nomeGrandeza'],
)
# %%
