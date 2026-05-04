#!/usr/bin/env python3


artifacts = [
    {
        'name': 'Ice Wand',
        'power': 71,
        'type': 'accessory'
    },
    {'name': 'Ice Wand', 'power': 112, 'type': 'armor'},
    {'name': 'Fire Staff', 'power': 104, 'type': 'weapon'},
    {'name': 'Lightning Rod', 'power': 80, 'type': 'relic'},
    {'name': 'Fire Staff', 'power': 118, 'type': 'focus'}
]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (
            list(sorted(artifacts, key=lambda item: item["power"]))
    )


def main() -> None:
    sorted_list = artifact_sorter(artifacts)
    print(sorted_list)


if __name__ == "__main__":
    main()
