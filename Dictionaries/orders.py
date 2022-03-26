def print_funct(orders_dict):
    for (key, value) in orders_dict.items():
        result = float(value[0]) * float(value[1])
        print(f"{key} -> {result:.2f}")


def orders():
    orders_dict = dict()

    while True:
        command = input()
        if command == "buy":
            print_funct(orders_dict)
            break
        name, price, qty = command.split()
        if name in orders_dict:
            orders_dict[name] = [float(price), (float(qty) + orders_dict[name][1])]
        else:
            orders_dict[name] = [float(price), int(qty)]


orders()
