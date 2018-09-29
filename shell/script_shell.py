import os
from time import sleep

class script:
    def __init__(self, start, count):
        self.start = start
        self.count = count

    def chegada(self):
        print("analysing with "+ str(self.count) +" arrivals")
        os.system("java -cp bin;lib\* ServidorWeb "+str(self.count)+" 0.4 1 20 -t >saida_chegada/arquivo-"+str(self.count)+".txt")

    def n_serv(self):
        print("analysing with "+ str(self.count) +" servers")
        os.system("java -cp bin;lib\* ServidorWeb 12 0.4 "+str(self.count)+" 20 -t >n_servidor/arquivo-"+str(self.count)+".txt")
        
    def chegada_serv_3(self):
        print("analysing with "+ str(self.count) +" arrivals")
        os.system("java -cp bin;lib\* ServidorWeb "+str(self.count)+" 0.4 3 20 -t >saida_chegada_serv/arquivo-"+str(self.count)+".txt")
