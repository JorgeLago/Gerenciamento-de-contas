class Conta:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
       
    @property
    def numero(self, numero):
        self._numero = numero
    
    @property
    def saldo(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        self._saldo -= valor

    def extrato(self):
        print("O saldo da conta é {} do titular {}. ".format(self._saldo, self._titular))

    def depositar(self, valor):
        self._saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

class Poupanca(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)

        
class Corrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self._limite = limite


print("Qual o tipo de Conta deseja Abrir?")
tipo_conta = int(input("(1) Poupança ou (2) Conta Corrente: "))

if tipo_conta == 1: 
    numero_conta=(input("Numeração da conta, definido pela Agência: "))
    titular_conta=str(input("Qual o nome do titular?:")).title()
    saldo_inicial=float(input("Qual o valor inicial da conta?: "))
    
    nova_poupanca = Poupanca(numero_conta, titular_conta, saldo_inicial)
    nova_poupanca = titular_conta

else:
    numero_conta=(input("Numeração da conta, definido pela Agência: "))
    titular_conta=str(input("Qual o nome do titular?:")).title()
    saldo_inicial=float(input("Qual o valor inicial da conta?: "))
    limite_inicial=(input("Limite inicial da conta, definido pelo Gerente: "))

    nova_corrente = Corrente(numero_conta, titular_conta, saldo_inicial, limite_inicial)
    nova_corrente = titular_conta


    print("O que deseja fazer agora?: ")
    funcao = int(input("(1) Saque\n(2) Deposito\n(3) Extrato\n(4) Transferência: "))

    if funcao == 1:
        valor = int(input("Qual o valor deseja sacar?: "))
        titular_conta._saldo -= valor


