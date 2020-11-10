

# This code checks the temperature
#Get the current temperature from the user

#temperature = int(input('What is the temperature now ? '))
# temp = input("How is the temperature now? ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

#Compare current temperature <= 0
#Print current temperature is freezing: True or False
# if temp <= 0:
#         print("It's not freezing")
# else:
#         print('Get yourself a cuppa is freezing')

temperature = int(input('What is the temperature now ? '))
if temperature <= 0:
    print('Today is freezing: {}'.format(temperature))
else:
    print('Today is a warm day')



temperature = int(input('What is the temperature now ? '))
today = temperature <= 0
print('It is freezing: {}'.format(today))
