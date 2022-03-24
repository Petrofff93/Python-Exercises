race_list = input().split()
first_racer = 0
second_racer = 0

list_lenght = len(race_list)
middle_index = list_lenght // 2

first_half = race_list[:middle_index]
second_half = race_list[middle_index + 1:]

for i in first_half:
    current_pts = int(i)
    first_racer += current_pts
    if current_pts == 0:
        first_racer *= 0.80

for k in reversed(second_half):
    second_current = int(k)
    second_racer += second_current
    if second_current == 0:
        second_racer *= 0.80
if first_racer > second_racer:
    print(f'The winner is right with total time: {second_racer:.1f}')
else:
    print(f'The winner is left with total time: {first_racer:.1f}')