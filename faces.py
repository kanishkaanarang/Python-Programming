def main():
    a=input("enter a string with emoticon")
    return a

def convert(a):
    s=a.split()
    for l in s:
        if l==":)":
            print("🙂",end=" ")
        elif l==":(":
            print("🙁",end=" ")
        else:
            print(l,end=" ")

a=main()
convert(a)
