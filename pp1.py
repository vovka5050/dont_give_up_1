import random
import string

def generate_password(length=12):
    # Определяем набор символов
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Генерируем и выводим 3 пароля
for _ in range(3):
    print(f"Сгенерированный пароль: {generate_password()}")