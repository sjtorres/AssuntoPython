# - Acumuladores

n = 1
soma = 0

while n <= 5:
    x = int(input('Digite o %d número' %n))
    soma += x
    n += 1
print('Soma: %d' %soma)