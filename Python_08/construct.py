#!/usr/bin/env python3
import sys
import os


def inside_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")


def outside_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print(
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"
    )
    print(
        "To enter the construct, run:\n"
        "python3 -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n"
        "\n"
        "Then run this program again."
    )


def main() -> None:
    is_venv = (sys.prefix != sys.base_prefix)
    if is_venv:
        inside_venv()
    else:
        outside_venv()


if __name__ == "__main__":
    main()
