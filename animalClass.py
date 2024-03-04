from os import system
import graphviz;
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


    # def draw(self):
    #     actual = self.inicio
    #     cont=1
    #     dot = 'digraph G {;'
    #     while actual!=None:
    #         dot += f'n{cont} [label="{actual.dataGato[0]}"];'
    #         if (cont != 0):
    #             dot += f'n{cont+1} -> n{cont};'
    #     dot += '}'
    #     f = open('graficaOS.gv', 'w')
    #     f.write(dot)
    #     f.close()
    #     system('dot -Tpdf graficaOS.gv -o graficaOS.pdf')
    #     system('cd ')

    def draw(self):
        file=open('graphviz.dot','w')
        actual = self.inicio
        cont = 1
        # print(f"\n**   Se dibujo el grafico   **")
        file.write('digraph G{')
        # estado=""
        while actual!=None:
            if(actual.dataGato[2]>0):
                estado="vivo"
            else:
                estado="muerto"
            file.write(f'\n{actual.dataGato[1]} -- Energia {actual.dataGato[2]};')
            file.write(f'\n{actual.dataGato[1]} -- Tipo: {actual.dataGato[3]};')
            file.write(f'\n{actual.dataGato[1]} -- Estado: {estado};')
            file.write('\n')
            
            cont = cont + 1
            actual=actual.next
        file.write('}')
        file.close()
        system('dot -tpng graphviz.dot -o imagen.png')
        system('cd ./graphviz.png')
        
    
    def globalList(self):
        lista=[]
        actual = self.inicio
        cont = 1
        while actual!=None:
            print(f"\n{cont}. [{actual.dataGato[0]}] - {actual.dataGato[1]}")
            print(f"     Energia: {actual.dataGato[2]}")
            print(f"     Typo: {actual.dataGato[3]}")
            
            parraf=[
                f"{cont}. [{actual.dataGato[0]}] - {actual.dataGato[1]}",
                f"     Energia: {actual.dataGato[2]}",
                f"     Typo: {actual.dataGato[3]}"
            ]
            parraf = list(map(lambda line: line + '\n', parraf))
            doc = open("./resumen.petworld_result", "a", encoding='utf-8')
            doc.writelines(parraf)
            doc.close()
            # print(actual.next)
            # print("__________________________________________\n")
            cont = cont + 1
            actual=actual.next

    def printListAnimals(self):
        actual = self.inicio
        cont = 1
        while actual!=None:
            print(f"{cont}) {actual.dataGato}\n")
            # print(actual.next)
            # print("__________________________________________\n")
            cont = cont + 1
            actual=actual.next