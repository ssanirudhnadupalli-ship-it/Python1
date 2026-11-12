from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL Database")

class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB Database")

class Oracle(Database):
    def connect(self):
        print("Connected to Oracle Database")

d1 = MySQL()
d2 = MongoDB()
d3 = Oracle()

d1.connect()
d2.connect()
d3.connect()