from txt_handler import handler
from queueing_theory import queueing

def questao2():
    dados = []
    dir_ = 'saida_chegada'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    theory.tempo_medio()

def questao3():
    dados = []
    dir_ = 'n_servidor'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    theory.tmp_md_resp()

def questao4a():
    dados = []
    dir_ = 'saida_chegada_serv'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    theory.tmp_md_resp_percent()

def questao4b():
    dados = []
    dir_ = 'n_servidor'
    hand = handler(dados, dir_)
    hand.dados_arquivos()

    theory = queueing(dados)
    print("A porcentagem do servidor ficou em %.2f percent no cenário da questão 3 com 12 requisições fixas e um nímero de servidores variavél." %theory.percent())

questao2()
questao3()
questao4a()
questao4b()
