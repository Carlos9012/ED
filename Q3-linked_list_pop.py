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

    
if __name__ == "__main__":
  
  pf = Pilha()
  pf.push('A')
  print(pf.data, pf.data)
  pf.push('B')
  print(pf.next.data , pf.data)
  pf.push('C')
  print(pf.next.data, pf.data)
  print(pf.data, None)
  print("____")
  print(pf.data, pf.next.data)
  pf.pop()
  print(pf.data, pf.next.data)
  pf.pop()
  print(pf.data , pf.data)
  pf.pop()
  print(pf.data)
  print()

  