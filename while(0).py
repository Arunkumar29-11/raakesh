b=int(input("how many wickets"))
r=0
a=0
for i in range(b):
    for j in range(6):
        k=int(input("enter the run"))
        if(k!=0):
            r+=k
            print("Your score",r)
        else:
            print("out")
    break    
print("Your total score",r)             
        
    
