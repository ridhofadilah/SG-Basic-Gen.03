x = input()
a = 0
b = True
for i in x:
    if (i == '('):
        a += 1
    elif (i == ')') :
        if a > 0:
            a-=1;
        else:
            b = False ;
            break
if a > 0:
   b = False;
if b == False :
    print (" Tidak Seimbang")
else :
    print ("Seimbang")