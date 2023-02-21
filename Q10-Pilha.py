

class Pilha:

  def __init__(self, data=None, next=None, cont=0, index=0, box=None):
    val = []
    self.data = data
    self.next = next
    self.cont = cont
    self.index = index
    self.box = box
    self.val = val

  def insert(self, newData=None):
    if newData is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1
    self.val.append(self.data)

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


  def _10_a(self, box=None, cont=1):
    caixa = Pilha()
    filaAux = Pilha()
    print(box)
    while True:
      f = self.remove()
      filaAux.insert(f)
      print(cont,f)
      if box == f:
        caixa.insert(cont)
      if f is None:
        break
      cont+=1
    
    for i in self.val:
      f = filaAux.remove()
      pf.insert(f)

    caixa.print()
    return
   
  def _10_b(self, box=None, cont=1):
    self.val.reverse()
    caixa =[]
    for i in self.val:
      if i == box: 
        caixa.append(cont)
      cont+=1
    print(caixa)
    return

if __name__ == "__main__":

  pf = Pilha()
  pf.insert('A')
  pf.insert('B')
  pf.insert('C')
  pf.insert('C')
  pf.insert('D')
  pf.insert('E')
  pf.insert('E')
  pf.insert('B')
  pf._10_a('E')
  pf.print()
