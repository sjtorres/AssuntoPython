# - telefonia02

m = float(input('Minutos: '))

if m < 200:
    preco = 0.20
elif m <= 400:
    preco = 0.18
elif m <= 800:
    preco = 0.15
else:
    preco = 0.08
print('Sua conta é de R$%5.2f' %(m*preco))
