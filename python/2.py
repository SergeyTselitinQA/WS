int_var = 10               # целое число
float_var = 3.14           # не целое (число с плавающей точкой)
str_var = "hello"          # строка
list_var = [1, 2, 3]       # список
tuple_var = (1, 2, 3)      # кортеж
dict_var = {"a": 1, "b": 2}# словарь
set_var = {1, 2, 3}        # множество
bool_var = True            # булево значение
none_var = None            # без значения (None)

# Преобразования, которые работают:
print(int(float_var))        # 3  (отбрасывает дробную часть)
print(float(int_var))        # 10.0
print(str(int_var))          # '10'
print(str(float_var))        # '3.14'

# list() и tuple() принимают итерируемые объекты:
print(list("abc"))           # ['a','b','c']
print(tuple([1,2,3]))        # (1,2,3)

# Преобразовать целое в список — обернуть в список:
print([int_var])             # [10]

# Или превратить число в строку, затем в список символов:
print(list(str(int_var)))    # ['1','0']

# dict() — принимает итерируемый из пар (ключ, значение):
print(dict([("x", 1), ("y", 2)]))  # {'x':1, 'y':2}

# set() из итерируемого:
print(set([1,2,2,3]))        # {1,2,3}

# Преобразования с None:
# Нельзя вызывать none_var(...) — это ошибка.
# int(None) / float(None) вызовет TypeError. Чтобы безопасно проверять:
def safe_int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None

print(safe_int("7"))   # 7
print(safe_int("a"))   # None
print(safe_int(None))  # None
