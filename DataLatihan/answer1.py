data1 = "Data1.txt"
<<<<<<< HEAD
=======
data2 = "Data2.txt"
>>>>>>> 54fd24fcc1ceb26221e1e7500236ea1ea98f470b

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
<<<<<<< HEAD

teks = readData(data1)
a= []

for word in teks :
	if word == 'I' :
		a.append('*')
	elif word == 'and' or word == 'The' or word == 'you' :
		a.append('*'*3)
	else :
		a.append(word)

paragraf = ' '.join(a)
print (paragraf)
=======
>>>>>>> 54fd24fcc1ceb26221e1e7500236ea1ea98f470b
