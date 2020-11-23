student = {
    'name':'John',
    'class': '6',
    'id': 10
}
print(student['name'])# if I know thew key exist
if 'class' in student.keys():
    print('class was found')

print(student.get('marks')) # if I am not sure the key exist
#print(student['marks'])

for key in student:
    print(key,student[key])
print(student.keys())
print(student.values())

for key,value in student.items():
    print(key,value)



