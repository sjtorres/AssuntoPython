# - Fatorial de 10

i = 1
fat = 1
n = int(input('Digite um Número: '))

while i <= n:
    fat *= i
    i += 1
print('O fatorial %d é: %d' %(n, fat))