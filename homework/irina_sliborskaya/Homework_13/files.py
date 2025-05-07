import datetime
import os


dates = []

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(okulik_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    split_text = data_line.split(' - ')
    new_data = split_text[0].split('. ')[1]
    dates.append(new_data)

date1 = datetime.datetime.strptime(dates[0], "%Y-%m-%d %H:%M:%S.%f")
date2 = datetime.datetime.strptime(dates[1], "%Y-%m-%d %H:%M:%S.%f")
date3 = datetime.datetime.strptime(dates[2], "%Y-%m-%d %H:%M:%S.%f")
now = datetime.datetime.now()

print(date1 + datetime.timedelta(weeks=1))
print(date2.strftime('%A'))
print((now - date3).days)
