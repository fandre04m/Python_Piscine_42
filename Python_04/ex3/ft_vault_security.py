#!/usr/bin/env python3


def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt") as c_file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(c_file.read())
        with open("classified_data.txt", "a") as s_file:
            message = "[CLASSIFIED] New security protocols archived"
            s_file.write(message)
            print("SECURE PRESERVATION:")
            print(message)
            print("Vault automatically sealed upon completion")
    except OSError as e:
        print(e)
        print("Vault automatically sealed after error")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
