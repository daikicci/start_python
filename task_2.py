# Задание 2.
# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

with open('task_2.txt', 'r', encoding='utf-8') as my_f:
    content = my_f.readlines()
    str_num = len(content)
    word_num_dict = {i+1: len(content[i].split()) for i in range(str_num)}
    print(f'В файле {str_num} строк.\n'
          f'Количество слов:')
    for key in word_num_dict.keys():
        print(f'{key} строка: {word_num_dict[key]}')
