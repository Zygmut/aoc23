from pathlib import Path
import click

data_path = (Path(__file__).resolve()).parent / "data" / "input.txt"

if not data_path.exists():
    print("❌ Input file not found. Create `input.txt` under data folder")
    exit(1)

INPUT_CONTENT = data_path.read_text()

@click.command()
def part_1(input_content: str = INPUT_CONTENT):
    """Command for part 1."""
    print("🥇 Part 1")


@click.command()
def part_2(input_content: str = INPUT_CONTENT):
    """Command for part 2."""
    print("🥇 Part 1")


@click.group()
def cli():
    """Base group for the application."""


cli.add_command(part_1)
cli.add_command(part_2)


if __name__ == "__main__":
    cli()
