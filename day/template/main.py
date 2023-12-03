from pathlib import Path


def part_1(input_content: str):
    """Command for part 1."""


def part_2(input_content: str):
    """Command for part 2."""


if __name__ == "__main__":
    data_path = (Path(__file__).resolve()).parent / "data" / "input.txt"

    if not data_path.exists():
        print("❌ Input file not found. Create `input.txt` under data folder")
        exit(1)

    input_content = data_path.read_text()

    print("Part 1")
    print(part_1(input_content))

    print("Part 2")
    print(part_2(input_content))
