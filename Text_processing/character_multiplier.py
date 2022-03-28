strings = input().split()

first = strings[0]
second = strings[1]
total_sum = 0

if len(first) == len(second):
    for item in list(zip(first, second)):
        total_sum += ord(item[0]) * ord(item[1])
    print(total_sum)
else:
    if len(first) > len(second):
        for item in list(zip(first, second)):
            total_sum += ord(item[0]) * ord(item[1])
        add_sum = first[len(second):]
        for i in add_sum:
            total_sum += ord(i)
        print(total_sum)
    else:
        for item in list(zip(first, second)):
            total_sum += ord(item[0]) * ord(item[1])
        add_sum = second[len(first):]
        for i in add_sum:
            total_sum += ord(i)
        print(total_sum)



