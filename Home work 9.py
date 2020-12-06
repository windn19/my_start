# Не знаком с игрой "Дурак"
# Попробую создать игру "Покер"

# Подключаю необходимые библиотеки
import random
import re
from copy import copy



####################################                                    ####################################
###############################      Техаский покер против "Компьютера"      ###############################
####################################                                    ####################################

# Создадим карту
class Card():

    # Перечислим возможные масти и значения карт
    # list_values = ['Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    # list_suits = ['spades', 'hearts', 'diamonds', 'clubs']
    list_values = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка',
                   'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз']
    list_suits = ['пик', 'червей', 'бубен', 'треф']

    # Назначим случайные атрибуты при создании карты либо заданные
    def __init__(self, value = 'random', suit = 'random'):

        # Добавим атрибуты карты
        self.value = value
        self.suit = suit

        # Добавим возможность задавать артрибуты цифрами
        if type(self.value) == int:
            self.value = Card.list_values[self.value]
        if self.value == 'random':
            self.value = random.choice(Card.list_values)
        if type(self.suit) == int:
            self.suit = Card.list_suits[self.suit]
        if self.suit == 'random':
            self.suit = random.choice(Card.list_suits)



    # Отформатируем вывод карты
    def __str__(self):
        # return '{} of {}'.format(self.value, self.suit)
        return '{} {}'.format(self.value, self.suit)

    # Отформатируем представление объекта
    def __repr__(self):
        return '{} {}'.format(self.value, self.suit)

    # Определим условия равентсва обектов
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    # Определим условия сравнения объектов
    def __lt__(self, other):
        return Card.list_values.index(self.value) < Card.list_values.index(other.value)

    def __le__(self, other):
        return Card.list_values.index(self.value) <= Card.list_values.index(other.value)

    # Добавим возможность задания атрибутов
    def addAttribute(self, value, suit):
        if type(value) == int:
            value = Card.list_values[value]
        if type(suit) == int:
            suit = Card.list_suits[suit]

        self.value = value
        self.suit = suit


# Создадим колоду
class Deck:

    # Создадим саму колоду
    deck = []

    # Наполним каолоду картами
    def __init__(self):
        Deck.deck = [Card(val, suit) for suit in Card.list_suits for val in Card.list_values]

    # Добавим возможность перетасовать карту
    def shuffle(self):
        Deck.deck = random.sample(Deck.deck, len(Deck.deck))

    # Вытаскиваем карту из колоды
    def pick(self):
        return Deck.deck.pop()


# Создадим игрока
class Player:

    # Зададим атрибуты игрока
    def __init__(self, name = 'Unknow', hand = [], points = 0):
        self.name = name
        self.hand = hand
        self.points = points

    # Форматируем вывод игрока
    def __str__(self):
        return 'Player {}'.format(self.name)

    # Добавим возможность перименовать
    def rename(self, name):
        self.name = name

    # Добавить карту в руку
    def add_card(self, card):
        self.hand.append(card)

    # Добавить поинты
    def add_point(self, points):
        self.points += points


# Создадим противника  - The set of simple algorithms (набор нехитрых алгоритмов)
class SetSimpleAlgorithms:

    name = 'SSA'

    def __init__(self, hand = [], points = 0):

        self.hand = hand
        self.points = points

    # Форматируем вывод игрока
    def __str__(self):
        return 'Player {}'.format(SetSimpleAlgorithms.name)

    # Добавим поинты
    def add_point(self, points):
        self.points += points

    # Добавить карту в руку
    def add_card(self, card):
        self.hand.append(card)


