'''
7.
а) Дан текстовий файл f. Переписати у файл g всі рядки з вихідного файлу. Порядок
рядків замінити на зворотній.
Виконала Новіцька В.І. 122Б
'''
import random

with open('f_task_a.txt', 'w+') as f:
    count = 0
    sample = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'duis', 'aute', 'reprehenderit', 'excepteur', 'fint', 'occaecat']
    while count < 5:  # згенеруємо 5 рядків, в кожному по одному по 5 слів у рандомному порядку
        count += 1
        f.write(' '.join((random.choices(sample, k = 5))) + '\n')
        # об'єднаємо у строку за допомогою методу join(), оскільки функція random.choices() повертає список

with open('f_task_a.txt', 'r') as f, open('g_task_a.txt', 'w') as g:
    f_rev = f.readlines()  # у змінну запишемо всі рядки файлу
    print(f'Lines: \n{f_rev}')
    f_rev.reverse()  # розташуємо рядки у зворотньому порядку
    print(f'Lines reversed: \n{f_rev}')
    for line in f_rev:
        g.write(str(line))