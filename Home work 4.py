
# Home work 4

### Задание 1 ####

# добавим функцию random
import random

# создадим список 20 имен
name = ['София', 'Анастасия', 'Дарья', 'Мария', 'Анна', 'Виктория', 'Полина', 'Елизавета', 'Екатерина', 'Ксения',
        'Валерия', 'Варвара', 'Александра', 'Вероника', 'Арина', 'Алиса', 'Алина', 'Милана', 'Маргарита', 'Диана']

# Создадим функцию, которая возвращает N имен из списка  *args (надеюсь я правильно понял условия)
def F(list_name, N):
    list_N_name = [random.choice(list_name) for i in range(N)]
    return list_N_name

# Выводим результат
list_name = F(name, 100)
print(list_name)


### Задание 2 ###

# Создаем функцию, которая ищет самое часто встречающееся имя из списка на входе
def top_name(list):
    top_name = list[0]
    for i in range(len(list)):
        top_name = list[i] if list.count(list[i]) > list.count(top_name) else top_name
    return top_name

# выводим результат
print('Самае часто всречаемое имя:', top_name(list_name))


### Задание 3 ###

# создаем функцию вывода самой редкой буквы, с которого начинаются имена в списке
def rare_leeter(list):
    list_letter = [list[i][0] for i in range(len(list))]
    rare_letter = list_letter[0]
    for j in range(len(list_letter)):
        rare_letter = list_letter[j] if list_letter.count(list_letter[j]) < list_letter.count(rare_letter) else rare_letter
    return rare_letter

#выводим результат
print('Самая редкая первыя буква имени:', rare_leeter(list_name))

### Задание PRO ###

# находим самый поздний log по времени из файла log
log = open('/Users/stanislaff/Downloads/log', 'r')
log_list = log.readlines()
time_log = [log_list[i][11:19] for i in range(len(log_list))]
time_log.sort(reverse = True)
log_top = time_log[0]

#выводим резултат
print('Время самого позднего лога: ', log_top)