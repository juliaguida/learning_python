


count= 0
for number in range(1,4):
    count = count + number
    print(number)
        

mylist = [0, 1, 2, 4]
def sum_list(mylist):
    count= 0
    for number in mylist:
        count = count + number
    return mylist

    assert sum_list([1, 2, 3]) == 6
    assert sum_list([1, 2, 3, 4]) == 10
    print(sum_list([1, 3]))

#Guess game:

# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input( ' Guess: '))
#     guess_count += 1
#     guess = int((input( ' Guess: '))
# if guess == secret_number:
#        print('You win!!!')
#             #break
# else:
#  print('You did not win this time, thank you for playing')

#Car game:
command = ''
started = True
while command != 'quit':
    command = input(' >').lower()
    if command == 'start':
         print('Car started...')
    if started:
             print( 'Car already started... ')
    

    elif command == 'stop':
        print('Car stopped!')
        if not started:
           print('Car is already stopped!')
        else:
            started = False
            print('Car stopped!')

    elif command == 'help':
        print("""
           start - to start the car
           stop - to stop the car.
           quit - to quit
        
       """ )
    else: 
       print( " I don't understand ")
       
number = 0
while number < 3:
    print( "Le'ts keep looping")
    number += 1

#Car game:

command = ''
started = False
while command != 'quit':
    command = input(' >').lower()
    if command == 'start':
         print('Car started...')
         if started:
             print( 'Car is already started ')
         else:
             started = True
             print('Car started')

    elif command == 'stop':
     
        print('Car stopped!')
        if not started:
           print('Car is already stopped!')
        else:
            started = False
            print('Car stopped!')

    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car.
quit - to quit
        
       """ )
    elif command == 'quit':

      print('Thank you for playing bye!!!')
    else: 
       print( " I don't understand ")


number = 0
while number < 3:
    print( "Le'ts keep looping")
    number += 1

nums = [1, 2, 3, 4]
for numbers in range(5):
    if numbers == 3:
        print( 'Found it!')
        continue
    print(numbers)

x= 0
while True:
    if x < 5:
     print(x)
    x+= 1

