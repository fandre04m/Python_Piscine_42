#!/usr/bin/env python3

def ft_coordinate_system() -> None:
    #    import sys
    print("=== Game Coordinate System ===")
    bad_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{bad_str}\"")
    coord_list = bad_str.split(",")
    try:
        for coord in coord_list:
            coord = int(coord)
        bad_tuple = tuple(coord_list)
        print(f"{bad_tuple}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f"Error details - Type: {e.__class__.__name__}, "
            f"Args: {e.args}"
        )


if __name__ == "__main__":
    ft_coordinate_system()
