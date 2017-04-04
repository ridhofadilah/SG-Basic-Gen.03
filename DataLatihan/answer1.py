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
for i in x:
	if i == 'I': txt.append('*')
	elif ((i == 'and') or (i == 'you') or (i == 'the')) : txt.append('*')
	else: txt.append(i)

h = ' '.join(txt)
print(h)