# Объяви переменные: a = 5, b = "10". Выведи их типы (type()).
a = 5
b = "10"

print(type(a))
print (type(b))

# Преобразуй b в число и выведи сумму a + int(b).

b = int(b)
print(a + b)

# Создай список lst = [1,2,3]. Добавь элемент 4 и выведи lst.

lst = [1,2,3]
lst.append(4)
print(lst)

# Создай словарь user = {"id": 1, "name": "Alex"}. Выведи значение по ключу "name".

user = {"id": 1, "name": "Alex"}
print(user["name"])