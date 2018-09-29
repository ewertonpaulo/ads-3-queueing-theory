# ads-3-queueing-theory
In this  laboratory activity is presented the insue of queueing theory, envolving a simulator of a web system.
## Ambiente:
```
$ pip install matplotlib
```
### Scripts de automação dos testes:

Podemos encontrar os scripts na pasta shell no arquivo script_shell.py e sua inicialização recursiva no arquivo run_script.py.
### Questão 1:
O modelo mais adequado para se analisar o desempenho deste sistema foi
o M/M/m. Ele é utilizado para a modelagem de sistemas que apresentam uma
única fila diante de vários servidores idênticos, ou sistemas multiprocessados. Os
parâmetros utilizados para esse modelo são:

• Taxa de chegada de clientes por unidade de tempo λ;
• Taxa de serviço de cada um dos servidores por unidade de tempo
μ;
• Quantidade de servidores m.
O estado é determinado pelo número n de clientes que se encontram na fila
e nos servidores.
### Questão 2:
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao2.1.png)
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao2.2.png)

Como se pode observar, os tempos médios de resposta e principalmente de fila crescem com o aumento da taxa de chegada.
Estes dados deixam claro que o sistema não é escalável, pois com  aumento
da carga, o tempo médio de resposta cresce aumentando a fila.
Podemos observar o numero de requisições concluidas e submetidas em relação a taxa de chegada:

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao2.3.png)
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao2.4.png)

### Questão 3:
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao3.png)

Como observado na imagem, a quantidade minima para se obter um tempo médio de resposta menor menor que 0.5 é com o número de servidores maior que 1. Sendo assim a quantidade minima de servidores é 2.

### Questão 4:
Letra a:

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao4.2.png)

Aqui podemos observar por completo oque foi coletado de testes e o resultado.
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/questao4.1.png)

Como se pode observar apenas nos cados com um número de 1 a 6 requisições que o tempo de resposta fica menor que 0.5.
Letra b:

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-3-queueing-theory/blob/master/graficos/2018-09-29%20(1).png)
Trecho de código para realizar calculo:
```py
def percent(self):
        for dado in self.dados:
            num_serv = dado[2]
            tp_medio_resp = dado[5]

            if tp_medio_resp <= 0.5:
                return num_serv/12*100
```


