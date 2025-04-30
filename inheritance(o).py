class raja:
    def king(self):
        self.a=int(input("enter the value of a"))
class roja(raja):
    def rose(self):
        self.b=int(input("enter the value of b"))
class devil(roja):
    def dose(self):
        self.c=self.a+self.b
        print("the answer is",self.c)
sinc=devil()
sinc.king()
sinc.rose()
sinc.dose()
