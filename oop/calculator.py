def addition(int1,int2):
    int1 = input("enter first number ")
    int2 = input("enter second number ")
    print((int(int1) + int(int2)))

addition(1 , 5)

def subtraction(int1,int2):
            int1 = input("enter first number ")
            int2 = input("enter second number ")
            print((int(int1) - int(int2)))

subtraction(1 , 5)

def multiply(int1,int2):
    int1 = input("enter first number ")
    int2 = input("enter second number ")
    print((int(int1) * int(int2)))

multiply(1 , 5)

def multi_addition(*multiargs):
    total = 0
    for arg in multiargs:
        total += arg
    return total