# Author: NV 1/12/2021

ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]
names =[]
bets =[]

for row in ledger:
    iteration = 0
    for row, value in enumerate(ledger):
        if ledger[value] == str():
            bets.append(value)
            iteration += 1
        else:
            names.append(value)
            iteration += 1

print(bets)
print(names)