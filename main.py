#import all classes


#--> FUNCTIONS
#save file to charge
def chargeFile(title):
    print("\n***  ",title,"  ***\n")
    #save rout at var
    rout = input("> Ingresa la ruta del archivo: ")
    #charge file XML
    file = open(rout,'rt',encoding='utf-8')
    # parameters
    # 1. file rout
    # 2. file management
    # r --> read
    # w --> write
    # a --> append
    # x --> create
    
    # t --> text mode
    # b --> bytes - for photografe or images
    # 3. special characters 
    
    readAllLines = file.readlines()
    print(readAllLines)
    return readAllLines
    
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
            file_data=chargeFile("Cargar Archivo")
            
            for element in file_data:
                print(element)
            
            principalMenu()
        elif(op==2):
            print("\n========================================================")
            print("==             ***  Fin del programa  ***             ==")
            print("========================================================\n")
            exit
        # elif(op==3):
        #     #request user option
        #     lista=input("\n> Ingrese el tipo de lista que desea imprimir: ")
        #     viewList(lista)
        #     principalMenu()
        else:
            print("¡Opcion no valida!")
            principalMenu()
    else:
        print("> Error: debes ingresar un número como opción.")
        principalMenu()
        
#VARS

principalMenu()