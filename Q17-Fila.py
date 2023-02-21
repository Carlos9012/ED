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

  def _17_a(self, v1=None, cont=0, num = 0):
    caixa = Fila()
    box = Fila()
    print(v1)
    x=0
    for i in v1:
      x+=1
    while True:
      f = self.pop()
      print(cont, f)
      for i in v1:
        if cont is not i:
          num+=1
          box.push(f)
          if num == x:
            caixa.push(f)
      cont+=1
      num=0
      if f is None:
        break
    
    caixa.pop()
    while True:
        f = caixa.pop()
        pf.push(f)
        if f is None:
            break

    pf.print()
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
  
  def _17_b(self, v1=None,v2=None,cont=0):
    a.reverse()
    print(a)
    pf.len()
    if self.af == False:
      return print('Valores invalidos, insira-os em ordem crescente')
    
    for i in b:
        print(cont, i)
        cont+=1
    for i in a:
        b.pop(i)
    print(b)

    return


if __name__ == "__main__":
  a = [1,5,7]
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
  pf._17_a(a)
  pf._17_b(a,b)

