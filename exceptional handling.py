a=int(input("enter the a value"))
b=int(input("enter the b value"))
try:
    print("ithu try")
    c=a/b
    print(c)
except ZeroDivisionError as i:
    print("ithu zero division error")
except expection as i:
    print("ithu expection")
finally:
    print("ithu finally")  
