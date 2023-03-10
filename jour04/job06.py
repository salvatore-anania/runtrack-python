
L =[5,7,8,9,34]
temp = L[0]
last = len(L)-1
L[0] = L[last]
L[last] = temp
print(L)