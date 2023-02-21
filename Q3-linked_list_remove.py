class Fila:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def insert(self, newData=None, ):
    if newData is None:
      return

    f = Fila(newData, None)

    filaAux = self #copia
    while filaAux.next is not None:
      filaAux = filaAux.next

    filaAux.next = f

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
  

    
if __name__ == "__main__":
  
  pf = Fila()
  pf.insert('A')
  pf.insert('B')
  pf.insert('C')
  pf.print()
  print("____")
  print(pf.data, pf.next.data)
  pf.remove()
  print(pf.data, pf.next.data)
  pf.remove()
  print(pf.data , pf.data)
  pf.remove()
  print(pf.data)

  