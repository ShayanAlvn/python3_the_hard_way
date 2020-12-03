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
   
    @classmethod 
    def set_raise_amt(cls , amount):#in classmethod cls is like self in other defs
        cls.amount_of_raise = amount #we can change all employees amount_of_raise by "Emplotee.set_raise_amt(x)" 'just another way to do that'

    @classmethod
    def from_string(cls , emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first , last , pay)

    @staticmethod # we will use staticmethod whenever we don't want to have acces to any of class vars
    def is_workday(day):# in this method we don't have any self or cls as first input
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
  
class Developer(Employee):
    amount_of_raise = 1.10

    def __init__(self , first , last , pay , prog_lang):
        super().__init__(first , last , pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self , first , last , pay , employees=None):
        super().__init__(first , last , pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self , emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self , emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->',emp)

emp_1 = Employee('corey' , 'Schafer' , 10000)
emp_2 = Employee('tomas' , 'muller' , 20000)

# print(emp_1.__dict__)
# emp_1.amount_of_raise = 1.05 #only changing raise amount of emp_1
# #I could change all employees raise amount with "Employee.amount_of_raise = 1.05"
# emp_1.apply_reise()
# emp_2.apply_reise()
# print(emp_1.pay)
# print(emp_2.pay)
# print(Employee.num_of_emps)

# #creating another emp by string var manual
# emp_string_1 = 'John-doe-70000'
# emp_string_2 = 'Steve-smith-30000'
# emp_string_3 = 'mr-hello-50000'

# first , last , pay = emp_string_1.split('-')
# emp_3 = Employee(first , last , pay)
# print(emp_3.__dict__)

# #now i am going to create another emp by using a @classmethod's def 
# emp_4 = Employee.from_string(emp_string_2)
# print(emp_4.__dict__)

# # i am going to use @staticmethod 
# import datetime
# my_date = datetime.date(2020 , 4 , 10)

# print(Employee.is_workday(my_date))

#now i am going to use inheritance
emp_d1 = Developer('cristiano' , 'ronaldo' , 90000 , 'python')
print(emp_d1.email)
print(emp_d1.pay)
emp_d1.apply_reise()
print(emp_d1.pay)
print(emp_d1.prog_lang)
