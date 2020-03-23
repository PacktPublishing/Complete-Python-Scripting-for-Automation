#NameError
#TypeError
#FileNotFoundError
#ZeroDivisionError

try:
	print("This is try block")
	import fabric
	print(a)
	#print(4+"hi")
	#open('asdfas.txt')
	#print(5/0)
	
except FileNotFoundError:
	print("File is not present to open it")
except NameError:
	print("Variable is not defined")
except TypeError:
	print("Adding number and string is not possible")
except ZeroDivisionError:
	print("Division with zero is not possible")
except ModuleNotFoundError:
	print("Please install fabric to use it")
except Exception as e:
	print(e)
finally:
	print("Finally this will executes")

