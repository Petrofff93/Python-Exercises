def courses(item):
    for x in range(1, int(input()) + 1):
        item.append(input())
    return item


my_list = []
print(courses(my_list))
