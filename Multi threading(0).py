from time import sleep
from threading import*
class arun(Thread):
    def run(self):
        for a in range(5):
            print("hiiii")
            sleep(4)
class kumar(Thread):
    def run (self):
        for a in range(7):
            print("hlo")
            sleep(8)
t1=arun()
t2=kumar()
t1.start()
t2.start()
print("asdf")
