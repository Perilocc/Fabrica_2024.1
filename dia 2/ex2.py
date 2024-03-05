class Animal():
    def __init__(self, tipo, nome, idade, porte, ):
        self.tipo = tipo
        self.nome = nome
        self.idade = idade
        self.porte = porte
    
    def andar(self):
        print("O {} de idade {} e porte {} está andando".format(self.tipo, self.idade, self.porte))
        
class Cachorro(Animal):
    def latir(self):
        print("O {} de nome  {} e de {} porte  está latindo".format(self.tipo, self.nome, self.porte))

class Gato(Animal):
    def miar(self):
        print("O {} de nome {} e de {} porte  está miando".format(self.tipo, self.nome, self.porte))
        
dog = Cachorro("Cachorro", "Bethoven", 2, "grande")
dog.latir()

cat = Gato("Gato", "Garfield", 2, "pequeno")
cat.miar()