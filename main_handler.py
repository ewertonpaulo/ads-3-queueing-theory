from txt_handler import handler
import matplotlib.pyplot as plt
from queueing_theory import queueing

dir_ = 'saida_chegada'
dados = []

hand = handler(dados, dir_)
hand.dados_arquivos()

def questao2(dados):
    theory = queueing(dados)
    theory.tempo_medio()

questao2(dados, list_x, list_y)
