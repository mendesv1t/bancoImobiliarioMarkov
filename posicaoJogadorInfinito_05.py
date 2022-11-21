from matrizTransicao_01 import *

def geraMatrizTransicao():

    matriz = np.zeros([123, 123])
    for i in range(0, 123):
        linha = estadoTransicao(i)
        matriz[i] = linha

    return matriz

def probablidadesZ(t:int):
    m = geraMatrizTransicao()

    vetorInicial = np.zeros([123])
    vetorInicial[0] = 1

    for i in range(t):
        vetorInicial = vetorInicial.dot(m)

    probs_z = []
    for i in range(0, 40):
        z_0 = vetorInicial[i]
        z_1 = vetorInicial[i+40]
        z_2 = vetorInicial[i+80]

        z = z_0 + z_1 + z_2

        if (i == 20):
            z += vetorInicial[120]
            z += vetorInicial[121]
            z += vetorInicial[122]

        probs_z.append(z)

    return probs_z


def posicaoZ(z, n=1000000):
    probs = probablidadesZ(n)

    p = probs[z]

    return p

probabilidades_z = []
for i in range(40):
  p_z = posicaoZ(i)
  probabilidades_z.append(p_z)
  print("P(Z= "+ str(i) + ") = " + str(p_z))

