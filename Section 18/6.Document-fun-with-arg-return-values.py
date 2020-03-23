'''
def get_addition(a,b):
	result=a+b
	#print(f"The addition of {a} and {b} is: {result}")
	return result
def main():
	a=eval(input("Enter your first number: "))
	b=eval(input("Enter your second number :"))
	result=get_addition(a,b)
	print(f"The addition of {a} and {b} is: {result}")
	return None
main()
'''

def multiply_num_10(value):
	#result=value*10
	#return result
	return value*10


def main():
	num=eval(input("Enter your number: "))
	result=multiply_num_10(num)
	print("The result is: ",result)




main()