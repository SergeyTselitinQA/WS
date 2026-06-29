str = "Python"

print(str[3])

text = "Python"


# print(text[1:4])   # "yth"  — с индекса 1 до 4 (не включая 4)
# print(text[:3])    # "Pyt"  — с начала до индекса 3
# print(text[3:])    # "hon"  — с индекса 3 до конца
# print(text[:])     # "Python" — вся строка целиком
# print(text[::-1])  # "nohtyP" — вся строка в обратном порядке
# print(text[::2])   # "Pto"  — каждый второй символ
print(text[2:5])
print(text[:2])
print(text[2:])
print(text[:])
print(text[::-1])
print(text[::2])

print(len(text))
print(str + " "  + "язык" + " " + "text")
print(f"Я изучаю {text} c 10 лет!")
print("Всем \"Привет \"")
print(r"'\"Gh")

# upper() и lower() — изменить регистр
# replace() — заменить одно на другое
# split() — разбить строку на список по разделителю
# strip() — убрать лишние пробелы по краям
# startswith() и endswith() — проверить начало и конец

up = "ClasS"
lo = "ping"
print(up.upper())
print(up.lower())
print(lo.upper())
print(lo.lower())

text_replace = "Собака вышла поплавать в бассейне"
print(text_replace.replace("вышла", "выбежала"))
print(text_replace.replace("а", "-"))

roles = "водитель! учитель! врач"
print(roles.split("!"))

email = "   vrvr rvrvr frfrfrvrf      "
print(email.strip())

url = "https://api.example.com/users"

print(url.startswith("https"))
print(url.startswith("users"))
print(url.endswith("users"))
print(url.endswith("https"))

