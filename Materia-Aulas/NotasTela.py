# - Leia 4 notas e mostre notas na tela e a média

v = []
i = 1

while i <= 4:
    n = float(input("Informe a %dº nota: " %i))
    v.append(n)
    i += 1
s = 0
i = 0
while i < 3:
    s += v[i]
    i += 1
print("Minhas notas: ", v)
print("Minha média: %3.2f" %(s/i))