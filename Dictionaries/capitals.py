countries = input().split(", ")
capital = input().split(", ")

my_dict = {item: value for (item, value) in list(zip(countries, capital))}
for key, value in my_dict.items():
    print(f"{key} -> {value}")
