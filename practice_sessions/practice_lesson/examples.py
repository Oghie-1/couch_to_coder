#!/usr/bin/python3
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    a, b = b, a+b

my_list = [1, 2, 3, 4, 5]
idx = 1


def element_at(my_list, idx):
    if idx >= 0 and idx < len(my_list):
        return my_list[idx]
    else:
        return None



result = element_at(my_list, idx)
#print("Element at index {:d} is {}".format(idx, result))


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    else:
        return None


my_list = [1, 2, 3, 4, 5]
#idx = 1
#element = 4
new_list = replace_in_list(my_list, idx, element)


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for item in my_list:
        return item
    

print(print_reversed_list_integer(my_list))
