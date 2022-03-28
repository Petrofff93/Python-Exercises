import string

data = input().split(", ")
expected_elements = string.digits + string.ascii_letters + '-' + '_'

for item in data:
    bool_check = True
    if 3 > len(item) or len(item) > 16:
        bool_check = False
    elif len([x for x in item if x in expected_elements]) != len(item):
        bool_check = False
    else:
        if bool_check:
            print(item)




