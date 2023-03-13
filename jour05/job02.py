def draw_rectangle(x,y):
    for i in range(x):
        if i==0 or i==x-1:
            print("|"+"-"*y+"|")
        else:
            print("|"+" "*y+"|")

print("entrez une hauteur :")
height= int(input())
print("entrez une largeur :")
width= int(input())

draw_rectangle(height,width)