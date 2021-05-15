class User:
    """Класс для всех пассажиров"""
    user_count = 0
    def __init__(self, name, age, adress, vagon, mesto):
        self.name = name
        self.age = age
        self.adress = adress
        self.vagon = vagon
        self.mesto = mesto
        User.user_count += 1

    def asdf_count(self):
        print('Всего пассажиров: %d' % User.user_count)

    def asdf_user(self):
        print('Имя: {}. Возраст: {}. Адрес: {}. Вагон: {}. Место: {}.'.format(self.name, self.age, self.adress, self.vagon, self.mesto))

user1 = User('Вася', 23,'Чебоксары', 1, 22,)
user2 = User('Маша',19,'Белгород', 3, 54,)
user3 = User('Петя', 24, 'Москва', 1, 13)
user4 = User('Ваня', 23, 'Санкт - Петербург', 2, 39)
user5 = User('Таня', 20, 'Москва', 1, 7)

user1.asdf_user()
user2.asdf_user()
user3.asdf_user()
user4.asdf_user()
user5.asdf_user()

print('Всего пассажиров: %d' % User.user_count)

