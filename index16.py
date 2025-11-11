import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    attempts += 1
    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print(f"Правильно Число попыток: {attempts}")
        break

