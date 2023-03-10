def draw_rectangle(x,y):
    for i in range(x):
        print("|",end='')
        if i==0 or i==x-1:
            for i in range(y):
                print("-",end='')
        else:
            for i in range(y):
                print(" ",end='')
        print("|")

print("entrez une hauteur :")
height= int(input())
print("entrez une largeur :")
width= int(input())

draw_rectangle(height,width)