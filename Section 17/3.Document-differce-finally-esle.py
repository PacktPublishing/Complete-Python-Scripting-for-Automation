try:
	a=9
	print(a)
except NameError:
	print("Variable is not defined")
except Exception as e:
	print("Exception occured:",e)
else:
	print("This will execute if there is no exceptions in try block")
finally:
	print("This will executes always")
