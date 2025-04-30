print("enter (vote) for vote result")
print("enter (mark) for mark result")
a=int(input("enter your age"))
if(a==35):
    class pen:
        def gen(self):
            s=int(input("enter your age"))
        if (s<18):
            print("You are not eligible")
            
        else:
            print("You are eligible")
        ken=pen()
        ken.gen()
elif(a==25):
    class door:
        def key(self):
            s=int(input("enter your mark"))
        if(s<35):
            print("you are failed")
        elif(s==35):
            print("You are just passed")
        else:
            print("you are passed")
        wood=door()
        wood.key()
else:
    print("error occured")
    

