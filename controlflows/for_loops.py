list_data = [1, 2, 3, 4, 5]

for num in list_data:
    print(num* 2)
    print("-----" + str(num))

embedded_lists = [[1, 2, 3], [4, 5, 6]]
for data in embedded_lists:
    for num in data:
        print(num)

dict_data= {1:{"name": "gav", "age": "20"}, 2: {"name": "boo", "age": "299"} }
# for key in dict_data:
#     print(key)
for dictionary in dict_data.values():
    for value in dictionary.values():
        print(value)

# for dictionary in dict_data.values():
#     print(dictionary["name"])
# for value in dict_data.values():
#     print(value)

# for key in dict_data:
#     print(dict_data[key])


list_data = [1, 2, 3, 4, 5, 6, 7]
for num in list_data:
    # if num ==3:
    #     print("i found 3")
    # elif num > 3:
    #     print("too far")
    # else:
    #     print("too soon")
    if num % 3 == 0:
        print(num)

        
