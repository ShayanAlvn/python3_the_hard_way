#get() in dict
somethingsfortest = {'color_1' : 'green' , 'color_2' : 'red' , 'color_3' : 'blue'}
print(somethingsfortest.get('color_1' , 'i could not found it'))
print(somethingsfortest.get('color_4' , 'i could not found it'))

#loop in dict
for key , value in somethingsfortest.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")