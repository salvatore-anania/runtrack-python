def aliments(type,saison):
	if type=="fruits" and saison=="hiver":
		print("orange, mandarine et kiwi")
	elif type=="fruits" and saison=="ete":
		print("Poire,fraise,cassis")
	elif type=="legume" and saison=="hiver":
		print("carotte,topinambour,endive")
	elif type=="legume" and saison=="ete":
		print("artichaut,aubergine,navet")

aliments("fruits","hiver")
aliments("fruits","ete")
aliments("legume","hiver")
aliments("legume","ete")