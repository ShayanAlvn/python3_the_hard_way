#ex13 & ex14
from sys import argv
script , user_name , file_name= argv
print(f"hello {user_name} , my name is OO")
prompt = '> '
print("Do you like your life?")
answer = input(prompt)
print("Wow")

#ex15
txt = open(file_name)
print(f"here is your {file_name} : ")
print(txt.read())

#ex16
print(f"i am going to erase the whole {file_name} ...")
target = open(file_name , 'w')
print("truncating the file ...")
target.truncate()
print("now give me three lines to write in it ...")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)

target.write(line2)

target.write(line3)


print("now i am going to close it ...")
target.close()
target1 = open(file_name)
print("let's see the new file : ")
print(target1.read())
