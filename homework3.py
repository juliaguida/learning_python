#"write a program that enables the users to input two integers, 
# num1 and num2 and then prints if num1 is divisible by num2 or not"


#If statement solution:
numb1= int(input('Please enter a number '))
numb2= int(input('Please enter a number '))
total = numb1 + numb2
if total / 2:
     print(total,'This number is divided by 2 ' )
else:
     print(total,' is not divided by 2 ')

#for loop solution:    
total = 0
numb1= int(input('Please enter a number '))
numb2= int(input('Please enter a number '))
for i in range(2):
    total += 1
    print( 'This number is divide by 2')

#while statement:
#The loop goes continuesly
total = 0 
numb1= int(input('Please enter a number '))
numb2= int(input('Please enter a number '))
total = numb1 + numb2
while total / 2:
    total += 1
    print(total, 'This number is divided by 2')
else:
    print('{}This number is not divided by 2'.format(total))





