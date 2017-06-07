# - Exemplo passando parametro com retorno

def aumento(p1, p2):
    nsal = (p1 * p2) /100
    return (nsal + p1)

sal = float(input("Salário Atual: "))
per = int(input("Porcentagem de aumento: "))

print (aumento(sal, per))