# Создадим саму игру
class TexasHoldEm:
    # Генератор очередности хода
    def genrator_turn(self):
        n = 0
        while True:
            if n % 2 == 0:
                yield 'player'
            else:
                yield 'SSA'
            n += 1

    def __init__(self, points = 1000):
        self.deck = Deck()                                 # Добавим колоду
        self.player = Player()                             # Добавим игрока
        self.SSA = SetSimpleAlgorithms()                   # Добавим SSA
        self.table = []                                    # Создадим список карт на столе
        self.bank = 0                                      # Создадим переменную для банка
        # Раздадим поинты
        self.player.add_point(points)                      # Начислим поинты игроку
        self.SSA.add_point(points)                         # Начислим поинты SSA
        self.status = 'ready'                              # Статус игры
        self.gen_turn = TexasHoldEm.genrator_turn(self)    # Герератор очереди хода играков
        self.bet_player = 0                                # Ставка игрока
        self.bet_SSA = 0                                   # Ставка SSA
        self.command_SSA = []                              # Добавим список команд SSA

    # Старт игры
    def start(self):
        # Обновим колоду
        self.deck = Deck()
        self.deck.shuffle()
        # Обновим карты на руках
        self.player.hand = []
        self.SSA.hand = []
        # Раздаем карты участникам
        self.player.add_card(self.deck.pick())
        self.SSA.add_card(self.deck.pick())
        self.player.add_card(self.deck.pick())
        self.SSA.add_card(self.deck.pick())
        # Обновим стол
        self.table = []
        # Выложим 3 карты на стол
        self.table.append(self.deck.pick())
        self.table.append(self.deck.pick())
        self.table.append(self.deck.pick())
        # Изменим статус
        self.status = 'Preflop'

    # Введем функцию для наполнения списка команд SSA в соответствующих пропорциях
    def add_com_SSA(self, f, c, r, ch):
        for i in range(f):
            self.command_SSA.append('fold')
        for i in range(c):
            self.command_SSA.append('call')
        for i in range(r):
            self.command_SSA.append('raise ' + str(i))
        for i in range(ch):
            self.command_SSA.append('check')

    # Декоратор - функция не будет выполнена при статусе игры - финиш
    def skip(func):
        def wrapper(self):
            if self.status != 'fast_finish':
                func(self)
        return wrapper

    # Ход игрока
    @skip
    def action(self):
        # Напечатаем возможные команды
        print('fold - сбросить карты, сдаться\ncall - поддержать ставку соперника')
        print('raise + сумма - поднять ставку на сумму\ncheck - оставить текущую ставку')
        # Просим игрока сделать ход
        command = input('Сделайте ход:')
        # Игрок сдается
        if command == 'fold':
            # Добавим выигрыш SSA
            self.SSA.add_point(self.bank + self.bet_player)
            # Обнулим банк
            self.bank = 0
            self.bet_SSA = 0
            self.bet_player = 0
            # Изменим стату игры
            self.status = 'fast_finish'
            print('Побеждает SSA')

        # Уравниваем ставку
        if command == 'call':
            # Списываем со счета разницу
            self.player.add_point(self.bet_player - self.bet_SSA)
            # Выравниваем ставку
            self.bet_player = copy(self.bet_SSA)

        # Поднимаем ставку
        if 'raise' in command:
            # Вытащим число из команды
            r = int(re.findall('(\d+)', command)[0])
            self.player.add_point(-r)
            # Если ставка игрока меньше ставки SSA сначала их уровняем
            if self.bet_player < self.bet_SSA:
                # Спишим разницу со счета игрока
                self.player.add_point(self.bet_player - self.bet_SSA)
                # Добавим это значение в ставку
                self.bet_player += self.bet_SSA - self.bet_player
            # Увеличим ставку
            self.bet_player += r

    # Ход SSA
    @skip
    def action_SSA(self):
        # Выберем ход SSA рандомно
        command = random.choice(self.command_SSA)
        # Если ставка SSA меньше чем игрока, не позволим ему сделать чек
        if self.bet_SSA < self.bet_player:
            while command == 'check':
                command = random.choice(self.command_SSA)
        # Напечатаем итоговую команду
        print('SSA:', command)
        # Игрок сдается
        if command == 'fold':
            self.player.add_point(self.bank + self.bet_SSA)
            self.bet_SSA = 0
            self.bet_player = 0
            self.bank = 0
            self.status = 'fast_finish'
            print('Побеждает', self.player.name)

        # Уравниваем ставку
        if command == 'call':
            # Списываем разницу со счета
            self.SSA.add_point(self.bet_SSA - self.bet_player)
            # Выравниваием ставку
            self.bet_SSA = copy(self.bet_player)

        # Поднимаем ставку
        if 'raise' in command:
            # Вытащим число из команды
            r = int(re.findall('(\d+)', command)[0])
            # Спишим поинты со счета игрока
            self.SSA.add_point(-r)
            # Если ставка SSA меньше ставки игрока сначала их уровняем (иначе возможно повешение ниже ставки игрока)
            if self.bet_SSA < self.bet_player:
                # Спишим разницу со счета SSA
                self.SSA.add_point(self.bet_SSA - self.bet_player)
                # Добавим это значение в ставку
                self.bet_SSA += self.bet_player - self.bet_SSA
            # Увеличим ставку
            self.bet_SSA += r

    # Завершение тогов
    def bet_end(self):
        # Добавляем ставки в банк
        self.bank += self.bet_SSA + self.bet_player
        # Обнуляем значения ставок играков
        self.bet_SSA = 0
        self.bet_player = 0

    # Проверим наличие комбинаций у игрока или SSA и вернем эквивалент комбинации в цифрах
    def chek_set(self, name):
        if name == self.SSA.name:
            set_list = self.SSA.hand + self.table
        else:
            set_list = self.player.hand + self.table

        # Отсортируем список
        set_list.sort()

        # Проверим на королевский стрит флеш
        # Спискок комбинаций
        royalFlush = [[Card(x, 0) for x in Card.list_values[8:]],
                      [Card(x, 1) for x in Card.list_values[8:]],
                      [Card(x, 2) for x in Card.list_values[8:]],
                      [Card(x, 3) for x in Card.list_values[8:]]]
        # Проверим по списку
        for rf in royalFlush:
            if len([x for x in rf if x in set_list]) == 5:
                print('{}: Роял стрит флеш'.format(name))
                return 90      # Максимальный бал

        # Проверим на стрит флеш
        streetFlush = []
        # Список комбинаций
        for s in Card.list_suits:
            for x in range(9):
                setT = []
                for v in Card.list_values[x: x + 5]:
                    setT.append(Card(v, s))
                streetFlush.append(setT)
        # Проверим по списку
        for sf in streetFlush:
            if len([x for x in sf if x in set_list]) == 5:
                print('{}: Стрит флеш'.format(name))
                return 80 + Card.list_values.index(set_list[-1].value)  # 90 + старшая карта в случае одинаковых комбинаций

        # Вытащим только значения из списка
        set_list_value = [x.value for x in set_list]

        # Проверим на каре
        for v in Card.list_values:
            if set_list_value.count(v) == 4:
                print('{}: Каре'.format(name))
                return 70 + Card.list_values.index(set_list[-1].value)

        # Проверим на фул хаус
        for v1 in Card.list_values:
            for v2 in Card.list_values:
                if v1 != v2:
                    if set_list_value.count(v1) >= 3 and set_list_value.count(v2) >= 2:
                        print('{}: Фул хаус'.format(name))
                        return 60 + Card.list_values.index(set_list[-1].value)

        # Вытащим только масть из списка
        set_list_suit = [x.suit for x in set_list]

        # Провери на флеш
        for s in Card.list_values:
            if set_list_suit.count(s) >= 5:
                print('{}: Флеш'.format(name))
                return 50 + Card.list_values.index(set_list[-1].value)

        # Проверим на стрит
        street = []
        # Список комбинаций
        for x in range(9):
            setT = []
            for v in Card.list_values[x: x + 5]:
                setT.append(v)
            street.append(setT)
        # Проверим значения по списку
        for st in street:
            if len([x for x in st if x in set_list_value]) == 5:
                print('{}: Стрит'.format(name))
                return 40 + Card.list_values.index(set_list[-1].value)  # 50 + старшая карта в случае одинаковых комбинаций

        # Проверим на тройку
        for v in Card.list_values:
            if set_list_value.count(v) == 3:
                print('{}: Тройка'.format(name))
                return 30 + Card.list_values.index(set_list[-1].value)

        # Проверим на две пары
        for v1 in Card.list_values:
            for v2 in Card.list_values:
                if v1 != v2:
                    if set_list_value.count(v1) >= 2 and set_list_value.count(v2) >= 2:
                        print('{}: Две пары'.format(name))
                        return 20 + Card.list_values.index(set_list[-1].value)

        # Проверим на пару
        for v in Card.list_values:
            if set_list_value.count(v) == 2:
                print('{}: Пара'.format(name))
                return 10 + Card.list_values.index(set_list[-1].value)

        # Если комбинаций не найдене вернем просто значение старшей карты
        print('{}: Старшая карта'.format(name))
        return Card.list_values.index(set_list[-1].value)

    # Выведем на печать состояние игры
    def display(self):
        # Создадим словарик с текущими данными
        dict_display = {
            'playername': self.player.name,
            'ssaname': self.SSA.name,
            'playerpoints': self.player.points,
            'ssapoint': self.SSA.points,
            'bank': self.bank,
            'None': '',
            'playerbet': self.bet_player,
            'ssabet': self.bet_SSA,
            'cardplaer1': self.player.hand[0].value + ' ' + self.player.hand[0].suit,
            'cardplaer2': self.player.hand[1].value + ' ' + self.player.hand[1].suit,
            'cardssa1': 'XXXXX',
            'cardssa2': 'XXXXX',
            'cardtable1': self.table[0].value + ' ' + self.table[0].suit,
            'cardtable2': self.table[1].value + ' ' + self.table[1].suit,
            'cardtable3': self.table[2].value + ' ' + self.table[2].suit,
        }
        # Не показываем 4 и 5 карту в первом раунде
        if self.status == 'flop':
            dict_display['cardtable4'] = ''
            dict_display['cardtable5'] = ''
        # Показываем 4 карту во втором раунде
        if self.status == 'turn':
            dict_display['cardtable4'] = self.table[3].value + ' ' + self.table[3].suit
            dict_display['cardtable5'] = ''
        # Показываем 5 карту в третьем раунде
        if self.status == 'river':
            dict_display['cardtable4'] = self.table[3].value + ' ' + self.table[3].suit
            dict_display['cardtable5'] = self.table[4].value + ' ' + self.table[4].suit
        # Карты соперника показываем только в конце
        if self.status == 'finish' or self.status == 'fast_finish':
            # Пытаемся показать карты, если их не существует не выводим
            try:
                dict_display['cardtable4'] = self.table[3].value + ' ' + self.table[3].suit
            except IndexError:
                dict_display['cardtable4'] = ''
            try:
                dict_display['cardtable5'] = self.table[4].value + ' ' + self.table[4].suit
            except IndexError:
                dict_display['cardtable5'] = ''

            dict_display['cardssa1'] = self.SSA.hand[0].value + ' ' + self.table[0].suit
            dict_display['cardssa2'] = self.SSA.hand[1].value + ' ' + self.table[1].suit
        else:
            dict_display['cardssa1'] = 'XXXXX'
            dict_display['cardssa2'] = 'XXXXX'

        print("############################### Texas hold'em #######################################\n \
        \n \
        {d[playername]:30}{d[None]:30}{d[ssaname]:30}\n \
        Points:{d[playerpoints]:4}{d[None]:49}Points:{d[ssapoint]:4}\n \
        Bet:{d[playerbet]:4}{d[None]:52}Bet:{d[ssabet]:4}\n \
        {d[None]:30}Bank: {d[bank]:4}\n \
        \n \
        Cards:{d[None]:24}Table:{d[None]:24}Cards:\n \
        {d[cardplaer1]:30}{d[cardtable1]:30}{d[cardssa1]:30}\n \
        {d[cardplaer2]:30}{d[cardtable2]:30}{d[cardssa2]:30}\n \
        {d[None]:30}{d[cardtable3]:30}{d[None]:30}\n \
        {d[None]:30}{d[cardtable4]:30}{d[None]:30}\n \
        {d[None]:30}{d[cardtable5]:30}{d[None]:30}\n \
        ".format(d = dict_display))

    @skip
    def finish(self):
        self.status = 'finish'
        # Вскрываем карты
        self.display()

        # Считаем результаты
        result_player = self.chek_set(self.player.name)
        result_SSA = self.chek_set(self.SSA.name)
        # Определяем победителя
        if result_SSA > result_player:
            print('Побеждает SSA')
            self.SSA.add_point(self.bank)
        elif result_SSA == result_player:
            print('Ничья')
            self.SSA.add_point(self.bank / 2)
            self.player.add_point(self.bank / 2)
        else:
            print('Побеждает', self.player.name)
            self.player.add_point(self.bank)

        # Обнуляем банк
        self.bank = 0






