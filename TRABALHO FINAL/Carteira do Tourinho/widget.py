from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QTimer
from perguntas_ui import Ui_Perguntas
from telainicial_ui import Ui_tela_inicial
from menuprincipal_ui import Ui_menu_principal
import tourinho as tr



class Tela_Inicial(QWidget, Ui_tela_inicial):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon("imagens/touro_icon.png"))
        touro = QPixmap("imagens/touro.png")  
        self.label_touro.setPixmap(touro)

        self.botao_cadastrar.clicked.connect(self.clicar_cadastrar)
        self.botao_jacadastrado.clicked.connect(self.clicar_jacadastrado)

    def clicar_cadastrar(self):
        nome = self.line_edit_nome.text()
        saldo = self.line_edit_saldo.text()
        if not saldo.isdigit():
            self.label_notificacao.setText("O saldo precisa ser um número")
        else:
            tr.cliente.mudar_dados(nome, saldo, "Moderado")
            tr.cliente.salvar_dados("dados")
            self.hide()
            self.perguntas = Perguntas()  
            self.perguntas.showMaximized()
    

    def clicar_jacadastrado(self):
        try:
            if tr.cliente.carregar_dados("dados"):
                pass
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            self.label_notificacao.setText('Arquivo Inexistente')
        else:
            tr.cliente.calcular_lucro_prejuizo()
            self.hide()
            self.menu_principal = Menu_Principal()
            self.menu_principal.showMaximized()


#####################################################################


class Perguntas(QWidget, Ui_Perguntas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("imagens/touro_icon.png"))
        self.respostas = []
        self.botao_finalizado.clicked.connect(self.clicar_finalizado)
        

    def caixas(self, a , b , c):
        if a.isChecked():
            self.respostas.append("a")
        elif b.isChecked():
            self.respostas.append("b")
        elif c.isChecked():
            self.respostas.append("c")


    def respostas_das_caixas(self):
        self.caixas(self.botao_a_1, self.botao_b_1, self.botao_c_1)
        self.caixas(self.botao_a_2, self.botao_b_2, self.botao_c_2)
        self.caixas(self.botao_a_3_1, self.botao_b_3_1, self.botao_c_3_1)
        self.caixas(self.botao_a_3_2, self.botao_b_3_2, self.botao_c_3_2)
        self.caixas(self.botao_a_4, self.botao_b_4, self.botao_c_4)
        count_a = self.respostas.count("a") 
        count_b = self.respostas.count("b") 
        count_c = self.respostas.count("c") 
        if count_a > count_b and count_a > count_c: 
            tr.cliente.tipo = "Conservador"
            tr.cliente.salvar_dados("dados")    
        elif count_b > count_a and count_b > count_c: 
            tr.cliente.tipo = "Moderado"
            tr.cliente.salvar_dados("dados")   
        elif count_c > count_a and count_c > count_b: 
            tr.cliente.tipo = "Arrojado"
            tr.cliente.salvar_dados("dados")    

    def clicar_finalizado(self):
            self.respostas_das_caixas()
            self.hide()
            self.menu_principal = Menu_Principal()
            self.menu_principal.show()


######################################################################



