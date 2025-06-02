my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recurs(my_list, x = 0):
    if x < len(my_list):
        print(my_list[x])
        recurs (my_list, x + 1)
    else:
        print ('Конец списка')
        

recurs(my_list)