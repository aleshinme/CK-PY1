list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

Max = max(list_numbers)
Last = list_numbers[-1]
Item = Max
index = list_numbers.index(Item)
list_numbers[-1] = Max
list_numbers[9] = Last
print(list_numbers)
