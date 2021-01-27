

def first_non_consecutive(arr):

    arr = [1,2,3,4,6,7,8,10]
    #your code here
    # create the array
    #non_consec = []
    #look through it and check if the last number -1 is != than 1
    for i in range (1,len(arr)):
         print(i)
        if arr[i]- arr[i-1] != 1:
         print(arr)
        if arr[i+1] - arr[i] == 0:
         print(arr)










# dict1 = {'a': 12, 'for': 25, 'c': 9} 
# dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 
  
  
# # adding the values with common key 
# for key in dict2: 
#     if key in dict1: 
#         dict2[key] = dict2[key] + dict1[key] 
#     else: 
#         pass
          
# print(dict2) 
    