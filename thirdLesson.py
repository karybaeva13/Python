'''list1 = ["winter", "spring", "summer", 8, 20, 5, "bananas", "apples"]
print(f"Yesterday I came to buy some {list1[7]} and haven't found any for {list1[4]} dollars sale")
answer = input(f"What else were you looking for? {list1[6]} or {list1[7]}? ")
if answer := list1:
    print("Yes, you can buy it here")
'''
    
# price = int(input('Enter price'))
# print('Change is', 500-price)

'''num1 = 2
num2 = 3
num1 = int(num1) + int(num2)
print(f"Сумма двух чисел равна {num1}")
'''

'''s = "sublime"
print("s[0], s[-1] =>", s[0], s[-1])
print("s[1:4] =>", s[1:4])
print("s[-4:] =>", s[-4:])
print('replace:', s.replace("li", "te"))
print("повтор:", "la " * 3)'''

s = "sublime
try:
    s[0] = "S"
except TypeError as e:
    print("Нельзя изменить символ по индексу:", e)