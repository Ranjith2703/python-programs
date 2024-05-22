d={}
s=str(input("enter a string:" ))
sp=s.split()
for i in sp:
       d[i]=sp.count(i)
print(d)