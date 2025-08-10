def calculator():
    print("Калькулятор (+, -, *, /)")
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            op = input("Введите операцию (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else "Ошибка: деление на 0"
            else:
                result = "Неверная операция"
            print(f"Результат: {result}")
            break
        except ValueError:
            print("Ошибка: введите числа!")


calculator()