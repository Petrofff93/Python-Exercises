secret = input().split(" ")
rev = ""
my_string = ""
final = ""
second_part = ""

for word in secret:
    for frag in word:
        if frag.isdigit():
            rev += frag
        else:
            my_string += frag
    if len(my_string) > 1:
        second_part = my_string[-1:] + my_string[1:-1] + my_string[:1]
    else:
        second_part = my_string
    final = chr(int(rev)) + second_part
    if word == secret[-1]:
        print(final, end="")
    else:
        print(final, end=" ")
    my_string = ""
    rev = ""
