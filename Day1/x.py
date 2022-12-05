def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Part 1
    totals = []
    totals.append(0)

    for line in lines:
        if line == "\n":
            totals.append(0)
        else:
            num = int(line.strip())
            totals[-1] += num

    print(max(totals))

    # Part 2
    total = 0

    for i in range(3):
        new_max = max(totals)
        totals.remove(new_max)
        total += new_max
    
    print(total)

    

if __name__ == '__main__':
    main()