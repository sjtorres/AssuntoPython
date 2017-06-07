# Fazer um programa que peça dois valores (X e Y) no programa principal e uma função realize a troca dos valores, ou seja,
#  X recebe o conteúdo de Y e Y receberá o conteúdo de X

x = int(input("Informe um valor: "))
y = int(input("Informe outro valor: "))

def troca(x, y):
    v = x
    x = y
    y = v

    return x, y
print(troca(x, y))