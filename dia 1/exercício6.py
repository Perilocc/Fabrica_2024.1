divisores = 0

num = int(input("Digite um número: "))

for i in range(2, num):
    if num % (i) == 0:
        divisores = divisores + 1
        
if divisores == 1:
    print("O número {}".format(num), end=" não é Primo.")
else:
    print("O número {}".format(num), end=" é Primo")
    print(divisores)