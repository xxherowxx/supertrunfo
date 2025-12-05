```python
import random

Cartas do jogo - países com características
cartas = [
    {"nome": "Brasil", "populacao": 213, "pib": 1.8, "area": 8516},  # PIB em trilhões USD, área em mil km²
    {"nome": "Estados Unidos", "populacao": 331, "pib": 21.4, "area": 9834},
    {"nome": "China", "populacao": 1441, "pib": 14.3, "area": 9597},
    {"nome": "Índia", "populacao": 1380, "pib": 2.9, "area": 3287},
    {"nome": "Rússia", "populacao": 146, "pib": 1.7, "area": 17098},
    {"nome": "Japão", "populacao": 126, "pib": 5.1, "area": 378},
]

def escolher_carta():
    return random.choice(cartas)

def jogar():
    print("Bem-vindo ao Super Trunfo - Países!\n")
    
    carta_jogador = escolher_carta()
    carta_computador = escolher_carta()

    while carta_computador == carta_jogador:
        carta_computador = escolher_carta()

    print(f"Sua carta: {carta_jogador['nome']}")
    print("Escolha a categoria para comparar:")
    print("1 - População (milhões)")
    print("2 - PIB (trilhão USD)")
    print("3 - Área (mil km²)")
    escolha = input("Digite o número da categoria: ")

    if escolha == "1":
        categoria = "populacao"
    elif escolha == "2":categoria = "pib"
    elif escolha == "3":
        categoria = "area"
    else:
        print("Categoria inválida!")
        return

    valor_jogador = carta_jogador[categoria]
    valor_computador = carta_computador[categoria]

    print(f"\nSua carta: {carta_jogador['nome']} - {categoria}: {valor_jogador}")
    print(f"Carta do computador: {carta_computador['nome']} - {categoria}: {valor_computador}\n")

    if valor_jogador > valor_computador:
        print("Você venceu!")
    elif valor_jogador < valor_computador:
        print("Você perdeu!")
    else:
        print("Empate!")

if name == "main":
    jogar()
``` 
