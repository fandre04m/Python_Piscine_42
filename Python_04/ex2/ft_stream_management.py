#!/usr/bin/env python3
import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        arch_id = input("Input Stream active. Enter archivist ID: ")
        stat_report = input("Input Stream active. Enter status report: ")
        print(
            f"\n[STANDARD] Archive status from {arch_id}: {stat_report}",
            file=sys.stdout
        )
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr
        )
        print("[STANDARD] Data transmission complete")
    except OSError as e:
        print(f"UNEXPECTED ERROR: {e}", file=sys.stderr)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
