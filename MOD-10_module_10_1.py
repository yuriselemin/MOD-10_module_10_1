from threading import Thread
from time import sleep
from datetime import datetime

# Домашнее задание по теме "Создание потоков"

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Потоковая запись № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name} ')


start_time_functions = datetime.now()
write_words(10, 'variant1.txt')
write_words(30, 'variant2.txt')
write_words(200, 'variant3.txt')
write_words(100, 'variant4.txt')
end_time_functions = datetime.now()
print(f'Разница работы функций: {end_time_functions - start_time_functions} секунд')



start_time_threads = datetime.now()
threads = []
for count, file_name in [(10, 'variant5.txt'), (30, 'variant6.txt'), (200, 'variant7.txt'), (100, 'variant8.txt')]:
    t = Thread(target=write_words, args=(count, file_name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end_time_threads = datetime.now()
print(f'Разница работы потоков: {end_time_threads - start_time_threads} секунд')



