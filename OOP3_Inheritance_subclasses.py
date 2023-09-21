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
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang): # added programming language
        #use first, last and pay from the parent class Employee.
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    # printing the names of the emplyees full name
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())





dev_1 = Developer("John", "Deere", 20000, "Python")
dev_2 = Developer("Michael", "Jordan", 30000, "Java")
mgr_1 = Manager("Sue", "Morgan", 900000, [dev_1])

print(mgr_1.email)
#print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.email)
# #dev_1.apply_raise()
# print(dev_1.prog_lang)