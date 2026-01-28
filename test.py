def test(some_tuple: tuple) -> list:
    some_list=[]
    for elem in some_tuple:
        some_list.append(elem)
    return some_list
print(test((1, 2, 3 ,4,8 , 9 ,675 ,5 ,5 ,5 ,6, 7,7,)))