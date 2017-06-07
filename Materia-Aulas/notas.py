# - Calculando Notas

notas = [8, 8, 9, 9.5, 8.5]
soma = 0
i = 0

while i < 5:
    soma += notas[i]
    i += 1

print('Média das notas é: %3.2f' %(soma/i))