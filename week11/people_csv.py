

# {'id': '1', 'name': 'Alice', 'age': '20', 'height': '50', 'weight': '120.6'}
# {'id': '2', 'name': 'Freddie', 'age': '21', 'height': '74', 'weight': '190.6'}
# {'id': '3', 'name': 'Bob', 'age': '17', 'height': '48', 'weight': '120'}
# {'id': '4', 'name': 'Margarida', 'age': '19', 'height': '45', 'weight': '130'}
# {'id': '5', 'name': 'Roberto Alves', 'age': '18', 'height': '40', 'weight': '125'}

# Logic:
# Output:
# the oldest person in this is Freddie
import csv

max_age = 0
max_age_person = ''

with open('people.csv','r') as fh:
    people = csv.DictReader(fh)
    for i in people:
        if max_age < int(i['age']): #0 < 20  Is 0(alice) < 20 yes it is then make the new max_age
            max_age = int(i['age']) #20 > 21 Freddy max_age
            max_age_person = i['name']

print('The oldest person in this is {}.'.format(max_age_person)) 



                #HomeWork

# 1) - Print the total weight of the all people.
#      Output the total weight of the all people is 686.2

total_weight = 0
with open('people.csv', 'r') as fh:
    people = csv.DictReader(fh)
    for i in people:
       total_weight = total_weight + float(i['weight'])

    print(total_weight)
      

# 2) - #Output the shortest person in this case is Alice
# Julia you are the computer?

shortest_person = 1000
shortest_person_name = ''   

with open('people.csv', 'r') as fh:
    people = csv.DictReader(fh)
    for i in people:
        if shortest_person > int(i['height']): # code only works if I change the operator to greather sign <.
            shortest_person = int(i['height']) 
            shortest_person_name = i['name']

print(shortest_person_name)

a = 22
b = 10
if a > b:
    a = b


#3) - Output the tallest person in this case Freddie


# The loop starts the iteration as 0 it will increase to 1 in the next iteration(1itera 0 + 0 =  0, 2itera 1 + 0 = 1 until it meets the condition.)

tallest_height = 0
tallest_person = ''
with open('people.csv', 'r') as fh:
    people = csv.DictReader(fh)
    for person in people:
        if tallest_height < int(person['height']):
            tallest_height= int(person['height'])
            tallest_person = person['name']
print('The tallest person in this case is {}'.format(tallest_person))





    
#List list of list of list of dictionary