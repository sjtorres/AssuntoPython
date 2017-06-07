# - Leia e mostre 10 números na ordem inversa

v = []
i = 1

while i <= 10:
    n = int(input("Informe o %dº número: " %i))
    v.append(n)
    i += 1
i = 9
while i >= 0:
    print(v[i])
    i -= 1
