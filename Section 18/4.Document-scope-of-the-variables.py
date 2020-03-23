def myfunction1():
	x=60  #This is local variable
	print("Welcome to functions")
	print("x value from fun1: ",x)
	#myfunction2()
	return None


def myfunction2(y):  #Parameter
	print("Thank you!!")
	print("x value from fun2: ",y)
	return None

def main():
	#global x
	x=10 
	myfunction1()
	myfunction2(x)  #Argument
	return None


main()











