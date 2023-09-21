class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
emp_1 = Employee("Tom", "Cruz", 2000000)
emp_2 = Employee("Tim", "Lee", 400000)

print(Employee.raise_amt)
