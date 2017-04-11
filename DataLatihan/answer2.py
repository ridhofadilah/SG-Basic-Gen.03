data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

def unique(y):
	output = []
	for x in y:
		if x not in output:output.append(x)
	return output

x = readData(data1)
y = readData(data2)

x = unique(x)
y = unique(y)

b = set(x).intersection(y)

print (b)

x = readData(data1)
y = readData(data2)
txt = []

for i in x:
	for j in y:
		if i == j:
			if i not in txt:
				txt.append(i)
			

print(txt)

