name = 'ibrohim'
if name:
    cnt = len(name)
    print(cnt)

name = 'ibrohim'
if (cnt := len(name)) != 0:
    print(cnt)

if 10 > 5:
    print(10)


"""
1) Дано целое число. Если оно является положительным то прибавить к нему 20, в противном случае вычесть из него 5. Вывести полученное число
"""
intager1 = int(input())
if intager1 > 0:
    print(f'you entered a number greater than 0: {intager1 + 20}')
else:
    print(f'you entered a less number than 0:{intager1 - 5}')
"""
2) Дано два числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2.
"""

number1 = int(input())
number2 = int(input())
if number1 + number2 > 5:
    print(f'your number greater than 5:{number1 + 1} ')
elif number1 + number2 == 5:
    print("you need to enter greater or lesser number ")
else:
    print(f'it isn`t greater than 5 {2}')
    """
    3) Ввести 2 числа. Если их произведение отрицательно, умножить его на 8 и вывести на экран, в противном случае увеличить его в 1,5 раза и вывести на экран.
    """
num1 = float(input())
num2 = float(input())
num3 = num2 + num1
if num3 < 0:
    print(f'number is lesser than 0: {num1 + num2 * 8}')
else:
    print(f'number is entered less than 0 {num1 + num2 * 1.5}')

"""
4) Составить программу, которая запрашивает ввод температуры тела человека и определяет, здоров он или болен
"""
temperature = float(input('enter the temperature:'))

if temperature > 37.5:
    print("your temperature is higher")
elif temperature < 0 or temperature == 0:
    print('cold temperature')
else:
    print("your temperature is normal")

"""
5) Составить программу, которая запрашивает ввод трех значений температуры и проверяет, есть ли среди них температура таяния льда. Если такая температура введена, вывести на экран сообщение «Введена температура таяния льда», иначе «Такой температуры нет»
"""

"""
# 6) Составить программу, чтобы компьютер запросил имя пользователя и его год рождения, затем подсчитал возраст человека, в зависимости от года рождения.
# """
from datetime import datetime

name = input('enter your name ')
born = int(input('enter when you born '))
year_u = datetime.now().year
result = year_u - born
if result >= 0:
    print(f'{name}`s age is {result} ')
else:
    print('error')
"""
7) Программа спрашивает возраст пользователя.
— Если возраст меньше или равен 18, то вывести: «Вам нужно учиться».
— Если возраст больше 18, но меньше или равен 50 — «Вам нужно работать»
— Если возраст больше 50, но меньше или равен 59 — «Вам скоро на пенсию»
— Если возраст больше 59, но меньше 110 — «Вы пенсионер».
"""
age = int(input())
if age <= 18:
    print('you need to learn')
elif 18 < age <= 50:
    print('you need to work')
elif 50 < age <= 59:
    print("you`ve reached retirement age")
elif 59 < age <= 110:
    print('you are in the retirement')
else:
    print('maybe you dead')
"""
8) Напишите программу, которая принимает целое число от 1 до 12 и возвращает название месяца и количество дней.
"""
mon = int(input())
if mon == 1:
    print('january 31 days ')
elif mon == 2:
    print('feburary 28 days ')
elif mon == 3:
    print('march 31 days')
elif mon == 4:
    print('april 30 days')
elif mon == 5:
    print('may 31 days')
elif mon == 6:
    print('june 30 days')
elif mon == 7:
    print('july 31 days')
elif mon == 8:
    print('august 31 days')
elif mon == 9:
    print('september 30 days')
elif mon == 10:
    print('october 31 days')
elif mon == 11:
    print('november 30 days')
elif mon == 12:
    print('december 31 days')
else:
    print('date isn`t found')

"""
10) Если заданы два целых числа, они возвращают свое произведение только в том случае, если произведение не больше 1000, иначе возвращают свою сумму
"""
product1 = int(input('first product'))
product2 = int(input('second product'))
result = product1 * product2
result2 = product1 + product2
if result < 1000:
    print(result)
else:
    print(result2)
"""
11) Напишите программу для отображения «Hello», если введенное пользователем число кратно пяти, в противном случае выведите «Bye».
"""
user = int(input())
if user > 5:
    print('hello')
else:
    print('bye')
"""
12) ** Написать программу, которая спрашивает у пользователя год и определяет является ли год високосным. (справка: В соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100 или кратен 400).
"""
jumping_year = int(input())
if jumping_year * 100 * 4:
    print('jumping year')
else:
    print('wrong jumping year')
"""
13)
"""

chocolate_parts = int(input('chocolate parts: '))
length = int(input('lenght: '))
width = int(input('weight: '))
if width % 2 == 0 and length % 2 == 0 and chocolate_parts % 2 == 0:
    print('yes')
else:
    print('no')
