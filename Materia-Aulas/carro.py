# - carro

v = int(input('Qual a velocidadedo carro: '))

if v > 110:
    print ('Você foi multado!')
    multa = (v-110) * 5
    print ('O valor da multa é de R$%5.2f' %multa)
else:
    print('Parabéns, você não foi multado!')