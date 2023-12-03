from pathlib import Path
from functools import reduce


def part_1(input_content: str):
    input_data: list[str] = input_content.splitlines()

    numbers = [tuple(filter(str.isdigit, line)) for line in input_data]
    print(numbers)
    composed_numbers = [f"{number[0]}{number[-1]}" for number in numbers]
    res = sum(map(int, composed_numbers))
    return res


def part_2(input_content: str):
    input_data = input_content.splitlines()

    trans_data = [replace_text_numbers(line) for line in input_data]
    res = part_1(input_content="\n".join(trans_data))
    return res


def replace_text_numbers(line: str) -> str:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    replace_list = []
    start = 0
    for i in range(len(line) + 1):
        for number, replacement in number_map.items():
            if number in line[start:i]:
                replace_list.append(number)
                start = i - 1
                break

    return reduce(
        lambda acc, val: acc.replace(val, f"|{number_map.get(val, " | ")}|"),
        replace_list,
        line,
    )


if __name__ == "__main__":
    data_path = (Path(__file__).resolve()).parent / "data" / "input.txt"

    if not data_path.exists():
        print("ERROR: Input file not found. Create `input.txt` under data folder")
        exit(1)

    input_content = data_path.read_text()

    print("Part 1")
    print(part_1(input_content))

    print("Part 2")
    print(part_2(input_content))
