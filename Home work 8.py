##### Home work 8 #####
import time
import psutil
import os

# Напишим декоратор подсчета времени выполнения функции
def timer_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('Время выполнения функции {} составило: {} сек'.format(func, time.time() - start))
    return wrapper

# Напишим декоратор подсчета затраченой памяти
def memory_function(func):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        memory_start = proc.memory_info().rss
        func(*args, **kwargs)
        print('Функция потребляет памяти: {} байт'.format(proc.memory_info().rss - memory_start))
    return wrapper

# Напишим функуцию сосзания списка натуральных числел
@timer_function
@memory_function
def getListInt(count):
    list_int = []
    for i in range(count):
        list_int.append(i)
    return list_int

# Напишим генератор создания натуральных чисел
# @timer_function
@memory_function
def genInt(count):
    for i in range(count):
        yield i

# Сравним время создания герерата и списка натуральных чисел, также потребление опреативной памяти
getListInt(1000000)
genInt(1000000)



