#Задание из пункта 1.1 переписать в виде функции.
# Говоря иначе, надо написать такую функцию,
# которая будет ожидать что пользователь введёт два числа,
# после чего надо будет от первого числа отнять второе и вывести результат.
# Примечание: если будет время, написать два варианта функции.
# Первый – в котором два числа это аргументы функции,
# и второй в котором аргументов функции нет,
# просто внутри функции будет код на чтение чисел которые введёт пользователь.
#вариант №1
def zx ():
    n1 = int(input())
    n2 = int(input())
    x = n1 - n2
    print(x)

zx()

#вариант#2
def zx (n1, n2):
    x = n1 - n2
    print(x)

zx(100, 50)