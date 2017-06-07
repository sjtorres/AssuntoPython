# - Ler e mostrar um vetor

vetor = []
i = 1

while i <= 5:
    n = int(input("Digite o %dº número: " %i))
    vetor.append(n)
    i += 1
print("Vetor lido: ", vetor)
