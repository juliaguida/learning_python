# Write a program that takes 2 numbers as arguments to a function and returns the sum of those 2 numbers

def add_func(number1,number2):
    return number1 + number2

numb1 = int(input('Enter a number: '))
numb2 = int(input('Enter another: '))

result = add_func(numb1,numb2)
print(result)