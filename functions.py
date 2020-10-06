mylist = [0, 1, 2, 4]
def sum_list(mylist):
    count= 0
    for number in mylist:
        count = count + number
    return mylist

    assert sum_list([1, 2, 3]) == 6
    assert sum_list([1, 2, 3, 4]) == 10
    print(sum_list([1, 3]))
