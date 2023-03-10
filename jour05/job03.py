def draw_diag(x):
    print("+"+"-"*(x)+"+")
    for i in range(x):
        print("|",end='')
        for j in range(x):
            if j==x-i-1:
                print(" ",end='')
            else:
                print("#",end='')
        print("|")
    print("+"+"-"*(x)+"+")


print("entrez une hauteur :")
n= int(input())

draw_diag(n)