import re

output = list()

while True:
    text = input()
    if text == "":
        print(" ".join(output))
        break
    expression = r"\d+"
    matches = re.findall(expression, text)
    for match in matches:
        output.append(match)
