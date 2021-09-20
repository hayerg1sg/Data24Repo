user_input = True

while user_input:
    age = input("how old are you?")
    if age.isnumeric() :
        if age <117:
            user_input = False
