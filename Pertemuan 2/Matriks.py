data = [[1,2,3],[4,5,6],[7,8,9]]
data2 = [[1],[2],[3]]
 
matriks = []
matriks1 =[]
for each in data:
	counter =0
	isimatriks=0
	for isi in each:
		counter +=1
		counter2 =0
		for each2 in data2:
			for isi2 in each2:
				counter2+=1
				if counter == counter2 :
					isimatriks += (isi*isi2)
	matriks1.append(isimatriks)

counter  = 0
temp1=[]
temp2=[]
temp3=[]

for each in matriks1:
	counter +=1 
	if counter==1:
		temp1.append(each)
	elif counter == 2:
		temp2.append(each)
	else:
		temp3.append(each)
matriks.append(temp1)
matriks.append(temp2)
matriks.append(temp3)
print (matriks)