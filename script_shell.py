import os
from time import sleep


class script:
    def __init__(self, n_range):
        self.n_range = n_range

    def chegada(self):
        for i in range(10, self.n_range):
            os.system("java -cp bin;lib\* ServidorWeb "+str(i)+" 0.4 1 20 -t >saida_chegada/arquivo-"+str(i)+".csv")

    def n_serv(self):
        for i in range(self.n_range):
            os.system("java -cp bin;lib\* ServidorWeb 12 0.4 "+str(i)+" 20")
