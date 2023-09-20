#  OOP in Python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last
emp_1 = Employee("Tom", "Cruz", 90000)
emp_2 = Employee("Michael","Jordan", 100000)
print(emp_1.fullname())
print(Employee.fullname(emp_2))
print(emp_1.email)
