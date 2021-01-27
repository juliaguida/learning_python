# Expected Output: 
# Apple is red in colour
# Banana is yellow in colour
# Pear is green in colour


fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(fruit)
    fruit_name = fruit['name'].title()
    print('{} is {} in colour'.format(fruit_name,fruit['colour']))

bag = [
    'Apple',
    'Banana',
    'Pear'
    ]
for item in bag:
    print(item)