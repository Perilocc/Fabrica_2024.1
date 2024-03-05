# Atividade 1: 
"""
n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    print("O número {} é par".format(n1)) 
else:   
    print("O número {} é impar".format(n1))"""
    

# Atividade 2:
# While    
"""
numeros = []
n = 0
while n < 100:
    n = n + 2
    numeros.append(n)
    print(n)

soma = sum(numeros)
print(soma)"""

# for
"""
i = -1
lista = ["maça", "banana", "cajarana"]
for fruta in lista:
    print( "\n" + fruta)
    i += 1
    for letra in  lista[i]:
        print(letra)"""

# for in range
"""
list = []
for i in range(0, 100, 5):
    n = i
    list.append(i)
    print(n + i)"""


# Atividade 3:

#Com return
"""
def soma(x, y):
    x = int(x)
    y = int(y)
    return print(x + y)

x = input("Digite um número: ")
y = input("Digite outro número: ")

soma(x, y)
"""

# Sem retorno

def helloworld():
    print("hello world!!")
    print("Quem tá lendo, tá me devendo um pipuz")

helloworld()
