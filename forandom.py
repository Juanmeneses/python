from random import randint

lanzamientos = int(input("Indique cuantas veces se lanzaran el dado "))
dado = randint(1,6)

for n in  range(lanzamientos):
    dado = randint(1,6)
    print dado
    if (dado == 6):
        print "Ha ganado $600!"        
    elif (dado == 3):
        print "Has ganado $300!"        
    elif (dado == 1):
        print ("Siga participando")
    else:
        print("Mala suerte! has perdido $50 u.u ") 
    
                        

