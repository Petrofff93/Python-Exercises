char1 = input()
char2 = input()
sequence = input()
total = 0

for i in range((ord(char1)+1), ord(char2)):
    for k in sequence:
        if ord(k) == i:
            total += i
print(total)
