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


def part1(data: list[str]) -> None:
    return None


def part2(data: list[str]) -> None:
    return None


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
