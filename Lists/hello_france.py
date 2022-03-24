def hello_france(items, budget):
    ticket_price = 150
    profit = 0
    all_items = items.split("|")
    shopping_list = list()

    for item in all_items:
        current_item = item.split("->")
        i = current_item[0]
        price = float(current_item[1])

        if i == "Clothes" and price <= 50:
            pass
        elif i == "Shoes" and price <= 35:
            pass
        elif i == "Accessories" and price <= 20.50:
            pass
        else:
            continue
        if budget >= price:
            budget -= price
            my_price = f'{(price * 1.4):.2f}'
            shopping_list.append(my_price)
            profit += price * 0.40
    new_list = [float(num) for num in shopping_list]

    total_sum = sum(new_list) + budget
    if total_sum >= ticket_price:
        print(*shopping_list)
        print(f"Profit: {profit:.2f}")
        print("Hello, France!")
    else:
        print(*shopping_list)
        print(f"Profit: {profit:.2f}")
        print("Not enough money.")


hello_france(input(), int(input()))