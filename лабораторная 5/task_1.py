# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
copy = []  # Создание пустого списка
for i in range(0, 16):  # Задаем отрезок чисел
    dictionary = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}  # Система исчисления - значение в этой системе
    copy.append(dictionary)  # Позволяет склеить все словари в список

pprint(copy)
