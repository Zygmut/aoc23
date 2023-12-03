from pathlib import Path
from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass
class Reveal:
    red: int
    green: int
    blue: int

    @staticmethod
    def from_list(data: list[str]):
        obj_vars = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for single_reveal in data:
            obj_vars.update(
                {single_reveal.split(" ")[1].lower(): int(single_reveal.split(" ")[0])}
            )

        return Reveal(obj_vars.get("red"), obj_vars.get("green"), obj_vars.get("blue"))

    @staticmethod
    def to_tuple(reveal) -> tuple:
        return (reveal.red, reveal.green, reveal.blue)


@dataclass
class Game:
    identifier: int
    reveals: list[Reveal]

    @staticmethod
    def from_str(line: str):
        return Game(
            identifier=line.split(":")[0].split(" ")[1],
            reveals=list(
                map(
                    Reveal.from_list,
                    [reveal.split(", ") for reveal in line.split(": ")[1].split("; ")],
                )
            ),
        )


def part_1(input_content: str, restriction: dict) -> int:
    """Command for part 1."""
    input_data = input_content.splitlines()
    games = tuple(map(Game.from_str, input_data))
    reveals = tuple(
        (int(game.identifier), tuple(map(Reveal.to_tuple, game.reveals)))
        for game in games
    )
    max_balls = tuple(
        (reveal_group[0], tuple(map(max, zip(*reveal_group[1]))))
        for reveal_group in reveals
    )
    compliant_games = tuple(
        game[0]
        for game in max_balls
        if game[1][0] <= restriction.get("red")
        and game[1][1] <= restriction.get("green")
        and game[1][2] <= restriction.get("blue")
    )

    return sum(compliant_games)


def part_2(input_content: str):
    """Command for part 2."""

    input_data = input_content.splitlines()
    games = tuple(map(Game.from_str, input_data))
    reveals = tuple(tuple(map(Reveal.to_tuple, game.reveals)) for game in games)
    max_balls = tuple(tuple(map(max, zip(*reveal_group))) for reveal_group in reveals)
    powers = tuple(reduce(mul, ball_set, 1) for ball_set in max_balls)

    return sum(powers)


if __name__ == "__main__":
    data_path = (Path(__file__).resolve()).parent / "data" / "input.txt"

    if not data_path.exists():
        print("❌ Input file not found. Create `input.txt` under data folder")
        exit(1)

    input_content = data_path.read_text()
    restriction = {"red": 12, "green": 13, "blue": 14}

    # print("Part 1")
    # print(part_1(input_content, restriction))

    print("Part 2")
    print(part_2(input_content))
