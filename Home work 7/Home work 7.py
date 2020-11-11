####### Home work 7 #######
import datetime

import json
import csv
from docxtpl import DocxTemplate
import time




# Создадим словарик с данными об автомобилях
data = [{'brand': 'Huynday', 'model': 'Accent', 'fuel_consumption': 8, 'cost': 5000},
        {'brand': 'Renault', 'model': 'Logan', 'fuel_consumption': 10, 'cost': 3500},
        {'brand': 'Toyota', 'model': 'Camry', 'fuel_consumption': 12, 'cost': 10000},
        {'brand': 'Mercedes-Benz', 'model': 'Gelandewagen', 'fuel_consumption': 20, 'cost': 8000}]

# Засечем время
start_time = time.time()

# Преобразуем словари в текст и заишим построчно
with open('Home work 7/cars.txt', 'w') as f:
    for line in data:
        f.write(str(line))

print('Время записи данных в TXT фаил {} секунд'.format(time.time() - start_time))


# Засечем время
start_time = time.time()

# Загружаю шаблон doc документа
template = DocxTemplate('Home work 7/template_cars.docx')

# Формирую начальные параметры записи
context = {'title': 'The catalog of cars',
           'description': 'Only good cars!'}

# Сформируем данные для записи в таблицу шаблона
n = 1 # инициализируем счетчик
# Проходим по списку машин
for car in data:
    # Перебираем значения словаря
    for key,val in car.items():
        context[key + str(n)] = val # Меняем под шаблон
    n += 1

# Записываем данные в шаблон
template.render(context)
# Сохраняем результат в doc
template.save('Home work 7/Catalog_of_cars.docx')

print('Время записи данных в шаблон DOC {} секунд'.format(time.time() - start_time))



# Засечем время
start_time = time.time()

# Запишим данные о машинах в файл csv
with open('Home work 7/cars.csv', 'w') as f:
    # Зададим параметры записи
    writer = csv.DictWriter(f, delimiter = ';', fieldnames = ['brand', 'model', 'fuel_consumption', 'cost'])
    # Создадим названия столбцов
    writer.writeheader()
    # Циклом запишим данные о машинах
    for i in range(len(data)):
        writer.writerow(data[i])

print('Время записи данных в CSV фаил {} секунд'.format(time.time() - start_time))

# Засечем время
start_time = time.time()

# Преобразуем данные в формат json и сохраним в txt
with open('Home work 7/data_json.txt', 'w') as f:
    json.dump(data, f)

print('Время записи данных JSON в TXT фаил {} секунд'.format(time.time() - start_time))

