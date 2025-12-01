import os


def parse_input(file_path: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def part1(data: list[str]) -> None:
    return None


def part2(data: list[str]) -> None:
    return None


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
