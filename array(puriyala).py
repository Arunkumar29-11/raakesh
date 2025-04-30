from array import*
print("hlo")
mark=7#inga nama enna potam po ithu than total mark ya last la varum
x=[4,3,2,1]
y=array('i',[])#varum array procket madum podalam confirm ma ya array kula letter podanum illa array brocket manaula pota letter ya than for la use pananum
for i in range(2):
    a=int(input("Which actor is called ya super star\n 1.vijay \n2.Ajith \n3.Hiphop\n4.Rajani"))
    y.append(a)#appened confirm podonum but nama ans bathala vara enna nalum podam lam mala pothu ya than kela call panumum
    if(y[0]==x[0]):
        print("correct answer")
    else:
        print("wrong answer")
    b=int(input("Which actor us called a Hiphop tamizla\n1.soorai \n2.ajith \n3.vijay \n4.aathi"))
    y.append(b)
    if(y[1]==x[1]):
        print("correct answer")
    else:
        print("wrong answer")
    c=int(input("Whish actor name is called a Thala \n1.vijay \n 2.ajith kumar \n 3.vijaysethupathi \n 4.Rajani"))
    y.append(c)
    if(y[2]==x[2]):
        print("correct answer")
    else:
        print("wrong answer")
    d=int(input("which actor name is called a ThalaPathi \n1.vijay  \n2.ajith kumar \n3.soorai\n4.sivakathickeyan"))
    y.append(d)
    if(y[3]==x[3]):
        print("correct answer")
    else:
        print("wrong answer")
    break
print("total mark",mark)#total mark patyhula enna nalamu podalam but mark mala call panuirukam so kela confirm ma mark podanum irukam so kela mark confirm call pananum
        
    
