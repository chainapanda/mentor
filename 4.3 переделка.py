def zx1 ():
    n1, n2 = int(input()), int(input())
    print(n1 - n2)

def zx2 ():
    c = int(input("Введите градусы Цельсия для конвертации в Фаренгейты "))
    print(f'{c} градусов по Цельсию это {int(c * 9 / 5) + 32} градусов по Фаренгейту')

def zx3 ():
    n1, n2 = int(input()), int(input())
    x = n1 - n2
    print(x)
    n3 = int(input())
    x1 = (n3 * x)
    print(x1)
    n4 = int(input())
    x2 = (x1 + n4)
    print(x2)

def proverka (a):
    if a != 1 and a != 2 and a != 3:
        print('Такой функции нет')
    if a == 1:
        zx1()
    if a == 2:
        zx2()
    if a == 3:
        zx3()


proverka(5)