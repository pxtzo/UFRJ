#THE GAME

#from Dungeon Nuclear import *
from random import randint
from random import choice

class Personagem:
    def __init__(self,forca,agilidade,sorte):
        self.verificar_atributos(forca,agilidade,sorte)
        self.forca = forca
        self.agilidade = agilidade
        self.sorte = sorte
        self.vida = 100      
        self.lutando = False #adicionar o self.lutando nos lugares que precisa
        self.turno = True
        self.arma = ['barra de chumbo']
        self.defesa = []
        self.irradiado = 1
        

    def verificar_atributos(self,forca,agilidade,sorte):
        if not((forca in (0,1,2,3)) and (agilidade in (0,1,2,3)) and (sorte in (0,1,2,3))):
            print('Erro: um dos atributos nao eh um numero de 0 a 3')
            exit()
        else:
            if (forca + agilidade + sorte) != 3:
                print('Erro: a soma da forca, agilidade e sorte deve ser igual a 3')
                exit()

    def andar(self): #talvez essa funcao morra
        a = 1


    def entrar_em_sala(self):
        self.escolha = (input('Voce encontrou uma porta. Deseja entrar? [S ou N]')).lower()
        if self.escolha == 's':
            print('Prepare-se!')
            qualsala = randint(1,5)
            if qualsala == 1 or qualsala == 2:
                print('Voce entrou em uma Sala de Combate.')
            if qualsala == 3:
                print('Voce entrou em uma Sala de Regeneracao.')
            if qualsala == 4 or qualsala == 5:
                print('Voce entrou na Sala do Bau!')


    def atacar(self,entidade):
        if not self.lutando:
            print('Nao ha nenhum inimigo para atacar.')
            #inimigo.recebeu_ataque()
            #self.finalizou_turno

    def rezar(self):
        if self.sorte == 3:
            deu_certo = randint(1,8)
        elif self.sorte == 2:
            deu_certo = randint(1,15)
        elif self.sorte == 1:
            deu_certo == randint(1,25)
        else:
            deu_certo == randint(1,50)

        if self.lutando and ('fuso_fissao' in sala_de_combate.entidades_na_sala):
            if deu_certo:
                print('Voce rezou mas...Meu deus!!! Parece que voce, de alguma forma, atingiu o fuso_fissao e ele ficou atordoado!')
                fuso_fissao.vida -= 30
                if fuso_fissao.vida <= 0:
                    print('Voce conseguiu derrotar o FUSO_FISSAO rezando! Que loucura!')
                    self.lutando = False
                    fuso_fissao.recebeu_ataque()
                else:
                   print('Ainda eh sua vez!')
                   self.iniciou_turno()
            else:
                print('Voce rezou mas parece que nada aconteceu...Voce perdeu o turno.')
                self.finalizou_turno()

        elif self.lutando:
            if deu_certo:
                print('Voce rezou mas...Meu deus!!! Parece que, de alguma forma, voce derrotou todos os inimigos da sala!')
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        list.remove(sala_de_combate.entidades_na_sala,entidade)
                self.lutando = False
                self.iniciou_turno()
            else:
                print('Voce rezou mas parece que nada aconteceu...Voce perdeu o turno.')
                self.finalizou_turno()

        elif 'player' in sala_de_regeneracao.entidades_na_sala:
            if deu_certo:
                print('Parece que...algo mudou...')
                sala_de_regeneracao.maior_regeneracao = True #pedir pro peixoto adicionar isso
                
            else:
                print('Sera que...algo mudou...?')
            self.iniciou_turno()

        else:
            print('Voce rezou mas sera que algo mudou...?')
            self.iniciou_turno()
                

    def ver_vida(self):
        if self.vida <= 0:
            print('Sua vida chegou a 0.\nSua jornada nuclear chegou ao fim.\nVoce nao conquistou esse mundo. Va embora desse dominio. FIM.')
            return #dar um jeito de resetar o jogo. Regenerar vida, resetar itens, salas. Sair da sala.
        elif 0 < self.vida <= 15:
            print(f'Voce esta em estado crítico. Voce possui {self.vida} de vida. FUJA!')
        elif 15 < self.vida <= 30:
            print(f'Muito cuidado! Voce possui {self.vida} de vida.')
        elif 30 < self.vida <= 60:
            print(f'Sua vida esta mais baixa mas nao eh o fim. Voce possui {self.vida} de vida.')
        elif 60 < self.vida <= 90:
            print(f'Voce tem alguns arranhoes. Voce possui {self.vida} de vida.')
        else:
            print(f'Voce esta saudavel. Voce possui {self.vida} de vida.')


    #def iniciou_o_jogo  colocar coisas como: voce entra, qual os atributos do seu personagem
            #essa funcao precisa ser fora das classes pq nao vai ter player ainda



    def iniciou_turno(self): #mostrar as opcoes pro jogador / colocar isso quando acabar turno do inimigo
        if self.lutando and ('fuso_fissao' in sala_de_combate.entidades_na_sala):
            print('--Derrote Fuso_fissao--')
            while True:
                print('O que voce deseja fazer agora?\n1- Atacar\n2- Ver vida\n3- Rezar\n4- Morrer\nNao se pode fugir desse desafio. Somente desistir.\nSelecione um numero\n')
                decisao = input()
                if decisao not in ('1','2','3','4'):
                    print('Selecione um numero valido\n')
                else:
                    break

            
                
            #colocar o que acontece pra cada opcao

        elif self.lutando:
            print('--Derrote os inimigos--')
            while True: 
                print('O que voce deseja fazer agora?\n1- Atacar\n2- Ver vida\n3- Rezar\n4- Fugir\n5- Morrer\nSelecione um numero\n')
                decisao = input()
                if decisao not in ('1','2','3','4','5'):
                    print('Selecione um numero valido\n')
                else:
                    break

            if decisao == '1':
                while True:
                    print('Qual inimigo voce vai atacar?')
                    conta_opcoes = 1
                    for entidade in sala_de_combate.entidades_na_sala:
                        if entidade in ['contaminante','emissor','derretedor','supernova']:
                            print(f'{conta_opcoes}- Atacar {entidade}')
                            conta_opcoes += 1
                    print(f'{conta_opcoes}- Voltar\nSelecione um numero')
                    decisao_ataque = input()
                    if decisao_ataque not in range(conta_opcoes):
                        print('Selecione um numero valido\n')
                    else:
                        break
                novo_conta_opcoes = 0
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        novo_conta_opcoes += 1
                        if decisao_ataque == str(conta_opcoes): 
                            print('Voltando...')
                            self.iniciou_turno()
                        elif decisao_ataque == str(novo_conta_opcoes):
                            self.atacar(entidade)
                            #a principio isso ta certo

            elif decisao == '2':
                self.ver_vida()
                self.iniciou_turno()

            elif decisao == '3':
                self.rezar()

            elif decisao == '4':
                if self.vida >= 50:
                    print('Ih...fugindo com tanta vida... Mas os inimigos ainda vao tentar te atacar...')
                else:
                    print('Voce vai tentar fugir. Mas os inimigos tambem vao tentar te atacar...')
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        eval(entidade).escolha_de_ataque()
                print('Voce escapou do combate.')
                self.lutando = False
                list.clear(sala_de_combate.entidades_na_sala)
                self.iniciou_turno() #eh pra estar funcionando

            else:
                print('Voce decidiu morrer. Tudo bem...?')
                self.vida = 0
                self.ver_vida()
                

        else:
            if 'player' in sala_de_regeneracao.entidades_na_sala:
                print('Voce entra em uma sala estranha.\nVoce ve cruzes vermelhas e um motor nuclear que parece alimentar essa sala.')
                while True:
                    print('O que voce deseja fazer agora?\n1- Ligar o motor\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\nSelecione um numero\n')
                    decisao = input()
                    if decisao not in ('1','2','3','4','5'):
                        print('Selecione um numero valido\n')
                    else:
                        break

            #colocar o que acontece pra cada opcao

            elif 'player' in sala_de_bau.entidades_na_sala:
                    print('Aparentemente ha um conteiner nessa sala.')
                    while True:
                        print('O que voce deseja fazer agora?\n1- Abrir o conteiner\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\nSelecione um numero\n')
                        decisao = input()
                        if decisao not in ('1','2','3','4','5'):
                            print('Selecione um numero valido\n')
                        else:
                            break

                #colocar o que acontece pra cada opcao

            elif 'player' in sala_de_combate.entidades_na_sala:
                print('Voce derrotou todos os inimigos. Parece que eles deixaram cair algo no chao.')
                while True:
                    print('O que voce deseja fazer agora?\n1- Pegar o objeto no chao\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\nSelecione um numero\n')
                    decisao = input()
                    if decisao not in ('1','2','3','4','5'):
                        print('Selecione um numero valido\n')
                    else:
                        break

                #colocar o que acontece pra cada opcao

            else:
                print('Voce esta vagando pela area nuclear')
                while True:
                    print('O que voce deseja fazer agora?\n1- Entrar em uma sala\n2- Ver vida\n3- Rezar\n4- Morrer\nSelecione um numero\n')
                    decisao = input()
                    if decisao not in ('1','2','3','4'):
                        print('Selecione um numero valido\n')
                    else:
                        break
                
            

        
            
    def finalizou_turno(self):
        if self.irradiado > 0:
            self.vida -= self.irradiado
            print(f'Voce recebeu {self.irradiado} de dano de radiacao.')
            self.irradiado -= 1
            self.ver_vida()

        if 'player' in sala_de_combate.entidades_na_sala:
            for entidade in sala_de_combate.entidades_na_sala:
                if entidade in ['contaminante','emissor','derretedor','supernova','fuso_fissao']:
                    eval(entidade).escolha_de_ataque()

        self.iniciou_turno()
                            #ver se quando ele mata na vida morre tudo mesmo ???
                            

