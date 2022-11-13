import random


def get_unique_list_numbers() -> list[int]:
    elements = [x for x in range(-10, 10)]  # Создаем строку с элементами от -10 до 10
    roster = random.sample(elements, 15)  # Создаем случайную последовательность из созданных элементов

    return roster


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
