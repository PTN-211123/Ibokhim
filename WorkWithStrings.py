import re

# 1) В примере найти и вывести трехзначные числа с помощью регулярных выражений.
sample = 'Exercises number 1, 12, 13, and 345 are important 456'
result = re.findall(r'\d{3}', sample)
print(result)

# 2) Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
colors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']

Find_All_Colors = [i for i in colors if re.match(r'#\b[0-9A-Fa-f]{6}\b', i)]

print(Find_All_Colors)

# 3) Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.
text = ['breakfast 09:00', 'breakfast 90:00', 'lunch 13:00', 'lunch 13:61', 'dinner 19:05', 'dinner 37:98',
        'at 24:01 dinner']

formatting = [time for time in text if re.match(r'\b([01]\d|2[0-3]):[0-5]\d\b', time)]

print(formatting)

# 4) Создать запрос для выбора из текста дробных чисел с разделителем дробной части в виде точки. Разряды целой части могут не выделяться или отделяться пробелом или запятой. 1231.12313

numbers = [1231.12313, 2121.121, 3.14, 6598, 9898787, 999.99, '098 90', '123,123']

valid_numbers = [num for num in numbers if re.match(r'\b(?:\d+[ ,]?)?\d+\.\d+\b', str(num))]

print(valid_numbers)
#5) ** Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который работал с конфигурациями маршрутизатора (можно переделать весь скрипт для работы с регуляркой)

MAC_address = '00-04-5A-63-A1-66'

# Use re.findall to find all occurrences of the pattern
Mac_list = re.findall(r'[0-9A-Fa-f]+', MAC_address)

print(Mac_list)

#WORKING WITH JSON

import json

