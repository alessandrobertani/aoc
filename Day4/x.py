
def contains(x: list[int], y: list[int]) -> bool:
    return x[0] <= y[0] and x[1] >= y[1]

def ranges_overlap(x: list[int], y: list[int]) -> bool:
    return x[0] <= y[0] <= x[1] or y[0] <= x[0] <= y[1]

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    
    total_contained = 0
    total_overlap = 0
    for line in lines:
        ranges = line.strip().split(",")
        x, y = [int(x) for x in ranges[0].split("-")], [int(x) for x in ranges[1].split("-")]
        
        # PART 1
        if contains(x, y) or contains(y, x):
            total_contained += 1

        # PART 2
        if ranges_overlap(x, y):
            total_overlap += 1

    print(total_contained)
    print(total_overlap)

if __name__ == '__main__':
    main()