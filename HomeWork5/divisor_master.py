### Home Work 5 ###

### Задание 1 ###

# Создаем функцию, которая проверяет входное число на принадлежноть к простым числам
def p_num(a):
    '''
    :param a: int in range from 2 to 1000
    :return: True if "a" belongs to primes, or False
    '''
    if a == 1: return False
    n = 2
    while a % n != 0:
        n += 1
    return a == n


### задание 2 ###

# Создаем функцию, которая вернет список всех делителей числа
def div_num(a):
    '''
    :param a: int in range from 1 to 1000
    :return: list of all dividers
    '''
    div_list = [i for i in range(1, a) if a % i == 0]
    return div_list


### задание 3 ###

#  Создадим функцию которая вернет самый большой простой делитель числа
def max_div_p(a):
    '''
    :param a: int in range from 1 to 1000
    :return: Largest integer divisor of number
    '''
    i = 2
    div = []
    while a != 1:
        if a % i == 0:
            div.append(i)
            a /= i
        else:
            i += 1
    return max(div)

### задание 4 ###

# Создадим функцию, которая возвращет каноническое разложение числа
def kan(a):
    '''
    :param a: int in range from 1 to 1000
    :return: str - canonical prime factorization
    '''
    b = str(a)                                                      # Сохраняю началено значение в str
    i = 2                                                           # нахожу все простые множители
    div = []
    while a != 1:
        if a % i == 0:
            div.append(i)
            a /= i
        else:
            i += 1
    can = [b + ' = ']                                               # создаю первую часть вывода
    for i in range(len(div)):                                       # проверяю каждый множетель
        if div.count(div[i]) > 1:                                   # если он встречается больше одного раза
            x = str(div[i]) + '^' + str(div.count(div[i])) + ' * '  # считаю сколько раз и возвожу в соответствующую степень
            None if x in can else can.append(x)                     # если такой множетель уже добавлен ничего не делаю
        else:                                                       # если множетель в единственном числе, просто добавляю его
            can.append(str(div[i]) + ' * ')
    can = ''.join(can)[:-3]                                         # формирую единую строку без лишнего знака "*"
    return can


### задание 4 ###

# Создадим функцию, которая возращает самый большой делитель числа
def max_div(a):
    '''
    :param a: int in range from 1 to 1000
    :return: Largest number divider
    '''
    div_list = [i for i in range(1, a) if a % i == 0]
    return max(div_list)


# Проверяем результаты
if __name__ == '__main__':

    # Проверяем работу функции p_nam()
    print(p_num(15), p_num(864), p_num(101))

    # проверяем функцию div_num()
    print(div_num(864))

    # проверяем функцию big_div_p()
    print(max_div_p(864))

    # проверяем функцию kan()
    print(kan(864))

    # проверяем функцию max_div()
    print(max_div(864))