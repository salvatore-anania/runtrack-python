def calcul(num1,operator,num2):
	if operator=="+":
		return num1+num2
	elif operator=="-":
		return num1-num2
	elif operator=="*":
		return num1*num2
	elif operator=="/":
		return num1/num2
	elif operator=="%":
		return num1%num2


print(calcul(5,"+",4))
print(calcul(5,"-",4))
print(calcul(5,"*",4))
print(calcul(5,"/",4))
print(calcul(5,"%",4))