import math

def notes(list):
    for i in range(len(list)):
        if list[i]%5>=3 and list[i]>40:
            list[i]= list[i]+(5-list[i]%5)

list=[22, 4, 16, 9, 11, 12, 14, 5, 41,42,43,44]
notes(list)
print(list)