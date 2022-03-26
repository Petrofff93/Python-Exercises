def s_parking():
    number_of_lines = int(input())
    parking_dict = dict()
    for _ in range(number_of_lines):
        command = input().split()

        if command[0] == "register":
            name = command[1]
            plate = command[2]
            if name not in parking_dict:
                parking_dict[name] = plate
                print(f"{name} registered {plate} successfully")
            else:
                print(f"ERROR: already registered with plate number {plate}")
        if command[0] == "unregister":
            name = command[1]
            if name not in parking_dict:
                print(f"ERROR: user {name} not found")
            else:
                print(f"{name} unregistered successfully")
                del parking_dict[name]
    for (key, value) in parking_dict.items():
        print(f"{key} => {value}")


s_parking()
