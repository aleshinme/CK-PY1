import random


def get_random_password() -> str:

    elements = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"  # Ввод строки доступных символов
    password = random.sample(elements, 12)  # C помощью функции выбирается 12 случайных символов из строки доступных
    c = (''.join(map(str, password)))  # C помощью функции символы объединяются в одну строку
    return c


print(get_random_password())
print(get_random_password())
