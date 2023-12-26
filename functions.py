# 1) Напишите функцию, чтобы найти максимальное из трех чисел
def maximal(user):
    user = int(input('max 3 numbers: '))
    if user <= 999:
        typer = f'your number is = {user}'
    else:
        typer = 'sorry we did not find that number'

    return typer


max1 = maximal(int)
print(max1)


# 4) Напишите функцию, для переворота строки
#
# Пример строки: 1234abcd
#
# Результат: dcba4321
def sum1():
    summ = (input('enter the number with commas: '))[::-1]
    return summ


res = sum1()
print(res)


# 6) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра
#
# Пример строки: ‘The quick Brow Fox’
#
# Результат:
#
# Кол-во символов в верхнем регистре: 3
#
# Кол-во символов в нижнем регистре: 12

def count_words_and_lines():
    text = input('enter the text: ')

    words = text.split()
    word_count = len(words)

    lines = text.splitlines()
    line_count = len(lines)

    print(f"numbers of words: {word_count}")
    print(f"numbers of spaces: {line_count}")


#
#
# count_words_and_lines()
# 88) Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых. Написать функцию bank, принимающая количество денег и лет, и возвращающую сумму, которая будет на счете через years лет
def bank():
    rub = float(input('enter the rub: '))
    years = int(input('enter the year: '))

    pr = 0.10

    res2 = rub * (1 + pr) ** years
    print(res2)


#
#
# bank()
# 11) Напишите функцию, которая будет принимать количество секунд и возвращать их в днях-часах-минутах-секундах
#
# 91000 секунд = 1 день, 1 час, 16 минут, 40 секунд
def split_seconds(seconds):
    days = seconds // (24 * 60 * 60)
    hours = (seconds % (24 * 60 * 60)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return days, hours, minutes, remaining_seconds


seconds_example = 91000
days, hours, minutes, remaining_seconds = split_seconds(seconds_example)

print(f"{seconds_example} seconds = {days} days, {hours} hours, {minutes} minutes, {remaining_seconds} seconds")
