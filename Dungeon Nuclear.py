#Trabalho Dungeon Nuclear

from random import randint
from random import choice

class Personagem:
    def __init__(self,forca,agilidade,sorte):
        self.verificar_atributos(forca,agilidade,sorte)
        self.forca = forca
        self.agilidade = agilidade
        self.sorte = sorte
        self.vida = 100
        self.atacou = False
        self.lutando = False
        self.turno = True
        self.arma = ['barra de chumbo']
        self.defesa = []

    def verificar_atributos(self,forca,agilidade,sorte):
        if not((forca in (0,1,2,3)) and (agilidade in (0,1,2,3)) and (sorte in (0,1,2,3))):
            print('Erro: um dos atributos nao eh um numero de 0 a 3')
            exit()
        else:
            if (forca + agilidade + sorte) != 3:
                print('Erro: a soma da forca, agilidade e sorte deve ser igual a 3')
                exit()

    def andar(self):
        if self.lutando:
            print('Voce esta no meio do combate! Nao eh possivel andar!(Voce perdeu o turno.)')
            self.turno = False


    def atacar(self):
        if not self.lutando:
            print('Nao ha nenhum inimigo para atacar.')


    def ver_vida(self):
        if self.vida <= 0:
            print('Sua vida chegou a 0.\nSua jornada nuclear chegou ao fim.\nVoce nao conquistou esse mundo. Va embora desse dominio. FIM.')
            return #dar um jeito de resetar o jogo. Regenerar vida e resetar itens
        elif 0 < self.vida <= 15:
            print(f'Voce esta em estado crítico. Voce possui {self.vida} de vida. Nao lute. FUJA!')
        elif 15 < self.vida <= 30:
            print(f'Sua vida esta baixa. Muito cuidado! Voce possui {self.vida} de vida. Procure nao tomar muitos riscos.')
        elif 30 < self.vida <= 60:
            print(f'Voce tem feridas superficiais mas nao eh o fim. Voce possui {self.vida} de vida.')
        elif 60 < self.vida <= 90:
            print(f'Voce nao corre muito perigo em seu estado atual. Voce possui {self.vida} de vida.')
        else:
            print(f'Voce esta com muita saude. No maximo uns pequenos arranhoes. Voce possui {self.vida} de vida.')
            
            
            


class Inimigo:
    def __init__(self):
        self.forca = 1
        self.agilidade = 1
        self.vida = 20
        self.fator_aleatorio = randint(1,2)

    def alterar_fator_aleatorio(self):
        if f'{self.__class__.__name__.lower()}' == 'fuso-fissao':
            self.fator_aleatorio = randint(1,3)
        else:
            self.fator_aleatorio = randint(1,2)

    def atacar(self): # depois do proximo if precisa ter um not
        if(player.turno):# and self.fator_aleatorio == 1: #and ((f'{self.__class__.__name__.lower()}') in sala.entidades_na_sala):
            if player.agilidade > self.agilidade:
                minimo_para_golpe = 15
            elif player.agilidade == self.agilidade:
                minimo_para_golpe = 10
            else:
                minimo_para_golpe = 5

            tentativa_de_golpe = randint(1,20)
            if tentativa_de_golpe >= minimo_para_golpe:
                dano = 7*self.forca
                player.vida -= dano
                print(f'{self.__class__.__name__} te deu um ataque comum. Voce recebeu {dano} de dano.')
                player.ver_vida()
            else:
                print(f'Voce esquivou do ataque de um {self.__class__.__name__.lower()}.')

            player.turno = True
                
                


class Radioativo(Inimigo):
    def __init__(self):
        Inimigo.__init__(self)
        
        
        
    

player = Personagem(2,1,0)
radioativo = Radioativo()
inimigo = Inimigo()



radioativo.atacar()
