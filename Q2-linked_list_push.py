class Pilha:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def push(self, newData=None):
    if newData is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1

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
  
  pf = Pilha()
  pf.push('A')
  print(pf.data, pf.data)
  pf.push('B')
  print(pf.next.data , pf.data)
  pf.push('C')
  print(pf.next.data, pf.data)
  print(pf.data, None)
  pf.print()