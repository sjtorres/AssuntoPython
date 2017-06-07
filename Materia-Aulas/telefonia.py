# - telefonia

m = float(input('Minutos: '))

if m < 200:
    print('Sua conta é de R$%5.2f' %(m*0.20))
elif m >= 200 and m <= 400:
    print('Sua conta é de R$%5.2f' %(m*0.18))
else:
    print('Sua conta é de R$%5.2f' %(m*0.15))