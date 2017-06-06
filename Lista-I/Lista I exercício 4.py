s = float(input('Salário: '))
p = float(input('Porcentagem de aumento: '))
aumento = s * p / 100
novo = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %novo)
