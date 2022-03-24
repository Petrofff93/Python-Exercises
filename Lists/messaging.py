num_sequence = input().split(" ")
text_string = input()
new_text = ''
sum = 0

for seq in num_sequence:
    for ele in seq:
        sum += int(ele)
    if sum > len(text_string):
        sum -= len(text_string)
    new_text += text_string[sum]
    new_string = list(text_string)
    new_string.pop(sum)
    text_string = ''
    sum = 0

    for i in new_string:
        text_string += i

print(new_text)