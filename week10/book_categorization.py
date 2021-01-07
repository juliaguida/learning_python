# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) as input and outputs the century and decade (e.g. "18th Century, 70s decade")


year = int(input('Please enter a year between 1800 and 1950: '))
century = int(year/100)
decade = year%100 - year%10
print('{}th century, {}s decade.'.format(century,decade))

    
  


