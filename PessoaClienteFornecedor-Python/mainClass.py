class Pessoa:
	def __init__(self, nome, endereco, telefone, email)
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone
		self.email = email

	def imprimir(self)
		print('Meu nome é %s , moro %s e meu e-mail é %s' %(self.nome, self.endereco, self.email))

class Cliente(Pessoa):
	def __init__(self, cpf, rg, vendas)
		Pessoa.__init__(self, nome, endereco, telefone, email)
		self.cpf = cpf
		self.rg = rg
		self.vendas = []

	def imprimirDados(self)
		print('Nome: %s\nTelefone: %s\nEndereço: ' %(self.nome, self.telefone, self.endereco))

	def realizarVenda(self, produto, valor)
		self.vendas.append([produto, valor])

	def imprimirVenda(self)
		print('Resumo das Vendas do %s' %(self.nome))
		for v in self.vendas:
			print('%10s %10s' %(v[0], v[1]))

class Fornecedor(Pessoa):
	def __init__(self, cnpj, nomeFantasia, compras)
		Pessoa.__init__(self, nome, endereco, telefone, email)
		self.cnpj = cnpj
		self.nomeFantasia = nomeFantasia
		self.compras = []

	def realizarCompras(self, produto, valor)
		self.compras.append([produto, valor])

	def imprimirCompras(self)
		print('Resumo de Compras do: %s' %(self.nome))
		for c in self.compras:
			print('%10s %10s' %(c[0], c[1]))
