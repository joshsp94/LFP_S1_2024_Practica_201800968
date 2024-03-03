class NodoGato:
    def __init__(self, dataGato):
        #atributos que nos van a servir para los nodos
        self.dataGato = dataGato
        self.next = None

class animalList:
    def __init__(self):
        #linked list attributes
        self.inicio = None
        self.final = None
    
    def addAnimal(self, dataGato=[]):
        #sino existe ningun elemento en la lista enlazada hace lo next
        if self.inicio == None:
            aux = NodoGato(dataGato)
            self.inicio = aux
            self.final = aux
        #si la lista NO esta vacia hace lo next
        else:
            aux = NodoGato(dataGato)
            self.final.next=aux
            self.final=aux

     #function to feed a cat
    def feed(self, name, plus):
        actual = self.inicio
        cont = 1
        while actual!=None:
            if(actual.dataGato[1]==name):
                if(float(actual.dataGato[2])>0):
                    actual.dataGato[2] = float(actual.dataGato[2])+plus    
                    return actual.dataGato
            cont = cont + 1
            actual=actual.next
        return actual 
    
    #function to play with a cat
    def play(self, name, plus):
        actual = self.inicio
        cont = 1
        while actual!=None:
            if(actual.dataGato[1]==name):
                if(float(actual.dataGato[2])>0):
                    actual.dataGato[2] = float(actual.dataGato[2])-plus    
                    return actual.dataGato
            cont = cont + 1
            actual=actual.next
        return actual 

    #function to validate cat exist
    def valAnimal(self, name):
        actual = self.inicio
        cont = 1
        while actual!=None:
            if(actual.dataGato[1]==name):
                # print(f"\n**    cliente {actual.dataGato[0]} encontrado.   **")
                return actual.dataGato
            cont = cont + 1
            actual=actual.next
        return actual 

    def printListAnimals(self):
        actual = self.inicio
        cont = 1
        while actual!=None:
            print(f"{cont}) {actual.dataGato}\n")
            # print(actual.next)
            print("__________________________________________\n")
            cont = cont + 1
            actual=actual.next