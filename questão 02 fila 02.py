import random
import time

class Fila:
  def __init__(self):
    self.elementos = []

  def lenght(self):
    return len(self.elementos)

  def isEmpyt(self):
    return len(self.elementos)==0

  def enqueue(self,valor):
    self.elementos.append(valor)

  def dequeue(self):
    if(not(self.isEmpyt())):
      self.elementos.pop(0)

def main():

  fila = Fila()
  #Adicionei os documentos através de um for 
  for i in range(1,6):
    fila.enqueue("documento %s"%(i)) 
  print (fila.elementos)
  print()

  print("Preparando impressão...")
  print()
  print("Aguarde")
  intervalo =  random.randint(1,8)

  tempo1 = time.time()
  time.sleep(intervalo)
  fila.dequeue()
  tempo2 = time.time()
  tempo_total = tempo2-tempo1
  print("Pronto, documento impresso.")
  print("O tempo de impressão foi de: %.f segundos"%(tempo_total))
  print(fila.elementos)
  print()
  print("Pronto para imprimir o próximo documento")

if (__name__ == "__main__"):
    main()


