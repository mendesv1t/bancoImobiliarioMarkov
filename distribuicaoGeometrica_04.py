from jogadasAteIrPreso_03 import *
def esperancaY(y):
  esperanca = 0
  for q in range(len(y)):
    esperanca += y[q]
  return esperanca/len(y)

print("Y=y  = " + str(y))
e = esperancaY(y)
print("Aproximação para E(Y): " + str(round(e,2)))