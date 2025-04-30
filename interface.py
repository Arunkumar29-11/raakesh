from abc import ABC, abstractmethod
class bank(ABC):
    def balance_check(self):
        pass
    def interest(self):
        pass
class SBI(bank):
    def balance_check(self):
        print("balance is 100 rupess")
    def interest(self):
        print("SBI intrest is 76 ruppes")
s=SBI()
s.balance_check()
s.interest()
            
            
