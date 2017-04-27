my_variable = "hello"

#print(my_variable[0])

for character in my_variable: #itarables are strings, lists, sets, tuples, and more
    print(character)

user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = input("Should we print again? (y/n) ")
    if user_input =='n':
        user_wants_number = False
