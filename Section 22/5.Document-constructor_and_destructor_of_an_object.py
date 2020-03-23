class Person(object):
	def __init__(self,name,age):
		print("an object has been created")
		self.name=name
		self.age=age		
		return None
	def __del__(self):
		print("object has been deleted")
		return None


per1=Person('Jhon',26)


