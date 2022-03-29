import string

text = input().split()
first_l = ""
last_l = ""
number = ""
total_sum = 0

for item in text:
    first_l = item[0]
    last_l = item[-1]
    number = item[1:-1]

    if first_l.isupper():
        total_sum += int(number) / int(string.ascii_uppercase.index(first_l) + 1)
    elif first_l.islower():
        total_sum += int(number) * int(string.ascii_lowercase.index(first_l) + 1)

    if last_l.isupper():
        total_sum -= int(string.ascii_uppercase.index(last_l) + 1)
    elif last_l.islower():
        total_sum += int(string.ascii_lowercase.index(last_l) + 1)

print(f"{total_sum:.2f}")

