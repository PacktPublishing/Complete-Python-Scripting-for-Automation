#Working with text files
'''
fo=open('newdemo.txt','w')
#print(fo.mode)
#print(fo.readable())
#print(fo.writable())
fo.close()
'''
'''
my_content=["This is a data -1\n","This is a data-2\n","This is a data-3"]
fo=open("random.txt",'w')
fo.write("This is a first line\n")
fo.write("This is a second line\n")
fo.write("This is a third line")
#fo.writelines(my_content)
fo.close()
'''
'''
my_content=['This is using loop-iteratioin-1','This is using loop-iterantion-2','This is using loop-iteratioin-3']

fo=open("with_loop.txt",'a')

for each_line in my_content:
	fo.write(each_line+"\n")
fo.close()
'''
'''

fo=open("with_loop.txt","r")
data=fo.read()
fo.close()

print(data)
'''
'''
fo=open("with_loop.txt","r")
print(fo.readline())
print(fo.readline())
fo.close()
'''

fo=open("with_loop.txt","r")
data=fo.readlines()
fo.close()
'''
for each in range(3):
	print(data[each])   #data[0], data[1],data[2]
'''
print(data[-1])














