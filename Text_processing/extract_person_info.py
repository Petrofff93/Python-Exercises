num_iterator = int(input())
name = ""
age = ""
index = 1

for _ in range(num_iterator):
    current_input = input()
    for item in range(len(current_input)):
        if current_input[item] == "@":
            index = item
            while current_input[index+1] != "|":
                name += current_input[index + 1]
                index += 1
    index = 1
    for item in range(len(current_input)):
        if current_input[item] == "#":
            index = item
            while current_input[index+1] != "*":
                age += current_input[index + 1]
                index += 1
    print(f"{name} is {age} years old.")
    name = ""
    age = ""
