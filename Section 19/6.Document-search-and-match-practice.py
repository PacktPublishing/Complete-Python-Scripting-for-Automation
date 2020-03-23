import re
text="""This  is for
python2 and there are two major
vers python3 and python in future python4"""

pat=r'\bpython[23]?\b'
'''
#print(re.findall(pat,text))
match_ob=re.search(pat,text)
#rint(match_ob)
if match_ob:
	print("match from ur pattern: ",match_ob.group())
	print('Starting index: ',match_ob.start())
	print('Ending index: ',match_ob.end()-1)
	print("Length: ",match_ob.end()-match_ob.start())
else:
	print("No match found")
'''
text="""PYTHON2 and there are two major
vers python3 and python in future python4"""

pat=r'\bpython[23]?\b'
match_ob=re.match(pat,text,re.I)
if match_ob:
	print("match from ur pattern: ",match_ob.group())
	print('Starting index: ',match_ob.start())
	print('Ending index: ',match_ob.end()-1)
	print("Length: ",match_ob.end()-match_ob.start())
else:
	print("No match found")

