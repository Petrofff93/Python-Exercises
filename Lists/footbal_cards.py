def football_cars(card):
    a_team = 11
    b_team = 11

    cards_list = set(card.split(" "))
    is_end = False

    for item in cards_list:
        if "A" in item:
            a_team -= 1
        elif "B" in item:
            b_team -= 1
        if a_team < 7 or b_team < 7:
            is_end = True
            break

    if is_end:
        print(f"Team A - {a_team}; Team B - {b_team}")
        print("Game was terminated")
    else:
        print(f"Team A - {a_team}; Team B - {b_team}")


football_cars(input())
