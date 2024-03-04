medias = 0

for i in range(5):
    media = int(input("Digite sua nota: "))
    medias = medias + media
    
media_geral = (medias/5)

print("A média Aritmética entre as 5 notas é {}".format(media_geral))