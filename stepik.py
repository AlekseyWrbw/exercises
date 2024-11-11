#Вводится число N, выведите все чётные числа от 2 до N, включая N.

number = int(input())
number_list=[]
for i in range(1, number+1):
    if i%2==0:
        number_list.append(i)
for k in number_list:
    print(k, end=' ')