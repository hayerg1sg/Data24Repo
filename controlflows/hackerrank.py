# n=input("please enter a number ")
# while not n.isnumeric() or (int(n)<1 or int(n)>100):
#     n=input("please enter a number ")
# n = int(n)
#
# if n % 2 != 0:
#     print("weird1")
# else:
#     if n >=2 and n<=5:
#         print("not weird 2")
#     elif n>=6 and n<=20:
#         print("weird3")
#     else:
#         print("not weird4")
n = input("enter a number")
n = int(n)

while n>0:
    n -=1
    print(n*n)



