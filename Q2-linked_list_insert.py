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

  def toArray(self, array=[1]):
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
  p = Fila()
  p.print()

  p.insert('A')
  p.insert('B')
  p.insert('C')
  p.print()
  print(p.next.data, p.next.data)
  print(p.next.data, p.next.next.data)
  print(p.next.next.data, p.next.next.next.data)
  print(p.next.next.next.data, p.data)
  
  