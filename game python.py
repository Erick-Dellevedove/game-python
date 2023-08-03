import random
from os import system, name


def limpa_tela():
    # Windows
    if name == "nt":
        _ = system("cls")
    # outro SO
    else:
        _ = system("clear")


def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")


# lista de palavras para o jogo
palavras = ["banana", "uva", "morango", "abacate", "laranja"]
# escolhe aleatoriamente as palavras
palavra = random.choice(palavras)
# list comprehension
letras_descobertas = ['_' for letra in palavra]
# número de chances
chances = 6
# lista para as letras erradas
letras_erradas = []

# chama a função game para exibir a mensagem de boas-vindas
game()

while chances > 0:
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    tentativa = input("\nDigite uma letra: ").lower()

    if tentativa in palavra:
        index = 0
        for letra in palavra:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)

    if "_" not in letras_descobertas:
        print("\nVocê venceu, a palavra era:", palavra)
        break

# verifica se o jogador perdeu o jogo
if "_" in letras_descobertas:
    print("\nVocê perdeu, a palavra era:", palavra)

print("\nObrigado, volte sempre! :)\n")
