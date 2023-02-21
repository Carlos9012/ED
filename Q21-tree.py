class NodoArvore: 

  
  def __init__(self, key=None, esq=None, dir=None):
        self.key = key
        self.esq = esq
        self.dir = dir
  
  def printTree(self, level=0):
    if self == None:
      return

    if self.dir is not None:
      self.dir.printTree(level + 1)

    print((' ' * 4 * level) + '-> ' + self.item)
    
    if self.esq is not None:
      self.esq.printTree(level + 1)
  def __repr__(self):
        return '%s <- %s -> %s' % (self.esq and self.esq.key, self.key, self.dir and self.dir.key)
if __name__ == "__main__":
  
  raiz = NodoArvore(40)

  raiz.esq = NodoArvore(20)
  raiz.dir  = NodoArvore(60)

  raiz.dir.esq  = NodoArvore(50)
  raiz.dir.dir   = NodoArvore(70)
  raiz.esq.esq = NodoArvore(10)
  raiz.esq.dir  = NodoArvore(30)
  print(raiz)
  print(raiz.esq)
  print(raiz.dir)