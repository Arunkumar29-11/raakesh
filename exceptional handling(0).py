a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
try:
    d=a/b
    print(d)
    k=int(input("enter the value of k"))
    print(k)
except ZeroDivisionError as mahes:
    print("hey,you cannot divide a number of zero")
except Exception as mahes:
    print("something went wrong")
finally:
    print("finally")
