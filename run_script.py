import os
from shell.script_shell import script

count = 10
start = 1000


def recursive_question2(count):
    while count < start:
        scr = script(start, count)
        scr.chegada()
        count = count + 20
        return recursive_question2(count)

def recursive_question3(count):
    while count < start:
        scr = script(start, count)
        scr.n_serv()
        count = count + 20
        return recursive_question3(count)

print('coletando dados com numero de servidores variando')
recursive_question2(count)
print('coletando dados com taxa de chegada variando')
recursive_question3(count)