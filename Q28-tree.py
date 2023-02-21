class NodoArvore: 

  
  def __init__(self, key, dir, esq):
    self.item = key
    self.dir = dir
    self.esq = esq
  
  def printTree(self, level=0):
    if self == None:
      return

    if self.dir is not None:
      self.dir.printTree(level + 1)

    print((' ' * 4 * level) + '-> ' + self.item)
    
    if self.esq is not None:
      self.esq.printTree(level + 1)
    return
    
  def inOrder(self, atual):
    if atual != None:
        self.inOrder(atual.esq)
        print(atual.item,end=" ")
        self.inOrder(atual.dir)
    return
  
  def preOrder(self, atual):
    if atual != None:
        print(atual.item,end=" ")
        self.preOrder(atual.esq)
        self.preOrder(atual.dir)
    return
       
  def posOrder(self, atual):
    if atual != None:
        self.posOrder(atual.esq)
        self.posOrder(atual.dir)
        print(atual.item,end=" ")
    return

  def nivel(self, atual):
    if atual != None:
        print(self.item,end=" ")
        self.preOrder(self.esq)
        self.preOrder(self.dir)
    return

  def altura(self, atual):
    if atual == None or atual.esq == None and atual.dir == None:
        return 0
    else:
        if self.altura(atual.esq) > self.altura(atual.dir):
            return  1 + self.altura(atual.esq) 
        else:
            return  1 + self.altura(atual.dir) 


  def contarNos(self, atual):
    if atual == None:
        return 0
    else:
        return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

  def folhas(self): 
    box_1 = []
    box_2 = []
    box_1.append(A)
 
    while len(box_1) != 0:
      folha = box_1.pop()
 
      if folha.esq:
        box_1.append(folha.esq)
 
      if folha.dir:
        box_1.append(folha.dir)
 
      elif not folha.esq and not folha.dir:
        box_2.append(folha)
     
    while len(box_2) != 0:
        print(box_2.pop().item, end = " ")
    


  
if __name__ == "__main__":
  
  I = NodoArvore('I', None, None)
  H = NodoArvore('H', None, None)
  G = NodoArvore('G', H, I)
  F = NodoArvore('F', None, I)
  E = NodoArvore('E', None, None)
  D = NodoArvore('D', None, None)
  
  C = NodoArvore('C', F, G)
  B = NodoArvore('B', D, E)

  A = NodoArvore('A', C, B)
  
  A.printTree()
  A.folhas()