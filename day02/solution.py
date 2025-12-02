import os


def parse_input(file_path: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def has_pattern(n: str) -> bool:
    l = len(n)
    for i in range(1, l // 2 + 1):
        if not l % i == 0:
            continue
        count = l // i
        first_segment = n[0:i]
        for j in range(count):
            if n[j * i : (j + 1) * i] != first_segment:
                break
        else:
            return True

    return False


def part1(data: list[str]) -> int:
    sum: int = 0
    ranges = data[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            n = str(n)
            l = len(n)
            if n[0] == "0" and l > 1:
                sum += int(n[1:])
            elif l % 2 == 0:
                # print(n, n[0 : l // 2], n[l // 2 :])
                if n[0 : l // 2] == n[l // 2 :]:

                    sum += int(n)
    return sum


def part2(data: list[str]) -> int:
    sum: int = 0
    ranges = data[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if has_pattern(str(n)):
                sum += n
    return sum


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
