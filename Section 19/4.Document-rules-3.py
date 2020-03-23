import re
'''
text="This is a pythonnnn and python aaa haaaafd xyzaaaaaaaa"
#my_pat=r'\bpython{4}\b'
my_pat=r'\bxyza{8}\b'
print(re.findall(my_pat,text))
'''
text="xaz asdfa sdf xaaz xaaaaaaaz xaaaaz  xz"
#my_pat=r'\bxa{2,}z\b'
#my_pat=r'xa{1,}z'
#my_pat=r'xa*z'   
my_pat=r'xa?z'
print(re.findall(my_pat,text))