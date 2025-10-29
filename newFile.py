# import math as mt

# num1 = 5.0
# num2 = round(num1)
# num5 = mt.radians(90)
# num7 = mt.pow(3, 2)
# num8 = mt.sqrt(25)

# print(num7)

# exit()



# print(max(3, 4, 5, 7, 9))
# print(min(1, 4, 5, 6, -7))

def c_to_f(c) :
    return round(((c * 9 / 5) + 32), 1)
def f_to_c(f) :
    return round(((f - 32) * 5 / 9), 1)

answ = input('В какой шкале вы хотите ввести температуру: Цельсия или Фаренгейта? ')
if answ == "Цельсия":
   c = float(input('Введите температуру в Цельсиях '))
   print(f"Конвертирование температуры из шкалы {answ} в {c} градусов приравнивается к {c_to_f(c)} градусам Фаренгейта")

elif answ == "Фаренгейта":
    f = float(input('Введите температуру в Фаренгейтах '))
    print(f"Конвертирование температуры из шкалы {answ} в {f} градусов приравнивается к {f_to_c(f)} градусам Цельсия")

else:
    print("Шкала не распознана")