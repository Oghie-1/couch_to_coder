#!/usr/bin/python3

import importlib.util
import py_compile
def print_list_integer(my_list=[]):
    i = my_list
    for items in i:
       print(items)

idx = 2
element = -9
my_list = [1, 2, 3, 4, 5]

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    return "{}".format(my_list)
    #for item in my_list:
        #return item


#print(print_reversed_list_integer(my_list))



#def print_reversed_list_integerx(my_list=[]):
    my_list.reverse()
    for item in my_list:
        print(item)


#print_reversed_list_integerx(my_list)


def new_in_list(my_list, idx, element):
    if idx >= 0 or idx < len(my_list) : 
        print("{}".format(my_list))
    else:
        my_list[idx] = element
        new_list = my_list
        print((new_list))


new_in_list(my_list, idx, element)

#!/usr/bin/python3

# Compile the Python source file (hidden_4.py) into a .pyc file
py_compile.compile('hidden_4.pyc')

# Load the compiled module
module_name = 'hidden_4'
module_spec = importlib.util.spec_from_file_location(
    module_name, module_name + '.pyc')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

# Enumerate and print the attributes
if __name__ == "__main__":
    for attr_name in dir(module):
        if not attr_name.startswith("__") and \
            attr_name not in ["__main__", "__name__"]:  # exlude special attr
            print(attr_name)
