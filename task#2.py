# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        words = (" ".join(text)).split()
        count_dict = {}
        for el in words:
            count_dict[el] = len(el)
        inv_count_dict = {}
        for k, v in count_dict.items():
            inv_count_dict[v] = inv_count_dict.get(v, []) + [k]
        count_max = 0
        for k in inv_count_dict.keys():
            if k > count_max:
                count_max = k
        print(inv_count_dict[count_max])


longest_words('article.txt')
