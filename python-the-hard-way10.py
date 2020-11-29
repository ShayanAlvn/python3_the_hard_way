#ex39
numbers ={'one' : '1','two' : '2','three' : '3','four' : '4'}
numbers['five'] = '5'

print("I can count up to 5 ... \n 1 , 2 , 3, 4 , ",numbers['five'])

for num , i in numbers.items():
    print(f"string {num} ...and...int {i} ")

get_number = numbers.get('six' , '*i am sorry we do not have it...*')
print("for 'six' our output is : ",get_number)