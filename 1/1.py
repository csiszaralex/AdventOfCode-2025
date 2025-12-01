file: str = "./input.txt"


zeros: int = 0
current: int = 50

with open(file) as f:
    for line in f:

        sign: int = 1 if line[0] == "R" else -1
        value: int = int(line[1:])

        current = (current + sign * value) % 100

        if current == 0:
            zeros += 1
        # print(value, current, line)

print(zeros)
