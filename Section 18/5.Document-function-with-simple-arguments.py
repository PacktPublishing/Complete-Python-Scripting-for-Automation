'''
def get_result(value):  #parameters/positional arguments
	result=value+10
	print(f'Your result is: {result}')
	return None
def main():
	#global num
	num=eval(input("Enter your number: "))
	get_result(num)  #Arguments
	return None

main()
'''
def get_add(p,q):
	aresult=p+q
	print(f'The addition of {p} and {q} is: {aresult}')
	return None
def get_sub(m,n):
	sresult=m-n
	print(f'The sub of {m} and {n} is: {sresult}')
	return None

def main():
	a=eval(input("Enter your first num: "))
	b=eval(input("Enter your second num: "))
	get_add(a,b)
	get_sub(a,b)
	#x=50
	#get_sub(19,x)
	return None

main()
