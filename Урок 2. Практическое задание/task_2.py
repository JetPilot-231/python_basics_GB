"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

arr = input('Введите целые числа через пробел: ').split()
i = 0
while i < len(arr) - 1:
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    i = i + 2
    if i == len(arr) - 1:
        break
print(arr)
