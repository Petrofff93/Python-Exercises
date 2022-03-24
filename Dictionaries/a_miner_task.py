my_dict = dict()

while True:
    command = input()
    if command == "stop":
        for (key, value) in my_dict.items():
            print(f"{key} -> {value}")
        break
    value = int(input())
    if command in my_dict:
        my_dict[command] += value
    else:
        my_dict[command] = value
