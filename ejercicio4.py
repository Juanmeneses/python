

llamada = int(input("indique el largo de la llamada"))
valor_minuto = 60

if llamada <=10 :
    valor = valor_minuto * llamada
    print(f"su llamada duro {llamada} minutos y el valor total fue de {valor} pesos")
else:
    recargo = (valor_minuto * llamada)*0.05
    valor = (valor_minuto * llamada) + recargo
    print(f"su llamada duro {llamada} minutos y el valor total fue de {valor} pesos")