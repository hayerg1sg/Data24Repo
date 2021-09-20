def greeting(name: str, age: int):
    print(f"hello {name}")

greeting("gav")


def additon(int1, int2):
    return int1 + int2

print(additon(2, 3))

def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)
multi_args()