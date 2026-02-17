#!/usr/bin/env python3

def ft_score_analytics() -> None:
    import sys
    print("=== Garden Score Analytics ===")
    scores = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                score = int(arg)
                scores.append(score)
            except ValueError:
                print(f"'{arg}' -> Not a valid score!")
        print(
            f"Scores processed: {scores}\n"
            f"Total players: {len(sys.argv) - 1}\n"
            f"Total score: {sum(scores)}\n"
            f"Average score: {sum(scores) / len(scores)}\n"
            f"High score: {max(scores)}\n"
            f"Low score: {min(scores)}\n"
            f"Score range: {max(scores) - min(scores)}"
        )
    else:
        print(
            f"No scores provided. Usage: pyhton3 {sys.argv[0]} "
            "<score1> <score2> ..."
        )


if __name__ == "__main__":
    ft_score_analytics()
