#more practice
class Employee:
    def __init__(self , first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first , self.last)


emp_1 = Employee('corey' , 'Schafer' , 10000)
emp_2 = Employee('tomas' , 'muller' , 20000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())