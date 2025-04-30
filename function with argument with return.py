def raja(h):
    a=h*10
    print("the cost of tickets",a)
    return a
def king(h):
    a=h*20
    print("the cost of the tickets",a)
    return a
print("1.chennai")       
print("2.coimbatore")
k=int(input("where are u going"))     
if(k==1):                             
    h=int(input("how many tickets"))
    a=raja(h)
elif(k==2):
    h=int(input("how many tickets"))
    a=king(h)
else:
    print("error")
