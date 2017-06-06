conta = int(input('Conta: '))
pgto = int(input('Pagamento: '))
troco = pgto - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
  while troco >= nota:
    print ('Uma nota de %d' %nota)
    troco -= nota

