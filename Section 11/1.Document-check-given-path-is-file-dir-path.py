#This is a platform independet script(you can run on any operating system)
import os
path=input("Enter your path: ")

if os.path.exists(path):
	print(f"Given path : {path}is a valid path")
	if os.path.isfile(path):
		print("and it is a file path")
	else:
		print("and it is a directory path")
else:
	print(f"Given path : {path} is not existing on this host")