def distance(marche, hauteur):
    distance=marche*hauteur
    distance*=70
    return distance/100


print("il parcourt",distance(5,6),"metres par semaine.")