# Property decorators getter, setter as in Java
# https://www.youtube.com/watch?v=jCzT9XFZ5bw
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

        
    # setting deleter
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1  = Employee("John", "Smith")
# cant run the following code need setter
emp_1.fullname = "Jack Ma"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname