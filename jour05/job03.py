def draw_diag(hauteur):
    print("+"+"-"*(hauteur)+"+")
    for ligne in range(hauteur):
        print("|"+"#"*(hauteur-ligne-1)+" "+"#"*ligne+"|")
    print("+"+"-"*(hauteur)+"+")


print("entrez une hauteur :")
n= int(input())

draw_diag(n)