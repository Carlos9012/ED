class Pilha:

  def __init__(self, data=None, next=None, cont=1):
    self.data = data
    self.next = next
    self.cont = cont

  def push(self, newData=None, ):
    if newData is None:
      return

    f = Pilha(newData, None)

    filaAux = self #copia
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
      self.cont += 1

    return poped

  
  def toArray(self, array):
    
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  def isEmpyt(self):
    p1 = Pilha(self.data, self.next)

    filaAux = Pilha()
    filaAux.push(self.next)

    while self.next is not None:
      self.pop()

    while filaAux.data is not None:
      f = filaAux.pop()
      p1.push(filaAux.next)
    
    if pf.data is None:
      print("é vazio")

    return

  
  def print(self):
    if pf.data is None:
        pf.pop()
    array = self.toArray([])
    print(array)

  def index(self, cont=0):
    self.pop()
    pf = Pilha(self.data, self.next)
    self.cont-=1

    while self.cont >= cont+1:
      print(self.cont , self.data)
      self.pop()
      cont += 1

    pf.print()

    return 
    
if __name__ == "__main__":
  
  pf = Pilha()
  pf.push('A')
  pf.push('B')
  pf.push('C')
  pf.index()
