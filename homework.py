"""""
1) Составить три формы присвоение следующего вида x, y, z = y, z, x (придумать способ применения )
First way
"""""
x = 'x'
y = 'y'
z = 'z'
mix = y, z, x
print(mix)
"""
second way
"""
x = 'x'
y = 'y'
z = 'z'
special_for_x = x
special_for_z = z
special_for_y = y
print(special_for_y)
print(special_for_z)
print(special_for_x)
"""
third way
"""
answers = '''
x={}
y={}
z={}
'''
print(answers.format(y, z, x))

"""
2) Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:
num1 = '3.14'
num2 = '4'
"""

num1 = 3.14
num2 = 4
a = f'3.14+4={round(float(num1) + int(num2), 2)}'
b = f'3.14-4={round(float(num1) - int(num2), 2)}'
c = f'3.14*4={round(float(num1) * int(num2), 2)}'
d = f'3.14/4={round(float(num1) / int(num2), 2)}'
e = f'3.14**4={round(float(num1) ** int(num2), 2)}'
print(a)
print(b)
print(c)
print(d)
print(e)
"""
3) Воспользуйтесь различными методами строк
"""
str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '
print(str1.lstrip(' << ').rstrip(' -   ').lower())
print(str2.lstrip('  ').rstrip(' \n .   ').upper())
print(str3.lstrip(' (( ').rstrip(' - :+   ').lower())

"""
4) Обработайте каждую переменную и получите результат как на картинке:
"""
string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'

print(string1[::-1])
print(string2[5:8], string2[13:])
print(string3[0:11][::2])
"""
5) С помощью метода строк Замените слово show на display и создайте другую переменную
"""
show = 'show ip brief'
display = show.replace('show', 'replace')
print(show)
print(display)
"""
6) ** В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
"""
ticket = int(input('place number: '))
seat = (ticket - 1) // 4 + 1
print(f'number compartment {seat}')
"""
7) Подсчитайте общее количество цифр в числе.
Например, число 75869 , поэтому на выходе должно быть 5 .
"""
count = str(75869)
print(f"{len(count)}")
