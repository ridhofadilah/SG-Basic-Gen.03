data = [1,2,3]
data2 = [[1,2,3],[4,5,6],[7,8,9]]
 

matriks =[]

for x in data2:
	d=0
	e=0
	for a in x:
		d+=1
		c = 0
		for b in data:
			c += 1
			if c == 1 and d == 1:
				e+=(a*b)
			elif c==2 and d==2:
				e+= (a*b)
			elif c==3 and d==3:
				e+= (a*b)
	matriks.append(e)

print (matriks)