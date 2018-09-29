from txt_handler import handler
import matplotlib.pyplot as plt
from queueing_theory import queueing

dados = []

def questao2(dados):
    dir_ = 'saida_chegada'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    theory.tempo_medio()

def questao3(dados):
    dir_ = 'n_servidor'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    theory.tmp_md_resp()

questao3(dados)
