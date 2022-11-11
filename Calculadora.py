import os

def operacao():
    print("Bem vindo a calculadora!")
    print("----------------")
    print(" 0 : Soma")
    print(" 1 : Subtração")
    print(" 2 : Multiplicação")
    print(" 3 : Divisão")
    print(" 4 : Exponenciação")
    print("----------------")
    print("Escolha uma operação: ")
    op = int(input())
    if op == 0:
        os.system('cls')
        print("Operação de soma escolhida!")
        print("----------------")
        print("Escolha o primeiro número:")
        op1 = float(input())
        print("Escolha o segundo numero número:")
        op2 = float(input())
        print("----------------")
        res = op1 + op2
        print("O resultado da soma de {} + {} é igual à: {}".format(op1,op2,res))
        print("\n")
        print("Deseja fazer outra operação? (Y/N) :")
        retorno = input()
        if retorno == "y":
            os.system("cls")
            operacao()
        else:
            print("Obrigado por ultilizar nossa calculadora!")
            exit()
    elif op == 1:
        os.system('cls')
        print("Operação de subtração escolhida!")
        print("----------------")
        print("Escolha o primeiro número:")
        op1 = float(input())
        print("Escolha o segundo numero número:")
        op2 = float(input())
        print("----------------")
        res = op1 - op2
        print("O resultado da subtração de {} - {} é igual à: {}".format(op1,op2,res))
        print("\n")
        print("Deseja fazer outra operação? (Y/N) :")
        retorno = input()
        if retorno == "y":
            os.system("cls")
            operacao()
        else:
            print("Obrigado por ultilizar nossa calculadora!")
            exit()
    elif op == 2:
        os.system('cls')
        print("Operação de multiplicação escolhida!")
        print("----------------")
        print("Escolha o primeiro número:")
        op1 = float(input())
        print("Escolha o segundo numero número:")
        op2 = float(input())
        print("----------------")
        res = op1 * op2
        print("O resultado da multiplicação de {} x {} é igual à: {}".format(op1,op2,res))
        print("\n")
        print("Deseja fazer outra operação? (Y/N) :")
        retorno = input()
        if retorno == "y":
            os.system("cls")
            operacao()
        else:
            print("Obrigado por ultilizar nossa calculadora!")
            exit()
    elif op == 3:
        os.system('cls')
        print("Operação de divisão escolhida!")
        print("----------------")
        print("Escolha o primeiro número:")
        op1 = float(input())
        print("Escolha o segundo numero número:")
        op2 = float(input())
        print("----------------")
        res = op1 / op2
        print("O resultado da divisão de {} / {} é igual à: {}".format(op1,op2,res))
        print("\n")
        print("Deseja fazer outra operação? (Y/N) :")
        retorno = input()
        if retorno == "y":
            os.system("cls")
            operacao()
        else:
            print("Obrigado por ultilizar nossa calculadora!")
            exit() 
    elif op == 4:
        os.system('cls')
        print("Operação de exponenciação escolhida!")
        print("----------------")
        print("Escolha o primeiro número:")
        op1 = float(input())
        print("Escolha o segundo numero número:")
        op2 = float(input())
        print("----------------")
        res = op1 ** op2
        print("O resultado da exponiação de {} elevado à {} é igual à: {}".format(op1,op2,res))
        print("\n")
        print("Deseja fazer outra operação? (Y/N) :")
        retorno = input()
        if retorno == "y":
            os.system("cls")
            operacao()
        else:
            print("Obrigado por ultilizar nossa calculadora!")
            exit()
    else:
        print("Digite um numero válido!")
        operacao()
operacao()
    