a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print("Наибольшее число:", a)
elif b > a:
    print("Наибольшее число:", b)
else:
    print("Числа равны")



num =int(input("Введите число: "))

if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")



a = -67
if a > 0:
    print(a)
elif a < 0:
    print(a*-1)


a = input("Введите первое число: ")
b = input("Введите второе число: ")

if a != b:
    print("Yes")
else:
    print("No")

num = float(input("Введите число: "))

if num > 100 or num < -100:
    print("-")
else:
    print("+")