def print_func(legendary, junk, special):
    print(f"{special} obtained!")
    print(f"shards: {legendary['shards']}")
    print(f"fragments: {legendary['fragments']}")
    print(f"motes: {legendary['motes']}")

    for (key, value) in junk.items():
        print(f"{key}: {value}")


def legendary_farm():
    leg_items_dict = {'shards': 0, 'motes': 0, 'fragments': 0}
    leg_items_list = ['shards', 'motes', 'fragments']
    junk_items_dict = dict()
    is_obtained = False

    while True:
        items = input().lower()
        items = items.split()

        for value, materials in zip(items[0::2], items[1::2]):
            materials = materials.lower()
            value = int(value)
            if materials in leg_items_list:
                if materials not in leg_items_dict:
                    leg_items_dict[materials] = value
                else:
                    leg_items_dict[materials] += value

                if int(leg_items_dict[materials]) >= 250:
                    leg_items_dict[materials] -= 250
                    special_item = ""
                    if materials == "shards":
                        special_item = "Shadowmourne"
                    elif materials == "fragments":
                        special_item = "Valanyr"
                    elif materials == "motes":
                        special_item = "Dragonwrath"

                    print_func(leg_items_dict, junk_items_dict, special_item)
                    is_obtained = True
            else:
                if materials not in junk_items_dict:
                    junk_items_dict[materials] = value
                else:
                    junk_items_dict[materials] += value

            if is_obtained:
                break
        if is_obtained:
            break


legendary_farm()
