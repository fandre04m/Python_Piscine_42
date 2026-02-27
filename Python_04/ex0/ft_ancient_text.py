#!/usr/bin/env python3

def ft_recover_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    text = None
    try:
        text = open("ancient_fragments.txt")
        print(
            f"Accessing Storage Vault: {text.name}\n"
            "Connection established...\n\n"
            "RECOVERED DATA:"
        )
        print(text.read())
    except OSError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if text is not None:
            text.close()
            print("\nData recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    ft_recover_text()
