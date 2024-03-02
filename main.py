#import all classes


#--> FUNCTIONS
    
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
                input("\n> Ingresa la ruta del archivo a leer: ")
            except:
                print("> Error: verifica los parametros enviados.")

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