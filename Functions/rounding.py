def rounding_func(item):
    my_list = [float(item) for item in item]
    converted_list = [round(item) for item in my_list]
    return converted_list


rounding = input().split()
print(rounding_func(rounding))
