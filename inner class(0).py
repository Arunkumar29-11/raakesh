class student:
    def __init__(self,name,rollno):
        self.name =name
        self.rollno=rollno
        self.lap=self.laptop()
    def show (self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand=input("enter the brand")
            self.cpu=input("enter the cpu")
            self.ram=input("enter the ram")
        def show (self):
            print(self.brand,self.cpu,self.ram)
s1=student("navin",2)
s2=student("jenny",3)
s1.show()
s2.show()
lap1=student.laptop()
