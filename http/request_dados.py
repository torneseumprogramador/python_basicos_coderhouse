import requests
import pandas as pd
import pdb

url = "https://restcountries.com/v3.1/all"
# url = "http://127.0.0.1:5000/clientes"

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    dados = response.json()
    df =  pd.DataFrame(dados)

    nomes = [dado["name"]["common"] for dado in dados]
    regioes = [dado["region"] for dado in dados]
    capitais = []

    for dado in dados:
        if "capital" in dado and dado["capital"] is not None:
            if isinstance(dado["capital"], list):
                capitais.append(', '.join(dado["capital"]))
            else:
                capitais.append(dado["capital"])
        else:
            capitais.append(None)

    linguas = []

    for dado in dados:
        if "languages" in dado and dado["languages"] is not None:
            # Extrai os nomes dos idiomas de cada dicionário e os junta em uma string
            idiomas = ', '.join(dado["languages"].values())
            linguas.append(idiomas)
        else:
            linguas.append(None)

    # Junta todas as strings de idiomas em uma única linha


    # pdb.set_trace()

    df_formatado = pd.DataFrame({
        "Nome": nomes,
        "Capital": capitais,
        "Regiao": regioes,
        "Lingua": linguas,
    })


    print(df_formatado)

    # pdb.set_trace() # debugger

    # for dado in dados:
    #     print(dado["name"]["common"])

string = "[{'id': '1', 'nome': 'maça'}, {'id': '2', 'nome': 'banana'}]"

array_dict = [
    {'id': '1', 'nome': 'maça'},
    {'id': '2', 'nome': 'banana'}
]