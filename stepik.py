###STRINGS

#Вводится число N, выведите все чётные числа от 2 до N, включая N.

number = int(input())
number_list=[]
for i in range(1, number+1):
    if i%2==0:
        number_list.append(i)
for k in number_list:
    print(k, end=' ')

def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False  # Числа меньше или равные 1 не являются простыми
    if n <= 3:
        return True   # 2 и 3 являются простыми числами
    if n % 2 == 0 or n % 3 == 0:
        return False  # Исключаем четные числа и кратные 3

    # Проверяем делители от 5 до √n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def print_primes_up_to_n(N):
    """Выводит все простые числа от 1 до N включительно."""
    for num in range(1, N + 1):
        if is_prime(num):
            print(num)

# Пример использования
N = int(input("Введите целое число N: "))
print(f"Простые числа от 1 до {N}:")
print_primes_up_to_n(N)


'''
Вводится число, если это число является чётным и оно больше 10 - 
напечатайте 1, если число нечётное или отрицательное напечатайте -1, во всех других случаях  печатайте 0.
'''
number = int(input())

if number > 10 and number%2 == 0:
    print(1)
elif number < 0 or number%2 !=0:
    print(-1)
else:
    print(0)


#Вводится строка, количество символов нечётное. Выведите элемент, который находиться посередине строки.

word = input()

if len(word)%2 != 0:
    print(word[round(len(word)/2 + 0.1)-1])

'''
Вводится 2 числа, ширины и высота прямоугольника. Затем вводится символ из которого будет состоять этот прямоугольник.
Напечатайте прямоугольник.
'''

# put your python code here
first = int(input())
second = int(input())
third = input()

for i in range(second):
    print(first*third)

#Вводится число N нужно вывести максимальный делитель этого числа, не считая само число N.

number = int(input())

for i in range(1, number):
    if (number) % (number - i) == 0:
        print(number - i)
        break

'''Вводится строка - пароль, нужно проверить является ли пароль надёжным. Условия надёжности пароля:
1) Длина не менее 8 символов
2) Есть заглавная буква (и строчная буква)
3) Есть цифра

Если пароль надёжный напечатайте: "Пароль надёжный", в ином случае "Придумайте другой пароль"'''

passw = input()
upper = False
lower = False
digit = False

for i in passw:
    if i.isupper() == True:
        upper = True
    if i.islower() == True:
        lower = True
    if i.isdigit() == True:
        digit = True

if upper == True and lower == True and digit == True and len(passw) > 7:
    print("Пароль надёжный")
else:
    print("Придумайте другой пароль")
