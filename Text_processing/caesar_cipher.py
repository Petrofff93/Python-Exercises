my_text = input()
decrypted = ""

for i in my_text:
    decrypted += chr(ord(i)+3)
print(decrypted)
