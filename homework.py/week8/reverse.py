# Write a program to take a sentence from the user and 
# Print the length of the sentence,
# Print the sentence in reverse order and
# Print the number of spaces in the sentence.
# Extension” Please use array functions and for loop rather than the reverse() method and reverse the words:
# 	Example: if the user enters: user_input = ‘I am doing well’
# 				Output:	  display output = ‘well doing am I’

# Split the input string into a list based on spaces list = [‘I’, ‘am’, ‘doing’, ‘well’]
# Create new list in reverse order list[::-1] reversed_list = [‘well’, ‘doing’,’am’, ‘I’]
# Convert list into a string separated by spaces. ‘ ’.join(reversed_list)

phrase = input('Please enter a phrase here and Python will surprise you with the style:')
string_len = len(phrase)
list = phrase.split()
new_list = ''.join(reversed(phrase))
print(list, new_list,string_len)



# phrase = input( 'Please enter any phrase that comes in your mind.')
# reversedstring= ''.join(reversed(phrase))
# print(reversedstring)
# print(len(phrase))
# #print(list(reversed(phrase)))

