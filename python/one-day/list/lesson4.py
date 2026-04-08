# Создайте список numbers с пятью произвольными числами.
# Выведите третий элемент списка numbers.
# Добавьте число 10 в конец списка numbers.
# Удалите второй элемент из списка numbers и выведите список.

#numbers = [1, 2, 3, 4, 5]
# print(numbers[2])
# numbers.append(10)
# del numbers[1]
# print(numbers)

# Создайте список fruits с тремя названиями фруктов.
# Объедините списки numbers и fruits в один новый список combined.
# Проверьте, сколько элементов находится в списке combined.
# Выведите последний элемент списка combined.
# Создайте срез списка combined, который включает в себя элементы со второго по четвертый (включительно).

# numbers = [1, 2, 3, 4, 5]
# fruits = ["apple", "manga", "lemon"]
# combined = numbers + fruits
# print(len(combined))
# print(combined[-1])
# combined = combined[1:5]
# print(combined)

# Создайте копию списка combined с помощью среза и присвойте его переменной combined_copy.
# Поменяйте значение первого элемента списка combined_copy на "яблоко".
# Выведите исходный список combined и список combined_copy после изменения.

combined = ["apple", "manga", "lemon"]
combined_copy = combined[:]
combined_copy[0] = "яблоко"
print(combined)
print(combined_copy)