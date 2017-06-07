def calculaTabuada(n):
    if (n <= 0):
        print ("Informe um número válido para calcular a tabuada!")
    else :
        print ("Calculando tabuada do ", n, "...")

        for multiplicador in range(1, 11):
            resultado = multiplicador * n
            print (n, " x ", multiplicador, " = ", resultado)

#solicita a entrada do nro
numero = int(raw_input("Informe o número para calcular a tabuada: "))
calculaTabuada(numero)
