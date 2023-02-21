

class Queue:

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

    p1 = Queue(self.data, self.next)

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

  def len(self, cont=1, f=None):
    pf = Queue(self.data, self.next)
    filaAux = Queue()
    filaAux.insert(self.next)
    
    while True:
      f = self.remove()
      self.cont+=1
      if f is None:
        break

    while True:
      f = filaAux.remove()
      self.val.append(f)
      pf.insert(f)
      if f is None:
        break
    print(self.val)
    self.cont-=1
    print(self.cont)
    return 

  def _index(self, index = None, cont=1):
    p1 = Queue(self.data, self.next)
    filaAux = Queue()
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
    return


   
  def _16_a(self,v1=None, cont=0):
    print(c)
    box = c.copy()
    c.clear()
    for i in box:
      if i != v1:
        c.append(i)
    print(c)
    return

if __name__ == "__main__":
  c = ['A', 'B', 'C', 'C', 'D', 'E', 'E', 'B']
  pf = Queue()
  pf._16_a('E')