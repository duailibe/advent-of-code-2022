import os


winner = lambda i: (i + 1) % 3
loser = lambda i: (i - 1) % 3


def score_part_1(play):
    [opponent, mine] = play
    op_index = "ABC".index(opponent)
    mine_index = "XYZ".index(mine)

    points = mine_index + 1
    if mine_index == op_index:
        points += 3
    elif mine_index == winner(op_index):
        points += 6

    return points


def score_part_2(play):
    [opponent, result] = play

    op_index = "ABC".index(opponent)
    points = "XYZ".index(result) * 3

    if result == "X":
        points += loser(op_index) + 1
    elif result == "Y":
        points += op_index + 1
    else:
        points += winner(op_index) + 1

    return points


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        data = f.read().strip()

    plays = [play.split() for play in data.split("\n")]

    print("Part 1:", sum(map(score_part_1, plays)))
    print("Part 1:", sum(map(score_part_2, plays)))
