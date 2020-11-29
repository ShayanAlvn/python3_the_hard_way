#ex38
ten_things = "a b c d e"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["f" , "g" , "h" , "i" , "j" , "k" , "l" , "m"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding : " , next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff)) 
print('#'.join(stuff[3:5])) 