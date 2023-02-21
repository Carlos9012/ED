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


  def altura(self, atual):
    if self is None:
        return 0
    if atual == None or atual.esq == None and atual.dir == None:
        return 1
    else:
        if self.altura(atual.esq) > self.altura(atual.dir):
            return  1 + self.altura(atual.esq) 
        else:
            return  1 + self.altura(atual.dir) 

  

if __name__ == "__main__":
  G = NodoArvore('G', None, None)
  F = NodoArvore('F', None, None)
  E = NodoArvore('E', None, None)
  D = NodoArvore('D', None, None)
  
  C = NodoArvore('C', F, G)
  B = NodoArvore('B', D, E)

  A = NodoArvore('A', C, B)
  
  A.printTree()
  print('Altura: ',A.altura(A))