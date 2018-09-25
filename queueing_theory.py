# TxDeChegMed TempDeServMed NumServi RequiSubme RequiConcl TempMDeResp TamMDaFila
import matplotlib.pyplot as plt



class queueing:
    def __init__(self, dados):
        self.dados = dados

    def tempo_medio(self):
        data = [[],[]]
        for dado in self.dados:
            tx_chegada = dado[0]
            tp_medio_resp = dado[5]
            data[1].append(tp_medio_resp)
            data[0].append(tx_chegada)

        grafico.plot(self, data[0], data[1],'tempo médio')

class grafico:
    def plot(self,x,y,title):
        plt.plot(x, y)
        plt.title(title)
        plt.show()

    
