#!/usr/bin/env python3
import sys
import importlib


def matrix_organizer() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    matrix_data = np.random.randn(100, 3)
    print(matrix_data[:5])
    print()
    data_frame = pd.DataFrame(data=matrix_data, columns=['Health', 'Strength', 'Stamina'])
    print(data_frame[data_frame['Strength'] > 1.5])
    print()
    plt.title('Agent Profile - Health vs. Stamina')
    plt.scatter(data_frame['Health'], data_frame['Stamina'], alpha=0.5)
    plt.xlabel('Health Score')
    plt.ylabel('Stamina Score')
    plt.grid(True)
    plt.show()


def main() -> None:
    dependencies = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualization ready"
    }
    missing = []
    is_venv = (sys.prefix != sys.base_prefix)
    if not is_venv:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(
            "To enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\n"
            "Then run this program again."
        )
    else:
        print("\nLOADING STATUS: Loading programs...\n")
        for package in dependencies.keys():
            try:
                importlib.import_module(package)
            except ImportError:
                missing.append(package)
        if missing:
            print(f"ERROR - Missing dependencies: {', '.join(missing)}")
            print(
                "For pip run: 'pip install -r requirements.txt'\n"
                "For poetry run: 'poetry install'"
            )
        else:
            print(
                ""
            )
            matrix_organizer()


if __name__ == "__main__":
    main()
