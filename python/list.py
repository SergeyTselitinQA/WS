# Создание списка

empty_list = []
number = [1, 2, 3, 4, 5]
print(empty_list)
print(number)

# Получение элементов списка

print(number[3])
my_list = [1, 2, 3, ["a", "b", "c"], 4]
print(my_list[3][2])
data = [["row1_col1", "row1_col2"], ["row2_col1", "row2_col2"]]
print(data[0][1])

users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob",   "role": "user"},
]
print(users[1]["name"])