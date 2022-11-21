from matrizTransicao_01 import *

# -------------------------------------------------------------------------------
from random import randint

duplas = [2, 4, 6, 8, 10, 12]

class Estado:
    def __init__(self, duplas, posicao, turnosCadeia, dados):
        self.duplas = duplas
        self.posicao = posicao
        self.turnosCadeia = turnosCadeia
        self.dados = dados
        self.status = ''
        self.exibicao =  str(posicao) + self.status

        if (duplas > 0):
            self.status = ''

        if (turnosCadeia > 0):
            self.status = ' Preso'

    def update(self):
        if (self.duplas > 0):
            self.status = ''
        elif (self.turnosCadeia > 0):
            self.status = ' Preso'
        else:
            self.status = ''

        if (self.posicao > 119):
            self.exibicao = "20" + ((self.turnosCadeia % 40) * "'" + self.status) 
        else:
            self.exibicao = str(self.posicao) + ((self.duplas) * "'") + self.status
        

def jogarDados():
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    return (d1, d2)

def proximoEstado(estadoAtual:Estado, jogada:tuple):
    novoEstado = Estado(estadoAtual.duplas, estadoAtual.posicao, estadoAtual.turnosCadeia, jogada)

    if (estadoAtual.turnosCadeia == 0):
        if (novoEstado.duplas == 2):
            if (jogada[0] == jogada[1]):
                novoEstado.duplas = 0
                novoEstado.posicao = 20
                novoEstado.turnosCadeia += 1
            else:
                novoEstado.duplas = 0
                novoEstado.posicao += (jogada[0] + jogada[1])
        else:
            if (jogada[0] == jogada[1]):
                novoEstado.duplas += 1
            else:
                novoEstado.duplas = 0
                novoEstado.posicao += (jogada[0] + jogada[1])
    else:
        if (estadoAtual.turnosCadeia == 3):
            novoEstado.duplas = 0
            novoEstado.turnosCadeia = 0
        else:
            if (jogada[0] == jogada[1]):
                novoEstado.duplas = 0
                novoEstado.turnosCadeia = 0
            else:
                novoEstado.turnosCadeia += 1

    novoEstado.posicao %= 40
    novoEstado.update()

    return novoEstado


#método que executa a simulação de t jogadas, partindo do 0.
#ele armazena os estados do jogador ao longo das t jogadas efetuadas
def simulacao(t:int):
    estadoInicial = Estado(0, 0, 0, (0,0))
    estados = [estadoInicial]
    estadosExibicao=[estadoInicial.exibicao]

    contador = 1
    while contador < t:
        dados = jogarDados()
        estado = proximoEstado(estados[contador-1], dados)
        estadosExibicao.append(estado.exibicao)
        estados.append(estado)
        contador += 1

    return [list(map(lambda e: e.posicao, estados)), estadosExibicao]




# solicitação de quantidade de jogadas para análise de posições no tabuleiro ao longo do tempo:
#qtdJogadas = input("Digite a quantidade de jogadas que deseja simular: ")
#simular = simulacao(int(qtdJogadas))

simular = simulacao(10000)
print("Posições no tabuleiro longo do tempo:")
print("(X_t = x_t): "+ str(simular[1]))


  