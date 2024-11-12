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