# Создаем экземпляр игры
game = TexasHoldEm()
# Просим пользователя ввести его имя
game.player.rename(input('Введите свое имя: '))
# Инициализируем начала игры
game.start()
# Задаем пропорции для команд SSA
game.add_com_SSA(2, 35, 35, 28)

# Играем пока не загоним оппонента в минус
while game.player.points > 0 and game.SSA.points > 0:

    # Инициализируем начало игры
    game.start()

    # Определяем чей ход
    turn = next(game.gen_turn)
    print('ход игрока:', turn)

    # Пройдум все раунды циклом
    for round_game in ['flop', 'turn', 'river']:
        # Определяем текущий статус
        game.status = round_game
        print('status:', game.status)

        # Добавим карту во втором и третьем кругах
        if game.status == 'turn' or game.status == 'river':
            game.table.append(game.deck.pick())

        # Выведем текущее состояния игры на экран
        game.display()

        # Если первым ходит SSA
        if turn == 'SSA':
            # Если это первый круг, начинаем с обязательных ставок
            if game.status == 'flop':
                # Начальная ставка
                game.player.add_point(-2)
                game.bet_player = 2
                game.display()
            # Во всех остальных случаях ходим по очереди
            else:
                # Ход SSA
                game.action_SSA()
                game.display()
                # Просим игрока сделать свой ход
                game.action()
                game.display()
            # Если ставки не равны, торгуемся пока не уровняем их
            while game.bet_SSA != game.bet_player:
                # Ход SSA
                game.action_SSA()
                game.display()
                # Просим игрока сделать свой ход
                game.action()
                game.display()
                # Разрываем цикл если статус финиш
                if game.status == 'fast_finish': break
        # Если первым ходит игрок
        else:
            # Если это первый круг, начинаем с обязательных ставок
            if game.status == 'flop':
                # Начальная ставка
                game.SSA.add_point(-2)
                game.bet_SSA = 2
                game.display()
            # Во всех остальных случаях ходим по очереди
            else:
                # Просим игрока сделать свой ход
                game.action()
                game.display()
                # Ход SSA
                game.action_SSA()
                game.display()
            # Если ставки не равны, торгуемся пока не уровняем их
            while game.bet_SSA != game.bet_player:
                # Просим игрока сделать свой ход
                game.action()
                game.display()
                # Ход SSA
                game.action_SSA()
                game.display()
                # Разрываем цикл если статус финиш
                if game.status == 'fast_finish': break
        # Конец торгов
        game.bet_end()
        # Разрываем цикл если статус финиш
        if game.status == 'fast_finish': break

    # Завершаем партию
    game.finish()

    # Выведем текущее состояние игры на экран
    game.display()

'''
Доработать:
Добавить логику работы SSA расчитывая вероятность успеха (хотя это уже совсем другая тема)
Добавить проверку на ошибки при вводе команд пользователя
Добавть возможность All in
Переодичестки очищать консоль


'''