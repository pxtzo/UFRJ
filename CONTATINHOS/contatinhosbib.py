contatos = []

#1 
def criarcontato (nome, telefone = '', email = '', instagram = ''):
    ''' Funcao que retorna as informações de um contato, nome, telefone, email
    e instagram, str, str , str, str -> lista'''
    telefones = [telefone,]
    contato = [nome, telefones, email, instagram]
    return contato



#2
def atualizarcontato (contato, indice, novainfo):
    '''Funcao que atualiza as informações de um contato, indice ->
    0=nome, 1=telefone, 2=email, 3=instagram; list, int, str -> bool'''
    if indice == 0 or indice == 2 or indice == 3:
        contato[indice] = novainfo
        return True
    elif indice == 1 and (novainfo != contato[1][0]):
        list.append(contato[1], novainfo)
        return True
    else:
        return False



#3
def excluirtelefone(contato, tel):
    '''funcao para excluir um telefone do contato, list, str -> bool'''
    if tel in contato[1]:
        list.remove(contato[1], tel)
        return True
    else:
        return False



#4
def buscardados (contatos,nome):
    i = 0
    nome1 = str.lower(nome)
    retorno = []
    while i < len(contatos):
        nome2 = contatos[i][0]
        nome2 = str.lower(nome2)
        if nome1 in nome2:
            list.append(retorno,contatos[i]) 
        i += 1
    return retorno



#5
def quem_ligou (telefone):
    '''funcao que retorna os dados do contatinho relacionado ao telefone, str -> list'''               
    for i in range(len(contatos)):
        if type(contatos[i][1]) is list:
            for j in range(len(contatos[i][1])):
                if telefone in contatos[i][1][j]:
                    return contatos[i]
        if telefone in contatos[i][1]:
            return contatos[i]
    else:
        return []  
                      
    

#6
def excluircontato (contatos, indice):
    '''funcao que exclui um contato, list, int -> none'''
    list.remove(contatos, contatos[indice])



#7
def aglutinarcontatos (contatos, indice1, indice2):
    '''funcao que junta dois contatos caso o usuario salvou a mesma pessoa duas vezes
    as informaçoes serão agregadas ao contato do primeiro indice, list, int, int -> none'''
    if (indice1 != indice2):
        for i in range(len(contatos[indice1])):      
            if contatos[indice1][i] == '' and contatos[indice2][i] != '':
                contatos[indice1][i] = contatos[indice2][i]
        for j in range(len(contatos[indice1][1])):
            if contatos[indice1][1] == '' and contatos[indice2][1] != '':
                list.remove(contatos[indice1][1], '')
            elif contatos[indice2][1][j] not in contatos[indice1][1][j]:
                list.append(contatos[indice1][1], contatos[indice2][1][j])
        excluircontato(contatos, indice2)
    