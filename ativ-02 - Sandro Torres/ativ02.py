class bombaCombustivel():
        def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
                self.tipoCombustivel = tipoCombustivel
                self.valorLitro = valorLitro
                self.quantidadeCombustivel = quantidadeCombustivel
                
        def abastecerPorValor(self):
                print(50 / self.valorLitro)

        def abastecerPorLitro(self):
                print(self.valorLitro * 50)
                
        def alterarValor(self, valor):
                self.valorLitro = valor
                print("Valor do combustivel ajustado %s é de: %.2f " %(self.tipoCombustivel, self.valorLitro))

        def alterarCombustivel(self, tc):
                self.tipoCombustivel = tc
                print("Seu Combustivel agora é: %s " % (self.tipoCombustivel))

        def alterarQuantidadeCombustivel(self):
                self.quantidadeCombustivel = 5000
                print(self.quantidadeCombustivel)
