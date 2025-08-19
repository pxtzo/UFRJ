from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade
    
        
    @abstractmethod
    def acelerar(self):
        self.__velocidade += self.aceleracao
        print (f'O {self.__class__.__name__} está a {self.__velocidade}k/m.')


    @abstractmethod
    def desacelerar(self):
        x = self.__velocidade - self.desaceleracao
        if x < 0:
            print(f'Deve-se respeitar a velocidade mínima (0 k/m)')
        else:
            x = self.__velocidade
            print (f'O {self.__class__.__name__} está a {self.__velocidade}k/m.')

    def exibir_velocidade(self): 
        return f'A velocidade atual é {self.__velocidade}'
    

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.aceleracao = 10
        self.desaceleracao = 8

    def acelerar(self):
        return Veiculo.acelerar(self)

    def desacelerar(self):
        return Veiculo.desacelerar(self)

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.aceleracao = 15
        self.desaceleracao = 10

    def acelerar(self):
        return Veiculo.acelerar(self)

    def desacelerar(self):
        return Veiculo.desacelerar(self)

class Caminhao(Veiculo):
    def __init__(self):
        super().__init__()
        self.aceleracao = 5
        self.desaceleracao = 3

    def acelerar(self):
        return Veiculo.acelerar(self)

    def desacelerar(self):
        return Veiculo.desacelerar(self)
    

carro = Carro()
moto = Moto()
caminhao = Caminhao()
carro.desacelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
moto.acelerar()
moto.desacelerar()
caminhao.desacelerar()