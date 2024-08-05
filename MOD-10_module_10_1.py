

from time import sleep
from threading import Thread
from datetime import datetime

# Домашнее задание по теме "Создание потоков"

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Потоковая запись № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name} ')

start_time =  datetime.now()

write_words(10, 'variant1.txt')
write_words(30, 'variant2.txt')
write_words(200, 'variant3.txt')
write_words(100, 'variant4.txt')

end_time_functions = datetime.now()
print(f'Работа потоков: {end_time_functions - start_time} секунд')

thread1 = Thread(target=write_words, args=(10, 'variant5.txt'))
thread2 = Thread(target=write_words, args=(30, 'variant6.txt'))
thread3 = Thread(target=write_words, args=(200, 'variant7.txt'))
thread4 = Thread(target=write_words, args=(100, 'variant8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_threads = datetime.now()
print(f'Работа потоков: {end_time_threads - end_time_functions} секунд')



