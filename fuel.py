def main():
    a=input("Fraction  :")
    b=convert(a)
    print(gauge(b))

def convert(a):
    try:
        L=a.split("/")
        b=(int(L[0])/int(L[1]))*100
        return b
    except ZeroDivisionError:
        pass
    except ValueError:
        pass


def gauge(b):
    if b>="99":
        return f"F"
    elif b<="1":
        return f"E"
    else:
        return f"{b}%"


if __name__=="__main__":
    main()

