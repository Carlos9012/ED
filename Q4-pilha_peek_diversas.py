
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

  def initByArray(self, array=None):
    if array is None or len(array) == 0:
      self.data = None
      self.next = None
    
    else:
      self.data = array[0]
    
      P = Pilha()
      P.initByArray(array[1:])
      if P.data is not None:
        self.next = P

  def toArray(self, array=[]):
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  def insert(self, newData=None, fist=None):
    if self is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1
    p.insert(0,newData)
    print()
  
  def peek(self):
    array = self.data
    print(array)

  
  def print(self):
    array = self.toArray([])
    print(array)


if __name__ == "__main__":
  p = Pilha()
  p.push('A')
  p.push('B')
  p.push('C')
  p.print()
  p.peek()
  p.print()
