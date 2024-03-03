from datetime import date
from datetime import datetime

#import all my classes
from animalClass import *

#--> FUNCTIONS

#save file to charge
def viewList():
    animal.globalList()
    
def chargeFile(title):
    print("\n***  ",title,"  ***\n")
    #save rout at var
    rout = input("> Ingresa la ruta del archivo: ")
    #charge file XML
    file = open(rout,'rt',encoding='utf-8')
    # parameters
    # 1. file rout + name file + extension 
    #   example: /Users/josuedesarrollador/Documents/GitHub/LFP_S1_2024_Practica_201800968/prueba.petworld
    # 2. file management
    #   r --> read
    #   w --> write
    #   a --> append
    #   x --> create
    
    #   t --> text mode
    #   b --> bytes - for photografe or images
    # 3. validate special characters
    
    readAllLines = file.readlines()

    return readAllLines

def createAnimal(name):
    #Actual date
    today = date.today()
    now = datetime.now()
    
    dateNow = f"{today.day}/{today.month}/{today.year}, {now.hour}:{now.minute}"
    #created a new client
    animal.addAnimal([dateNow, name, 100.00, "gato"])
    print(f"***  [{dateNow}] El gato {name} se agrego correctamente   ***")

def feedAnimal(name, plus):
    #Actual date
    today = date.today()
    now = datetime.now()
    dateNow = f"{today.day}/{today.month}/{today.year}, {now.hour}:{now.minute}"
    search = searchAnimal(name)
    vida = float(search[2])

    if(search==None):
        print(f"***  El gato {name} no existe   ***")
    else:
        if(vida>0):
            updatate = animal.feed(name, plus)
            print(f"***  [{dateNow}] {name}, Gracias. Ahora mi energia es {updatate[2]}   ***")
        else:
            print(f"***  [{dateNow}] {name}, Muy tarde. Ya me morí  ***")

def playWithAnimal(name, plus):
    # Actual date
    today = date.today()
    now = datetime.now()
    dateNow = f"{today.day}/{today.month}/{today.year}, {now.hour}:{now.minute}"
    search = searchAnimal(name)
    vida = float(search[2])

    if(search==None):
        print(f"***  El gato {name} no existe   ***")
    else:
        if(vida>0):
            updatate = animal.play(name, plus)
            print(f"***  [{dateNow}] {name},Gracias por jugar conmigo. Ahora mi energia es {updatate[2]}   ***")
        else:
            print(f"***  [{dateNow}] {name}, Muy tarde. Ya me morí  ***")

def searchAnimal(name):
    searchAnimal = animal.valAnimal(name)
    return searchAnimal

#--> VIEW USER MENUS
#create principal menu
def principalMenu():
    print("\n===========================================")
    print("==             Menu Principal            ==")
    print("===========================================")
    print("==                                       ==")
    print("==  1. PetManager                        ==")
    print("==  2. Salir                             ==")
    print("==                                       ==")
    print("===========================================")
    
    #request user option
    op=input("\n> Ingrese una opción: ")
    
    #Validate op is a number
    it_is = op.isnumeric()
    
    if (it_is==True):
        #convert op to int var
        op=int(op)
        # Options to principal menu
        if(op==1):            
            try:
                file_data=chargeFile("Cargar Archivo")
                
                for element in file_data:
                    x = element.split(":")
                    
                    # filter action to realise
                    if(x[0]=="Crear_Gato"):
                        name= x[1].split("\n")
                        #validate cat exist
                        exist = searchAnimal(name[0])
                        if(exist == None):
                            createAnimal(name[0])
                        else:
                            print(f"El nombre {name[0]} ya existe y no puede ser registrado dos veces")
                    elif(x[0]=="Dar_de_Comer"):
                        data = x[1].split(",")
                        name = data[0]
                        peso = data[1].split('\n')

                        plus = 12 + float(peso[0])
                        feedAnimal(name, plus)
                    elif(x[0]=="Jugar"):
                        data = x[1].split(",")
                        name = data[0]
                        time = data[1].split('\n')

                        #operate data
                        plus = float(time[0]) * 0.1
                        playWithAnimal(name, plus)
                    elif(x[0]=="Resumen_Mascota"):
                        # Actual date
                        today = date.today()
                        now = datetime.now()
                        dateNow = f"{today.day}/{today.month}/{today.year}, {now.hour}:{now.minute}"
                        name= x[1].split("\n")
                        #validate cat exist
                        exist = searchAnimal(name[0])
                        
                        if(exist == None):
                            print(f"El nombre {name[0]} no existe")
                        else:
                            print (f" Resumen para {name[0]} ".center(50, '-')) 
                            print("\n")
                            print(" ".rjust(5, ' ')+dateNow+" - "+exist[1])
                            print (f"     Energia: {exist[2]}") 
                            print (f"     Tipo: {exist[3]}") 
                            print("\n")
                            print("-".rjust(50, '-'))
                    elif(x[0]=="Resumen_Global"):
                        today = date.today()
                        now = datetime.now()
                        dateNow = f"{today.day}/{today.month}/{today.year}, {now.hour}:{now.minute}"
                        print (f"{dateNow} "+"-".rjust(24, '-')+f" Resumen Global "+"-".ljust(24, '-')) 
                        print("\n")
                        viewList()
                        print("\n")
                        print("-".rjust(50, '-'))
                    else:
                        print("**   opcion invalida   **")
            except:
                print("**   Error, algo salio mal   **")
            principalMenu()
        elif(op==2):
            print("\n========================================================")
            print("==             ***  Fin del programa  ***             ==")
            print("========================================================\n")
            exit
        elif(op==3):
            viewList()
            principalMenu()
        else:
            print("¡Opcion no valida!")
            principalMenu()
    else:
        print("> Error: debes ingresar un número como opción.")
        principalMenu()
        
#VARS
animal=animalList()

principalMenu()