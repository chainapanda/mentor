city = []  # делаем пустой список
s = input()  # вводим первую строку
while s:  # пока введённая строка не пуста:
    if s not in city:  # если строка не в списке:
        city.append(s)  # добавляем её
    s = input()  # принимаем следующую строку

x = sorted(city)
print(x[0 : 2])
