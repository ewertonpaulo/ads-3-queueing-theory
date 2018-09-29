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
        data = [[],[],[],[],[]]
        for dado in self.dados:
            tx_chegada = dado[0]
            tp_medio_resp = dado[5]
            tp_med_fila = dado[6]
            rq_submet = dado[3]
            rq_concl = dado[4]

            data[0].append(tx_chegada)
            data[1].append(tp_medio_resp)
            data[2].append(tp_med_fila)
            data[3].append(rq_submet)
            data[4].append(rq_concl)

        grafico.plot(self, data[0], data[1],'taxa de chegada x por tempo médio resposta y')
        grafico.plot(self, data[0], data[2],'taxa de chegada x por tempo médio fila y ')
        grafico.plot(self, data[0], data[3],'taxa de chegada x por req. submetidas y ')
        grafico.plot(self, data[0], data[4],'taxa de chegada x por req. concluidas y ')

    def tmp_md_resp(self):
        data = [[],[]]
        for dado in self.dados:
            num_serv = dado[2]
            tp_medio_resp = dado[5]

            data[0].append(num_serv)
            data[1].append(tp_medio_resp)

        grafico.plot(self, data[0], data[1],'numero de servidores x por tempo médio resposta y')
