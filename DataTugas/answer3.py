data1 = "DataSet.txt"

def readData(data1):
    x = []
    with open(data1) as data:
        for line in data:
            x = line.split()
    return x

x = readData(data1)
z = []
c = []
for i in x:
    if (i.isdigit() == True) : z.append(i)
for i in x :
    if (i.isdigit() == True) : c.append(z.pop())
    else : c.append(i)
k = []
i = c[0]
i = ' '.join(l[0].upper() + l[1:] for l in i.split())
k.append(i)

for count in range(1,len(c)):
    i = c[count]
    n = c[count-1]
    if (n[len(n)-1] == '.') : i = ' '.join(l[0].upper() + l[1:] for l in i.split())
    k.append(i)

k = ' '.join(k)
print (k)