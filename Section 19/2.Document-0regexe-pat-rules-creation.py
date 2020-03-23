import re
text="This . is a python and it is easy to learn and it is popular one for dev and automation"
'''
my_pat= 'i[ston]' #is,it,io,in
#print(len(re.findall(my_pat,text)))
print(re.findall(my_pat,text))

'''


#my_pat="x[abcdeflmnopq]y" ==> xay,xby.....xqy
#      ="x[a-fl-q]y"
'''
my_pat='\.'
print(re.findall(my_pat,text))
'''
'''
text="This is a ip address of my db1 server: 255.255.255.255  2456234512341234"

my_pat="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(my_pat,text))
'''


'''
text="This is python @ 345 _ - ("
print(re.findall('\w',text))
#print(re.findall('.',text))
print(re.findall("\W",text))
'''


text="456 90 this is about deciaml re98gex"
print(re.findall('\d\d',text))