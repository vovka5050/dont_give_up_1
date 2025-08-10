def is_palindrome(text):
    # Приводим к нижнему регистру и убираем пробелы
    cleaned_text = text.lower().replace(" ", "")
    # Проверяем, является ли строка палиндромом
    return cleaned_text == cleaned_text[::-1]

# Тестируем несколько строк
test_strings = ["радар", "привет", "А роза упала на лапу Азора"]
for s in test_strings:
    result = "палиндром" if is_palindrome(s) else "не палиндром"
    print(f"Строка '{s}' — {result}")