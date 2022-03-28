word = input()
new_word = ""

for i in range(len(word)):
    if len(new_word) == 0:
        new_word += word[i]
    if new_word[-1] == word[i]:
        continue
    else:
        new_word += word[i]

print(new_word)




