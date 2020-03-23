#sfile="C:\\Users\\Automation\\Desktop\\random.txt"
#dfile="C:\\Users\\Automation\\Downloads\\newrandom.txt"
sfile=input("Enter your source file: ")
dfile=input("Enter your destination file: ")
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()