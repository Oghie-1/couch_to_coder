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
