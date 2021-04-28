#Пользователь вводит три числа, надо выписать на экран те числа которые делятся без остатка на 2.
# Если ни одно число не делится без остатка на 2, то вывести «Нет таких чисел»
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
    print(n1, n2, n3)
elif n1 % 2 == 0 and n2 % 2 == 0:
    print(n1, n2)
elif n1 % 2 == 0 and n3 % 2 == 0:
    print(n1, n3)
elif n2 % 2 == 0 and n3 % 2 == 0:
    print(n2, n3)
elif n1 % 2 == 0:
    print(n1)
elif n2 % 2 == 0:
    print(n2)
elif n3 % 2 == 0:
    print(n3)
else:
    print('Нет четных чисел')
