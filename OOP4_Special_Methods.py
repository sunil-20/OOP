# Magic Methods double underscore "__" {Dunder}

class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# repr unimbiguous representation of object. used in debugging/ logging, seen by other developers.
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

# str readable representation of object, use as a display to the user.
# it escapes _repr_ method
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)


emp_1 = Employee("Tom", "Cruz", 20000)
emp_2 = Employee("Jackie", "Chen", 30000)

#print(emp_1) # this prints the str method only irrespective of repr

# calling the method specifically to access both
# print(repr(emp_1)) # printing employee instance whithout object info..
# print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

# dunder method for addition int and str objects
print(int.__add__(1,2))
print(str.__add__("a", "b"))