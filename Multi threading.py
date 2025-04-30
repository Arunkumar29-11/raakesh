from time import sleep
from threading import*
class thala(Thread):
    def run(self):
        for v in range(4):
            print("thala na tamil nadu la ajith paru")
            sleep(50)
class thalapathi(Thread):
    def run(self):
        for j in range(3):
            print("thalapathi na tamilnadu la vijay paru")
            sleep(9)
t1 = thala()
t2 = thalapathi()
t1.start()
t2.start()
print("hiphop tamilza")
