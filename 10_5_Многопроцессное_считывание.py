import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
    all_data.append(line)


filenames = [f'./Files_for_10_5/file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for filename in filenames:
    read_info(filename)
stop = datetime.now()
print('Линейный метод:', stop - start)


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    stop = datetime.now()
    print('Многопроцессный метод:', stop - start)
