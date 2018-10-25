#testCommit
def readFile(path):
	tmp = 0
	joomb = ""
	d = {}
	global x,y,z
	with open(path) as inf:
		for i in inf.read().replace("\n",";").replace(" ","").split(";"):
			if i!=' ':
				print(i)
				if tmp % 4 == 0 :
					d[i] = 0
					joomb = i
				elif tmp % 4 == 3:
					d[joomb] += float(i)
					z += float(i)
					d[joomb] /= 3
				elif tmp % 4 == 1:
					x += float(i)
					d[joomb] += float(i)
				else :
					y += float(i)
					d[joomb] += float(i)
				tmp+=1
	x = x/(len(d)-1)
	y = y/(len(d)-1)
	z = z/(len(d)-1)
	return d

def writeFile(path,d):
	with open(path,"w") as inf:
		for i in d:
			if i!="":
				s = str(round(d[i],9))+'\n'
				inf.write(s)
		s = str(round(x,9)) + " " + str(round(y,9))+ " "+ str(round(z,9))
		inf.write(s)

x= 0.0 
y= 0.0 
z= 0.0 

d = readFile("/home/egzy/Documents/Arithmetic code/ind.txt");
print(x," ",y," ",z)
print(len(d))
writeFile("/home/egzy/Documents/Arithmetic code/ind1.txt",d)
