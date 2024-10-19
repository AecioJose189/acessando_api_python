import requests 
lista_ceps = ['01153000', '20050000', '70714020']
lista_endereco = []

for cep in lista_ceps:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    req = requests.get(url, timeout=3)
    endereco = req.json()
    lista_endereco.append([endereco["cep"], endereco["logradouro"], endereco["bairro"], endereco["localidade"]])
