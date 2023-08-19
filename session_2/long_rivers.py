#!/usr/bin/python3

rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

def print_river_name(rivers=[]):
    for item in rivers:
        if "name" in item:
            print("{}".format(item["name"], end=" "))

print_river_name(rivers)
