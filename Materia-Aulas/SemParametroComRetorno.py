# - Sem parametros e com retorno

def aumento():
    sal = float(input("Salário Atual: "))
    per = int(input("Porcentagem de aumento: "))

    return (sal*(1+(per/100)))
print (aumento())
