#!/usr/bin/env python3
import math


def coord_parser(coord_str: str) -> tuple:
    coord_list = coord_str.split(",")
    try:
        parsed_list = [int(c) for c in coord_list]
        coord_tuple = tuple(parsed_list)
        print(f"Parsed position: {coord_tuple}")
        return coord_tuple
    except ValueError as e:
        raise ValueError(
                f"{e}\nError details - Type: {e.__class__.__name__}, "
                f"Args: {e.args}"
                )


def distance_calculator(old_pos: tuple, new_pos: tuple) -> float:
    x1, y1, z1 = old_pos
    x2, y2, z2 = new_pos
    distance = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2 +
            (z2 - z1) ** 2
            )
    return distance


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    old_pos = (0, 0, 0)
    manual_pos = (10, 20, 5)
    print(f"\nPosition created: {manual_pos}")
    distance = distance_calculator(old_pos, manual_pos)
    print(f"Distance between {old_pos} and {manual_pos}: {distance:.2f}")
    good_str = "3,4,0"
    print(f"\nParsing coordinates: \"{good_str}\"")
    try:
        new_pos = coord_parser(good_str)
        distance = distance_calculator(old_pos, new_pos)
        print(f"Distance between {old_pos} and {new_pos}: {distance}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    bad_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{bad_str}\"")
    try:
        coord_parser(bad_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    print("\nUnpacking demonstration:")
    curr_pos = (3, 4, 0)
    x, y, z = curr_pos
    print(f"Player at x={curr_pos[0]}, y={curr_pos[1]}, z={curr_pos[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
