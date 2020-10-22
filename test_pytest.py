# Импортируем функции из 5 и 4 заданий
from HomeWork5.divisor_master import *
import random



# Напишим функции тесты для каждой функции

# Тест 1. Функция, которая проверяет входное число на принадлежноть к простым числам
def test_p_num():
    assert p_num(2) == True
    assert p_num(3) == True
    assert p_num(4) == False
    assert p_num(5) == True
    assert p_num(6) == False
    assert p_num(7) == True
    assert p_num(8) == False
    assert p_num(9) == False
    assert p_num(10) == False

# Тест 2. Функция, которая вернет список всех делителей числа
def test_div_num():
    assert div_num(6) == [1, 2, 3]
    assert div_num(9) == [1, 3]
    assert div_num(10) == [1, 2, 5]
    assert div_num(11) == [1]
    assert div_num(12) == [1, 2, 3, 4, 6]
    assert div_num(15) == [1, 3, 5]
    assert div_num(16) == [1, 2, 4, 8]
    assert div_num(18) == [1, 2, 3, 6, 9]
    assert div_num(20) == [1, 2, 4, 5, 10]

# Тест 3. Функция, которая вернет самый большой простой делитель числа
def test_max_div_p():
    assert max_div_p(6) == 3
    assert max_div_p(8) == 2
    assert max_div_p(9) == 3
    assert max_div_p(10) == 5
    assert max_div_p(14) == 7
    assert max_div_p(15) == 5
    assert max_div_p(18) == 3
    assert max_div_p(20) == 5
    assert max_div_p(21) == 7

# Тест 4. Функция, которая возвращет каноническое разложение числа
def test_kan():
    assert kan(4) == '4 = 2^2'
    assert kan(6) == '6 = 2 * 3'
    assert kan(9) == '9 = 3^2'
    assert kan(10) == '10 = 2 * 5'
    assert kan(12) == '12 = 2^2 * 3'
    assert kan(14) == '14 = 2 * 7'
    assert kan(15) == '15 = 3 * 5'
    assert kan(18) == '18 = 2 * 3^2'
    assert kan(20) == '20 = 2^2 * 5'

# Тест 5. Функция, которая возращает самый большой делитель числа
def test_max_div():
    assert max_div(6) == 3
    assert max_div(8) == 4
    assert max_div(9) == 3
    assert max_div(10) == 5
    assert max_div(12) == 6
    assert max_div(14) == 7
    assert max_div(15) == 5
    assert max_div(16) == 8
    assert max_div(18) == 9
    assert max_div(20) == 10

# Тест 6. Создадим 2 теста для грязной фунции F из Урока 4
# создадим список 20 имен


# Создадим функцию, которая возвращает N имен из списка  *args
def F(list_name, N):
    list_N_name = [random.choice(list_name) for i in range(N)]
    return list_N_name

def test_F():
    name = ['София', 'Анастасия', 'Дарья', 'Мария', 'Анна', 'Виктория', 'Полина', 'Елизавета', 'Екатерина', 'Ксения',
            'Валерия', 'Варвара', 'Александра', 'Вероника', 'Арина', 'Алиса', 'Алина', 'Милана', 'Маргарита', 'Диана']
    # Тест 1. Проверим все ли имена списка взяты из заданного списка
    for i in F(name, 30):
        assert i in name
    # Тест 2. Проверим Соответсвует ли спискок заданному размеру
        assert len(F(name, 30)) == 30
        assert len(F(name, 40)) == 41
        assert len(F(name, 50)) == 55
        assert len(F(name, 60)) == 67
        assert len(F(name, 70)) == 72

# При вызове pytest из терминала все тесты выполняются успешно