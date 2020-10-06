print('      / | ')
print('     /  | ')
print('    /   | ')
print('   /    | ')


character_name = 'John'
character_age = '35'
character_name = 'Tom'
character_age = '50'
print('There once was a man name was'+ character_name + ',')
print('He was ' + character_age + 'years old' ',')
print('He really liked the name John')
print('He did not like being '+ character_age + ',')

# to add a new line with \ scape character
string_var = 'Giraffe\nLong neck'
print(len(string_var))
print(string_var[0])
# this call pasing a parameter in this case 'a' so python
# will return which index is 'a' in the list it is also a 
#string method
print(string_var.replace('Giraffe','Animal'))
#print(string_var.index('a'))

#from math import *
# print((ceil(4.7))
# print(abs(4.7))

print( 3 * (2 + 5))
my_numb = 5
print(str(my_numb)  + ' is my favourite number')

numb1= int(input('Please enter a number: '))
numb2= int(input('Please enter a number: '))
print(max(numb1,numb2))

# Mad Libs Game:
color = input(' Enter a color: ')
plural_noun = input(' Please enter a plural noun: ')
celebrity =   input(' Enter a celebrity: ')
print(' Roses are {}' .format(color) )
print(' {} are blue'.format(plural_noun) )
print(' I like {}'.format(celebrity))