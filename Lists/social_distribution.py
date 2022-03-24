def social_distribution(population, minimum_wage):
    is_equal = True
    for item in population:
        if item < minimum_wage:
            need = minimum_wage - item
            wealthiest = max(population)
            index_rich = population.index(wealthiest)
            index_poor = population.index(item)
            if wealthiest - need >= minimum_wage:
                population[index_rich] -= need
                population[index_poor] += need
            else:
                is_equal = False
                break
    if is_equal:
        print(population)
    else:
        print("No equal distribution possible")


peoples_wage = list(map(int, input().split(", ")))
minimum = int(input())
social_distribution(peoples_wage, minimum)