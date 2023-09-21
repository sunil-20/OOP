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
    # creating classmethod
    @classmethod 
    # common convention to use cls as self in class
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        #split the string 
        first, last, pay = emp_str_1.split("-")
        return cls(first, last, pay)

# changing the raise amount to 5 % using the class method
Employee.set_raise_amt(1.05)
    
emp_1 = Employee("Tom", "Cruz", 2000000)
emp_2 = Employee("Tim", "Lee", 400000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1) # From_string alternative constructor
print(new_emp_1.email)
print(new_emp_1.pay)



# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

