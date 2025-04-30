from abc import ABC
class DBInterface(ABC):
    def connect(self):
        pass
    def disconnect(self):
        pass
class oracle(DBInterface):
    def connect(self):
        print("connecting to oracle data base...")
    def disconnect(self):
        print("disconnecting to prale data base....")
class sybase(DBInterface):
    def connect(self):
        print("connecting to sybase database...")
    def disconnect(self):
        print("disconnecting to sybase data base....")
x=DBInterface()
x.connect()
x.disconnect()
        
    
