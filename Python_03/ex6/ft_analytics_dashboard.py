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


def ft_dict_comprehensions(players: dict) -> None:
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


def ft_set_comprehensions() -> None:
    players = [
        "alice",
        "bob",
        "charlie",
        "diana",
        "alice",
        "charlie"
    ]
    achievements = [
        "treasure_hunter",
        "boss_slayer",
        "level_10",
        "first_kill",
        "treasure_hunter",
        "first_kill",
        "level_10"
    ]
    regions = {
        "north": "active",
        "central": "active",
        "east": "active",
        "west": "stand-by"
    }
    unique_players = {player for player in players}
    unique_achiev = {achiev for achiev in achievements}
    active_regions = {
        region for region, state in regions.items() if state == "active"
    }
    print(
        f"Unique players: {unique_players}\n"
        f"Unique achievements: {unique_achiev}\n"
        f"Active regions: {active_regions}\n"
    )


def ft_analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    ft_list_comprehensions()
    print("=== Dict Comprehension Examples ===")
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
    ft_dict_comprehensions(players)
    print("=== Set comprehension Examples ===")
    ft_set_comprehensions()
    print("=== Combined Analysis ===")
    total_players = len(players)
    tot_uniq_achiev = len({
            achiev for data in players.values()
            for achiev in data["achievements"]
    })
    average_score = sum([
        data["score"] for data in players.values()
    ]) / len(players)
    player_stats = [
        (data["score"], name, len(data["achievements"]))
        for name, data in players.items()
    ]
    top_score, top_name, top_achiev = max(player_stats)
    print(
        f"Total players: {total_players}\n"
        f"Total unique achievements: {tot_uniq_achiev}\n"
        f"Average score: {average_score:.1f}\n"
        f"Top perfomer: {top_name} "
        f"({top_score} points, {top_achiev} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
