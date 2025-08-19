import narada as nrd
import pickle
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Cliente:
    def __init__(self, nome, saldo, tipo):
        self.nome = nome
        self.tipo = tipo
        self.__saldo = float(saldo)
        self.investimentos = {'Meta': [0, None, 'META', 0], 'Google': [0, None, 'GOOG', 0], 'Apple': [0, None, 'AAPL', 0], 'Microsoft': [0, None, 'MSFT', 0],
                              'Tesla': [0, None, 'TSLA', 0], 'Bitcoin': [0, None, 'BTC-USD', 0], 'Ethereum': [0, None, 'ETH-USD', 0],'Solana': [0, None, 'SOL-USD', 0],
                              'Cardano': [0, None, 'ADA-USD', 0], 'Zcash': [0, None, 'ZEC-USD', 0], 'Ouro': [0, None, 'GC=F', 0], 'Petroleo': [0, None, 'CL=F', 0], 
                              'Gas': [0, None, 'NG=F', 0], 'Prata': [0, None, 'SLV', 0], 'Algodao': [0, None, 'CT=F', 0], 'AGG': [0, None, 'AGG', 0],
                              'SHY': [0, None, 'SHY', 0], 'VNQ': [0, None, 'VNQ', 0], 'GOVT': [0, None, 'GOVT', 0], 'BND': [0, None, 'BND', 0]}
        self.dados = {'nome' : None, 'tipo' : None, 'saldo' : None, 'investimentos' : None}
        
    @property
    def saldo (self):
        return self.__saldo
    
    @saldo.setter
    def saldo (self, novo_valor):
        try:
            novo_valor = float(novo_valor)
            self.__saldo = novo_valor
        except:
            return('Saldo deve ser um número')
    
    def mudar_dados (self, novo_nome, novo_saldo, novo_tipo):
        self.nome = novo_nome
        self.saldo = novo_saldo
        self.tipo = novo_tipo

    def investir (self, investimento, valor):
        try:
            valor = float(valor)
            valor = round(valor, 2)
            if valor <= 0:
                raise ValueError('Não é possível investir um valor menor ou igual a zero')
            if valor > self.saldo:
                raise ValueError('O saldo não pode ser negativado')
            for element in self.investimentos.keys():
                if element.lower() == investimento.lower():
                    self.saldo -= valor
                    self.investimentos[element][0] += valor
                    self.investimentos[element][1] = dt.datetime.now().date()
                    return f'Você investiu ${valor} em {self.investimentos[element]}\nSeu novo saldo é: {self.saldo}'
        except:
             return 'O valor de entrada deve ser um número maior que zero'
    
    def vender (self, investimento, valor):
        try:
            valor = float(valor)
            valor = round(valor, 2)
            if valor <= 0:
                raise ValueError ('Não é possível vender um valor menor ou igual a zero')
            for element in self.investimentos.keys():
                if element.lower() == investimento.lower():
                    if (self.investimentos[element][0] - valor) < 0:
                         return 'Não é possível ficar com um investimento negativo'
                    self.saldo += valor
                    self.investimentos[element][0] -= valor
                    self.investimentos[element][1] = dt.datetime.now().date()
                    return f'Você vendeu ${valor} em {self.investimentos[element]}\nSeu novo saldo é: {self.saldo}'
        except:
             return 'O valor de entrada deve ser um número maior que zero'
        
    def ver_grafico_real (self, investimento):
        for element in self.investimentos.keys():
                if element.lower() == investimento.lower():
                            inicio = dt.datetime(2024,7,1)
                            fim = dt.datetime.now()
                            dado_preços = nrd.coletar_dados_api(self.investimentos[element][2], inicio, fim)
                            preços_reais = dado_preços['Close'].values
                            datas = dado_preços.index
                            plt.plot(datas, preços_reais, color = 'black', label = f'Preço de {investimento}')
                            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
                            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
                            plt.xticks(rotation=45)
                            plt.title(f'Preço de {element}')
                            plt.xlabel('Dias')
                            plt.ylabel(f'Preço, em dólares, do investimento em {element}')
                            plt.legend()
                            ultimo_preco = preços_reais[-1].item()
                            plt.text(0.99, 0.99, f'Último preço: ${ultimo_preco:.2f}', ha='right', va='top', transform=plt.gca().transAxes)
                            plt.text(0.99, 0.05, f'Meu investimento: ${self.investimentos[element][0]:.2f}', ha='right', va='top', transform=plt.gca().transAxes)
                            plt.show()
                            break
    
    def calcular_lucro_prejuizo (self):#rode toda vez ao abrir/fechar o programa
        for element in self.investimentos.keys():
            if self.investimentos[element][1] != dt.datetime.now().date() and self.investimentos[element][1]:
                inicio = self.investimentos[element][1]
                fim = dt.datetime.now().date()
                dado_preços = nrd.coletar_dados_api(self.investimentos[element][2], inicio, fim)
                preços_reais = dado_preços['Close'].values
                if len(preços_reais) >= 2:
                    preço_inicial = preços_reais[0].item()
                    preço_final = preços_reais[-1].item()
                    variação = ((preço_final - preço_inicial)/preço_inicial) + 1
                    self.investimentos[element][3] = f'{round((variação - 1)*100, 2)}%'
                    self.investimentos[element][0] *= variação
                    self.investimentos[element][0] = round(self.investimentos[element][0], 2)
                    self.investimentos[element][1] = fim

    def usar_narada (self, investimento):
        narada = nrd.criar_instancia(investimento.lower())
        narada.comparar()
    
    def ver_pizza(self):
        labels = ['Saldo']
        valores = [self.saldo]
        dinheiro = self.saldo
        cores_base = ['#FFA500',
                 '#007bff', '#4169E1', '#00008B', '#191970', '#6495ED',
                 '#32CD32', '#228B22', '#008000', '#808000', '#2E8B57',
                 '#FF0000', '#DC143C', '#B22222', '#8B0000', '#FF6347',
                 '#FFFF00', '#FFD700', '#FFFFE0', '#DAA520', '#F0E68C',]
        cores = [cores_base[0]]
        for i, element in enumerate(self.investimentos.keys()):
            if self.investimentos[element][0] != 0:
                labels.append(element)
                valores.append(self.investimentos[element][0])
                cores.append(cores_base[i + 1])
                dinheiro += self.investimentos[element][0]
        plt.figure(figsize=(10, 10))
        plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Distribuição do Dinheiro', y = 1.05)
        plt.axis('equal')
        plt.text(1.1, 1.1, f'Tons de Azul -> Ações', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(1.1, 1.07, f'Tons de Verde -> Criptomoedas', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(1.1, 1.04, f'Tons de Vermelho -> Commodities', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(1.1, 1.01, f'Tons de Amarelo -> Títulos e Fundos', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(0.99, 0.05, f'Dinheiro Total: ${dinheiro:.2f}', ha='right', va='top', transform=plt.gca().transAxes)
        plt.show()
    
    def salvar_dados (self, arquivo):
        self.dados['nome'] = self.nome
        self.dados['tipo'] = self.tipo
        self.dados['saldo'] = self.saldo
        self.dados['investimentos'] = self.investimentos
        with open(f'{arquivo}.pkl', 'wb') as file:
            pickle.dump(self.dados, file)
        print(f'{arquivo} salvo com sucesso')

    def carregar_dados (self, arquivo):
        try:
            with open(f'{arquivo}.pkl', 'rb') as file:
                self.dados = pickle.load(file)
        except Exception as erro:
            print(f'Erro! {erro.__class__}')
            return False
        else:
            self.nome = self.dados['nome']
            self.tipo = self.dados['tipo']
            self.saldo = self.dados['saldo']
            self.investimentos = self.dados['investimentos']
            return True
        
cliente = Cliente('### Default ####', '0', '### Default ####')
