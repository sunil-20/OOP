# Property decorators getter, setter as in Java
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    # new method created and remove the email attribute from init fx
    # add property decorator
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
emp_1  = Employee("John", "Smith")
#changing the first name doesn't change the email address. as John.Smith@company.com
# so, make a separate property decorator which allows to access method as attributes.
emp_1.first = "Jack"

print(emp_1.first)
# email method call needs parenthesis as follows
print(emp_1.email())
print(emp_1.email) # after adding @property decorator not need to specify as email()
print(emp_1.fullname) # access as an attribute