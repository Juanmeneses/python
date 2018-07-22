numbers = [1,2,3,4,5,6,7,8] 
vowels = "This is so much fun"

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]

no_vowels = ''.join(char for char in vowels if char not in "aeiou")
no_cons = ''.join (char for char in vowels if char not in "Thsmcfn")

print(evens)
print(odds)
print (no_vowels)
print(no_cons)