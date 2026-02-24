#!/usr/bin/env python3

import sys


def percentage_of_total(
    inv_items: dict,
    total_qty: int
) -> None:
    for name, qty in inv_items.items():
        percentage = (qty / total_qty) * 100
        print(
            f"{name}: {qty} {'unit' if qty == 1 else 'units'}"
            f" ({percentage:.1f}%)"
        )


def get_statistics(inv_items: dict) -> None:
    big = ["name", 0]
    small = ["name", sys.maxsize]
    for name, qty in inv_items.items():
        if qty > big[1]:
            big = (name, qty)
        if qty < small[1]:
            small = (name, qty)
    print(
        f"Most abundant: "
        f"{big[0]} ({big[1]} {'unit' if big[1] == 1 else 'units'})"
    )
    print(
        f"Least abundant: "
        f"{small[0]} ({small[1]} {'unit' if small[1] == 1 else 'units'})"
    )


def get_categories(inv_items: dict) -> None:
    categories = {
        "abundant": {},
        "moderate": {},
        "scarce": {}
    }
    for name, qty in inv_items.items():
        if qty < 4:
            categories["scarce"].update({name: qty})
        elif qty > 6:
            categories["abundant"].update({name: qty})
        else:
            categories["moderate"].update({name: qty})
    for category, items in categories.items():
        if len(items) > 0:
            print(f"{category.capitalize()}: {items}")


def check_existence(
    item_name: str,
    inv_items: dict
) -> bool:
    return item_name in inv_items


def ft_inventory_system() -> None:
    inv_items = {}
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        for item in sys.argv[1:]:
            try:
                name, qty = item.split(":")
                qty = int(qty)
                if qty < 1:
                    print(f"Invalid quantity for {item}, must be 1 or more")
                    continue
                inv_items[name] = qty
            except ValueError:
                print(f"Invalid format: {item}")
        qty_list = inv_items.values()
        total_qty = 0
        for num in qty_list:
            total_qty += num
        if total_qty == 0:
            return
        print(f"Total items in inventory: {total_qty}")
        item_types = len(inv_items)
        print(f"Unique item types: {item_types}")
        print("\n=== Current Inventory ===")
        percentage_of_total(inv_items, total_qty)
        print("\n=== Inventory Statistics ===")
        get_statistics(inv_items)
        print("\n=== Item Categories ===")
        get_categories(inv_items)
        restock = []
        for name, qty in inv_items.items():
            if qty == 1:
                restock.append(name)
        if len(restock) > 0:
            print("\n=== Management Suggestions ===")
            print(f"Restock needed: {restock}")
        print("\n=== Dictionary Properties Demo ===")
        print("Dictionary keys:", ", ".join(inv_items.keys()))
        print(
            "Dictionary values:",
            ", ".join(str(val) for val in inv_items.values())
        )
        check = check_existence("sword", inv_items)
        print(f"Sample lookup - 'sword' in inventory: {check}")
    else:
        print(
            "Must have at least 1 argument.\n"
            "Ex: python3 ft_inventory_system <item:quantity> <item:quantity>"
        )


if __name__ == "__main__":
    ft_inventory_system()
