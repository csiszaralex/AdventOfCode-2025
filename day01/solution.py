import os


def parse_input(file_path: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def part1(data: list[str]) -> int:
    zeros: int = 0
    current: int = 50
    for line in data:

        sign: int = 1 if line[0] == "R" else -1
        value: int = int(line[1:])

        current = (current + sign * value) % 100

        if current == 0:
            zeros += 1
    return zeros


def part2(data: list[str]) -> int:
    zeros: int = 0
    current: int = 50
    last: int = -1
    for line in data:

        sign: int = 1 if line[0] == "R" else -1
        value: int = int(line[1:])
        zeros += value // 100
        value = value % 100

        current = current + sign * value

        if current < 0:
            current += 100
            if last != 0 and current != 0:
                zeros += 1
        elif current >= 100:
            current -= 100
            if last != 0 and current != 0:
                zeros += 1

        if current == 0:
            zeros += 1
        last = current
    return zeros


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
