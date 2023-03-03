'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий 
набор натуральных чисел. У пользователя необходимо запрашивать новый 
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми 
значениями, то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, 
my_list = [7, 5, 3, 3, 2].
'''
rate = [7, 5, 3, 3, 2]
new_rate = int(input('Введите элемент рейтинга (натуральное число): '))
inserted = False
print(f'Исходный список: {rate}')

for i, el in enumerate(rate):
    if el < new_rate:
        rate.insert(i, new_rate)
        print(f'Новый элемент {new_rate} вставили на {i} позицию: {rate}')
        inserted = True
        break

if not inserted:
    rate.append(new_rate)
    print(f'Новый элемент {new_rate} добавили в конец списка: {rate}')
