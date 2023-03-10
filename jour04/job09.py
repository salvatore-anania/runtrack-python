
L =[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
min=L[0]
max=L[0]
for i in L:
    if i<min:
        min=i
    elif i >max:
        max=i
print(min,max)