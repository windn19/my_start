import requests
from tqdm import tqdm


# Для работы с HH сейчас нужно регистрировать приложение
# Я в своей работе использую сервис РемонтОнлайт который тоже имеет API
# Я для себя написал несколько функций для запросов с этого сервера, 2 из них я приведу ниже
# Ну и небольшой код для обработки некоторых вариантов данных с запросов, схожий с заданием

####### Функции запросов с РемОнлайн API #######


# Список клиентов
def GetCustomer(page = 'all',
                names = None,
                phones = None,
                emails = None,
                addresses = None,
                discount_codes = None,
                modified_at = None,
                created_at = None,
                ad_campaigns = None,
                juridical = None,
                conflicted = None,
                supplier = None):
    '''
    Возвращает словарь с данными клиенов с сврвера РемОнлайн
        :param page: int - Количесто страниц
        :param names: array - Фильтр по имени клиента. Учитывать клиентов у которых переданный параметр содержится в значении name клиента
        :param phones: array - Фильтр по телефону клиента. Учитывать клиентов у которы переданный параметр содержится в значении phone клиента
        :param emails: array - Фильтр по email клиента. Учитывать клиентов у которых переданный параметр содержится в значении email клиента
        :param addresses: array - Фильтр по адресу клиента. Учитывать клиентов у которых переданный параметр содержится в значении adress клиента;
        :param discount_codes: array - Фильтр по скидочным картам;
        :param modified_at: array - Фильтр по дате изменения сущности клиента. Массив из одного либо двух значений, которые содержат в себе timestamp. В случае, если массив состоит из одного значения, то оно является левой границей. Примеры: [1454277600000, 1456783200000], [1454277500000];
        :param created_at: array - Фильтр по дате создания клиента. Массив из одного либо двух значений, которые содержат в себе timestamp.В случае, если массив состоит из одного значения, то оно является левой границей. Примеры: [1454277600000, 1456783200000], [1454277500000];
        :param ad_campaigns: array - Массив идентификаторов источников откуда клиент узнал о нас;
        :param juridical: bool -  Вернуть только юридические лица, если правда, и только физические лица, если ложь;
        :param conflicted: bool - Вернуть конфликтных клиентов, если правда, и только не конфликтных, если ложь;
        :param supplier: bool - Вернуть клиентов являющихся поставщиками, если правда, и только обычных, если ложь;
        :return: Список словарей с данными клиентов
    '''
    # Мой ключ для доступо к API
    api_key = '...' # Выдан мне для формирования токенов, которые живут около 10 мин

    # Запрос и формирование token
    data_key = {'api_key': api_key}
    result = requests.post('https://api.remonline.ru/token/new', data = data_key).json()
    token = result['token']
    # print('Connection success: {}'.format(result['success']))

    # Параметры запроса
    param = {'token': token,
             'page': page,
             'names[]': names,
             'phones[]': phones,
             'emails[]': emails,
             'addresses[]': addresses,
             'discount_codes[]': discount_codes,
             'modified_at[]': modified_at,
             'created_at[]': created_at,
             'ad_campaigns[]': ad_campaigns,
             'juridical': juridical,
             'conflicted': conflicted,
             'supplier': supplier}

    # Делаем первый запрос, чтобы узнать количество страниц ответа
    if page == 'all':
        param['page'] = 1
        result_customer = requests.get('https://api.remonline.ru/clients/', params = param).json()
        page = result_customer['count'] // 50 + 1 if result_customer['count'] % 50 > 0 else result_customer['count'] // 50
        # print('Найдено {} клиентов на {} страницах'.format(result_customer['count'], page))

    # Создадим список для словарей клиентов
    list_dict = []

    # Перебираем циклом страницы
    for N in tqdm(range(1, page + 1), position = 0, desc = f"Найдено {result_customer['count']} клиентов. Загрузка"):
        # Задаем количество страниц
        param['page'] = N

        # Отправляем запрос на сервер
        result_customer = requests.get('https://api.remonline.ru/clients/', params = param).json()

        # Занесем каждое значение в список
        for dict_custom in result_customer['data']:
            list_dict.append(dict_custom)

    # Возвращаем список
    return list_dict

