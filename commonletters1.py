n1=input("Enter the string1:")
n2=input("Enter the string2:")
n3=set(n1).intersection(set(n2))#set is used for duplicate letters are removed
print(n3)#we can use & also(set(n1)&set(n2))