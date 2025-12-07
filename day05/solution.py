import os
import sys


def parse_input(file_path: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_input_files() -> list[str]:
    current_dir = os.path.dirname(__file__)
    txt_files = [f for f in os.listdir(current_dir) if f.endswith(".txt")]
    txt_files.sort()
    return txt_files


def part1Old(lines: list[str]) -> int:
    isFirst = True
    fresh: set[int] = set()
    sum = 0
    for line in lines:
        if line.strip() == "":
            isFirst = False
            continue
        if isFirst:
            start, end = map(int, line.split("-"))
            for num in range(start, end + 1):
                fresh.add(num)
        else:
            if not int(line) in fresh:
                sum += 1

    return sum


def part1(lines: list[str]) -> int:
    isFirst = True
    sum = 0
    fresh_ranges: list[tuple[int, int]] = []
    for line in lines:
        if line.strip() == "":
            isFirst = False
            continue
        if isFirst:
            start, end = map(int, line.split("-"))
            fresh_ranges.append((start, end))
        else:
            num = int(line)
            for start, end in fresh_ranges:
                if start <= num <= end:
                    sum += 1
                    break

    return sum


def part2(lines: list[str]) -> int:
    fresh_ranges: list[tuple[int, int]] = []
    for line in lines:
        if line.strip() == "":
            break
        start, end = map(int, line.split("-"))
        fresh_ranges.append((start, end))
    fresh_ranges.sort(key=lambda x: x[0])

    merged: list[tuple[int, int]] = []
    curr_start, curr_end = fresh_ranges[0]
    for next_start, next_end in fresh_ranges[1:]:
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
        print(merged)
    merged.append((curr_start, curr_end))
    full = sum((end - start + 1) for start, end in merged)


    return full


if __name__ == "__main__":
    txt_files = get_input_files()
    if not txt_files:
        print("Nem található .txt fájl a mappában.")
        sys.exit()

    print("Elérhető fájlok:")
    for i, filename in enumerate(txt_files, 1):
        print(f"{i}. {filename}")

    choice = int(input("\nVálassz egy számot: ")) if len(txt_files) > 1 else 1
    if 1 <= choice <= len(txt_files):
        selected_file = txt_files[choice - 1]
        print(f"---> Futtatás ezzel: {selected_file}")

        data = parse_input(selected_file)
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
    else:
        print("Érvénytelen sorszám.")
