#!/usr/bin/env python3


def error_handler(file_name: str) -> None:
    try:
        with open(file_name) as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file.name}'...")
            print(f"SUCCESS: Archive recovered - \''{file.read()}'\'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except OSError as e:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, all systems green")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    error_handler("lost_archive.txt")
    print()
    error_handler("classified_data.txt")
    print()
    error_handler("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
