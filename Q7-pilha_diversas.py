from hashlib import new


class Pilha:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def push(self, newData):
    if newData is None:
      return
    f = Pilha(newData)

    filaAux = self 
    while filaAux.next is not None:
      filaAux = filaAux.next
    
    filaAux.next = f

  def pop(self):
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

  
  def toArray(self, array):
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  
  def print(self):
    if pf.data is None:
        pf.pop()
    array = self.toArray([])
    print(array)

  def last(self):
    if pf.next is None:
        pf.pop()
    pf.print()
    print(pf.data)
    
if __name__ == "__main__":
  pf = Pilha()
  pf.push('A')
  pf.push('B')
  pf.push('C')
  pf.print()
  pf.last()
