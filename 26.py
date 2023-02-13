# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


def get_pow(number, power):
    return 1 if power == 0 else number * get_pow(number, power - 1)


A = int(input('Введите число: '))
B = int(input('Введите степень: '))
print(get_pow(A, B))
