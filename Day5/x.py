from string import ascii_uppercase

def main():
    
    with open("input.txt") as f:
        lines = f.readlines()

    # PART 1
    stack_lines = [x for x in lines if "[" in x]
    move_lines = [x.strip() for x in lines if "move" in x]

    stacks = [[] for _ in range(len(stack_lines[0]) // 4)]
    
    for line in stack_lines:
        for i in range(0, len(line), 4):
            if any(x in line[i:i+3] for x in ascii_uppercase):
                stacks[i//4].append(line[i+1])

    moves = []

    for line in move_lines:
        num_crates = int(line.split(" ")[1])
        from_stack = int(line.split(" ")[3]) - 1
        to_stack = int(line.split(" ")[5]) - 1
        moves.append({"num_crates": num_crates, "from_stack": from_stack, "to_stack": to_stack})

    for move in moves:
        for i in range(move["num_crates"]):
            stacks[move["to_stack"]].insert(i, stacks[move["from_stack"]].pop(0))

    print("".join(stacks[x][0] for x in range(len(stacks))))

if __name__ == '__main__':
    main()