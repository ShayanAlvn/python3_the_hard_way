name = "ada lovelace"
print(name.title())#initials Captal
print(name.upper())#all Captal
print(name.lower())#all small
python = ' python '
print(python.rstrip())
print(python.lstrip())
print(python.strip())
number = 14_000_000#python ignore _ in numbers
print(number)
#you can have Multiple Assignment in python 
x , y , z = 10 , 20 , 'hello'
print(f"our variables are:\n\t{x}\n\t{y}\n\t{z}")

#it will write somethings
print('*' *50)
import this


#the diffrence between append() and insert()
num=[12 , 15 , 45 , 63 , 84 , 54]
print(num)
num.append(100)
print(num)
num.insert(2 , 200)
print(num)

del num[3]#it will delete num[3]
print(num)
num.remove(15)#it will remove 15(you should have 15 in your array)
print(num)

popped_num = num.pop(-2)
print(popped_num)
print(popped_num)

num.sort()
print(num)#from less to more or if these are strings they will be in alphabetical order
num.sort(reverse = True)
print(num)
