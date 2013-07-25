import random

f = open('poetry.txt', 'r')

quatren = []
numerated_quatrens = {}
quatren_number = 1
 
while quatren_number < 10:
    for line in f:
        if len(quatren) < 4:
            quatren.append(line.rstrip())
            numerated_quatrens[quatren_number] = quatren
        else: 
            quatren = []
            quatren.append(line.rstrip())
            quatren_number += 1
            



        

