#!/usr/bin/env python3
import sys
import importlib
from importlib.metadata import version
from typing import List


def compare_dependencies(installed_vers: List[str]) -> None:
    print("Comparing dependency management (pip vs Poetry)...\n")

    pip_deps = {}
    poetry_deps = {}

    # Read requirements.txt (pip)
    try:
        with open("requirements.txt") as f:
            for line in f:
                if "==" in line:
                    name, ver = line.strip().split("==")
                    pip_deps[name] = ver
    except FileNotFoundError:
        print("File 'requirements.txt' not found")
    # Read pyproject.toml (Poetry)
    try:
        with open("pyproject.toml") as f:
            for line in f:
                if "^" in line and not line.startswith("["):
                    parts = line.strip().split("=")
                    if len(parts) == 2:
                        name = parts[0].strip()
                        ver = parts[1].strip().replace('"', '')
                        poetry_deps[name] = ver
    except FileNotFoundError:
        print("File 'pyproject.toml' not found")
    # Print based on current environment
    path = sys.prefix
    if "pypoetry/" in path:
        print("CURRENT ENVIRONMENT - POETRY (pyproject.toml):")
        for (pkg, ver), i_ver in zip(poetry_deps.items(), installed_vers):
            print(f" - Required: {pkg}={ver} --> Installed version: {i_ver}")
    else:
        print("CURRENT ENVIRONMENT - PIP (requirements.txt):")
        for (pkg, ver), i_ver in zip(pip_deps.items(), installed_vers):
            print(f"Required: {pkg}=={ver} --> Installed version: {i_ver}")


def matrix_organizer() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    matrix_data = np.random.randint(1, 201, size=(500, 2))
    print(
        f"Processing {matrix_data.shape[0] * matrix_data.shape[1]} "
        "data points..."
    )
    data_frame = pd.DataFrame(data=matrix_data, columns=['Health', 'Stamina'])

    plt.title('Agent Profile - Health vs. Stamina')
    plt.scatter(data_frame['Health'], data_frame['Stamina'], alpha=0.5)
    plt.xlabel('Health Score')
    plt.ylabel('Stamina Score')
    plt.grid(True, linestyle='--')

    print("Generating visualization...\n")
    print("Analysis complete!")
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.show()
    print(f"Results saved to: {output_file}")


def main() -> None:
    dependencies = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualization ready"
    }
    missing = []
    if not (sys.prefix != sys.base_prefix):
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
        print("Checking dependencies:")
        if missing:
            for package in missing:
                print(f"[KO] {package} package missing")
            print(
                "\nTo install with pip: 'pip install -r requirements.txt'\n"
                "To install with poetry: 'poetry install'"
            )
        else:
            versions = []
            for package, status in dependencies.items():
                ver = version(package)
                versions.append(ver)
                print(f"[OK] {package} ({ver}) - {status}")
            print()
            matrix_organizer()
            compare_dependencies(versions)


if __name__ == "__main__":
    main()
