# - Exemplo passando parametro e se retorno

sal = float(input("Salário Atual: "))
per = int(input("Porcentagem de aumento: "))

def aumento(p1, p2):
    nsal = (p1 * p2) /100
    print(nsal + p1)
aumento(sal, per)