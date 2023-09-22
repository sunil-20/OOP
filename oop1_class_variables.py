#  OOP in Python https://www.youtube.com/watch?v=BJ-VvGyQxho
# create a class Employee
class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps +=1
    def fullname(self):
        return self.first + " " + self.last
    # OR using .format:  return "{} {}".format(self.first, self.last)

    # create new instance variable which adds the raised amount to original pay.
    def apply_raise(self):
        # self.pay = int(self.pay * 1.04) # without class variable
        self.pay = int(self.pay * self.raise_amount) # with class variable need to specify self or Emplyee in the begining

print(Employee.num_of_emps)
emp_1 = Employee("Tom", "Cruz", 90000)
emp_2 = Employee("Michael","Jordan", 100000)
#print the attributes
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_emps)



print(emp_1.fullname())
print(Employee.fullname(emp_2))
print(emp_1.email)
