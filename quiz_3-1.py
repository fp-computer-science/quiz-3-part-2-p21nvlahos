# Author: NV 1/12/2021



def race_lst(younglings, race):
    end = []
    for index, value in enumerate(younglings):
        lst = [(value, race[index])]
        end += lst
    return end


younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']

print(race_lst(younglings, race))