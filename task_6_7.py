# Задание 6.
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

# Задание 7.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Используйте написанную ранее функцию int_func().

user_sentence_list = input('Введи слова из маленьких латинских букв, разделенные пробелами: ').split()
alp_rus = set(chr(n) for n in range(ord('а'), ord('я') + 1))


def ext_func(words_list):
    cap_words_list = []

    def int_func(one_word):
        global alp_rus
        if not one_word.isalpha() or not one_word.islower() or len(set(one_word).intersection(alp_rus)) > 0:
            return ''
        return word.capitalize()

    for word in words_list:
        cap_word = int_func(word)
        if cap_word:
            cap_words_list.append(cap_word)
        else:
            return ''
    return ' '.join(cap_words_list)


print(ext_func(user_sentence_list) or 'Это не то, что я просил.')
