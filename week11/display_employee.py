# import csv

# with open('employee_list.csv', 'r') as fh:
#       #reader gets the file display as a list of list.
#     reader = csv.reader(fh)
#     for employee in reader:
#       print('{} works in {} and their emplyoee ID is {}'.format(employee[0],employee[1],employee[2]))



        
# print('----------')
# with open('employee_list.csv', 'r') as fh:
#     #dict reader gets the file display as a list of dictionary.
#     csv_file = csv.DictReader(fh)
#     for employee in csv_file:
#         print('{} works in {} and their emplyoee ID is {}'.format(employee['Name'],employee['Department'],employee['ID']))

# street var is a list of dictionary.
street = [
  # i reprents everything that you have inside a list of dict bellow:

  # 0 {'house_number': 10,'house_owner': 'Julia'}, 
  # 1 {'house_number': 25,'house_owner': 'Nayana'},
  
  {'house_number': 10,'house_owner': 'Julia'},
  {'house_number': 25,'house_owner': 'Nayana'},
]
for i in street:
  print(i['house_owner'])

# print(street[1]['house_owner'])

# num = [11, 12, 13, 14]
# for i in num:
#   print(i) prints the whole list.
#
# students_marks var is a list of lists.
students_marks = [
  [25, 50, 75, 100],
  [50, 40, 50 ,60]
]
for i in students_marks:
  print(i[-1])
