file: str = "./input.txt"

zeros: int = 0
current: int = 50
last: int = -1

with open(file) as f:
    for line in f:

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
        # print(f"{line.strip()} -> {current} ({zeros})")

print(zeros)
