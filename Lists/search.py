n = int(input())
word = input()
my_strings = []

for i in range(1, n + 1):
    current_string = input()
    my_strings.append(current_string)
print(my_strings)

for i in range(len(my_strings) - 1, -1, -1):
    element = my_strings[i]

    if word not in element:
        my_strings.remove(element)
print(my_strings)