class conta_bancaria:
    def __init__(self, num_conta, nome_conta, saldo=0):
        self.num_conta = num_conta
        self.nome_conta = nome_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def imprimir_saldo(self):
        print(f'Saldo atual da conta: R$ {self.saldo:.2f}')


# Testando a classe conta_bancaria
conta = conta_bancaria(num_conta=1234, nome_conta='Gabriel Gostinski', saldo=1500)

conta.imprimir_saldo()  # Saldo atual da conta: R$ 1500.00

conta.depositar(500)  # Depósito de R$ 500.00 realizado. Saldo atual: R$ 2000.00

conta.sacar(200)  # Saque de R$ 200.00 realizado. Saldo atual: R$ 1800.00

conta.sacar(3000)  # Saldo insuficiente para realizar o saque.

conta.imprimir_saldo()  # Saldo atual da conta: R$ 1800.00
