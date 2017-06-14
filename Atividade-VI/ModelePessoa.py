class Pessoa:
    def __init__ (self, nome, peso, altura, idade = 0):
        self.nome = nome
        self.idade = 0
        self.peso = float(peso)
        self.altura = float(altura)
    def envelhecer (self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5
    def engordar (self, kg):
        self.peso += kg
    def emagrecer (self, kg):
        self.peso -= kg
    def crescer (self, cm):
        self.altura += cm

