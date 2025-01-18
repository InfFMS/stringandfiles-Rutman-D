# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.


with open('task2.txt',"r", encoding='utf8') as f:
    file_line = f.read()

r = file_line.replace("Python", "Питон")
new_file = open("task2-1.py", "w", encoding='utf8')
new_file.write(r)
c = file_line.count("Python")
print(c)
new_file.close()