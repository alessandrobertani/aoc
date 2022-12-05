
POINTS = {"win": 6, "draw": 3, "loss": 0, "X": 1, "Y": 2, "Z": 3}
RES = {"X": "loss", "Y": "draw", "Z": "win"}

def compute_round(opp: str, my: str):
    match [opp, my]:
        case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
            return "draw"
        case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
            return "win"
        case ["A", "Z"] | ["B", "X"] | ["C", "Y"]:
            return "loss"

def compute_round_modified(opp: str, outcome: str):
    match [opp, outcome]:
        case ["A", "draw"] | ["B", "loss"] | ["C", "win"]:
            return "X"
        case ["A", "loss"] | ["B", "win"] | ["C", "draw"]:
            return "Z"
        case ["A", "win"] | ["B", "draw"] | ["C", "loss"]:
            return "Y"


def compute_points(my: str, res: str):
    return POINTS[my] + POINTS[res]

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # PART 1
    total_score = 0
    for line in lines:
        opp, my = line.strip().split()
        res = compute_round(opp, my)
        total_score += compute_points(my, res)

    print(total_score)

    # PART 2
    total_score = 0
    for line in lines:
        opp, res = line.strip().split()
        res = RES[res]
        my = compute_round_modified(opp, res)
        total_score += compute_points(my, res)

    print(total_score)

if __name__ == '__main__':
    main()