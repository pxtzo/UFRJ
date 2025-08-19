'''
Narada, inspirado pelo mensageiro dos deuses da literatura védica,
é um algoritmo que utiliza machine learning para prever o valor de investimentos no próximo dia
para o trabalho final de Computação 2 da UFRJ
Créditos ao canal no YouTube: NeuralNine (Fonte da lógica para treinar as RNNs e previsão de valores)
Versão do Python: 3.11.3
'''
#Importando módulos
import abc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime as dt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, LSTM

# ------ Classe Abstrata Base ---------
class Narada(abc.ABC):
    def __init__(self):
        self.dias_previstos = 60 #quantidade de dias anteriores usada para prever o dia seguinte
        self.inicio = dt.datetime(2002,1,1)
        self.fim = dt.datetime(2024,6,30)
        self.x_treinar = []
        self.y_treinar = []
        self.id, self.companhia, self.dado, self.model = None, None, None, None
    
    @abc.abstractmethod
    def criar_model (self): #Não utilize esse método, ele já é processado automaticamente
        '''Treina uma RNN com LSTM e Dropout -> Fonte: NeuralNine'''
        self.coletar_api()
        try:
            self.carregar_dados()
            print(f'Model de {self.companhia} carregado com sucesso!')
        except:
            self.model = Sequential() #cria um modelo linear que empilha camadas
            self.model.add(LSTM (units = 50, return_sequences = True, input_shape = (self.x_treinar.shape[1], 1)))
            self.model.add(Dropout (0, 2))
            self.model.add(LSTM (units = 50, return_sequences = True))
            self.model.add(Dropout (0, 2))
            self.model.add(LSTM (units = 50))
            self.model.add(Dropout (0, 2))
            self.model.add(Dense( units = 1))
            self.model.compile(optimizer = 'adam', loss = 'mean_squared_error')
            self.model.fit(self.x_treinar, self.y_treinar, epochs = 50, batch_size = 32)
            self.salvar_dados()
            print(f'Model de {self.companhia} treinado e salvo com sucesso!')

    @abc.abstractmethod
    def coletar_api (self): #Não utilize esse método, ele já é processado automaticamente
        '''Coleta dados da API do yfinance e modela os dados para uso futuro. Adaptado: NeuralNine'''
        self.dado = coletar_dados_api(self.id, self.inicio, self.fim) #coleta dados
        dado_normalizado = normalizar.fit_transform(self.dado['Close'].values.reshape(-1, 1))
        for i in range(self.dias_previstos, len(dado_normalizado)):
            self.x_treinar.append(dado_normalizado[i - self.dias_previstos: i, 0]) #entrada de janela de valores consecutivos do passado
            self.y_treinar.append(dado_normalizado[i, 0]) #saída do próximo ponto para cada conjunto de janela de valores
        self.x_treinar, self.y_treinar = np.array(self.x_treinar), np.array(self.y_treinar) #conversão para arrays
        self.x_treinar = np.reshape(self.x_treinar, (self.x_treinar.shape[0], self.x_treinar.shape[1], 1)) #redimensionamento

    @abc.abstractmethod
    def carregar_dados (self): #Não utilize esse método, ele já é processado automaticamente
        pass

    @abc.abstractmethod
    def salvar_dados (self): #Não utilize esse método, ele já é processado automaticamente
        pass

    @abc.abstractmethod
    def prever (self):
        '''Prevê o valor de um investimento no dia de amanhã. Fonte: NeuralNine'''
        inicio_teste = dt.datetime(2024,7,1)
        fim_teste = dt.datetime.now()
        dado_teste = coletar_dados_api(self.id, inicio_teste, fim_teste)
        dadosettar_total = pd.concat((self.dado['Close'], dado_teste['Close']), axis =0)
        model_inputs = dadosettar_total[len(dadosettar_total) - len(dado_teste) - self.dias_previstos:].values
        model_inputs = model_inputs.reshape(-1,1)
        model_inputs = normalizar.transform(model_inputs)
        dado_real = [model_inputs[len(model_inputs) + 1 - self.dias_previstos:len(model_inputs+1), 0]]
        dado_real= np.array(dado_real)
        dado_real = np.reshape(dado_real, (dado_real.shape[0], dado_real.shape[1], 1))
        previsão = self.model.predict(dado_real)
        previsão = normalizar.inverse_transform(previsão)
        return f'{previsão[0][0]:.2f}'

    @abc.abstractmethod
    def comparar (self):
        '''Compara os valores previstos e reais de um investimento. Adaptado: NeuralNine'''
        inicio_teste = dt.datetime(2024,7,1)
        fim_teste = dt.datetime.now()
        dado_teste = coletar_dados_api(self.id, inicio_teste, fim_teste)
        dadosettar_total = pd.concat((self.dado['Close'], dado_teste['Close']), axis = 0)
        model_inputs = dadosettar_total[len(dadosettar_total) - len(dado_teste) - self.dias_previstos:].values
        model_inputs = model_inputs.reshape(-1,1)
        model_inputs = normalizar.transform(model_inputs)
        preços_reais = dado_teste['Close'].values
        x_teste = []
        for x in range(self.dias_previstos, len(model_inputs)):
            x_teste.append(model_inputs[x-self.dias_previstos:x,0])
        x_teste = np.array(x_teste)
        x_teste = np.reshape(x_teste, (x_teste.shape[0], x_teste.shape[1], 1))
        preços_previstos = self.model.predict(x_teste)
        preços_previstos = normalizar.inverse_transform(preços_previstos)
        datas = dado_teste.index
        ultimo_preco = preços_reais[-1].item()
        previsão = float(self.prever())
        variação = ((previsão - ultimo_preco)/ultimo_preco)*100
        cor_variação = 'green' if variação > 0 else 'red'
        plot_variação = f'Variação prevista: +{variação:.2f}%' if variação > 0 else f'Variação prevista: {variação:.2f}%'
        plt.plot(datas, preços_reais, color = 'black', label = f'Preço Real de {self.companhia}')
        plt.plot(datas, preços_previstos, color = '#CD1671', label = f'Preço Previsto de  {self.companhia}')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
        plt.xticks(rotation=45)
        plt.title(f'Preço de {self.companhia}')
        plt.xlabel('Dias')
        plt.ylabel(f'Preço, em dólares, do investimento em {self.companhia}')
        plt.legend()
        plt.text(0.99, 0.99, f'Preço de hoje: ${ultimo_preco:.2f}', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(0.99, 0.1, f'Previsão de preço para amanhã: ${previsão:.2f}', ha='right', va='top', transform=plt.gca().transAxes)
        plt.text(0.99, 0.05, plot_variação, color=cor_variação, ha='right', va='top', transform=plt.gca().transAxes)
        plt.show()

# ------ Companhias ---------
class Meta (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'META'
        self.inicio = dt.datetime(2013,1,1)
        self.companhia = 'Meta'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('meta_model.h5')

    def salvar_dados(self):
        self.model.save('meta_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Alphabet (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'GOOG'
        self.inicio = dt.datetime(2005,1,1)
        self.companhia = 'Alphabet'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('google_model.h5')

    def salvar_dados(self):
        self.model.save('google_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Apple (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'AAPL'
        self.companhia = 'Apple'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('apple_model.h5')

    def salvar_dados(self):
        self.model.save('apple_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Microsoft (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'MSFT'
        self.companhia = 'Microsoft'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('microsoft_model.h5')

    def salvar_dados(self):
        self.model.save('microsoft_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Tesla (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'TSLA'
        self.inicio = dt.datetime(2011,1,1)
        self.companhia = 'Tesla'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('tesla_model.h5')

    def salvar_dados(self):
        self.model.save('tesla_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

# ----- Criptomoedas ----------
class Bitcoin (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'BTC-USD'
        self.inicio = dt.datetime(2015,1,1)
        self.companhia = 'Bitcoin'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('bitcoin_model.h5')

    def salvar_dados(self):
        self.model.save('bitcoin_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Ethereum (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'ETH-USD'
        self.inicio = dt.datetime(2018,1,1)
        self.companhia = 'Ethereum'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('ethereum_model.h5')

    def salvar_dados(self):
        self.model.save('ethereum_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Solana (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'SOL-USD'
        self.inicio = dt.datetime(2021,1,1)
        self.companhia = 'Solana'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('solana_model.h5')

    def salvar_dados(self):
        self.model.save('solana_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Cardano (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'ADA-USD'
        self.inicio = dt.datetime(2018,1,1)
        self.companhia = 'Cardano'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('cardano_model.h5')

    def salvar_dados(self):
        self.model.save('cardano_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Zcash (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'ZEC-USD'
        self.inicio = dt.datetime(2018,1,1)
        self.companhia = 'Zcash'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('zcash_model.h5')

    def salvar_dados(self):
        self.model.save('zcash_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

# --------- Commodities ----------
class Ouro (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'GC=F'
        self.companhia = 'Ouro'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('ouro_model.h5')

    def salvar_dados(self):
        self.model.save('ouro_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Petróleo (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'CL=F'
        self.companhia = 'Petróleo'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('petroleo_model.h5')

    def salvar_dados(self):
        self.model.save('petroleo_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Gás (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'NG=F'
        self.companhia = 'Gás Natural'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('gas_model.h5')

    def salvar_dados(self):
        self.model.save('gas_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Prata (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'SLV'
        self.companhia = 'Prata'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('prata_model.h5')

    def salvar_dados(self):
        self.model.save('prata_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class Algodão (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'CT=F'
        self.companhia = 'Algodão'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('algodão_model.h5')

    def salvar_dados(self):
        self.model.save('algodão_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

# -------- Títulos e Fundos --------
class AGG (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'AGG'
        self.inicio = dt.datetime(2004,1,1)
        self.companhia = 'iShares Core Bond ETF'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('agg_model.h5')

    def salvar_dados(self):
        self.model.save('agg_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class SHY (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'SHY'
        self.companhia = 'iShares Short-Term ETF'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('shy_model.h5')

    def salvar_dados(self):
        self.model.save('shy_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class VNQ (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'VNQ'
        self.inicio = dt.datetime(2005,1,1)
        self.companhia = 'Vanguard Real Estate ETF'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('vnq_model.h5')

    def salvar_dados(self):
        self.model.save('vnq_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class GOVT (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'GOVT'
        self.inicio = dt.datetime(2013,1,1)
        self.companhia = 'iShares U.S. Treasury ETF'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('govt_model.h5')

    def salvar_dados(self):
        self.model.save('govt_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

class BND (Narada):
    def __init__(self):
        super().__init__()
        self.id = 'BND'
        self.inicio = dt.datetime(2008,1,1)
        self.companhia = 'Vanguard Total Bond Market ETF'
        self.criar_model()
    
    def criar_model(self):
        return super().criar_model()
    
    def coletar_api(self):
        return super().coletar_api()
    
    def carregar_dados(self):
        self.model = load_model('bnd_model.h5')

    def salvar_dados(self):
        self.model.save('bnd_model.h5')
    
    def prever(self):
        return super().prever()
    
    def comparar(self):
        return super().comparar()

# ------------ Configurando Instâncias -------------
def criar_instancia(nome_narada):
    if nome_narada == 'meta':
        return Meta()
    elif nome_narada == 'google':
        return Alphabet()
    elif nome_narada == 'apple':
        return Apple()
    elif nome_narada == 'microsoft':
        return Microsoft()
    elif nome_narada == 'tesla':
        return Tesla()
    elif nome_narada == 'bitcoin':
        return Bitcoin()
    elif nome_narada == 'ethereum':
        return Ethereum()
    elif nome_narada == 'solana':
        return Solana()
    elif nome_narada == 'cardano':
        return Cardano()
    elif nome_narada == 'zcash':
        return Zcash()
    elif nome_narada == 'ouro':
        return Ouro()
    elif nome_narada == 'petroleo':
        return Petróleo()
    elif nome_narada == 'gas':
        return Gás()
    elif nome_narada == 'prata':
        return Prata()
    elif nome_narada == 'algodao':
        return Algodão()
    elif nome_narada == 'agg':
        return AGG()
    elif nome_narada == 'shy':
        return SHY()
    elif nome_narada == 'vnq':
        return VNQ()
    elif nome_narada == 'govt':
        return GOVT()
    elif nome_narada == 'bnd':
        return BND()
    else:
        return None

# ----------- Funcionalidades Importantes -------------------
def coletar_dados_api(companhia, inicio, fim):
    '''Função utilizada para coletar dados dos valores de ações de uma companhia utilizando a API do Yahoo'''
    dado = yf.download(companhia, inicio, fim)
    return dado

normalizar = MinMaxScaler(feature_range = (0, 1)) #Normaliza os dados
