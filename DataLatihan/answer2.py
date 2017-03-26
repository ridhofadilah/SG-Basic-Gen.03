data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
<<<<<<< HEAD
	return x

teks1 = readData(data1)
teks2 = readData(data2)
teks3 = []

for word1 in teks1 :
	for word2 in teks2 :
			if word1==word2 :
				counter = 0
				for word3 in teks3 :
					if word2 == word3 :
						counter += 1
				if counter == 0 :
					teks3.append(word2)

print (teks3)
=======
return x
>>>>>>> 54fd24fcc1ceb26221e1e7500236ea1ea98f470b
