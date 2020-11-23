#ex17
from sys import argv
from os.path import exists # it shows you that a file exists or not 

script , from_file , to_file = argv
print(f"i am going to copy {from_file} to {to_file} are you ok?")
answer = input("> ")
fromfile = open(from_file)
data = fromfile.read()

print(f"the final file is {len(data)} bytes long")
print(f"Does the out file exists? {exists(to_file)}")
print("are you ready?")
input("> ")
out_file = open(to_file, 'w')
out_file.write(data)
print("Done!")
out_file.close()
fromfile.close()

#ex18
def two_input(*args):#*agrs is for functions
    arg1 , arg2 = args
    print(f"first is : {arg1} , second is : {arg2}")

two_input("hi" , "how are you")
      