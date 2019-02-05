class Fila:
   def __init__(self):
       self._itens = list()

   def isVazio(self):
       return len(self._itens)==0

   # Referente ao peek. Não remove o útltimo item.
   def peek(self):
       tamanho = len(self._itens)
       return self._itens[0]

   def enqueue(self, item):
       self._itens.append(item)

   def dequeue(self):
       if self.isVazio():
           return False
       return self._itens.pop(0)

   def length(self):
       return len(self._itens)



class Pilha:
     def __init__(self):
           self.lista = []

     def push(self, valor):
           self.lista.append(valor)

     def pop(self):
           if(not(self.isEmpty ())):
                 return self.lista.pop()

     def isEmpty(self):
           return len(self.lista)==0

     def length(self):
           return len(self.lista)

     def peek(self):
           if(not(self.isEmpty())):
                 return self.lista[-1]



def main():

   p = Pilha()
   f = Fila()


   lista=[15,30,1,8]
   print("-- lista na ordem normal --")
   print()
   print(lista)
   for item in lista:
    p.push(item)
   for i in range (p.length()):
    valor=p.pop()
    f.enqueue(valor)

   lista_invertida=[]
   for i in range(f.length()):
    valor=f.dequeue()
    lista_invertida.append(valor)
   print()
   print()
   print("-- lista na ordem invertida --")
   print()
   print(lista_invertida)

if (__name__=="__main__"):
   main()
