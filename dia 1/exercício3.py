import random

times_futebol = ["Botafogo", "Flamengo", "Palmeiras", "Vasco", "Santos", "Água Santa", "Vitória"
                , "Paisandu", "Chapecoense", "Boa vista", "Fortaleza", "Corinthians"]


for i in range(5):
    time =  times_futebol[random.randint(0, len(times_futebol))]
    print("Time {}: {}".format(i + 1, time))