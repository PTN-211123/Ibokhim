# 2) Напишите скрипт который будет работать циклично в интерактивном режиме, скрипт должен запрашивать имя пользователя, если пользователь не вводя имя нажмет на Enter то скрипт должен завершиться (используйте break)
# while True:
#     user = str(input('enter your name: '))
#     if not user:
#         break

# 3) Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’], из него составить новый список, но без буквы ‘i’, результат: list2 = [‘mcros’, ‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)

list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []

for word in list1:
    new_word = ''
    for char in word:
        if char == 'i':
            pass
        else:
            new_word += char
    list2.append(new_word)

print(list2)

# 1) Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.
# 2) Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’], необходимо разделить на два списка, в первом только цифровые значения, а во втором только строки
list11 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']

nums = []
strs = []

for i in list11:
    if isinstance(i, (int, float)):
        nums.append(i)
    elif isinstance(i, str):
        strs.append(i)

print(nums)
print(strs)
# 3) Тот же самый пример, с сообщением после каждой итерации о том что элемент N добавлен
# 4) Приведенный ниже код назначает 5-ю букву каждого слова в food новый список fifth. Однако код в настоящее время выдает ошибки. Вставьте предложение try/except, которое позволит запустить код и создать список
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass

print(fifth)
# 5) Приведенный ниже код делит значения элемента на самого себя, но вылетает с ошибками, необходимо учесть все типы ошибок и дописать код (условия цикла менять нельзя, использовать полный синтаксис try/except/else)

my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list) + 5):

    try:
        result = my_list[index] / my_list[index]
    except ZeroDivisionError:
        print(f'there is some errors divide by zero {index}')

    except (TypeError, ValueError):
        print(f'data type error for item with index {index}')

    except Exception as e:
        print(f'unhandled error {e}')
    else:
        print(f'result of dividing an item with index {index}: {result}')

# 8) Следующий код работает отлично, если пользователь вводит цифровое значение, но всегда есть НО:
try:
    min = int(input("enter the number: "))
    max = int(input("enter the number: "))
except ValueError:
    print('error with number')
else:
    for i in range(min, max + 1):
        print(f"the square of number  {i} equal to {i * i}")


# 9) Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл еще лучше, задача разобраться со стандартной библиотекой logging
import logging

logging.basicConfig(filename='my_error.log')
logger = logging

try:
    1 / 0
except ZeroDivisionError as error:
    logger.error(error)
