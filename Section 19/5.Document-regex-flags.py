import re
'''
text="this is a string ThIs is a new staring THIS"
my_pat=r'this'
print(re.findall(my_pat,text,re.I))
'''
text="""this is a string EnD
this is second line enD
This is third line end
asfasd this end"""
#print(text)

#my_pat=r'^this'
my_pat=r'end$'

print(re.findall(my_pat,text,re.M|re.I))