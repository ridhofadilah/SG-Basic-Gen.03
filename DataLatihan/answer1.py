data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

x = readData(data1)
txt = []
<<<<<<< HEAD
for c in x:
	if c == 'I':txt.append('*')
	elif c =='you' or c == 'The' or c== 'and':txt.append('*'*3)
	else:txt.append(c)
txt = ' '.join(txt)
print(txt)
=======
for i in x:
	if i == 'I': txt.append('*')
	elif ((i == 'and') or (i == 'you') or (i == 'the')) : txt.append('*')
	else: txt.append(i)

h = ' '.join(txt)
print(h)
>>>>>>> refs/remotes/ComputingTelU/master
