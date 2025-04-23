temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23,
                25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda x: x > 28, temperatures))

print(f'max temperature is {max(hot_days)}')
print(f'min temperature is {min(hot_days)}')

count = len(hot_days)
average_temp = sum(hot_days) / count

print(f'average temperature is {average_temp}')
