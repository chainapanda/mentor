#Написать функцию которая на вход принимает 3 числа,
# сортирует их и выводит отсортированный список
# (сортировать надо по убыванию).

def data ():
    data = list(map(int, input('Введите числа через пробел ').split()))
    a = sorted(data, reverse = True)
    print(a)

data()

#у меня получилось на ввод не три числа