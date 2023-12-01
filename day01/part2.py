from __future__ import annotations

import argparse
import os.path

import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

DIGITS_TEXT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digits(line: str) -> list[int]:
    line_length = len(line)
    digits: list[int] = []
    for i, c in enumerate(line):
        # pretty ugly way to do this, but it works
        if c.isdigit():
            digits.append(int(c))
        if (potential_digit := line[i:min(i+3, line_length)]) in DIGITS_TEXT:
            digits.append(DIGITS_TEXT[potential_digit])
        if (potential_digit := line[i:min(i+4, line_length)]) in DIGITS_TEXT:
            digits.append(DIGITS_TEXT[potential_digit])
        if (potential_digit := line[i:min(i+5, line_length)]) in DIGITS_TEXT:
            digits.append(DIGITS_TEXT[potential_digit])
    return digits


def compute(s: str) -> int:
    lines = s.splitlines()
    result = 0
    for line in lines:
        digits = get_digits(line.strip())
        first_digit, last_digit = digits[0], digits[-1]
        num = first_digit * 10 + last_digit
        result += num
    return result


INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
EXPECTED = 281


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
