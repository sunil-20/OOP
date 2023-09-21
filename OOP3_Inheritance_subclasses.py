# inheritance and creating sub classes.
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)
        #return self.first + " " + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
# inheriting from Employee class
class Developer(Employee):
    pass


dev_1 = Employee("John", "Deere", 20000)
dev_2 = Employee("Michael", "Jordan", 30000)

print(dev_1.first)
print(dev_2.last)
print(dev_1.fullname())