def idly(i):
    a=i*5
    return a
def dosa(d):
    a=d*10
    return a
def poorai(p):
    a=p*20
    return a
def pongal(po):
    a=po*30
    return a
def vadai(v):
    a=v*5
    return a
print("welcome to come hotel krishna")
print("what is u want")
print("1.idly")
print("2.dosa")
print("3.poorai")
print("4.pongal")
print("5.vadai")
b=int(input("which one u can need"))
if(b==1):
    print("u will seleted a idly")
    c=int(input("how many idly u need"))
    a=idly(c)
    print("u cost is",a)
elif(b==2):
    print("u will seleted a dosa")
    c=int(input("how many dosa u need"))
    a=dosa(c)
    print("u cost is",a)
elif(b==3):
    print("u will seleted a poorai")
    c=int(input("how many poorai u need"))
    a=poorai(c)
    print("u cost is",a)
elif(b==4):
    print("u will seleted pongal")
    c=int(input("how many pongal u need"))
    a=pongal(c)
    print("u cost is",a)
elif(b==5):
    print("u will seleted vadai")
    c=int(input("how many vadai u need"))
    a=vadai(c)
    print("u cost is",a)
else:
    print("nothing u can selected")
