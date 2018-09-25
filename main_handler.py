from txt_handler import handler
import matplotlib.pyplot as plt
from queueing_theory import queueing

dir_ = 'saida_chegada/'
dados = []
list_x = []
list_y = []


hand = handler(dados, dir_)
hand.dados_arquivos()
def grafico(title, list_x, list_y):
    plt.plot(list_x,list_y)
    plt.title(title)
    plt.show()

def questao2(dados, list_x, list_y):
    data = []
    title = 'tempo médio'
    theory = queueing(dados, list_x, list_y, data)
    data = theory.tempo_medio()
    print(data)
    grafico(title, data[0], data[1])

questao2(dados, list_x, list_y)


