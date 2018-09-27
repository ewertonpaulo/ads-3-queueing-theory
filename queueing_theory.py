# TxDeChegMed TempDeServMed NumServi RequiSubme RequiConcl TempMDeResp TamMDaFila
import matplotlib.pyplot as plt

class grafico:
    def plot(self,x,y,title):
        plt.plot(x, y)
        plt.title(title)
        plt.show()

class queueing:
    def __init__(self, dados):
        self.dados = dados

    def tempo_medio(self):
        data = [[],[],[]]
        for dado in self.dados:
            tx_chegada = dado[0]
            tp_medio_resp = dado[5]
            tp_med_fila = dado[6]
            data[2].append(tp_med_fila)
            data[1].append(tp_medio_resp)
            data[0].append(tx_chegada)

        grafico.plot(self, data[0], data[1],'taxa de chegada x por tempo médio resposta y')
        grafico.plot(self, data[0], data[2],'taxa de chegada x por tempo médio fila y ')
