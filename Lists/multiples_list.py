factor = int(input())
count = int(input())

new_list = [num * factor for num in range(1, count + 1)]
print(new_list)