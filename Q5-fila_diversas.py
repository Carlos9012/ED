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

  def isEmpyt(self):
    if self.next is None:
      print("fila vazia")
  

if __name__ == "__main__":
  p = Fila()
  p.insert('A')
  p.insert('B')
  p.insert('C')
  p.isEmpyt()
  p.print()
  