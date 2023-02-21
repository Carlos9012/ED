from array import array
from importlib.util import set_loader
from re import I
from select import select
from xml.sax.handler import feature_namespace_prefixes


class Fila:

  def __init__(self, data=None, next=None, cont=1, dado=None, val=None, num=None, af= None):
    num = []
    val =[]
    dado = []
    self.data = data
    self.next = next
    self.cont = cont
    self.dado = dado
    self.num = num
    self.val = val
    self.af = af

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

  def _18_a(self, v1=0 , v2 =0, cont=0):
    caixa = Fila()
    box = Fila()
    while True:
      f = self.pop()
      print(cont+1,f)
      if v1 <= cont+1 and v2 > cont:
        caixa.push(f)
      else:
        box.push(f)
      if f is None:
        break
      cont+=1

    box.pop()

    while True:
        f =box.pop()
        pf.push(f)
        if f is None:
            break
    return
   
  def _18_b(self, v1=0 , v2 =0, cont=0):
    box = self.val.copy()
    self.val.clear()
    for i in box:
        print(cont, i)
        if v1 <= cont and v2 >= cont:
            cont
        else:
            self.val.append(i)
        cont+=1
    print(self.val)
    return

  def len(self, vil=None):
    a.reverse()
    a.append(0)
    x=0
    for i in a:
      if a.__len__() > x+2:
        if i <= a[x+1]:
          self.af = False
        x+=1
    a.pop()
    return print('______')
  

if __name__ == "__main__":
  a = [1,5,2,7]
  b = ['A', 'B', 'B', 'C', 'D', 'C', 'E', 'F']
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
  pf.len(a)
  '''pf._18_a(1,4)'''
  pf.print()
  pf._18_b(2,5)

