#exercicio veiculo hibrido

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = int(ano)

    def partir(self):
        print(f'{self.modelo} do ano {self.ano} está em movimento!\n')

    def mostrardados(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}')

class Motorizado(Veiculo):
    def __init__(self, marca, modelo, ano, potencia, combustivel):
        Veiculo.__init__(self, marca, modelo, ano)
        self.potencia = potencia
        self.combustivel = combustivel
    
    def alterarCombustivel(self, novoCombustivel): 
        print(f'Alterando combustível de {self.combustivel} para {novoCombustivel}\n')
        self.combustivel = novoCombustivel

class Eletrico(Veiculo):
    def __init__(self, marca, modelo, ano, autonomia, tempo_de_recarga):
        Veiculo.__init__(self, marca, modelo, ano)
        self.autonomia = autonomia
        self.tempo_de_recarga = int(tempo_de_recarga)

    def alterarAutonomia(self, novaAutonomia):
        print(f'Alterando autonomia de {self.autonomia} para {novaAutonomia}\n')
        self.autonomia = int(novaAutonomia)

class Hibrido(Motorizado, Eletrico):
    def __init__(self, marca, modelo, ano, potencia, combustivel, autonomia, tempo_de_recarga, capacidade_tanque, consumo_combustível):
        Veiculo.__init__(self, marca, modelo, ano)
        Motorizado.__init__(self, marca, modelo, ano, potencia, combustivel)
        Eletrico.__init__(self, marca, modelo, ano, autonomia, tempo_de_recarga)
        self.capacidade_tanque = float(capacidade_tanque) 
        self.consumo_combustível = float(consumo_combustível)

carro_motorizado = Motorizado("Chevrolet", "Onix LT", 2022, "100cv", "Gasolina")
carro_motorizado.alterarCombustivel("Etanol")
carro_motorizado.partir()

carro_eletrico = Eletrico("Tesla", "Model 3", 2020, 500, 30)
carro_eletrico.alterarAutonomia(600)
carro_eletrico.partir()

carro_hibrido = Hibrido("Toyota", "Prius", 2019, "100hp", "Gasolina", 200, 25, 40, 15)
carro_hibrido.partir()
carro_hibrido.alterarCombustivel("Etanol")
carro_hibrido.alterarAutonomia(220)
