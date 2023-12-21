# -*- coding: utf-8 -*-
# 2) Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные слова из каждой строки, после чего составьте список слов. В списке слова не должны дублироваться. После чего распечатайте список, в котором все слова будут отсортированы в алфавитном порядке. (используйте open)
file = open('txt/romeo.txt', mode='r')
a = file.read()
print(a.split())
a = file.close()
# 3) Напишите код программы, которая будет открывать файл «article.txt» и выводить на печать построчно последние строки в количестве lines (число которую можно запросить у пользователя). Число должно быть положительным (используйте with open)
# -*- coding: utf-8 -*-
lines = int(input("enter the value "))
with open('txt/article.txt', mode='r', encoding='utf-8') as file1:
    last_lines = file1.readlines()[-lines:]
    for line in last_lines:
        print(line.strip())

# 4) Документ «article.txt» содержит следующий текст: (используйте open)
with open('txt/article.txt', mode='r', encoding='utf-8') as size:
    c = size.read().split()
    bigger_value = max(c, key=len)
    print(f'word---------------------------------- {bigger_value}')
