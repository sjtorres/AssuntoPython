'''
1) Faça um programa que realize as operações de soma, subtração, multiplicação
e divisão de forma que cada operação matemática esteja em uma função distinta
(uma função para cada operação matemática). Os números devem ser obtidos fora
da função, e passados como parâmetro para as demais funções. Cada função deve
retornar o resultado para ser exibido fora delas. No início do programa deve
ser apresentado um menu ao usuário pedindo qual operação matemática ele deseja
fazer, ou se o usuário deseja finalizar o programa. O usuário pode realizar
quantos operações forem necessárias. Caso seja digitado uma opção inválida o
usuário deve ser informado e retornar ao menu de opções.
'''

def soma(v1,v2):
    return(v1+v2)
def sub(v1,v2):
    return(v1-v2)
def mult(v1,v2):
    return(v1*v2)
def div(v1,v2):
    return(v1/v2)
while True:
    print("Escolha uma das opções abaixo:")
    v = int(input("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair: "))
    if v==1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o primeiro número: "))
        print(soma(n1,n2))
    elif v==2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o primeiro número: "))
        print(sub(n1,n2))
    elif v==3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o primeiro número: "))
        print(mult(n1,n2))
    elif v==4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o primeiro número: "))
        print(div(n1,n2))
    elif v==5:
        break
    else:
        print("Opção Inválida")