digits = ""
letters = ""
chars = ""

text_input = input()
for i in text_input:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        chars += i

print(digits)
print(letters)
print(chars)
