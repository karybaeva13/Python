import math as mt
katet_1 = int(input('Введите длину катета: '))
katet_2 = int(input('Введите длину катета: '))
gip = int(input('Введите длину гипотенузы: '))
min_katet = min(katet_1, katet_2)
if katet_1 ** 2 + katet_2 ** 2 == gip ** 2:
  print(f"Синус наименьшего острого угла: {min_katet/gip}")