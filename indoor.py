a=input("Enter a string")
L=a.split()
for i in L:
    if i.isalnum():
        print(i.lower(),end=" ")
    else:
        print(i,end=" ")
