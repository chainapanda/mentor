name1 = input('Введите имя первого пассажира ')
vag_name1 = input('Введите номер вагона ')
mesto_name1 = input('Введит номер места в вагоне ')
dict1 = dict()
dict1[name1] = vag_name1, mesto_name1

name2 = input('Введите имя второго пассажира ')
vag_name2 = input('Введите номер вагона ')
mesto_name2 = input('Введит номер места в вагоне ')
dict2 = dict()
dict2[name2] = vag_name2, mesto_name2

name3 = input('Введите имя третьего пассажира ')
vag_name3 = input('Введите номер вагона ')
mesto_name3 = input('Введит номер места в вагоне ')
dict3 = dict()
dict3[name3] = vag_name3, mesto_name3

print(dict1)
print(dict2)
print(dict3)

# также можем добавить данные о последующих билетах данных пассажиров

name = input('Введите имя пассажира ')
vag_name = input('Введите номер вагона ')
mesto_name = input('Введит номер места в вагоне ')

if name == name1:
    dict1 = dict()
    dict1[name1] = (vag_name1, mesto_name1), (vag_name, mesto_name)
    print(dict1)
if name == name2:
    dict2 = dict()
    dict2[name2] = (vag_name2, mesto_name2), (vag_name, mesto_name)
    print(dict2)
if name == name3:
    dict3 = dict()
    dict3[name3] = (vag_name3, mesto_name3), (vag_name, mesto_name)
    print(dict3)

#выведем наши данные в файл
d = dict([(name1, dict1), (name2, dict2), (name3, dict3)])
with open('out.txt','w') as out:
    for key,val in d.items():
        out.write('{}:{}\n'.format(key,val))
