def delete(list_, index=None):
    if index is None:  # Задаем условие, если значение индекса не указано
        return list_[:len(list_) - 1]  # Возваращем  список при данном условии и удаляем последний символ
    else:
        return list_[:index] + list_[index + 1:]  # Значение индекса указано, удаляем элемент


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
