#ex32
the_count = [1 , 2 , 3 , 4 , 5 , 6]
fruits = ['apples' , 'oranges' , 'pears' , 'dimes']
mixed = [1 , 'apples' , 2 , 'oranges' , 3 , 'pears']
all_together =[]

for number in the_count:
    print(number)
    all_together.append(number)
#this for was just for numbers

for fruit in fruits:
    print(fruit)
    all_together.append(fruit)
#this for was just for strings

for x in mixed:
    print(f'this is mixed one ... {x}')
    all_together.append(x)

for element in all_together:
    print(f'this an element ... {element}')
