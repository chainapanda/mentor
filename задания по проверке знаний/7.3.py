city1 = 'Moscow'
city2 = 'St. Petersburg'
city3 = 'Ryazan'
city4 = 'Smolensk'
km1 = 706
km2 = 912
km3 = 395

Distance1 = dict()
Distance1[city1, city2] = km1
Distance2 = dict()
Distance2[city2, city3] = km2
Distance3 = dict()
Distance3[city1, city4] = km3

cityX, cityX2 = ((input('Введите города ч/з запятую ').split(",")))
if cityX == city1 and cityX2 == city2:
    print(km1)
elif cityX == city2 and cityX2 == city3:
    print(km2)
elif cityX == city1 and cityX2 == city4:
    print(km3)
else:
    print('НЕТ')
