import requests
"""
manaira = requests.get("https://viacep.com.br/ws/58038420/json/")

json = manaira.json()

print(manaira)
print(json)

print(json.get("cep", "Não tem Cep"))
"""

nome = requests.get("http://127.0.0.1:8000/api/pessoa/2")

json = nome.json()
print(json.get("primeiro_nome", "Sem nome"))
# Usar insomnia colocar url http://127.0.0.1:8000/api/pessoa/1 e testar post, get e delete
#Tarefa estudar insomnia