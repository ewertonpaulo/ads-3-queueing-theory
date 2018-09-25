# TxDeChegMed TempDeServMed NumServi RequiSubme RequiConcl TempMDeResp TamMDaFila
class queueing:
    def __init__(self, dados, list_x, list_y, data):
        self.dados = dados
        self.list_x = list_x
        self.list_y = list_y

    def tempo_medio(self):
        for dado in self.dados:
            tx_chegada = dado[0]/dado[1]
            tx_demanda = dado[0]/dado[5]
            p = tx_chegada/tx_demanda

            E = (1/tx_demanda)/(1 - p)
        
            self.list_x.append(tx_chegada)
            self.list_y.append(E)
        data = [self.list_x, self.list_y]

        return data
