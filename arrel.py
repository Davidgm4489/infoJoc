import random

resposta = 0

def adivinar_quadrat():
    num = random.randint(1, 100)
    quadrat = num ** 2
    resposta = int(input(f"Quina és l'arrel de {quadrat}: "))
    if resposta == num:
        print("Correcte")
        return 1
    else:
        print(f"Incorrecte, és {num}")
        return 0

for _ in range(5):
    resposta += adivinar_quadrat()

print(f"Has encertat {resposta} arrels")