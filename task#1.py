# Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в
# количестве lines (на всякий случай проверим, что
# задано положительное целое число). Протестируем
# функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines, file):
    if type(lines) != int or lines <= 0:
        print('You input incorrect number of lines')
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        for el in range(len(text) - lines, len(text)):
            print(text[el])

lines = int(input('Input number of lines :', ))
read_last(lines, 'article.txt')
