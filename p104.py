from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 50000

class Developer(Employee):
    def salary(self):
        return 40000

class Clerk(Employee):
    def salary(self):
        return 25000

e1 = Manager()
e2 = Developer()
e3 = Clerk()

print("Manager Salary:", e1.salary())
print("Developer Salary:", e2.salary())
print("Clerk Salary:", e3.salary())