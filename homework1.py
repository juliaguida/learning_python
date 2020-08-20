# Write a program that takes 10 numbers as input from the user and print the sum of those 10 numbers.


number = []
for i in range(10):
    input_number = int(input('Please enter a number '))
    number.append(input_number)

total = 0
for i in number:
    total += i
print('The total of number you entered is', total )

