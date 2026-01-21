def ft_count_harvest_iterative():
    days_left = int(input("Days until harvest: "))
    for day in range(1, days_left + 1):
        print("Day ", day)
    print("Harvest time!")
