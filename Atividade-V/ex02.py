'''
2) Altere o programa anterior fazendo com que todas as operações matemáticas
sejam realizadas por uma única função. Todas as funcionalidades devem ser
mantidas.
'''


def operaçoes(v):
    global n1, n2
    if v == 1:
        print(n1 + n2)
    elif v == 2:
        print(n1 - n2)
    elif v == 3:
        print(n1 * n2)
    elif v == 4:
        print(n1 / n2)


while True:
    print("Escolha a Opção")
    v = int(input("1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão \n 5-Sair\n "))

    if v == 1:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        operaçoes(v)
    elif v == 2:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        operaçoes(v)
    elif v == 3:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        operaçoes(v)
    elif v == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        operaçoes(v)
    elif v == 5:
        break
    else:
        print("Opção invalida!")