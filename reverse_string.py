#reverse string if you dont know string methods
#first
string = input()

reverse_str_list = []
for i in range(0, len(string)):
   reverse_str_list.append(string[len(string)-1-i])

reverse_str = ''.join(reverse_str_list)
print(reverse_str)

#second

string_2 = input()
reversed_string = ''
for char in string_2:
    reversed_string = char + reversed_string
print(reversed_string)