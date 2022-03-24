my_list = []
second_list = []

for i in range(1, int(input()) + 1):
    current_num = int(input())

    my_list.append(current_num)

command = input()

for num in my_list:
    if command == 'even':
        if num % 2 == 0:
            second_list.append(num)
    elif command == 'odd':
        if num % 2 != 0:
            second_list.append(num)
    elif command == 'negative':
        if num < 0:
            second_list.append(num)
    else:
        if num >= 0:
            second_list.append(num)

print(second_list)
