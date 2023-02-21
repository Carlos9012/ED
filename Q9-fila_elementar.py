from operator import index
import re


class Pilha:

  def __init__(self, data=None, next=None, cont=0, index=0):
    self.data = data
    self.next = next
    self.cont = cont
    self.index = index

  def insert(self, newData=None):
    if newData is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1


  def remove(self):
    if not self:
      return None
    
    poped = self.data
    if self.next is None:
      self.data = None
      self.next = None
    else:
      self.data = self.next.data
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


  def _index(self, index = None, cont=1):
    p1 = Pilha(self.data, self.next)
    #self.index = index
    filaAux = Pilha()
    filaAux.insert(self)

    while True:
      f = self.remove()
      print(cont,f)
      if index == cont:
        print("index *:", index, f)
      if f is None:
        break
      cont+=1
      
    while True:
      f = filaAux.remove()
      p1.insert(filaAux.data)
      p1.print()
      if f is None:
        p1.remove()
      break
    return f
   

  
if __name__ == "__main__":
  pf = Pilha()
  pf.insert('A')
  pf.insert('B')
  pf.insert('C')
  pf.insert('D')
  pf.insert('E')
  pf._index(4)
  
