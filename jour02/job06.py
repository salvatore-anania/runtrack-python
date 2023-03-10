def sign(nombre):
	if nombre > 0:
		print("positif")
	elif nombre < 0:
		print("negatif")
	elif nombre == 0:
		print("zero")
	else:
		print("ce n'est pas un nombre")


sign(3)
sign(-3)
sign(82646458)
sign(-98487348)
sign(30)
sign(0)