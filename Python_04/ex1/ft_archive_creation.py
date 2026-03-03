#!/usr/bin/env python3


def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    archive = None
    try:
        archive = open("new_discovery.txt", "w")
        print(f"Initializing new storage unit: {archive.name}")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        entries = (
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
        )
        archive.write(entries)
        print(entries)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{archive.name}' ready for long-term preservation.")
        archive.close()
    except OSError as e:
        print(e)
        print("Closing archive securely")
        if archive is not None:
            archive.close()


if __name__ == "__main__":
    ft_archive_creation()
