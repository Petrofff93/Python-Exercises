fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0

print("Cells:")

for cell in fire_cells:
    cells = cell.split(" = ")
    fire_type = cells[0]
    cell_value = int(cells[1])

    if fire_type == "High" and 81 <= cell_value <= 125:
        pass
    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        pass
    elif fire_type == "Low" and 1 <= cell_value <= 50:
        pass
    else:
        continue
    if water == 0:
        break
    if water < cell_value:
        continue
    else:
        water -= cell_value
        print(f"- {cell_value}")
        effort += cell_value * 0.25
        total_fire += cell_value

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")