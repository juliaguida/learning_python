

#List of lists or nested list =  a container list with another lists inside three axis, nested by container as on the code below:



list_of_list = [['Apple','Pear','Peach'],['Pie','Tart','pastry'],['Coffee','Milk','Sugar']]
for i in list_of_list:
    list_of_list.append('bue cheese')
    print(list_of_list)
    print(list_of_list[2][1])
    break
    

#update() and del()
'''fruits = {'Apple':'Green','country':'Argentina','harvest': 'November'}

 # don't run for loop in this block of code, if you do you will get the following error message list' object has no attribute 'update'. 
#for i in fruits:
fruits.update({'Apple': 'Red'}) # add all the changes to be made inside the dictionay as new key - identifer and value - data about the identifier.
del fruits['harvest']
print(fruits)
#get() method to return Not found rather than a Python error message.
    # for i in len(fruits):

print(fruits.get('harvest','Not Found'))
fruits['HarvestSeason'] = 'November'
print(fruits['HarvestSeason'])'''


fruits = [{'Apple':'Green','Country':'Argentina','Harvest': 'November'}]
for i in fruits:
    #fruits['Pear'] = 'Green'
    print(fruits[0])
    # if 'Apple' in fruits:
    #     print('Apple is in fruits')
   

workers = [{'name':'Mario','lastname':'Morais'},{'country':'Portugal','city': 'Leiria','contact':'07873419256'}]

# for loop gets the contact and lastname from the dictionary list
for i in workers:   
    print(workers[1]['contact'],workers[0]['lastname'])
    if workers[1] == 'country':
        print(i)
    else:
        print('There is no Portugal in workers')

list = []
list_of_fruits = input()
for item in list_of_fruits:
        list_of_fruits = list 
print(len(list_of_fruits))
if list_of_fruits == 'Apple':
    print('There is apple on the list')
else: 
    print('There is no apple or Apple in the list')
    