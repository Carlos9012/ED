import re


class Fila:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

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
    if pf.next is None:
        pf.remove()
    array = self.toArray([])
    print(array)

  def fist(self, pfist=None):
    pfist = pf.remove()
    pf.insert(pfist)
    print(pfist)


  def isEmpyt(self):
    p1 = Fila(self.data, self.next)
    filaAux = Fila()
    filaAux.insert(self.next)
    fila = filaAux.data

    while True:
      f = self.remove()
      if f is None:
        break
      
    while True:
      f = filaAux.remove()
      p1.insert(f)
      if f is None:
        break
    p1.remove()
    p1.print()
    
    return
    
if __name__ == "__main__":
  
  pf = Fila()
  '''pf.insert('A')
  pf.insert('B')
  pf.insert('C')'''
  pf.print()
  pf.isEmpyt()