import re
text='isa python l	earn and \n itis easy 	to'
#my_pat='^i[ts]'
#my_pat="learn$"
#my_pat=r"\blearn\b"
#my_pat=r"\Blearn\B"
my_pat=r"\n"
print(re.findall(my_pat,text))