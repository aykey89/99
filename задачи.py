name = "Леонид"
age = 17
city = "Люберцы"

print("Меня зовут", name)
print("Мне", age, "лет")
print("Я живу в городе", city)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Сумма чисел:", num1 + num2)
print("Произведение чисел:", num1 * num2)


favorite_color = "синий"
print("Мой любимый цвет:", favorite_color)


mood = input("Какое у вас сегодня настроение? ")
print("Сегодня я чувствую себя", mood)


input_str = input("Введите любую строку: ")
print("Длина строки:", len(input_str))


favorite_number = 7
print("Моё любимое число:", favorite_number)


celsius_temp = float(input("Введите температуру в градусах Цельсия: "))
print("Температура в Цельсиях:", celsius_temp)
fahrenheit_temp = celsius_temp * 9/5 + 32
print("Температура в Фаренгейтах:", fahrenheit_temp)


word = input("Введите любое слово: ")
print(word * 3)


name = "Анна"
print("Имя в верхнем регистре:", name.upper())
print("Имя в нижнем регистре:", name.lower())


number_str = input("Введите число в виде строки: ")
number_int = int(number_str)
print("Введенное число как целое число:", number_int)