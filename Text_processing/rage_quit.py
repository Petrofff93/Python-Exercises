text = input()
rage_text = ""
current_text = ""
numbers = ""

for index, elem in enumerate(text):
    if not elem.isdigit():
        if elem.isalpha():
            current_text += elem.upper()
        else:
            current_text += elem
    if elem.isdigit():
        numbers += elem
        if index < (len(text) - 1) and text[index+1].isdigit():
            continue
        else:
            rage_text += (current_text * int(numbers))
            numbers = ""
            current_text = ""

print(f"Unique symbols used: {len(set(rage_text))}")
print(rage_text)
