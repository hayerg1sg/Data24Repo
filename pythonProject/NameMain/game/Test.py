class Test:
    __count = 0

    def __init__(self):
        # type(self).__count += 1
        Test.__count = self.__count2 + 1


    def __del__(self):
        type(self).__count -= 1

    @property
    def count(self):
        return type(self).__count

    @property
    def __count2(self):
        return type(self).__count

x = Test()
print(f"x.count = {x.count}")

x2 = Test()
print(f"\nx2.count = {x2.count}")
print(f"x.count = {x.count}")

x.__count = 9
print(f"\nx.count = {x.count}")
print(f"x2.count = {x2.count}")
print(f"x.__count = {x.__count}")

del x2
print(f"\nx.count = {x.count}")