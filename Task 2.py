# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

arr= input("Введите число ")
list=arr
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)