my_text = input()

result = [my_text[i] + my_text[i + 1] for i in range(len(my_text))
          if my_text[i] == ":" and my_text[i] != " "]
[print(x) for x in result]
