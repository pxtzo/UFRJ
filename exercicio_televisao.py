#ex.televisao


class Televisao:
    def __init__(self, polegadas, marca, preço):
        self.polegadas = int(polegadas)
        self.marca = marca
        self.preço = preço
        self.estado = False
        self.canal = 1
        self.volume = 1

    def ligar_TV(self):
        self.estado = True
        return "Você ligou a televisão."
        canal = 1

    def desligar_TV(self):
        self.estado = False
        return "Você desligou a televisão."

    def verificar_estado(self):
        if self.estado:
            return "A televisão está ligada."
        else:
            return "A televisão está desligada."
        
    def mudar_de_canal(self,canal = 1):
        if not self.estado:
            return "A televisão está desligada."
        else:
            self.canal = canal

    def mudar_volume(self, volume):
        if self.estado:
            if 1<= volume < 80:
                self.volume = volume
                print(f'Volume alterado para: {self.volume}')
            elif 80 <= volume < 100:
                resposta = input('Volume alto, deseja continuar? [S ou N] ').lower()
                if resposta == 's':
                    self.volume = volume
                    print(f'Volume alterado para: {self.volume}')
                else:
                    self.volume = 79
                    print('Volume ajustado para: 79')
            else:
                print('Volume inválido')
        else:
            print('A TV está desligada! Ligue-a!')
    
    def exibir_infos(self):
        if not self.estado:
            return "A televisão está desligada."
        else:
            return f'Informaçoes da televisão:\nMarca: {self.marca}\nCanal: {self.canal}\nVolume: {self.volume}'
    


televisao01= Televisao(40,"LG",3000)
print(televisao01.ligar_TV())
#print(televisao01.verificar_estado())
televisao01.mudar_de_canal(70)
televisao01.mudar_volume(84)
#print(televisao01.mudar_volume(84))
print(televisao01.exibir_infos())
                    
