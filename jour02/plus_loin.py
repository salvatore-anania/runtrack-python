import math

def triangle(a,b,c):
	if a > 0 and b > 0 and c > 0:
		if a == b and b == c:
			print("le triangle est equilateral")
		elif a**2 + c**2 == b**2 or a**2 + b**2 == c**2 or b**2 + c**2 == a**2 :
			if a == b or a == c or b == c :
				print("le triangle est rectangle et isocele")
			else:
				print("le triangle est rectangle")
		elif a == b or a == c or b == c :
			print("le triangle est isocele")
		else:
			print("le triangle est quelconque")
	else:
		print("ce n'est pas un triangle")

triangle(0,4,5)
triangle(3,4,-6)
triangle(3,3,3)
triangle(3,4,5)
triangle(3,3,5)
triangle(3,8,5)