name = input("Введите своё имя: ")

if len(name) < 5:
    surname = input("Введите фамилию: ")
    print(name + surname)
    print(name.upper())
elif len(name) > 5:
    print(name.lower())
