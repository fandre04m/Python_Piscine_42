#!/usr/bin/env python3

def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {
            "first_kill", "treasure_hunter", "speed_demon",
            "first_kill", "first_kill", "level_10"
    }
    bob = {
            "level_10", "boss_slayer", "collector",
            "level_10", "level_10", "first_kill"
    }
    charlie = {
            "treasure_hunter", "boss_slayer", "perfectionist",
            "speed_demon", "level_10",
            "boss_slayer", "level_10"
    }
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")


if __name__ == "__main__":
    ft_achievement_tracker()
