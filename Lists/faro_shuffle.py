cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)
my_list = []

for i in range(0, shuffle):

    for p in range(0, mid):
        my_list.append(cards[p])
        my_list.append(cards[mid])
        mid += 1
    cards = my_list
    mid = int(length / 2)

print(my_list)