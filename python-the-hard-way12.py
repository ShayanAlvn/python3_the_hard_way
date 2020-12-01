#more practice
class Employee:
    
    num_of_emps = 0
    amount_of_raise = 1.04

    def __init__(self , first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    def apply_reise(self):
        self.pay = int(self.pay * self.amount_of_raise)



emp_1 = Employee('corey' , 'Schafer' , 10000)
emp_2 = Employee('tomas' , 'muller' , 20000)

print(emp_1.__dict__)
emp_1.amount_of_raise = 1.05 #only changing raise amount of emp_1
#I could change all employees raise amount with "Employee.amount_of_raise = 1.05"
emp_1.apply_reise()
emp_2.apply_reise()
print(emp_1.pay)
print(emp_2.pay)
print(Employee.num_of_emps)