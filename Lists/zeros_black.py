single_string = input().split(", ")

for i in single_string:
    if i == '0':
        single_string.append(single_string.pop(single_string.index("0")))

result = list(map(int, single_string))
print(result)