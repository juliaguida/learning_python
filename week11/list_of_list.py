

#List of lists or nested list =  a container list with another lists inside three axis, nested by container as on the code below:



# list_of_list = [['Apple','Pear','Peach'],['Pie','Tart','pastry'],['Coffee','Milk','Sugar']]
# for i in list_of_list:
#     list_of_list.append(['bue cheese'])
#     print(list_of_list[2][1])
#     print (len(list_of_list))
#     break

#update() and del()
fruits = {'Apple':'Green','country':'Argentina','harvest': 'November'}

 # don't run for loop in this block of code, if you do you will get the following error message list' object has no attribute 'update'. 
#for i in fruits:
fruits.update({'Apple': 'Red'}) # add all the changes to be made inside the dictionay as new key - identifer and value - data about the identifier.
del fruits['harvest']
print(fruits)
#get() method to return Not found rather than a Python error message.
    # for i in len(fruits):

print(fruits.get('harvest','Not Found'))
fruits['HarvestSeason'] = 'November'
print(fruits['HarvestSeason'])


fruits = [{'Apple':'Green','country':'Argentina','harvest': 'November'}]
for i in fruits:
    #fruits['Pear'] = 'Green'
    #print(fruits[0])
    if 'Apple' == fruits:
        print(fruits)


