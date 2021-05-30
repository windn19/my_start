# Home ork 11

# Инициализируем класс Игрока
class Player():

    def __init__(self, name, number, points):
        self.name = name        # Имя игрока
        self.number = number    # Номер игрока
        self. points = points   # Количество очков набраное игроком

    # Изменим формат печати данных об игроке
    def __str__(self):
        return f'Имя игока: {self.name} \nНомер игрока: {self.number} \nКоличество очков: {self. points}'

    # Изменим представления объекта
    def __repr__(self):
        return repr(self.name)

    # Зададим способы сравнивать объекты
    def __eq__(self, other):
        return self.points == other.points

    def __ne__(self, other):
        return self.points != other.points

    def __lt__(self, other):
        return self.points < other.points

    def __gt__(self, other):
        return self.points > other.points

    # Зададим некоторые математические операции
    def __add__(self, other):
        return self.points + other.points

    def __sub__(self, other):
        return self.points - other.points

    def __mul__(self, other):
        return self.points * other.points

    def __pow__(self, n):
        return self.points ** n




if __name__ =='__main__':
    player001 = Player('Василий Петров', 48, 109000)
    player002 = Player('Wonder woman', 36, 567010)

    print('Список игроков', [player001, player002])
    print(player001)
    print()
    print(player002)
    print()
    print(f'player001 == player002 - {player001 == player002}')
    print(f'player001 != player002 - {player001 != player002}')
    print(f'player001 > player002 - {player001 > player002}')
    print(f'player001 < player002 - {player001 < player002}')
    print()
    print(f'player001 + player002 = {player001 + player002}')
    print(f'player001 - player002 = {player001 - player002}')
    print(f'player001 * player002 = {player001 * player002}')
    print(f'player001 ** 3 = {player001 ** 3}')


