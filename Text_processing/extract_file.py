file_path = input().split("\\")
my_file = file_path[-1].split(".")
file = my_file[0]
extension = my_file[1]

print(f"File name: {file}")
print(f"File extension: {extension}")


