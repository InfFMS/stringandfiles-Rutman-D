# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

with (open('task1.txt') as f):
    s = f.readlines()
    n = f.read()

    # ls = n.split(' ')
    # print("cлов:", len(ls)-1)
    # print("строк:", len(s))
    # print("символы:", len(s[0]) + len(s[1]) + len(s[2]))
    print(s)

a=n.split("\n")
print(a)