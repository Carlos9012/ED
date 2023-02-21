from array import array
from importlib.util import set_loader
from re import I
from select import select
from xml.sax.handler import feature_namespace_prefixes


class Fila:

  def __init__(self, data=None, next=None, cont=1, dado=None, val=None, num=None):
    num = []
    val =[]
    dado = []
    self.data = data
    self.next = next
    self.cont = cont
    self.dado = dado
    self.num = num
    self.val = val

  def push(self, newData=None, ):
    if newData is None:
      return

    f = Fila(newData, None)

    filaAux = self #copia
    while filaAux.next is not None:
      filaAux = filaAux.next

    filaAux.next = f
    self.val.append(f.data)

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
    p1 = Fila(self.data, self.next)

    filaAux = Fila()
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

  def _print(self):
    array = self.toArray([])
    print(array)

  def index(self, cont=1):
    p1 = Fila(self.data, self.next)
    filaAux = Fila()
    filaAux.push(self)

    while True:
      f = self.pop()
      print(cont,f)
      cont+=1
      if f is None:
        pf.pop()
        break
      
    while True:
      f = filaAux.pop()
      p1.push(f)
      if f is None:
        break
    
    return

  def _array(self, cont=0):
    p1 = Fila(self.data, self.next)
    while True:
      f=p1.pop()
      cont +=1
      self.dado.append(f)
      if f is None:
        break
    self.dado.pop()
    return

  def len(self, cont=0):
    p1 = Fila(self.data, self.next)
    filaAux = Fila()
    filaAux.push(self)

    while True:
      f=p1.pop()
      self.cont +=1
      if f is None:
        break
    self.cont-=3
    print(self.cont)
    return 


  def _20_a(self,v1=None, v2=None, cont=0):
    index_num = Fila()
    index_val = Fila()
    caixa = Fila()
    box = Fila()
    print('valor :',v1)
    x = 0
    y = 0
    num=0
    
    for i in v1:
      y+=1
    for i in v2:
      box.push(i)
    box.pop()

    while True:
      f = self.pop()
      index_num.push(cont)
      index_val.push(f)
      print(cont+1,f)
      if f is None:
        break
      cont+=1
    index_num.pop()
    
    while True:
      f = index_val.pop()
      x = index_num.pop()
      num=0
      for i in v1:
        if x is i:
          j = box.pop()
          caixa.push(j)
        else:
          num+=1
          if num == y:
            caixa.push(f)
      if x is None:
        break
    caixa.pop()

    while True:
        f = caixa.pop()
        pf.push(f)
        if f is None:
            break

    return



if __name__ == "__main__":
  
  pf = Fila()
  pf.push('A')
  pf.push('B')
  pf.push('B')
  pf.push('C')
  pf.push('D')
  pf.push('C')
  pf.push('E')
  pf.push('F')
  pf.print()
  a = [1,8]
  b = ['u', 'n', 'o']
  ##pf._10_b(b, 'B')
  pf._20_a(a, b)
  pf.print()

