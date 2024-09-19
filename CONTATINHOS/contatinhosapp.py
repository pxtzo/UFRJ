import os
import contatinhosbib as cb
contatinhos = []



def criarcontato2():
    '''Função para criar contato na interface'''
    while True:
        print("Preencha as informações corretamente. \nNome é uma informação obrigatória, caso não queira digitar as demais, aperte enter.")
        nome2 = input("Digite o nome do contato: ")
        if nome2 == '':
            os.system('cls')
            print("Essa informação é obrigatória!\n")
        else:
            telefone2 = input("Digite o telefone do contato: ")
            email2 = input("Digite o email do contato: ")
            instagram2 = input("Digite o instagram do contato: ")
            os.system('cls')
            break
    return cb.criarcontato(nome2, telefone2, email2, instagram2)





def main():
    '''Função principal do aplicativo'''
    print("\n     - ContatinhosApp -\n- Sua Agenda de Contatinhos -")
    print("_____________________________")
    print("\nInicie criando seu primeiro contato!")
    contatinhos = [criarcontato2()]
    cb.contatos = contatinhos
    while True:
        print('\nContatinhos:')
        print(contatinhos)
        print("\nPara utilizar as funcionalidades, digite o código da opção escolhida.")
        print("1 - Criar novo contato\n2 - Buscar um contato\n3 - Atualizar um contato\n4 - Excluir um contato")
        print("5 - Identificar quem ligou\n6 - Aglutinar dois contatos\n7 - Sair")
        while True:
            usar = input("Qual funcionalidade deseja usar? ")
            if usar in '1234567' and usar != '':
                    usar = int(usar)
                    if 1 <= usar <= 7:
                        usar = str(usar)
                        break
                    else:
                        print('Índice inválido')
            else:
                print('Índice inválido')
        if usar == '1':
            os.system('cls')
            print('-Você selecionou a função de criar contato-')
            list. append(contatinhos, criarcontato2())
            os.system('cls')
            print('Novo contato adicionado com sucesso!')
        if usar == '2':
            os.system('cls')
            print('-Você selecionou a função de buscar um contato-')
            busca1 = input('Qual nome deseja buscar? ')
            os.system('cls')
            print(f'{cb.buscardados(contatinhos, busca1)}\n')
            print('Contato identificado com sucesso!\n')
        if usar == '3':
            os.system('cls')
            print('-Você selecionou a função de atualizar um contato-\n')
            print(contatinhos)
            while True:
                x = (input('\nQual o índice do contato que deseja atualizar? '))
                if x in '0123456789' and x != '':
                    x = int(x)
                    if 0 <= x <= len(contatinhos):
                        break
                    else:
                        print('Índice inválido')
                else:
                    print('Índice inválido')
            print('Qual informação deseja atualizar?\n0 - Nome\n1 - Telefone\n2 - Email\n3 - Instagram')
            while True:
                y = (input('\nDigite o código desejado: '))
                if y in '0123' and y != '':
                    y = int(y)
                    if 0 <= y <= 3:
                        break
                    else:
                        print('Índice inválido')
                else:
                    print('Índice inválido')
            if y == 1: 
                escolha = input('Deseja excluir ou adicionar um telefone? ')
                if escolha == str.lower('excluir'):
                    excluirtel = input('Qual telefone deseja excluir? ')
                    cb.excluirtelefone(contatinhos[x], excluirtel)
                    if contatinhos[x][1] == []:
                        list.append(contatinhos[x][1], '')
                    os.system('cls')
                    print('Informação excluída com sucesso!')
                elif escolha == str.lower('adicionar'):   
                    w = input('\nDigite a nova informação: ')
                    if '' in contatinhos[x][1]:
                        cb.atualizarcontato((contatinhos[x]), y, w)
                        list.remove(contatinhos[x][1], '')
                    else:    
                        cb.atualizarcontato((contatinhos[x]), y, w)
                    os.system('cls')
                    print('Nova infomação adicionada com sucesso!')        
            else:
                z = input('\nDigite a nova informação: ') 
                cb.atualizarcontato((contatinhos[x]), y, z)
                os.system('cls')
                print('Nova infomação adicionada com sucesso!')
        if usar == '4':
            os.system('cls')
            print('-Você selecionou a função de exlcuir um contato-')
            print(contatinhos)
            while True:
                excluir = (input('\nQual o índice do contato que deseja excluir? '))
                if excluir in '0123456789' and excluir != '':
                    excluir = int(excluir)
                    if 0 <= excluir <= len(contatinhos):
                        break
                    else:
                        print('Índice inválido')
                else:
                    print('Índice inválido')
            cb.excluircontato(contatinhos, excluir)
            print('\nContato excluído com sucesso!')
        if usar == '5':
            os.system('cls')
            print('-Você selecionou a função de identificar quem ligou-')
            while True:
                ligacao = input('Qual número que ligou para você? ')
                if ligacao == '':
                    print('Número inexistente')
                else:
                    break
            numero = cb.quem_ligou(ligacao)
            if numero == []:
                print('Número desconhecido')
            else:
                os.system('cls')
                print(numero)
                print('\nContato identificado com sucesso!')
        if usar == '6':
            os.system('cls')
            print('-Você selecionou a função de aglutinar dois contatos-')
            print('OBS: As informações do primeiro contato informado manterão as mesmas.')
            print('Caso tenha informações vazias, serão preenchidas pelas informações do segundo contato.\n')
            print(contatinhos)
            while True:
                ind1 = (input('\nQual o índice do primeiro contato que deseja aglutinar? '))
                if ind1 in '0123456789' and ind1 != '':
                    ind1 = int(ind1)
                    if 0 <= ind1 <= len(contatinhos):
                        break
                    else:
                        print('Índice inválido')
                else:
                    print('Índice inválido')
            while True:
                ind2 = (input('\nQual o índice do segundo contato que deseja aglutinar? '))
                if ind2 in '0123456789' and ind2 != '':
                    ind2 = int(ind2)
                    if 0 <= ind2 <= len(contatinhos):
                        break
                    else:
                        print('Índice inválido')
                else:
                    print('Índice inválido')
            cb.aglutinarcontatos(contatinhos, ind1, ind2)
            os.system('cls')
            print('\nContatos aglutinados com sucesso!\n')
        if usar == '7':
            os.system('cls')
            print('-Você selecionou a função sair-')
            print('Obrigado por escolher o ContatinhosApp :)')
            quit = input('Pressione enter para confirmar (caso não deseja, digite algo): ')
            os.system('cls')
            if quit == str.lower(''):
                break
main()

