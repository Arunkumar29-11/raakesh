
from array import*
print("hlo")
mark=3#inga nama enna nalum podala lam 
x=[3,2,1,2]#ithu place la nama correct answer oda Choice ya kudu irukan
y=array('i',[])#array la enna letter use pandramo aathey than for laiyum use pannanum(i)
for i in range(2):
    ans=int(input("the actor name of black adam\n 1.henry carvils\n2.robert pattinson\n3.dwayne johnson"))
    y.append(ans)#inga nama yathu append potu irukam?
    if(y[0]==x[0]):#array 0 irukthu than start aagum
        print("correct answer")
        mark+=2#inga yathu +2 potu iruku?
    else:
        print("wrong answer")
    ans=int(input("most wanted criminal in india \n1.rajini kanth\n2.jonny depp\n3.kamal hassan"))
    y.append(ans)
    if(y[1]==x[1]):#inga yathu array ikula 1 potu irukam?
        print("correct answer")
        mark+=2#inga yathu +=2 pothu irukam?
    else:
        print("wrong answer")
    ans=int(input("most wanted criminal in the world \n1.arnoldo jimenez \n 2.ajith kumar \n 3.joseph vijay"))
    y.append(ans)
    if(y[2]==x[2]):# inga yathu array ikula 2 potu irukam?
        print("correct answer")
        mark+=3#inga yathu +=3 pothu irukam?
    else:
        print("wrong answer")
    ans=int(input("which type of god wonder women \n1.cryptonion god \n2.demigod \n3.indian god"))
    y.append(ans)
    if(y[3]==x[3]):# inga yathu array ikula 3 potu irukam?
        print("correct answer")
        mark+=3#inga yathu +=3 pothu irukam?
    else:
        print("wrong answer")
    break
print("total mark",mark)#ithu yathu?
        
    
