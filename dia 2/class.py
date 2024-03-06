# Exemplo 1
"""
class Carro:
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print("Seu veículo de marca {}, modelo {} e de ano {} ligou".format(self.marca, self.modelo, self.ano))

class SmartCar(Carro):
    def localizar(self):
        print("{} está localizado em João Pessoa".format(self.modelo))
        
carro = Carro("Chevrolet", "Onix", 2020)
carro.ligar()

carro_de_hetcho = SmartCar("Jeep", "Compass", "2023")
carro_de_hetcho.ligar()
carro_de_hetcho.localizar()
"""

class Comida():
    
    def __init__(self, nome, preco, culinaria):
        self.nome = nome
        self.preco = preco
        self.culinaria = culinaria

    def vender(self):
        print("Estou vendendo {} original da culinaria {} por {} mil reis".format(self.nome, self.culinaria, self.preco))
        
class Pizza(Comida):

    def comer(self):
        print("Estou comendo {} que comprei por {} mil reis".format(self.nome, self.preco))

pizza = Pizza("Pizza portuguesa", 70, "italiana")
pizza.comer()

