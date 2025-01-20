# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
m = 0
s = ''

with open('task5.txt', 'r', encoding='utf8') as f:
    l = f.read()
    for i in range(len(l)):
        if len(l[i]) > m:
            m = len(l[i])
            s = l[i]
    #for c in ';:!?,.':
    #    l = l.replace(c, '')
    #l = l.split()

with open('task5-1.txt', 'w', encoding='utf8') as f:
    f.write(f"the longest word: {s}\n")
    f.write(f"its long: {m}\n")

with open('task5-1.txt', 'r', encoding='utf8') as f:
    r = f.read()

print(r)