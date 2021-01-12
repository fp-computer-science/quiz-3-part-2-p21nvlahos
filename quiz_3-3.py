# Author: NV 1/12/2021

import random

num = random.randint(0, 9999)
print(num)
print(len(str(num)))


if len(str(num)) != 4:
    num[-1] += "0"
else:
    print("")


troopers = []
while True:
    run = input("Name a clone? ")
    names = "CT-{0}".format(num)
    if run.upper() == "Y":
        print("New Clone Trooper name: {}".format(names))
        troopers += names
    elif run.upper() == "N":
        break

print(troopers)