class Menu_Principal(QWidget, Ui_menu_principal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("imagens/touro_icon.png"))
        self.dados_pessoais()
        self.minha_carteira()

        self.botao_prever.clicked.connect(self.prevendo)
        self.botao_confirmar.clicked.connect(self.investindo)  
        self.botao_ver_grafico.clicked.connect(self.visualizando_investimento)
        self.botao_saiba_mais.clicked.connect(self.sabendo_mais)
        self.botao_sobre_acoes.clicked.connect(self.sobre_acoes)
        self.botao_sobre_criptos.clicked.connect(self.sobre_criptos)
        self.botao_sobre_commodities.clicked.connect(self.sobre_commodities)
        self.botao_sobre_titulos.clicked.connect(self.sobre_titulos_e_fundos)
        self.botao_vender.clicked.connect(self.botao_vender_mensagem)
        self.botao_ver_grafico_pizza.clicked.connect(self.minha_carteira_ver_grafico)
        
        self.label_texto_inicial_investindo_2.setText(f'Você é um investidor do tipo {tr.cliente.tipo} e temos algumas dicas que podem te ajudar!')
        self.texto_conservador = "O conservador é o tipo de investidor que busca retorno financeiro das formas mais seguras possíveis, correndo o menor risco possível. Por muitos motivos um investidor pode ser considerado conservador, seja por seu objetivo ao obter lucros ou por uma filosofia financeira. O conservador é paciente ao obter lucros, sempre buscando os resultados mais confiáveis e para que no fim de um longo período de investimento, o retorno seja satisfatório. Muitas vezes o conservador será o investidor novato, este que ainda está aprendendo a investir e ainda não está acostumado com o territórios dos investimentos. Portanto, se você é novo nesse cenário, é amplamente recomendado que você inicie nesse mundo como um conservador para melhorar seu entendimento sobre os investimentos e como cada um funciona. Investimentos de renda fixa como: Tesouro Direto, CDBs, LCIs, LCAs devem ser o foco de um conservador, assim como Fundos Imobiliários, que também merecem atenção. Esse investidor deve ter cautela ao buscar ações, commodities e, principalmente, as criptomoedas, já que esses apresentam maiores variações e incertezas, o oposto do que o investidor conservador deseja para o seu investimento. Caso o investidor conservador deseje investir nesses últimos ativos mencionados, é preciso que o mesmo estude o funcionamento desses ativos de forma mais aprofundada para então evitar perdas severas de capital.</p>"
        self.texto_moderado = "O investidor moderado muitas vezes é associado ao investidor “mais lúcido” entre os 3 perfis gerais: conservador, moderado e arrojado; já que ele busca a confiabilidade e segurança do tipo conservador, mas também não perde a oportunidade de obter maiores lucros, como o arrojado. O moderado deve ter alguma experiência quando se trata de investimentos, seja por já ter investido previamente em ativos de renda fixa e/ou fundos imobiliários ou por ter estudado mais profundamente o funcionamento do mercado de investimentos. Como dito antes, esse perfil de investidor ainda mantém a segurança de seus investimentos. Ao menos 50% do total investido deve estar em renda fixa, garantindo que, em casos extremos, nem todo o capital seja perdido, já que a renda fixa é o ramo mais seguro dos investimentos. Por outro lado, o investidor moderado não perderá a chance de se aventurar um pouco em investimentos de mais alto risco, como Ações, Commodities e até mesmo Criptomoedas, mas sempre com cautela. Esses conjuntos de ativos apresentam maior variabilidade e, portanto, maiores possibilidades de lucro, mas em contrapartida, maiores chances de perda também. Isso significa que o investidor moderado não deve entrar nesses setores sem entender como funcionam, para que então suas finanças apresentam uma boa sintonia entre segurança e lucratividade. Enfim, o moderado deve evitar fortemente investir tudo em renda variável, ou seja, ativos que não sejam de renda fixa. Ao menos que o investidor tenha ampla experiência no mercado, evite grandes riscos e equilibre seus investimentos."
        self.texto_arrojado = "O investidor arrojado é aquele que busca os maiores lucros, enfrentando os mais diversos riscos no ramo do mercado de investimentos para alcançar esse objetivo. Esse investidor aplica apenas uma pequena parte de seu capital em investimentos de renda fixa e a maior parte vai para a renda variável, como: ações, commodities e criptomoedas. Dessa forma, o arrojado se aproveita ao máximo das variações no mercado para obter os lucros mais expressivos no menor tempo possível. Apesar disso parecer ótimo, a pessoa que apresenta esse perfil de investidor deve ter amplo conhecimento do mercado e muita experiência para investir dessa maneira. A bolsa de valores, o mundo do petróleo, ouro, prata e as moedas digitais, são em muitos casos uma armadilha para os investidores inexperientes que querem muito dinheiro em pouco tempo, não porque esses são investimentos falsos e sem valor, mas sim pela sua altíssima volatilidade. Novamente, para desfrutar das possibilidades financeiras que esses ativos voláteis apresentam, o arrojado precisa de muito conhecimento e, muitas vezes, não só do mundo das negociações de investimentos, mas em também, de geopolítica. Como exemplo, o valor do petróleo pode mudar facilmente com o início de uma guerra inesperada, ou do fechamento de negociações entre dois países. Entender o alcance de seus investimentos, perceber possibilidades em âmbito mundial e conectar esses padrões para aplicá-los em suas finanças; esse é um papel que somente o investidor arrojado pode realizar. Não se esqueça, se você não se sente fortemente preparado como um investidor ou não teve experiência relevante no que se diz sobre investimentos, evite investir como um arrojado."

        self.atualizar_pagina = QTimer(self)
        self.atualizar_pagina.timeout.connect(self.minha_carteira)
        self.atualizar_pagina.timeout.connect(self.dados_pessoais)
        self.atualizar_pagina.start(1000)  #atualiza a funcao a cada 1 segundo

        self.atualizar_notificacoes = QTimer(self)
        self.atualizar_notificacoes.timeout.connect(self.labels_notificacao)
        self.atualizar_notificacoes.start(5000)

    def dados_pessoais(self):
        self.label_dados_pessoais.setText(f'Nome: {tr.cliente.nome} | Investidor do tipo: {tr.cliente.tipo} | Saldo atual: {tr.cliente.saldo}')

    def labels_notificacao(self):
        self.label_notificacao_2.setText('')
        self.label_notificacao_4.setText('')
        self.label_notificacao_6.setText('')    

    def minha_carteira_ver_grafico(self):
        tr.cliente.ver_pizza()


    def minha_carteira(self):
        possiveis_investimentos = {'Meta': [self.label_stacked_meta], 'Google': [self.label_stacked_google],
                            'Apple': [self.label_stacked_apple], 'Microsoft': [self.label_stacked_microsoft],
                            'Tesla': [self.label_stacked_tesla], 'Bitcoin': [self.label_stacked_bitcoin],
                            'Ethereum': [self.label_stacked_ethereum],'Solana': [self.label_stacked_solana],
                            'Cardano': [self.label_stacked_cardano], 'Zcash': [self.label_stacked_zcash], 
                            'Ouro': [self.label_stacked_ouro], 'Petroleo': [self.label_stacked_petroleo], 
                            'Gas': [self.label_stacked_gas], 'Prata': [self.label_stacked_prata],
                            'Algodao': [self.label_stacked_algodao], 'AGG': [self.label_stacked_AGG],
                            'SHY': [self.label_stacked_SHY], 'VNQ': [self.label_stacked_VNQ],
                            'GOVT': [self.label_stacked_GOVT], 'BND': [self.label_stacked_bnd]}
        for investimento in possiveis_investimentos.keys():
            investido = [tr.cliente.investimentos[investimento][0], tr.cliente.investimentos[investimento][3]]
            possiveis_investimentos[investimento][0].setText(f'Valor Investido: {investido[0]}  |  Variação: {investido[1]}')
        

    
    def sabendo_mais(self):
        caixa_de_mensagem = QMessageBox()
        caixa_de_mensagem.setWindowIcon(QIcon("imagens/investidor.png"))
        if tr.cliente.tipo == 'Conservador':
            caixa_de_mensagem.setWindowTitle('Conservador')
            caixa_de_mensagem.setText(self.texto_conservador)
        elif tr.cliente.tipo == 'Moderado':
            caixa_de_mensagem.setWindowTitle('Moderado')
            caixa_de_mensagem.setText(self.texto_moderado)
        elif tr.cliente.tipo == 'Arrojado':
            caixa_de_mensagem.setWindowTitle('Arrojado')
            caixa_de_mensagem.setText(self.texto_arrojado) 
        caixa_de_mensagem.exec()
            
    


    def sobre_acoes(self):
        caixa_de_mensagem_acoes = QMessageBox()
        caixa_de_mensagem_acoes.setWindowIcon(QIcon("imagens/about.png"))
        caixa_de_mensagem_acoes.setWindowTitle('Ações')
        caixa_de_mensagem_acoes.setText('As ações representam uma fração da propriedade de uma empresa. Esse tipo de investimento oferece potencial de crescimento e apresenta volatilidade, visto que os preços das ações podem variar de acordo com o desempenho da empresa e das condições socioeconômicas.')
        caixa_de_mensagem_acoes.setDetailedText('Aderência ao perfil:\n\nConservador: Baixa a média\nModerado: Média\nArrojado: Alta')
        caixa_de_mensagem_acoes.exec()

    def sobre_criptos(self):
        caixa_de_mensagem_criptos = QMessageBox()
        caixa_de_mensagem_criptos.setWindowIcon(QIcon("imagens/about.png"))
        caixa_de_mensagem_criptos.setWindowTitle('Criptos')
        caixa_de_mensagem_criptos.setText('Criptomoedas são ativos digitais que usam blockchain¹ para transações seguras. Elas apresentam alto potencial de retorno, mas são extremamente voláteis e arriscadas.')
        caixa_de_mensagem_criptos.setDetailedText('Aderência ao perfil:\n\nConservador: Muito Baixa\nModerado: Média\nArrojado: Muito Alta')
        caixa_de_mensagem_criptos.exec()


    def sobre_commodities(self):
        caixa_de_mensagem_commodities = QMessageBox()
        caixa_de_mensagem_commodities.setWindowIcon(QIcon("imagens/about.png"))
        caixa_de_mensagem_commodities.setWindowTitle('Commodities')
        caixa_de_mensagem_commodities.setText('Commodities são recursos naturais ou matérias-primas negociadas globalmente. Elas oferecem proteção contra a inflação, mas seus preços podem ser voláteis devido a fatores externos, como oferta e demanda, geopolíticas e condições climáticas.')
        caixa_de_mensagem_commodities.setDetailedText('Aderência ao perfil:\n\nConservador: Média\nModerado: Alta\nArrojado: Muito Alta')
        caixa_de_mensagem_commodities.exec()


    def sobre_titulos_e_fundos(self):
        caixa_de_mensagem_titulos = QMessageBox()
        caixa_de_mensagem_titulos.setWindowIcon(QIcon("imagens/about.png"))
        caixa_de_mensagem_titulos.setWindowTitle('Títulos e Fundos')
        caixa_de_mensagem_titulos.setText('Títulos e fundos são investimentos voltados para estabilidade e renda previsível, sendo ideais para diversificação e estabilidade. Incluem renda fixa (como títulos do Tesouro) e fundos imobiliários, sendo apropriados para perfis conservadores. Nesse simulador, serão apresentadas opções de ETF (Exchange-Traded Fund), que são fundos de investimento negociados na bolsa que replicam o desempenho de um índice, setor ou classe de ativos.')
        caixa_de_mensagem_titulos.setDetailedText('Aderência ao perfil:\n\nConservador: Muito Alta\nModerado: Alta\nArrojado: Baixa a Moderada')
        caixa_de_mensagem_titulos.exec()

    

    def investindo(self):
        qual_investir = self.combo_box_qual_investir.currentText()
        quanto_investir = self.line_edit_quanto_investir.text()
        try:
            quanto_investir = float(quanto_investir)
            if quanto_investir > tr.cliente.saldo:
                raise RuntimeError ('Você não possui saldo suficiente')
            if quanto_investir <= 0:
                raise RuntimeError ('Não é possível investir um valor menor ou igual a zero')
            tr.cliente.investir(qual_investir, quanto_investir)
            tr.cliente.salvar_dados('dados')
            self.label_notificacao_2.setText(f"Parabéns! Você investiu R${quanto_investir} em {qual_investir}")
        except RuntimeError as erro:
            self.label_notificacao_2.setText(str(erro))
        except:
            self.label_notificacao_2.setText("Ação inválida.")

    def visualizando_investimento(self):
        qual_visualizar = self.combo_box_visualizar_investimento.currentText()
        tr.cliente.ver_grafico_real(qual_visualizar)


    def vendendo(self):
        qual_vender = self.combo_box_vender.currentText()
        quanto_vender = self.line_edit_quanto_vender.text()
        try:
            quanto_vender = float(quanto_vender)
            if quanto_vender <= 0:
                raise RuntimeError ('Você não pode vender um valor negativo.')
            if quanto_vender > tr.cliente.investimentos[qual_vender][0]:
                raise RuntimeError ('Não é possível ficar com um investimento negativo.')
            tr.cliente.vender(qual_vender, quanto_vender)
            tr.cliente.salvar_dados('dados')
            self.label_notificacao_6.setText(f'Parabéns! Você vendeu R${quanto_vender} de {qual_vender}')
        except RuntimeError as erro:
            self.label_notificacao_6.setText(str(erro))
        except:
            self.label_notificacao_6.setText("Ação inválida.")


    def botao_vender_mensagem(self):
        caixa_de_aviso = QMessageBox()
        caixa_de_aviso.setWindowTitle('Vender investimento')
        caixa_de_aviso.setWindowIcon(QIcon("imagens/aviso.png"))
        caixa_de_aviso.setText('Você tem certeza que deseja vender esse investimento?')
        caixa_de_aviso.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        mostrar_caixa = caixa_de_aviso.exec()
        if mostrar_caixa == QMessageBox.StandardButton.Ok:
            self.vendendo()
        


    def prevendo(self):
        qual_prever = self.combo_box_prever.currentText()
        tr.cliente.usar_narada(qual_prever)
