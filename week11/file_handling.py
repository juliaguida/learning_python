user_input = input('Please enter a line for the file: ')

fh = open('demo_file.txt','a')
fh.write(user_input)
fh.close()
fh = open('demo_file.txt','r')
print(fh.read())
fh.close()
