my_list = input().split()
my_map = map(int, my_list)

integer_list = list(my_map)
removal_count = int(input())

for i in range(removal_count):
    integer_list.remove(min(integer_list))

print(", ".join(map(str, integer_list)))