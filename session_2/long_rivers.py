#!/usr/bin/python3

rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

def length_of_list(rivers):
    count = 0
    for x in range(len(rivers)):
        count += 1
    return count

#fuction results as variables
length_of_list = length_of_list(rivers)

def print_river_name(rivers):
    for item in rivers:
        if "name" in item:
            print("\n", item["name"])

def sum_of_length(rivers):
    result = 0
    for item in rivers:
        if "length" in item:
            result += item["length"]
    return result

total_length = sum_of_length(rivers)

#print("Total length of rivers: ", total_length)

def converter(x):
    mile = x
    kilometer = mile * 1.6
    return kilometer

#extentions

def length_converter(rivers):
    for item in rivers:
        if "length" in item:
            new_length = converter(item["length"])
    return new_length

result = length_converter(rivers)

def find_river_name(rivers):
    for item in rivers:
        if "M" in item["name"]:
            print("\nRiver names that start with 'M': \n {}".format(item["name"]))


if __name__ == "__main__":
    print("\nThere are {} rivers  on this list.\n".format(length_of_list))
    print("\nThe Total length of the {} rivers, is {} in miles\n".format(length_of_list, total_length, result))
