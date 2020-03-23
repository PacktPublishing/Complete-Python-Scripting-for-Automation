'''

age=23


if age>30:
	print("Valid age")
else:
	raise ValueError("Age is less than 30")

'''
age=20

try:
	assert age>30
	print("Valid age")
except AssertionError:
	print("Raised with assert because age is lessthan 30")
except:
	print("Exception occured")

