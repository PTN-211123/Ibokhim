# bu mashq xato chiqargani uchun uzur so`rayman /Прошу прощения за ошибку в этом упражнении
# / \
#  |
#  |
#  |
#  |
#  1) Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5.
number = int(input('enter the number: '))
list1 = []
fib0 = 0
fib1 = 1

for i in range(1, number + 1):
    list1.append(fib1)
    fib0, fib1 = fib1, fib1 + fib0

if number >= 5:
    print('higher and equal to 5')
elif number <= 5:
    print('less equal to 5')

print(list1)

# # 2) Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в соответствующие переменные. Сохраните полученные значения в список.

fname = input('what is your name: ')
lname = input('what is your surname: ')
age = (input(f'please {fname} enter your age: '))

datas = [fname, lname, age]
print(datas)
#  3) Напишите программу, которая принимает от пользователя секвенцию чисел, разделенных запятой и пробелом. После чего запишите каждое число в список.
int_num = input('enter the number with , ')
nums = [int_num]
print(nums)

# 4) Напишите программу, которая принимает пример со СЛОЖЕНИЕМ у пользователя и затем выдает результат. (решите с помощью генератора списка)


# 5) Напишите программу, которая будет принимать три имени в качестве входных данных от пользователя в одном input() вызове функции.

# Ввод трех имен от пользователя в одном вызове input()
names = input('enter the name with spaces: ')

# Разбивка введенной строки на отдельные имена
name_list = names.split()

# Вывод имен
print('names:')
for name in name_list:
    print(name)

# 6) Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7]. напишите программу, которая превращает каждый элемент списка в его квадрат.
default_num = [1, 2, 3, 4, 5, 6, 7]

print(default_num)

new_nums = [num ** 2 for num in default_num]
print(new_nums, end='\n')

# 7) Создайте список из любимых вами блюд.
#
# Создайте список из любимых блюд вашего друга, скопировав свой список.
# Убедитесь что два списка разные, добавив по одному разному блюду в каждый список.
# Выведите два списка.

my_favourite_food = ['palov', 'kabab', 'manti', 'lagman']
friend = my_favourite_food.copy()

my_favourite_food.append('dolma')
friend.append('samsa')

print(my_favourite_food)
print(friend)

# 8) Создайте переменную user_num, которая будет принимать от пользователя число. Создайте числовой список от 1 до значения из переменной user_num (значение из переменной включительно). Выведите сам список и сумму его чисел.

# 9  Создайте два числовых списка от 1 до 100. Первый будет состоять только из четных чисел, а второй из нечётных. Выведите сам список и сумму его чисел.


even_number = int(input())

if even_number % 2 == 0:
    for even in range(2, 101, 2):
        print(even)
else:
    for odd in range(1, 101, 2):
        print(odd)
# 10) Напишите программу, которая выводит все четные числа из списка в исходном порядке, и останавливается когда число равно 815.
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]


num1 = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
        237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553,
        81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

for i in num1:
    if i == 815:
        break
    if i % 2 == 0:
        print(i)

# 11) Подсчитайте общее количество цифр в числе.

# Например, число 75869 , поэтому на выходе должно быть 5 .


while True:
    leight_number = int(input('enter the length number: '))
    print(len(str(leight_number)))

# 12) ** Напишите программу для отображения всех простых чисел в диапазоне (Учтите что пользователь может ввести отрицательное число)
# 13) *** Обработать строку ospf_route и вывести информацию на стандартный поток вывода как на картинке ниже:
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

parts = ospf_route.split()

protocol = parts[0]
subnet = parts[1]
ad_metric = parts[2][1:-1]
next_hop = parts[4][:-1]
last_update = parts[5].rstrip(',')
interface = parts[6]

print(f"protocol: {protocol}")
print(f"subnet: {subnet}")
print(f"AD/Metric: {ad_metric}")
print(f"next hop: {next_hop}")
print(f"last update: {last_update}")
print(f"interface: {interface}")
# 14  *** Получите список VLANов со строки:
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

numm = config[-17:]

list3 =[numm]


print(list3)