class Inimigo:
    def __init__(self):
        self.forca = 1
        self.agilidade = 1
        self.vida = 20
        self.fator_aleatorio = randint(1,2)

    def alterar_fator_aleatorio(self):
        if f'{self.__class__.__name__.lower()}' == 'fuso_fissao':
            self.fator_aleatorio = randint(1,3)
        elif f'{self.__class__.__name__.lower()}' == 'supernova':
            self.fator_aleatorio = 2
        else:
            self.fator_aleatorio = randint(1,2)

    def escolha_de_ataque(self):
        self.alterar_fator_aleatorio()
        if f'{self.__class__.__name__.lower()}' == 'fuso_fissao':
            if self.fator_aleatorio == 1:
                self.ataque_1()
            elif self.fator_aleatorio == 2:
                self.ataque_2()
            else:
                self.ataque_3()
        elif f'{self.__class__.__name__.lower()}' == 'supernova':
            self.ataque_2()
        else:
            if self.fator_aleatorio == 1:
                self.ataque_1()
            else:
                self.ataque_2()


    def ataque_1(self): # depois do proximo if precisa ter um not    #talvez nao precise de player.turno
        if(player.turno): #and ((f'{self.__class__.__name__.lower()}') in sala.entidades_na_sala):
            if player.agilidade > self.agilidade:
                minimo_para_golpe = 15
            elif player.agilidade == self.agilidade:
                minimo_para_golpe = 10
            else:
                minimo_para_golpe = 5 

            tentativa_de_golpe = randint(1,20)
            if tentativa_de_golpe >= minimo_para_golpe:
                dano = 4*self.forca
                player.vida -= dano
                print(f'{self.__class__.__name__} te deu um ataque comum. Voce recebeu {dano} de dano.')
                if f'{self.__class__.__name__.lower()}' in ['contaminante','emissor','fuso_fissao']:
                    self.irradiar() 
                    print(f'O ataque te irradiou! Voce esta com {player.irradiado} de radiacao.')
                player.ver_vida()
            else:
                print(f'Voce esquivou do ataque de um {self.__class__.__name__.lower()}.') 


    def recebeu_ataque(self):
        if self.vida <= 0:
            list.remove(sala_de_combate.entidades_na_sala,f'{self.__class__.__name__.lower()}')
            self.vida = eval(f'{self.__class__.__name__.lower()}_padrao').vida
            if f'{self.__class__.__name__.lower()}' in ['contaminante','emissor','derretedor','supernova']:
                print(f'Voce derrotou um {self.__class__.__name.lower()}')
            else:
                a = 1#funcao de player.completou_dungeon()
        else:
            player.finalizou_turno() #talvez isso nao deva ficar aqui e sim no final do ataque do player
            

