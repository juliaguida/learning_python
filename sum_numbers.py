"""version 1 without loops
number1 = int(input('Please enter a number '))
number2 = int(input('Please enter a number '))
number3 = int(input('Please enter a number '))
number4 = int(input('Please enter a number '))

sum = number1 + number2 + number3 + number4
print('Sum= {}'.format(sum))

#### version 2 with array and for loops
number = []
for i in range(10):
    input_number = int(input('Please enter a number '))
    number.append(input_number)

print(number)
# Calcuate the sum of all numbers in the array
total = 0
for i in number:
    total += i
print(total) """

# How to replace a index 2 from Tuesday to Wednesday ?

week = ['Monday', 'Tuesday', 'Friday', 'Thursday' ]
week = week.append('Wendesdasy')
print(week)


car = {
    "brand" : "Ford",
    "color" :  "White",
    "year"  :  "2020",
    "model" :  "michael Jordan shoes" ,   
} 
car ["year"] = 2021
print(car.get("year"))

#Reassigning the value of the year

#dictionary format
 #parameter = {
     #Two strings separate by a : and on the end of the line,
     # "" : "",
 #}

a = 5
b = 4
if a < b:
 print( 'You got it right')
else :
 print('4 is not greater than 5')

 #Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a = 10
b = 7
if a == b:
   print('1')
elif a > b:
    print('2')

else:
    print('3')


# While loop
i = 1

while i > 5:
    print('Blue')
    break
    i+= 1
    
    