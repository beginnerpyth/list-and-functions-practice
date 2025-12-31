def hero():
    try:
        x = int(input("enter a number"))
        b=int(input("enter a number"))
        c=b/x
        return c
        
    except ZeroDivisionError as e:
        print(e)
        return hero() 

    finally:
        print("yeah its done")
m=hero()
print(m)
