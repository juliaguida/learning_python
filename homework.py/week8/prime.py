num = 407 
   # check for factors
for i in range(2,num):
    if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
else:
           print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
