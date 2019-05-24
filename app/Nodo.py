class Nodo:

  def __init__(self, nombre, valor, linea, columna,  index):
    self.nombre=nombre
    self.valor=valor
    self.linea=linea
    self.columna=columna
    self.index=index
    self.hijos = []

  def append(self, nombre, valor, linea, columna,  index):
        item = Nodo(nombre, valor, linea, columna,  index)
        self.hijos.append(item)

  def append(self, hijo):
        self.hijos.append(hijo)


  def imprimir(self):
    for item in self.hijos:
        print self.getNombre() +":" + self.getValor() + " ----> " + item.getNombre() +":" + item.getValor()
        item.imprimir()

  def getNombre(self):
       return self.nombre

  def setNombre(self, nombre):
       self.nombre = nombre

  def getValor(self):
      return  self.valor

  def setValor(self, valor):
       self.valor = valor

  def getLinea(self):
       return self.linea

  def setLinea(self, linea):
       self.linea = linea

  def getColumna(self):
      return  self.columna

  def setColumna(self, columna):
       self.columna = columna

  def getIndex(self):
       return self.index

  def setIndex(self, index):
       self.index = index

  def printNodo(self):
       data= "nombre:"+self.getNombre() + "\n"
       data+="valor:"+self.getValor()    + "\n"
       data+="linea:"+str(self.getLinea())  + "\n"
       data+="columna:"+str(self.getColumna())  + "\n"
       data+="index:"+str(self.getIndex()) + "\n"
       print data
