import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
url2 = 'https://economia.awesomeapi.com.br/last/USD-BRL' 
response = requests.get(url)
response2 = requests.get(url2)
print(response)
if response.status_code == 200:
    dados_json = response.json()
    nuser = str(dados_json['userId'])
    titulo = str(dados_json['title'])
    print(f'O usuário de número {nuser} tem o título {titulo}\n\n\n')
    

if response.status_code == 200:
    dados_json2 = response2.json()
    dolar_hoje = float(dados_json2['USDBRL']['bid'])
    moeda_inicial = str(dados_json2['USDBRL']['code'])
    moeda_final = str(dados_json2['USDBRL']['codein'])
    print(f'A conversão atual de {moeda_inicial} para {moeda_final} é de aproximadamente {dolar_hoje}')
    print(f'e 1 {moeda_final} equivale à {(1 / dolar_hoje):.2f}{moeda_inicial}')