class Radioativo(Inimigo):
    def __init__(self):
        Inimigo.__init__(self)
        self.agilidade = 2

    def irradiar(self):
        player.irradiado += 1


class Fervente(Inimigo):
    def __init__(self):
        Inimigo.__init__(self)
        self.forca = 2
        self.ativou_calor = False

    def recebeu_ataque(self):
        if self.vida <= 0:
            list.remove(sala.entidades_na_sala,f'{self.__class__.__name__.lower()}')
            self.vida = eval(f'{self.__class__.__name__.lower()}_padrao').vida
            self.forca = eval(f'{self.__class__.__name__.lower()}_padrao').forca
            self.ativou_calor = False
        elif not self.ativou_calor and (self.vida < eval(f'{self.__class__.__name__.lower}_padrao').vida):
            self.forca += 1
            self.ativou_calor = True
            print(f'Esse {self.__class__.__name__.lower} SOBREAQUECEU e esta mais forte!')
            player.finalizou_turno()
        else:
            player.finalizou_turno()



class Contaminante(Radioativo):
    def __init__(self):
        Radioativo.__init__(self)
        self.vida = 40


class Emissor(Radioativo):
    def __init__(self):
        Radioativo.__init__(self)


class Derretedor(Fervente):
    def __init__(self):
        Fervente.__init__(self)


