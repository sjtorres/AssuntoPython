# - Utilizando Global passando parametro sem retorno

sal = float(input("Salário Atual: "))
per = int(input("Porcentagem de aumento: "))

def aumento(p2):
    global sal
    sal = (sal*(1+(p2/100)))
aumento(per)
print(sal)