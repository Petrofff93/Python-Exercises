number = int(input())

positive_list = []
negative_list = []
counter_positives = 0
sum_negatives = 0

for i in range(1, number + 1):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
        counter_positives += 1
    else:
        negative_list.append(num)
        sum_negatives += num

print(positive_list)
print(negative_list)
print(f'Count of positives: {counter_positives}\nSum of negatives: {sum_negatives}')
