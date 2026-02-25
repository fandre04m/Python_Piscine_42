#!/usr/bin/env python3

def ft_list_comprehensions() -> None:
    scores = [
        ("alice", 2300, True),
        ("bob", 1800, True),
        ("charlie", 2150, True),
        ("diana", 2050, False)
    ]
    high_scores = [name for name, score, _ in scores if score > 2000]
    doubled_scores = [score * 2 for _, score, _ in scores]
    active_players = [name for name, _, active in scores if active]
    print(
        f"Hight scores (>2000): {high_scores}\n"
        f"Scores doubled: {doubled_scores}\n"
        f"Active players: {active_players}\n"
    )


def ft_dict_comprehensions() -> None:
    players = {
        "alice": {
            "score": 2300,
            "achievements": [
                "treasure_hunter",
                "boss_slayer",
                "level_10",
                "first_kill",
                "indomitable"
            ],
            "special scores": [1337, 2450]
        },
        "bob": {
            "score": 1800,
            "achievements": [
                "treasure_hunter",
                "level_10",
                "pacifist"
            ],
            "special scores": [999, 1870, 2001]
        },
        "charlie": {
            "score": 2150,
            "achievements": [
                "treasure_hunter",
                "boss_slayer",
                "level_10",
                "first_kill",
                "indomitable",
                "death_bringer",
                "bug_stomper"
            ],
            "special scores": [867, 2500]
        }
    }
    scores = {
        "alicya": 2350,
        "robert": 1875,
        "jean": 999,
        "frank": 1337,
        "jules": 9000,
        "arthur": 2470
    }
    player_scores = {name: data["score"] for name, data in players.items()}
    score_categ = {
        "high": sum(1 for score in scores.values() if score > 2000),
        "medium": sum(1 for score in scores.values() if 1000 <= score <= 2000),
        "low": sum(1 for score in scores.values() if score < 1000)
    }
    achiev_num = {
        name: len(data["achievements"]) for name, data in players.items()
    }
    print(
        f"Player scores: {player_scores}\n"
        f"Score categories: {score_categ}\n"
        f"Achievement counts: {achiev_num}\n"
    )


# def ft_set_comprehensions() -> None:


def ft_analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    ft_list_comprehensions()
    print("=== Dict Comprehension Examples ===")
    ft_dict_comprehensions()


if __name__ == "__main__":
    ft_analytics_dashboard()
