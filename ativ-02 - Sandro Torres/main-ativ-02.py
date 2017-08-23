from ativ02 import bombaCombustivel



while True:
    menu = int(input('\nSistema do Posto\nMenu de opções:\n\n1-Cadastrar Bomba\n2-Alterar valor do litro do combustivel\n3-Alterar tipo de combustivel\n4-Alterar quantidade de combustivel\n5-Abastecer por valor\n6-Abastecer por litro\n7-Sair\nDigite a opção: '))
    if menu == 1:
        tipo = input('Digite o tipo de combustivel: ')
        litro = float(input('Digite o valor do litro: '))
        quantidade = float(input('Digite a quantidade de litros: '))

        bomba01 = bombaCombustivel(tipo, litro, quantidade)

    elif menu == 2:
        i = float(input('Digite o novo valor do combustivel: '))
        bomba01.alterarValor(i)
    elif menu == 3:
        i = input('Digite o novo combustivel: ')
        bomba01.alterarCombustivel(i)
    elif menu == 4:
        bomba01.alterarQuantidadeCombustivel()
    elif menu == 5:
        bomba01.abastecerPorValor()
    elif menu == 6:
        bomba01.abastecerPorLitro()
    elif menu == 7:
        print('Saindo.......')
        break
    else:
        print('Opção inválida!')