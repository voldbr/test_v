x=int(input('fizz = ',))
y=int(input('buzz = ',))
z=int(input('kinez diapazony = ',))
if  x==0 or y==0:
        print ("0 niza")
        exit()
for i in range (1, z+1):
    if  not(i%x):
        print ("F", end="")
    if  not(i%y):
        print ("B", end="")
    if  (i%x) and (i%y):
         print (i, end="")
