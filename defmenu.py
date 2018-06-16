def menu():
    print("1. primera opcion")
    print("2. segunda opcion")
    print("3. tercera opcion")
    print("4. cuarta opcion")
    return menu

#def suma ():
 #   a=int(input("ingresa un numero"))    
  #  b=int(input("ingresa otro numero"))    
   # c = a+b
    #return suma

while True:
    menu()
    optmenu = int(input("Elija una opcion "))

    if  optmenu == 1:        
        print (" ")
        input("Has pulsado la opcion 1. Pulsa una tecla para continuar")
    elif optmenu == 2:
        print (" ")
        input("Has pulsado la opcion 2. Pulsa una tecla para continuar")
    elif optmenu == 3:
        print (" ")
        input("Has pulsado la opcion 3. Pulsa una tecla para continuar")
    elif optmenu == 4:
        break
    else:
        print (" ")
        input("No has pulsado ninguna opcion correcta. Pulsa una tecla para continuar")
    

