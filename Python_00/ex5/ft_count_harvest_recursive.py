def count_recursive(days):
    if days <= 0:
        return
    count_recursive(days - 1)
    print("Day ", days)


def ft_count_harvest_recursive():
    days_left = int(input("Days until harvest: "))
    count_recursive(days_left)
    print("Harvest time!")
