'''
7.
б) Дан файл f, компоненти якого є цілими числами. Знайти кількість парних та
кількість двозначних чисел серед компонентів файлу. Результат вивести на екран.
Виконала Новіцька В.І. 122Б
'''
import random

with open('task_b.txt', 'w+') as f:
    count = 0
    while count < 10:  # згенеруємо 10 чисел
        count += 1
        f.write(str(random.randint(1,500)) + '\n')

with open('task_b.txt', 'r+') as f:
    num = []
    print(f'File contains:')
    for line in f:
        print(line)
        if (int(line) % 2 == 0) and (len(line) == 3):
            # якщо остача від ділення числа на 2 = 0, то число парне, і, якщо довжина рядка 3 (2 цифри і знак переносу
            # на новий рядок), то записуємо його до змінної num.
            num.append(line)
    print(f'Even numbers with two digits: {num}\nNumber of even numbers with two digits: {len(num)}')