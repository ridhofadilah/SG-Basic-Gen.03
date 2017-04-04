def Push(info, x):
	info.append(x)

def Seek(info,top):
	return(info[top])

def Pop(info,top):
	x = Seek(info,top)
	info.remove(x)
	return x

info = []
top = -1

teks = "()()()()(())((())))"
for each in teks :
	if each == '(':
		top += 1
		Push(info,each)
	elif (each == ')'):
		if (top != -1 and Seek(info,top)=='(' ) :
			top -= 1
			Pop(info,top)
		else :
			top +=1
			break

if top == -1:
	print ('valid')
else :
	print ('tidak valid')