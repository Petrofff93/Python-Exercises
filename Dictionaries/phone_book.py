my_book = dict()

while True:
    command = input()
    if command.isdigit():
        for _ in range(int(command)):
            name = input()
            if name in my_book:
                for key, value in my_book.items():
                    if key == name:
                        print(f"{key} -> {value}")
            else:
                print(f"Contact {name} does not exist.")
        break
    contact = command.split("-")
    my_book[contact[0]] = contact[1]
