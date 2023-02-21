class Fila:

  def __init__(self, data=None, next=None, cont=0, index=0):
    val = []
    self.data = data
    self.next = next
    self.cont = cont
    self.index = index
    self.val = val

  def insert(self, newData=None):
    if newData is None:
      return

    p1 = Fila(self.data, self.next)

    self.data = newData
    self.next = p1
    self.val.append(p1.data)
    

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

  def fist(self, pfist=None):
    pfist = pf.remove()
    pf.insert(pfist)
    print(pfist)


  def _index(self,index=None, cont=0, f=None):
    box = []
    self.val.pop(0)
    print(self.val)
    for i in self.val:
      cont+=1
      print(i)
      if cont  == index:
        box.append(i)
      
    print(box)

  
if __name__ == "__main__":
  pf = Fila()
  pf.insert('A')
  pf.insert('B')
  pf.insert('C')
  pf.insert('D')
  pf.insert('E')
  pf._index(3)
