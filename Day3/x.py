from string import ascii_lowercase, ascii_uppercase

VALUES = {key: value for key, value in zip(ascii_lowercase+ascii_uppercase, range(1, 53))}

def main():
    
    with open("input.txt", "r") as f:
        rucksacks = f.readlines()

    # PART 1
    total = 0
    for r in rucksacks:
        first_half = r[:len(r)//2]
        second_half = r[len(r)//2:]
        
        for c in ascii_lowercase + ascii_uppercase:
            if c in first_half and c in second_half:
                total += VALUES[c]

    print(total)

    # PART 2
    total = 0
    for i in range(0, len(rucksacks), 3):
        r1 = rucksacks[i]
        r2 = rucksacks[i+1]
        r3 = rucksacks[i+2]

        for c in ascii_lowercase + ascii_uppercase:
            if c in r1 and c in r2 and c in r3:
                total += VALUES[c]
    
    print(total)
    
if __name__ == '__main__':
    main()