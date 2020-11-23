

user1 = 'Anna'
user2 =  'Maria'
print('1',user1,user2)
expected output is user1 = 'Maria' and user2 = 'Anna'

starting point: apple in 'red basket', orange in 'blue basket'
apple in'black basket',orange in'blue basket', empty 'red basket'
apple in'black basket', orange in 'red basket', empty 'blue basket'
apple in 'blue basket', orange in 'red basket', throw 'black basket'

temp_user = user1
print('2',user1,user2)
user1 = user2
print('3',user1,user2)
user2 = temp_user
print(user1,user2)


x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
    

