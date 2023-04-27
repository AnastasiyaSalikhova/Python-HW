# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
# items = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# x = 0
# def nearest_value(items, x):
#     found = items[0]
#     for item in items:
#         if abs(item - x) < abs(found - x):
#             found = item
#     return found

# print(f'Ближайшее число к {x} в списке {items} является {nearest_value(items, x)}')
N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a:abs(a-x)))