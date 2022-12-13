class CPU:
    def __init__(self):
        self._registers = {"X": 1}
        self._instructions = {
            "addx": self._addx,
            "noop": self._noop,
        }
        self._cycle = 0
        self._cycle_values = {}
        self._crt = [["" for _ in range(40)] for _ in range(6)]
        self._curr_pixel = [0, 0]
    
    def dispatch(self, instruction, *args):
        self._instructions[instruction](*args)
    
    def _addx(self, value):
        for _ in range(2):
            self._cycle += 1
            self._cycle_values[self._cycle] = self._registers["X"]
            self._draw_on_crt()
        self._registers["X"] += value
    
    def _noop(self):
        self._cycle += 1
        self._cycle_values[self._cycle] = self._registers["X"]
        self._draw_on_crt()
    
    def _draw_on_crt(self):
        if self._curr_pixel[1] in range(self._registers["X"]-1, self._registers["X"]+2):
            self._crt[self._curr_pixel[0]][self._curr_pixel[1]] = "#"
        else:
            self._crt[self._curr_pixel[0]][self._curr_pixel[1]] = "."

        if self._curr_pixel[1] == 39:
            self._curr_pixel[1] = 0
            self._curr_pixel[0] += 1
        else:
            self._curr_pixel[1] += 1

    def get_cycle_value(self, cycle_n):
        return self._cycle_values[cycle_n]

    def get_crt(self):
        return self._crt
    
def main():

    with open("input.txt") as f:
        instructions = f.readlines()

    cpu = CPU()
    for instruction in instructions:
        if instruction.startswith("noop"):
            cpu.dispatch("noop")
        else:
            instr = instruction.strip().split(" ")[0]
            value = int(instruction.strip().split(" ")[1])
            cpu.dispatch(instr, value)
    
    # Part 1
    cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0
    for cycle in cycles:
        total_signal_strength += cycle * cpu.get_cycle_value(cycle)

    print(f"Part 1: {total_signal_strength}")

    # Part 2
    crt = cpu.get_crt()
    for row in crt:
        print("".join(row))

if __name__ == '__main__':
    main()
        