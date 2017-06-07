# - Media de 10 números

i = 1
m = 0

while i <= 10:
    n = int(input('%d Nota: ' %i))
    m += n
    i += 1
print('A media é: %5.2f' %(m/10))