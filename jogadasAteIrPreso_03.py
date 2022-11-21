from posicoesJogador_02 import *
def jogadasAtePrisao(estados):

    preso = False
    contador = 0

    for j in estados:
      if (j.turnosCadeia != 0 ):
          preso = True
          break
      elif (j.duplas == 0):
        contador +=1
      else:
        pass

    return contador if preso == True else 0


#supondo 1000 simulações de 10000 jogadas e seja Y a variável aleatória que representa o No de passos até a primeira prisão:
#foram feitas poucas simulações pela demora de execução do código
y = []
for i in range(0,1000):
    s = simulacao(10000)
    c = jogadasAtePrisao(s[0])
    y.append(c)


# output: valores para os quais y assume (demora aprox 1 min e 50s):
y.sort()
print("(Y = y): "+ str(y))