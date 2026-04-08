import random
pontos = 0
while True:
    print("="*40)
    print(" JOGO DA ROLETA")
    print("="*40)
    print("\n1. Se os números forem iguais, você ganha 5 pontos")
    decisao = input("Jogar?: 1.Sim | 2.Nao: ")
    if decisao == "":
        print("Opção inválida, tente novamente.")
    match decisao:
        case "1":
            aleatorio = random.randint(1, 10)
            aleatorio2 = random.randint(1, 10)
            print(f"\nSorteio: {aleatorio} e {aleatorio2}")
            if aleatorio == aleatorio2:
                print("Voce ganhou!!!")
                pontos += 5
            else:
                print("Voce nao acertou")
        case "2":
            print("Saindo do jogo")
            break
print(pontos)

