def bubble_sort(arr):
    n = len(arr)
    # Проходим по массиву
    for i in range(n):
        # Сравниваем соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами, если порядок неверный
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Отсортированный массив:", sorted_numbers)