def representation_data(a, b):
    result = [x for x in a if x == 0]
    print(f"Cupid's last position was {b}.")
    if len(result) != len(a):
        diff = abs(len(a) - len(result))
        print(f"Cupid has failed {diff} places.")
    else:
        print("Mission was successful.")


def heart_delivery(data):
    index_pos = 0
    cupids_last_pos = 0

    while True:
        command = input().split(" ")

        if command[0] == "Love!":
            break

        index = int(command[1]) + index_pos

        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")
        cupids_last_pos = index
        index_pos = index
    representation_data(data, cupids_last_pos)


numbers = list(map(int, input().split("@")))
heart_delivery(numbers)
