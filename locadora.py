import os

carros = [
        ("Chevrolet Onix Plus", 474),
        ("Toyota Corolla", 205),
        ("Fiat Toro", 409),
        ("Hyundai HB20", 130),
        ("Jeep Compass", 447),
        ("Fiat 500e", 351),
        ("Tesla Model S", 899),
        ("Celta Life", 700),
        ]
alugados = []


def mostrar(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))

while True:
    os.system("cls")
    print("=========")
    print("Bem vindo à locadora de carros!")
    print("=========")
    print("O que você deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system("cls")
    if op == 0:
        mostrar(carros)
    elif op == 1:
        mostrar(carros)
        print("=========")
        print("Escolha o codigo do carro que deseja alugar:")
        cod = int(input())
        print("Por quantos dias deseja alugar este carro?")
        dias = int(input())
        os.system("cls")
        print("Você escolheu {} por {} dias".format(carros[cod][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod][1]))
        print("0 - Sim | 1 - Não")
        conf = int(input())
        if conf == 0:
            print("Parabéns, você alugou o {} por {} dias.".format(carros[cod][0], dias))
            alugados.append(carros.pop(cod))
    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver")
        else:
            print("Segue a lista de carros alugados. Qual deseja devolver?")
            mostrar(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod2 = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro.".format(alugados[cod2][0]))
                carros.append(alugados.pop(cod2))

    print("")
    print("=========")
    print("Gostaria de continuar?")
    print("0 - Continuar | 1 - Sair")
    if int(input()) == 1:
        break