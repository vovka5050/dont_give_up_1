import random


def guess_number():
    secret = random.randint(1, 100)
    attempts = 0
    print("Угадайте число от 1 до 100!")

    while True:
        guess = int(input("Ваш ход: "))
        attempts += 1
        if guess < secret:
            print("Слишком мало!")
        elif guess > secret:
            print("Слишком много!")
        else:
            print(f"Поздравляем! Вы угадали число {secret} за {attempts} попыток!")
            break


guess_number()