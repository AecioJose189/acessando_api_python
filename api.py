import requests 

consultar_cep = int(input("Digite seu CEP: "))
lista_ceps = []
lista_ceps.append('{}'.format(consultar_cep))
print(lista_ceps)
lista_endereco = []

for cep in lista_ceps:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    req = requests.get(url, timeout=3)
    endereco = req.json()
    lista_endereco.append([endereco["cep"], endereco["logradouro"], endereco["bairro"], endereco["localidade"]])
for end in lista_endereco:
    print(end)