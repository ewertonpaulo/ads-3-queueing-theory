import os

class handler:
    def __init__(self, dados, dir_):
        self.dados = dados
        self.dir_ = dir_

    def dados_arquivos(self):
        arquivos = os.listdir(self.dir_)
        print('reading the data')
        for i in range(len(arquivos)):
            nome = self.dir_+"/"+arquivos[i]
            txt = open(nome,'r')
            linha = txt.readlines()
            linha[1] = linha[1].replace("\n,","")
            lista_linhas = linha[1].split()

            for h in range(len(lista_linhas)):
                lista_linhas[h] = float(lista_linhas[h].replace(",","."))
                self.dados.append(lista_linhas)

        txt.close()
        return self.dados.sort()