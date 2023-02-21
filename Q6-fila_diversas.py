import re


class Fila:

  def __init__(self, data=None, next=None, cont=0):
    self.data = data
    self.next = next
    self.cont = cont

  def insert(self, newData=None):
    if newData is None:
      return

    p1 = Fila(self.data, self.next)

    self.data = newData
    self.next = p1

  def remove(self):
    if not self:
      return None
    
    poped = self.data
    
    #if not self.next:
    if self.next is None:
      self.data = None
      self.next = None
    else:
      self.data = self.next.data
      #self.next = None
      self.next = self.next.next
    return poped

  def toArray(self, array=[]):
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  
  def print(self):
    array = self.toArray([])
    print(array)

  def fist(self, pfist=None):
    pfist = pf.remove()
    pf.insert(pfist)
    print(pfist)


  def isEmpyt(self):
    p1 = Fila(self.data, self.next)

    filaAux = Fila()
    filaAux.insert(self)

    while self.data is not None:
      self.remove()
      
    while filaAux.data is not None:
      f = filaAux.remove()
      p1.insert(filaAux.data)
      p1.print()
    print(None)
    return

  def len(self, cont=0):
    p1 = Fila(self.data, self.next)

    filaAux = Fila()
    filaAux.insert(self)

    while True:
      f=p1.remove()
      self.cont +=1
      if f is None:
        break

    print(self.cont-1)
    return



    
if __name__ == "__main__":
  
  pf = Fila()
  pf.insert('A')
  pf.insert('B')
  pf.insert('C')
  pf.print()
  pf.len()
  pf.print()

