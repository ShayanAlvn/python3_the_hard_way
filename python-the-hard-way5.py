#ex20
from sys import argv
script , file_name = argv

def print_all(f):
    print(f.read(),"\n")

def seek_print(f):
    f.seek(0)#the character it should start 
    #if we put 2 inside () it will start from third character

def print_line(f):
    print(f.readline())#every times it prints a line 
    #next time you use it it will move to next line

data = open(file_name)

print_all(data)
seek_print(data)
print_line(data)
print_line(data)

#ex21
def add(a , b):
    return a+b 
def subtract(a , b):
    return a-b
def multiply(a , b):
    return a*b
def devide(a , b):
    return a/b

a1=add(2,3)
a2=subtract(4,2)
a3=multiply(3,4)
a4=devide(6,3)
print(a1,"\n",a2,"\n",a3,"\n",a4)
print(add(a1 , subtract(a2 , multiply(a3 , devide(a4 , 1)))))
#you can use a def as an input for another def