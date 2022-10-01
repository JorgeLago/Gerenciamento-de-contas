class Poupanca:

    def __init__(self, numero, titular, saldo):
        print("Criando conta Poupança...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("O saldo da conta Poupança é {} do titular {}. ".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor
        print("Você efetuou um deposito de {} e seu novo saldo é {}.".format(valor, self.saldo))
