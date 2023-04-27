# 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# 1

def number_array(number, array_numbs):
    numb_occur = 0
    for i in array_numbs:
        if i == number:
            numb_occur += 1
    return numb_occur 
numb_elements = int(input("Введите колличество элементов в массиве: "))
array_numbers = []
for i in range (numb_elements):
    array_numbers.append(int(input(f"Введите число для {i} элемента массива: ")))
number = int(input("Введите число, колличество вхождений мы будем искать в массиве: ")) 
print(f"Колличество вхождений числа {number} в массиве {array_numbers} - {number_array(number, array_numbers)} раз ")       