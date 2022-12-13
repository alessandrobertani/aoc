from functools import reduce
from math import lcm

class Monkey:
    monkey_number = 0

    def __init__(self, starting_items, operation, test, if_true, if_false):
        self._items = starting_items
        self._operation = operation
        self._test = (test, if_true, if_false)
        self._monkey_true = None
        self._monkey_false = None
        self._id = Monkey.monkey_number
        Monkey.monkey_number += 1

        self._inspections = 0

    def __repr__(self):
        return f"Monkey {self._id}"

    def __str__(self):
        return f"Monkey {self._id}"

    def round(self, worry_reduction_factor=None):
        to_remove = []
        for i in range(len(self._items)):
            # Apply operation
            if self._operation[0] == "*":
                if self._operation[1] == "old":
                    self._items[i] *= self._items[i]
                else:
                    self._items[i] *= int(self._operation[1])
            else:
                if self._operation[1] == "old":
                    self._items[i] += self._items[i]
                else:
                    self._items[i] += int(self._operation[1])
            
            # Divide by worry reduction factor
            if worry_reduction_factor:
                self._items[i] %= worry_reduction_factor
            else :
                self._items[i] //= 3

            # Test
            if self._items[i] % self._test[0] == 0:
                self._monkey_true.add_item(self._items[i])
            else:
                self._monkey_false.add_item(self._items[i])
            
            to_remove.append(i)
            self._inspections += 1

        for i in to_remove[::-1]:
            self._items.pop(i)



    def add_item(self, item):
        self._items.append(item)

    def get_inspections(self):
        return self._inspections

    def get_items(self):
        return self._items

    def set_monkeys(self, monkey_true, monkey_false):
        self._monkey_true = monkey_true
        self._monkey_false = monkey_false

    def get_true_false(self):
        return self._test[1], self._test[2]

def exec_rounds(monkey_defs, num, part1):
    divisors = []
    monkeys = []
    for monkey_def in monkey_defs:
        monkey_def = monkey_def.split("\n")
        for line in monkey_def:
            line = line.strip()
            
        starting_items = [int(x.replace(",", "")) for x in monkey_def[1].split(" ")[2:]]
        print(starting_items)
        operation = (monkey_def[2].split(" ")[4], monkey_def[2].split(" ")[5])
        test = int(monkey_def[3].split(" ")[3])
        divisors.append(test)
        if_true = monkey_def[4].split(" ")[-1]
        if_false = monkey_def[5].split(" ")[-1]
        monkey = Monkey(starting_items=starting_items, operation=operation, test=test, if_true=if_true, if_false=if_false)
        monkeys.append(monkey)

    for monkey in monkeys:
        true, false = monkey.get_true_false()
        monkey.set_monkeys(monkeys[int(true)], monkeys[int(false)])

    for i in range(num):
        for monkey in monkeys:
            if part1:
                monkey.round()
            else:
                monkey.round(worry_reduction_factor=lcm(*divisors))

    inspections = sorted([monkey.get_inspections() for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]

def main():
    
    with open("input.txt") as f:
        monkey_defs = f.read().split("\n\n")

    first_result = exec_rounds(monkey_defs, 20, True)
    print(f"Part 1: {first_result}")

    second_result = exec_rounds(monkey_defs, 10000, False)
    print(f"Part 2: {second_result}")


if __name__ == "__main__":
    main()