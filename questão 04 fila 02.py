import random
import time

class Fila:
  def __init__(self):
    self.elementos = []
    self.nomes = ["cliente 1", "cliente 2", "cliente 3"]
    self.hora = []
    

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
  for i in range(1,4):
      fila.enqueue("cliente %s"%(i))
  print (fila.elementos)
  print()



  soma = 0

  for i in range(3):
      print("Aguarde, o %s está na espera"%(fila.nomes[i]))

      intervalo = random.randint(1,7)

      tempo1 = time.time()
      time.sleep(intervalo)
      fila.dequeue()
      tempo2 = time.time()

      tempo_total = tempo2 - tempo1
      
      
      print("Tempo de espera foi de %d segundos"%(tempo_total))
      print()

      soma = soma+tempo_total


  media = soma/3
  print("A média de tempo de espera dos clientes foi: %d segundos"%(media))
  print(fila.elementos)

if (__name__ == "__main__"):
    main()
