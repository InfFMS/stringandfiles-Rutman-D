# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.


l = sum(1 for line in open("task1.txt"))
print(l)

w = 0
s = 0

for i in open("task1.txt", encoding='utf-8'):
    #print("i =", i)
    w += len(i.split())
    s += len(i)

print(w-1)
print(s)

