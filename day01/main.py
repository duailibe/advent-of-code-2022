import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        data = f.read().strip()

    calories = sorted(
        [sum(map(int, elf.split("\n"))) for elf in data.split("\n\n")],
        reverse=True,
    )

    print("Part 1:", calories[0])
    print("Part 2:", sum(calories[:3]))
