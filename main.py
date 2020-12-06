
# Декоратор - функция не будет выполнена при статусе игры - финишь
def skip(func):
    def wrapper(*args, **kwargs):
        global status
        if status != 'finish':
            func(*args, **kwargs)
    return wrapper

status = 'finish'

@skip
def ttr(text):
    print(text)

ttr('привет')