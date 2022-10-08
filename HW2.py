# Задание 1
# На вход подается строка, состоящая из одного числа. Напишите программу, которая удваивает его.
av = str(input())
print(str(int(av) * 2))

# Задание 2
# Вводится число. Вывести его квадрат.
bv = int(input())
print(str(int(bv) ** 2))
# Задание 3
# Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
# Вывести, какая часть суток прошла
hour = int(input())
minutes = int(input())
seconds = int(input())
sec2 = hour * 3600 + minutes * 60 + seconds
print("seconds:", sec2)
print(round((sec2 / 86400), 4))

# Задание 4
# Вводится число. Вывести, оканчивается ли оно на цифру 7, не используя приведение к строке и операции над строками
seven = int(input())
ost = seven % 10
print(ost==7)

# Задание 5
# Вводятся коэффициенты уравнения ax2+bx+c=0. Вывести его корни(не забыть проверить, что a не равно 0)
a = int(input())
b = int(input())
c = int(input())
disc = b ** 2 - 4 * a * c
if a != 0:
    if disc == 0:
        kor0 = (-b) / (2 * a)
        print(round(kor0, 4))
    elif disc > 0:
        kor1 = (-b - (disc ** (0.5))) / (2 * a)
        kor2 = (-b + (disc ** (0.5))) / (2 * a)
        print(round(kor1, 4))
        print(round(kor2, 4))
    else:
        print('error')
else:
    print(round((-c)/b, 4))

# Задание 6
# Вводятся три числа. Вывести максимум из них.
chi1=int(input())
chi2=int(input())
chi3=int(input())
print(max(chi1, chi2, chi3))

# Задание 7
# Вводится число. Вывести среднее арифметическое (с точностью до двух знаков после запятой)
# тех чисел в диапазоне от единицы до введённого числа, которые делятся 5 или являются четными.
f=int(input())
summ=0
arif=0
kolvo=0
for i in range(1, f):
    if i%2==0 or i%5==0:
        summ+=i
        kolvo+=1
    else:
        continue
arif=summ/kolvo
print(round(arif, 2))