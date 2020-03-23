'''
import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
	df_l=os.listdir(path)
else:
	print("please provide valid path")
	sys.exit()
	

print(df_l)
p1=os.path.join(path,df_l[0])
p2=os.path.join(path,df_l[1])

if os.path.isfile(p1):
	print(f"{p1} is a file")
else:
	print(f"{p1} is a directory")

if os.path.isfile(p2):
	print(f"{p2} is a file")
else:
	print(f"{p2} is a directory")
'''



'''
print("befor loop")

for each in [2,3,4,5]:
	print("hello",each)


print("after loop")
'''

import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
	df_l=os.listdir(path)
else:
	print("please provide valid path")
	sys.exit()


list_of_files_dir=os.listdir(path)
print("all files and dirs: ",list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
	f_d_p=os.path.join(path,each_file_or_dir)
	if os.path.isfile(f_d_p):
		print(f'{f_d_p} is a file')
	else:
		print(f'{f_d_p} is a directory')
