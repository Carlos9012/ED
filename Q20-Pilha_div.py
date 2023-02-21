

class Queue:

  def __init__(self, data=None, next=None, cont=0, index=0, box=None, af =None):
    val = []
    self.data = data
    self.next = next
    self.cont = cont
    self.index = index
    self.box = box
    self.val = val
    self.af = af


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

  def valid(self, x = 0, y = 0, val = None):
    for i in a:
        x+=1
    for j in c:
        y+=1
    if x != y:
        print('listas invalidas')
        val = False
        return val
    return val 

  def len(self, cont =0):
    for i in c:
        cont+=1
    return cont

  def _20_b(self,v1=None, v2=None, cont=0, num=0):
    #verificação de indices, valores e nuancias menores
    pf.len()
    if self.af == False or pf.valid() == False:
      return print('Valores invalidos, insira-os em ordem crescente')

    b.reverse()
    for i in b:
      print(cont, i)
      cont+=1
    cont = 0

    for i in a:
      b.pop(i)
      b.insert(i,c[cont])
      cont+=1
    print(b)
    return
  

if __name__ == "__main__":
  pf = Queue()

  b = ['A', 'B', 'B', 'C', 'D', 'C', 'E', 'F']
  a = [0, 4, 7]
  c = ['u', 'n', 'o']
  pf._20_b(a,c)