class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("O saldo da conta é {} do titular {}. ".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