# Список заказов
def GetOders(page = 'all',
            sort_dir = 'asc',
            types = None,
            branches = None,
            brands = None,
            ids = None,
            id_labels = None,
            statuses = None,
            managers = None,
            engineers = None,
            clients_ids = None,
            client_names = None,
            client_phones = None,
            created_at = None,
            done_at = None,
            modified_at = None,
            closed_at = None):
    '''
    Возвращает список словарей заказов
    :param page: Количество страниц, по умолчанию - все
    :param sort_dir: asc|desc - Направление сортировки заказов
    :param types: array - Массив идентификаторов типов заказа
    :param branches: array - Перечень идентификаторов локаций
    :param brands: array - Перечень брендов
    :param ids: array - Массив системных идентификаторов заказов
    :param id_labels: array - Массив идентификаторов заказов
    :param statuses: array - Массив идентификаторов статусов для заказа
    :param managers: array - Массив идентификаторов сотрудников компании
    :param engineers: array - Массив идентификаторов сотрудников компании
    :param clients_ids: array - Массив идентификаторов клиентов
    :param client_names: array - Перечень имен клиентов
    :param client_phones: array - Перечень телефонных номеров клиентов
    :param created_at:array - Фильтр по дате создания. Массив из одного либо двух значений, которые содержат в себе timestamp. В случае, если массив состоит из одного значения, то оно является левой границей. Примеры: [0, 1454277600000], [1454277500000]
    :param done_at: array - Фильтр по дате готовности. Массив из одного либо двух значений, которые содержат в себе timestamp. В случае, если массив состоит из одного значения, то оно является левой границей. Примеры: [1454277600000, 1456783200000], [1454277500000]
    :param modified_at: array - Фильтр по дате изменения заказа
    :param closed_at:array - Фильтр по дате выдачи. Массив из одного либо двух значений, которые содержат в себе timestamp. В случае, если массив состоит из одного значения, то оно является левой границей. Примеры: [1456783200000, 1454925794507], [1454277500000]
    :return: Список словарей заказов
    '''

    # Мой ключ для доступо к API
    api_key = "..." # Выдан мне для формирования токенов, которые живут около 10 мин
    # start_range = datetime.datetime(2020, 10, 1).timestamp()
    # finish_range = datetime.datetime(2020, 10, 17).timestamp()

    # Запрос и формирование token
    data_key = {'api_key': api_key}
    result = requests.post('https://api.remonline.ru/token/new', data = data_key).json()
    token = result['token']
    # print('Connection success: {}'.format(result['success']))

    # Параметры запроса
    param = {'token': token,
             'page': 1,
             'sort_dir': sort_dir,
             'types[]': types,
             'branches[]': branches,
             'brands[]': brands,
             'ids[]': ids,
             'id_labels[]': id_labels,
             'statuses[]': statuses,
             'managers[]': managers,
             'engineers[]': engineers,
             'clients_ids[]': clients_ids,
             'client_names[]': client_names,
             'client_phones[]': client_phones,
             'created_at[]': created_at,
             'done_at[]': done_at,
             'modified_at[]': modified_at,
             'closed_at[]': closed_at}

    # Делаем первый запрос, чтобы узнать количество страниц ответа
    if page == 'all':
        param['page'] = 1
        result_oders = requests.get('https://api.remonline.ru/order/', params = param).json()
        page = result_oders['count'] // 50 + 1 if result_oders['count'] % 50 > 0 else result_oders['count'] // 50
        # print('Найдено {} заказов на {} страницах'.format(result_oders['count'], page))

    # Создадим список для словарей заказов
    list_dict = []

    # Перебираем циклом страницы
    for N in tqdm(range(1, page + 1), position = 0, desc = f"Найдено {result_oders['count']} заказов. Загрузка"):
        # Задаем номер страницы
        param['page'] = N

        # Отправляем запрос на сервер
        result_oders = requests.get('https://api.remonline.ru/order/', params = param).json()

        # Занесем каждое значение в список
        for dict_oders in result_oders['data']:
            list_dict.append(dict_oders)

    # Возвращаем список
    return list_dict

client = 'Иван Левин'

# Загрузим все заказа клиента Левин Иван
ordersLevin = GetOders(page = 'all', client_names = client)

# Посчитаем на какую сумму клиент сделал заказов за весь период
summOders = 0
for oder in ordersLevin:
    # вытаскиваем из словаря заказа оплаченную сумму
    summOders += oder['payed']

print(f'За весь период клиент {client} сделал {len(ordersLevin)} заказов на сумму {summOders} руб.')

# Код работает хорошо, для праверки могу выслать сформированный токен, но он живет около 10 мин, и после становится недействиельным