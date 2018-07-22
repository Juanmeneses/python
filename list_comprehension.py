lista = ['Elie','Tim','Matt']
lista2 = [1,2,3,4,5,6]
num1 = [1,2,3,4]
num2 = [3,4,5,6]
rango = range(1,100+1)
cadena = "amazing"

answer = [char[0] for char in lista]
answer2 = [num for num in lista2 if num % 2 ==0]
answer3 =[num for num in num1 if num in num2 ]
answer4 = [char[::-1].lower() for char in lista]
answer5 = [num for num in rango if num%12 ==0]
answer6 = [char for char in cadena if char not in ['a','e','i','o','u']]



print(answer)
print(answer2) 
print(answer3)
print(answer4)
print(answer5)
print(answer6)