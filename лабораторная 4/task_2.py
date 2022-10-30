def get_count_char(str_):
    letters = str_.lower()  # Перевод в строчные буквы для точного подсчета
    dictionary = {}  # Создание словаря
    for i in letters:  # Цикл для подсчета букв
        if i.isalpha():  # Цикл работает только с буквами, без символов и знаков
            if i in dictionary.keys():  # Если буква в ключах словаря
                count = dictionary[i]  # Присваивание
                count += 1  # Увеличение номера
                dictionary[i] = count  # Перезапись
            else:    # Если условие не соблюдается
                dictionary[i] = 1  # Значение не меняется
    return dictionary  # Возврат итогового словаря


def get_percent_correlation(str_):
    cor = get_count_char(str_)  # Вызов предыдущей функции для нахождения количества всех букв
    summary = sum(cor.values())  # Сумма всех значений из словаря
    for key in cor:  # Цикл
        cor[key] /= summary  # нахождение отношения
        cor[key] *= 100  # перевод в проценты
        cor[key] = round(cor[key])  # округление до целого до знака перед запятой
    return cor  # Возврат словаря


main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список 
        отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join.
        Приступим!!!!
    """

print(get_count_char(main_str))  # Вывод словаря "Буква" - "Количество"
# print(get_percent_correlation(main_str))  # Вывод словаря "Буква" - "Процентное соотношение (данная буква/все буквы)"
