
class ContaBancaria:
    def __init__(self, saldo_inicial: float):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo_inicial: float):
        if saldo_inicial < 0:
            raise ValorInvalidoException()
        else:
            self.__saldo = saldo_inicial

    def depositar(self, valor: float):
        try:
            if valor < 0:
                raise ValorInvalidoException('Não é possível depositar um valor negativo.')
        except ValorInvalidoException:
            print('Não é possível depositar um valor negativo.')
        else:
            self.saldo += valor


    def sacar(self, valor: float):
        try:
            if valor < 0:
                raise ValorInvalidoException
            if valor > self.saldo:
                raise SaldoInsuficienteException
        except ValorInvalidoException:
            print('Não é possível sacar um valor negativo.')
        except SaldoInsuficienteException:
            print(f"Saldo insuficiente. Saldo atual: {self.saldo}") 
        else:
            self.saldo -= valor


class ValorInvalidoException(Exception):
    def __init__(self, mensagem = "O saldo inicial não pode ser negativo."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)



class SaldoInsuficienteException(Exception, ContaBancaria):
    def __init__(self, mensagem = f"Saldo insuficiente."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)



def menu():
    print('Bem-vindo ao Banco do LP!')
    while True:
        try:
            saldoinicial = int(input('Digite o saldo inicial da sua conta: '))
        except:
            print("Saldo inválido.")
        else:
            conta = ContaBancaria(saldoinicial)
            break
    while True: 
        try:
            print('\nOpções disponíveis:\n1 - Depositar\n2 - Sacar\n3 - Consultar saldo\n0 - Sair')
            escolha = int(input('Escolha uma opção: '))
        except:
            print("Opcao inválida.")
        else:
            if escolha == 1:
                deposito = int(input('Valor que deseja depositar: '))
                conta.depositar(deposito)
            if escolha == 2:
                saque = int(input('Valor que deseja sacar: '))
                conta.sacar(saque)
            if escolha == 3:
                print(f'Saldo atual: R${conta.saldo}')
            if escolha == 0:
                print('Saindo...\n\nObrigado por usar nossos serviços!')
                break

def main():
    menu()


if __name__ == '__main__':
    main()