class Supernova(Fervente):
    def __init__(self):
        Fervente.__init__(self)
        self.vida = 15


class Fuso_fissao(Radioativo,Fervente):
    def __init__(self):
        Radioativo.__init__(self)
        Fervente.__init__(self)
    
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'


#quantidade_de_inimigos = randint(1,3)
#escolha = input('Voce encontrou uma porta. Deseja entrar? [S ou N]')
class Sala:
    def __init__(self):
        self.entidades_na_sala = []
        #self.escolha = input('Voce encontrou uma porta. Deseja entrar? [S ou N]')

    def personagem_entrou(self):
        if 





    def quantidade_de_inimigos(self):
        x = randint(1,3)
        return x



class Combate(Sala):
    def __init__(self):
        Sala.__init__(self)
 
       
    def spawnar_inimigos(self):
        possiveis_inimigos = ['contaminante', 'supernova', 'emissor', 'derretedor']
        count = 0
        y = self.quantidade_de_inimigos()
        print(f'Voce se deparou com {y} inimigo(s)')
        while count < y:
            self.entidades_na_sala.append(choice(possiveis_inimigos))
            count += 1
        

    def quantidade_de_inimigos(self):
        x = randint(1,3)
        return x

    #def desespawnar_inimigos(self):
        for entidade in self.entidades_na_sala:
            if entidade in ['contaminante', 'supernova', 'emissor', 'derretedor']:
                if eval(entidade).vida <= 0:
                    list.remove(self.entidades_na_sala, entidade)
                    eval(entidade).vida


class Regeneracao(Sala):
    def __init__(self):
        Sala.__init__(self)
        self.maior_regenerecao = False

    
    def healar(self):
        if self.maior_regenerecao:
            player.vida += 50
            print('Suas preces foram ouvidas. Os deuses irão lhe retribuir pela sua fé!\nVoce recebeu 50 de vida!')
        else:
            player.vida += 30
            print('Voce sentiu uma energia fluindo pelo seu corpo.\nVoce recebeu 30 de vida!')



class Bau(Sala):
    def __init__(self):
        Sala.__init__(self)
        self.conteiner = [] 
        self.entidades_na_sala.append(self.conteiner)    

    def abrirbau(self):
        escolha_do_bau = (input('Voce deparou-se com um bau misterioso dentro da sala. Deseja abri-lo? [S ou N]')).lower()
        if escolha_do_bau == 'n':
            print('Voce decidiu nao abrir o bau, nao há mais o que fazer na sala.')
            self.entidades_na_sala.clear()
        elif escolha_do_bau == 's':
            dentro_do_bau = randint(1,7)
            if dentro_do_bau == 1 or dentro_do_bau == 2 or dentro_do_bau == 3:
                barras = randint(1,3)
                if barras == 1:
                    print('Voce encontrou uma barra de chumnbo enferrujada.\n-Dano: 5- ')
                if barras == 2:
                    print('Voce encontrou uma barra de chumnbo levemente desgastada.\n-Dano: 8- ')
                if barras == 3:
                    print('Voce encontrou uma barra de chumnbo nova e reluzente.\n-Dano: 11- ')
            if dentro_do_bau == 4 or dentro_do_bau == 5 or dentro_do_bau == 6:
                escudos = randint(1,3)
                if escudos == 1:
                    print('Voce encontrou um escudo de madeira.\n-Defesa: 5-')
                if escudos == 2:
                    print('Voce encontrou um escudo de ferro.\n-Defesa: 15-')
                if escudos == 3:
                    print('Voce encontrou um escudo de chumbo potente.\n-Defesa: 30-')
            if dentro_do_bau == 7:
                player.vida -= 20
                print('O-o que? O bau virou um mimico e te atacou!!\nVoce perdeu 20 de vida.')
                player.ver_vida()

player = Personagem(2,1,0)
radioativo = Radioativo()
inimigo = Inimigo()
contaminante = Contaminante()


contaminante_padrao = Contaminante()
emissor_padrao = Emissor()
derretedor_padrao = Derretedor()
supernova_padrao = Supernova()
fuso_fissao_padrao = Fuso_fissao()


sala = Sala()
sala_de_combate = Combate()
sala_de_segeneracao = Regeneracao()
sala_de_bau = Bau()
sala.entrar()
#sala_de_combate.spawnar_inimigos()
sala_de_bau.abrirbau()



