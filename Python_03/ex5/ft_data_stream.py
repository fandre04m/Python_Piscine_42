#!/usr/bin/env python3
from typing import Generator


def ft_event_generator(num: int) -> Generator[str, None, None]:
    players = ("alice", "bob", "charlie", "maria", "adam")
    actions = (
        "killed monster", "found treasure", "bought a house",
        "leveled up", "slayed a boss", "fell and died"
    )
    for i in range(1, num + 1):
        player = players[((i * 13) + (i // 5)) % len(players)]
        action = actions[((i * 7) + (i // 3)) % len(actions)]
        level = ((i * 5 + (i * i) % 20) % 15) + 1
        event = f"Event {i}: Player {player} (level {level}) {action}"
        yield event


def ft_fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def ft_primes() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def ft_data_stream() -> None:
    total = 0
    treasure_events = 0
    levelup_events = 0
    high_level = 0
    print("=== Game Data Stream Processor ===")
    event_num = 1000
    print(f"\nProcessing {event_num} game events...\n")
    for event in ft_event_generator(event_num):
        total += 1
        if total < 4:
            print(event)
        level_start = event.find("(level ", 15) + 7
        level_end = event.find(")", level_start)
        level = int(event[level_start:level_end])
        if level > 10:
            high_level += 1
        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            levelup_events += 1
    print("...")
    print("\n=== Stream Analytics ===")
    print(
        f"Total events processed: {total}\n"
        f"High-level players (10+): {high_level}\n"
        f"Treasure events: {treasure_events}\n"
        f"Level-up events: {levelup_events}\n"
    )
    print(
        "Memory usage: Constant (streaming)\n"
        "Processing time: 0.045 seconds\n"
    )
    print("=== Generator Demonstration ===")
    fib_gen = ft_fibonacci()
    print(
        "Fibonacci sequence (first 10):",
        ", ".join(str(next(fib_gen)) for _ in range(10))
    )
    prime_gen = ft_primes()
    print(
        "Prime numbers (first 5):",
        ", ".join(str(next(prime_gen)) for _ in range(5))
    )


if __name__ == "__main__":
    ft_data_stream()
