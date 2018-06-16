from random import randint

lanzamientos = int(input("Indique cuantas veces se lanzaran el dado "))


for n in  range(lanzamientos):
    gana = 0
    dado = randint(1,6)
    print dado
    if (dado == 6):
        print "Ha ganado $600!, el total es ",gana         
    elif (dado == 3):     
        print "Has ganado $300! el total es ",gana      
    elif (dado == 1):
        print ("Siga participando, el total es ",gana)
    else:
        print("Mala suerte! has perdido $50 u.u, el total es ",) 
        

