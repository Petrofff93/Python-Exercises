text = input()
my_dict = dict()

for item in text:
    if item != " " and item not in my_dict:
        my_dict[item] = text.count(item)

for (key, value) in my_dict.items():
    print(f"{key} -> {value}")

