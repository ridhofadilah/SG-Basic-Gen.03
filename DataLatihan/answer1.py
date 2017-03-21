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
for c in x:
	if c == 'I':txt.append('*')
	if c =='you' or c == 'The' or c== 'and':txt.append('*'*3)
	else:txt.append(c)
txt = ' '.join(txt)
print(txt)