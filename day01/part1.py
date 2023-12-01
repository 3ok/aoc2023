from __future__ import annotations

import argparse
import os.path

import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_digit(line: str, *, first: bool) -> int:
    line_iter = line if first else reversed(line)
    for c in line_iter:
        if c.isdigit():
            return int(c)
    raise AssertionError(f'no digit found in {line}')


def compute(s: str) -> int:
    lines = s.splitlines()
    result = 0
    for line in lines:
        first_digit, last_digit = get_digit(
            line, first=True,
        ), get_digit(line, first=False)
        num = first_digit * 10 + last_digit
        result += num
    return result


INPUT_S = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
EXPECTED = 142


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
