import request
print('my programm')
print("I don't no what to write")


def time_task(*time, k):
  k = k + 1
  print(k, 'упражнений выполнено за', sum(*time) // 60, 'ч.', sum(*time) % 60, 'мин.')

time_list = [17, 15, 45, 38, 23, 21, 23, 10, 18]
time_task(time_list, 7)
