numbers_list = list(map(int, input().split(', ')))
work_list = list()
group = 10
counter = 0

while len(numbers_list) > 0:
    for item in numbers_list:
        if item <= group:
            work_list.append(item)
            numbers_list.remove(item)
            counter += 1
            break
    if counter > 0:
        counter = 0
        continue
    print(f"Group of {group}'s: {work_list}")
    work_list = []
    group += 10
if len(numbers_list) == 0:
    print(f"Group of {group}'s: {work_list}")