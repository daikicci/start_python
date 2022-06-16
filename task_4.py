# Задание 4.
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

with open('task_4.txt', 'r', encoding='utf-8') as my_f:
    with open('task_4_new.txt', 'w', encoding='utf-8') as my_f_new:
        str_num = len(my_f.readlines())
        my_f.seek(0)
        for i in range(str_num):
            string = my_f.readline().lower()
            for key in my_dict:
                if key not in string:
                    continue
                my_f_new.write(string.replace(key, my_dict[key]).capitalize())
