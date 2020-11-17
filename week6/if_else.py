
a = int(input('Enter a number: '))
b = int(input('Please enter another number:'))
if a > b:
    print('{} is greater than {}'.format(a,b))
elif b > a:
    print('{} is greater than {}'.format(b,a))
elif a == b:
    print('{} is equal to {}'.format(b,a))
else:
    print('This number are rubbish')
