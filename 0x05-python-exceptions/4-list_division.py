#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    L1 = len(my_list_1)
    L2 = len(my_list_2)
    if L1 > L2:
        list_length = L1
    else:
        list_length = L2

    for num in range(list_length):
        try:
            div = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
