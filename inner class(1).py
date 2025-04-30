class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.age)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='Hp'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student('bala',5)
s2=student('dinu',7)
s1.show()


