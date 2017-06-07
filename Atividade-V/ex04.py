# 4) Faça um programa com uma função que tenha um argumento numérico de entrada.
#  A função retorna ‘Positivo’, se seu argumento for positivo, ‘Negativo’ se o argumento for negativo, e ‘Neutro’ se for zero.

def positivo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "Neutro"
n1 = int(input("Digite um número: "))

print(positivo(n1))
