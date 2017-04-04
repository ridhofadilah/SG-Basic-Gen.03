data1 = "DataSet.txt"

def readData(data1):
    x = []
    with open(data1) as data:
        for line in data:
            x = line.split()
    return x

txt = readData(data1)
angka = []
kata = []

for i in txt:
    if (i.isdigit() == True): 
        angka.append(i)

for i in txt:
    if (i.isdigit() == True): 
        kata.append(angka.pop())
    else: 
    	kata.append(i)

data = []
i = kata[0]
i = ' '.join(l[0].upper() + l[1:] for l in i.split())

data.append(i)


for count in range(1,len(kata)):
    i = kata[count]
    n = kata[count-1]
    if (n[len(n)-1] == '.') : i = ' '.join(l[0].upper() + l[1:] for l in i.split())
    data.append(i)

data = ' '.join(data)
print (data)