#get() in dict
somethingsfortest = {'color_1' : 'green' , 'color_2' : 'red' , 'color_3' : 'blue'}
print(somethingsfortest.get('color_1' , 'i could not found it'))
print(somethingsfortest.get('color_4' , 'i could not found it'))

#loop in dict
for key , value in somethingsfortest.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

#A List in a Dictionary
favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],}

for name , languages in favorite_languages.items():
    print(name)
    for language in languages:
        print(language)

#a dictionary in dictionary
users = {
'aeinstein': {
'first': 'albert','last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")