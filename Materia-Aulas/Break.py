# - Calcule a soma de números inteiros até ser digitado 0

soma = 0

while True:
    u = int(input('Digite um Número, o (0 sai): '))
    if u == 0:
        break
    soma += u
print('A soma dos números digitados é: %d' %soma)