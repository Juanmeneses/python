horast = int(input("Indique cantidad de horas trabajadas en la semana "))
vhora = 2500
vbruto = vhora* horast
descuentosalud = vbruto * 0.07
descuentoafp = vbruto * 0.1
desctotal = descuentosalud + descuentoafp
vliquido = vbruto - desctotal

if horast >40:
    vliquido = vliquido + (vbruto * 0.5)
    print("el valor total a pagar es de ",vliquido)
else:    
    print ("el valor a pagar es de", vliquido)