# def year_leap(year):
# #If a year is multiple of 400 it is a leap year.
#     if year %400 == 0:
#         #print('This is a year leap ')
#     if year %4 == 0:
#         #print('This is a year leap')
#     if year %100 == 0:
#         #print('This is not a year leap')
#         return True
#         else:
#             return False
#         else:
#             return True
        

# year = 2020
# def year_leap(year)

year_leap = int(input('Please enter a year: '))
#If a year is multiple of 400 it is a leap year.
if year_leap %400 == 0:
    print('Leap year{}'.format(year_leap))
#If a year is multiple of 4 then it is a leap year
if year_leap %4 == 0:
    print('This is a leap {}'.format(year_leap))
#If a year is multiple of 100 then it is not a leap year
if year_leap %100 != 0:
    print( 'This is not a leap year {}'.format(year_leap))
#else:
    #print(" I don't know ")    