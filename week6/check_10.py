#Write a program that takes an input from the user and prints “Input was greater than 10” if the number was greater than 10
check_numb = int(input('Please enter a number: '))
 if check_numb > 10:
    print('The number {} is greater than 10 '.format(check_numb))
elif check_numb < 10:
#     print('This number is not greater than 10'.format(check_numb))