import numpy as np
from fractions import Fraction

#definindo estados da matriz de transição:
def estadoTransicao(linha):

    estado = np.zeros([123])

    #foram removidas as probabilidades de sequências iguais, pois elas não permitem percorrer a casa (apenas os estados auxiliares)
    probsCasas = [0, 0, 1/18, 1/18, 1/9, 1/9, 1/6, 1/9, 1/9, 1/18, 1/18, 0]

    #definindo probabilidades de partir do estado i, para o estado j:
    if (linha <= 119):
        linhaAux = linha % 40
        inicio = (linhaAux * 1)
        limiteTabuleiro = (12 + inicio) - 40
        for i in range(40):
            if (i > inicio) and (i <= (inicio + 12)):
                estado[i] = probsCasas[i-linhaAux-1]
            if (limiteTabuleiro >= 0) and (i <= limiteTabuleiro):
                estado[i] = probsCasas[len(probsCasas) - 1 - limiteTabuleiro + i]

        inicio = 40
        fim = 80
        if (linha >= 0 and linha <= 79):
            if (linha >= 40 and linha <= 79):
                inicio = 80
                fim = 120

            for j in range(inicio, fim):
                if (linha%40 == j%40):
                    estado[j] = 1/6
                else:
                    estado[j] = 0

        if (linha >= 80 and linha <= 119):
            estado[120] = 1/6

    else:
        if (linha == 120):
            estado[20] = 1/6
            estado[121] = 5/6

        if (linha == 121):
            estado[20] = 1/6
            estado[122] = 5/6

        if (linha == 122):
            estado[20] = 1
        
    return estado

  
#método para imprimir um determinado estado da matriz de transição:
def imprimeEstado(estado):
    linha = estadoTransicao(estado)

    linhaAux = []
    for j in range(len(linha)):
        linhaAux.append(str(Fraction(linha[j]).limit_denominator()))
    for i in range(5):
        print(''.join(['{:5}'.format(item) for item in linhaAux[i*40:(i+1)*40]]))


def imprimeMatrizTransicao(matriz):
  matrizAux = []
  for i in range(len(matriz)):
    estadoAux = []
    for j in range(len(matriz[i])):
      prob = str(Fraction(matriz[i][j]).limit_denominator())
      estadoAux.append(prob)
    matrizAux.append(estadoAux)
  
  print(('\n\n').join([''.join(['{:5}'.format(item) for item in row]) for row in matrizAux]))



matrizTransicao = np.zeros([123, 123])

#esse método valida a matriz de transição montada, caso um estado possua
#algum erro e ele printa o estado e a probabilidade somada.
def validaMatrizTransicao(matriz):
  for i in range(123):
      matrizTransicao[i] = estadoTransicao(i)

  for i in range(123):
      s = np.sum(matrizTransicao[i, :])
      if s != 1 and s < 0.99999:
          print(s)
          print(i)

# caso a função abaixo retorne algo, significa que algum estado não soma 1 no total das probabilidades:
validaMatrizTransicao(matrizTransicao)   

