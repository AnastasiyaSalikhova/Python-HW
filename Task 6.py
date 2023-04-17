# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер билета "))
if(n > 99999) and( n < 1000000):
    n1 = n // 100000
    n2 = (n - n1 * 100000) // 10000
    n3 = (n - n1 * 100000 - n2 * 10000) // 1000
    n4 = (n - n1 * 100000 - n2 * 10000 - n3 * 1000) // 100
    n5 = (n - n1 * 100000 - n2 * 10000 - n3 * 1000 - n4 * 100) // 10
    n6 = (n - n1 * 100000 - n2 * 10000 - n3 * 1000 - n4 * 100) % 10
    s1 = n1 + n2 + n3
    s2 = n4 + n5 + n6
    if s1 == s2:
        print (f"Это счастливы билет! ")
    else:
        print(f"Не повезло :(")
else:
    print(f"Не правильно ввели номер билета ")        