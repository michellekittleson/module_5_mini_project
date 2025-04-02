# Notes from Video "Python OOP Tutorial 1: Classes and Instances" https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee: # Class is a blueprint
    def __init__(self, first, last, pay): # constructor/initializer
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Shafer', 50000) # Instances of the Class
emp_2 = Employee('Test', 'User', 60000)

Employee.fullname(emp_1) # These two lines do the same thing
emp_1.fullname()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_2.last = 'Schafer'
# emp_1.email = 'Corey.Shafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())