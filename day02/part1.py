from __future__ import annotations

import argparse
import os.path

import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
BAG_CONTENT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_record(record: str) -> dict[str, int]:
    record_dict: dict[str, int] = {}
    for item in record.split(','):
        count, color = item.split()
        record_dict[color.strip()] = int(count)
    return record_dict


def parse_line(line: str) -> tuple[int, list[dict[str, int]]]:
    game, record = line.split(':')
    game_id = int(game.split()[1])
    records = record.split(';')
    all_records_dicts: list[dict[str, int]] = []
    for record in records:
        record_dict = parse_record(record)
        all_records_dicts.append(record_dict)
    return game_id, all_records_dicts


def is_possible(record_dict: dict[str, int]) -> bool:
    return (
        record_dict.get("red", 0) <= BAG_CONTENT["red"]
        and record_dict.get("green", 0) <= BAG_CONTENT["green"]
        and record_dict.get("blue", 0) <= BAG_CONTENT["blue"]
    )


def is_possible_all(all_records_dicts: list[dict[str, int]]) -> bool:
    return all(is_possible(record_dict) for record_dict in all_records_dicts)


def compute(s: str) -> int:
    lines = s.splitlines()
    result = 0
    for line in lines:
        game_id, all_records_dicts = parse_line(line)
        if is_possible_all(all_records_dicts):
            result += game_id
    return result


INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
EXPECTED = 8


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
