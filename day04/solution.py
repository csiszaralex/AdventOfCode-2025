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


def part1(data: list[str]) -> int:
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@" and how_much_neighbour(data, i, j) < 4:
                # print(f"i: {i}, j: {j}")
                sum += 1
    return sum


def part2(data: list[str]) -> int:
    sum = 0
    removed = 1
    while removed > 0:
        removed = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "@" and how_much_neighbour(data, i, j) < 4:
                    print(f"i: {i}, j: {j}")
                    data[i] = data[i][:j] + "." + data[i][j + 1 :]
                    removed += 1
                    sum += 1
    return sum


def how_much_neighbour(list: list[str], i: int, j: int) -> int:
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < len(list) and 0 <= nj < len(list[0]):
                if list[ni][nj] == "@":
                    count += 1
    return count


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
