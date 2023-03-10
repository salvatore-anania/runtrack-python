chaine = "abcdefghijklmnopqrstuvwxyz"
resultat=""
index=0
for i in range(1,16):
    for j in range(i):
        resultat+=chaine[index]
        index+=1
        if index==26:
            index=0
    print(resultat)
    resultat=""