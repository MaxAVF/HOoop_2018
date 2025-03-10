import random


class Fila(object):
    """Clase base de fila"""
    def __init__(self):
       """constructor de la clase Fila """
       self.enfila=0
       self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.fila.append(cliente)
        self.enfila+=1
        
    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if maxenfila < self.enfila:
            for i in range(self.enfila//2):
                filanueva.insertar(self.fila[0])
                self.enfila-=1
                self.fila.pop(0)

         
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.fila.append(cliente)
        self.enfila+=1

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)     

    

class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    clientes=[]
    categorias = ['general','preferencial']

#     for count in range(100):
#        cliente_nuevo=cliente()
#        cliente_nuevo.modificarcategoria(random.choice(categorias))
#        clientes.append(cliente_nuevo)
        
#     filapreferencial=FilaPreferencial()
#     filageneral=FilaGeneral()
    
#     for elem in clientes:
#         if elem.categoria='preferencial':
#             filapreferencial.insertar(elem)
            
#         if elem.categoria='general':
#             filageneral.insertar(elem)
            
    
            
            
    
        