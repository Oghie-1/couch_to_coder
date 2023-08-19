#!/usr/bin/python3
import math
import random


numList = []
for i in range(1):
    numList.append(random.randrange(0, 7))

i = len(numList)

while i < 2:
    print("\nThe length of list is: ", i, "\nand its content are:", numList)

