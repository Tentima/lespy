# Новая тема
# Тернарный оператор
# Генератор списков
n = -1
if n >= 0:
    print("Положительное")
else:
    print("Отрицательное")
##########################
print('больше нуля' if n>=0 else 'меньше нуля')
#################### обычный код
age = 20
if age >=18:
    starus ='взрослый'
else:
    status ='несовершеннолетний'
########################
status = 'взрослый' if age >= 18 else 'несовершеннолетний'
print(status)
################### внутри функции
def grade(score):
    return 'Отлично' if score >= 90 else 'Хорошо' if score >= 75 else 'Удовлетворенно' if score >= 60 else 'Двойка'
print(grade(79))
######################
numbers = [-2, -1, 0, 1, 2]
sin = ['положительное' if n>0 else 'Отрицательное' if n<0 else 'Ноль'for n in numbers]
print(sin)
#########################
temperature = -5
print(f"На улице {'тепло' if temperature > 0 else 'холодно'}")

# Генератор списков
numbers = [i for i in range(1,100)]
print(numbers)
##############
numbers2 = []
for i in range(1,100):
    numbers2.append(i)
    print(numbers2)
#########################
num_chet = [i for i in range(1,100) if i % 2 ==0]
print(num_chet)
##############################
num_sp = [i**2 for i in range(1,7)]
print(num_sp)
##################
sign = ['положительное' if x > 0 else 'отрицательное' if x<0 else 'Ноль' for x in [-2, -1, 0, 1, 2]]
print(sign)
#########################
words = ['python', 'django', 'ai']
lengths = [len(word) for word in words]
print(lengths)
##########################


# Задача: "Банковский счет"
# Функционал:
# 1. Проверить баланс
# 2. Пополнить
# 3. Снять
# 4. Выход из программы
balance = 0

def get_balance():
    return balance

def deposit(amount):
    global balance
    if amount >0:
        balance+=amount
        print(f"Пополнение на {amount} сом. Новый баланс: {balance}")
    else:
        print("Ошибка. Должно быть выше нуля")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Ошибка. Должно быть выше нуля")
    elif amount > balance:
        print("Недостаточно средств")
    else:
        balance -= amount
        print(f"Сняли {amount} Осталось: {balance}")

while True:
    print("""
    1. Проверить баланс
    2. Пополнить
    3. Снять
    4. Выход из программы""")
    choice = int(input("Выберите действие: "))
    if choice == 1:
        print(f"Баланс: {get_balance()}")
    elif choice == 2:
        deposit(float(input("Введите сумму: ")))
    elif choice == 3:
        withdraw(float(input("Введите сумму: ")))
    elif choice == 4:
        break
    else:
        print("Неверный ввод")
        continue
