from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self._velocidade = velocidade

    @property
    def velocidade(self):
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self,nova_vel):
        if nova_vel <= self._velocidade * 1.1:
            self._velocidade = nova_vel

    @abstractmethod
    def dirigir(self):
        pass

    def __str__(self):
        return f'Modelo: {self.modelo}, Vel máx: {self.velocidade}'
    

class CarroAutonomo(Veiculo):
    def __init__(self, modelo, velocidade, nivel_autonomia):
        Veiculo.__init__(self, modelo, velocidade)
        self.nivel_autonomia = nivel_autonomia

    def dirigir(self):
        print(f'Esse carro opera com {self.nivel_autonomia} de autonomia')

    def ativar_piloto_automatico(self):
        if self.nivel_autonomia >= 3:
            print('Piloto automático ativado')
        else:
            print('Piloto automático não pode ser ativado')

    def __str__(self):
        return (f'{Veiculo.__str__(self)}, Nivel de Autonomia: {self.nivel_autonomia}')
    

class CaminhaoAutonomo(CarroAutonomo):
    def __init__(self, modelo, velocidade, nivel_autonomia):
        CarroAutonomo.__init__(self, modelo, velocidade, nivel_autonomia)
        
    def dirigir(self):
        print(f'Esse caminhão possui {self.nivel_autonomia} de autonomia em longas distancias')

    def __str__(self):
        return (f'Caminhão Autonomo: {CarroAutonomo.__str__(self)}')
    
carro = CarroAutonomo("Tesla Model S", 200, 5)
print(carro)
carro.velocidade = 220
print(f"Nova velocidade: {carro.velocidade} km/h")
carro.velocidade = 210
print(f"Nova velocidade: {carro.velocidade} km/h")
print(carro.ativar_piloto_automatico())
carro_nivel_baixo = CarroAutonomo("Ford Focus", 180, 2)
print(carro_nivel_baixo.ativar_piloto_automatico())
caminhao = CaminhaoAutonomo("Volvo FH", 120, 4)
print(caminhao)
print(caminhao.dirigir())
