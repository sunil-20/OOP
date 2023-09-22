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
    # def __str__(self):
    #     pass
# calling the method


emp_1 = Employee("Tom", "Cruz", 20000)
emp_2 = Employee("Jackie", "Chen", 30000)

print(emp_1)
# repr(emp_1) # printing employee instance whithout object info..
# str(emp_1)