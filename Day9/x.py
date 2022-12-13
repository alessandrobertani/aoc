class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = [(x, y)]

    def update_positions(self, x, y):
        if (x, y) not in self.positions:
            self.positions.append((x, y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Rope:
    def __init__(self, length: int):
        self.points = [Point(0, 0) for i in range(length)]

    # Rules:
    # 1. If the head is two steps away in any direction, the tail will move one step in that direction
    # 2. If the head and tail aren't touching and aren't in the same row or column, the tail moves one step diagonally to keep up

    def adjust_horizontally(self, point, idx):
        previous_pt = self.points[idx-1]

        if abs(point.x - previous_pt.x) <= 1 and abs(point.y - previous_pt.y) <= 1:
            return
        
        if previous_pt.y != point.y:
            point.y += 1 if previous_pt.y > point.y else -1
        point.x += 1 if previous_pt.x > point.x else -1
        
        point.update_positions(point.x, point.y)

    def adjust_vertically(self, point, idx):
        previous_pt = self.points[idx-1]

        if abs(point.x - previous_pt.x) <= 1 and abs(point.y - previous_pt.y) <= 1:
            return
        
        if previous_pt.x != point.x:
            point.x += 1 if previous_pt.x > point.x else -1
        point.y += 1 if previous_pt.y > point.y else -1

        point.update_positions(point.x, point.y)

    def move_up(self):
        self.points[0].y += 1
        for i, point in enumerate(self.points[1:], 1):
            self.adjust_vertically(point, i)
        
    def move_down(self):
        self.points[0].y -= 1
        for i, point in enumerate(self.points[1:], 1):
            self.adjust_vertically(point, i)

    def move_left(self):
        self.points[0].x -= 1
        for i, point in enumerate(self.points[1:], 1):
            self.adjust_horizontally(point, i)

    def move_right(self):
        self.points[0].x += 1
        for i, point in enumerate(self.points[1:], 1):
            self.adjust_horizontally(point, i)


    def move(self, command, value):
        match command:
            case "U":
                for i in range(value):
                    self.move_up()
            case "D":
                for i in range(value):
                    self.move_down()
            case "L":
                for i in range(value):
                    self.move_left()
            case "R":
                for i in range(value):
                    self.move_right()

    def get_tail(self):
        return self.points[-1]


def print_grid(rope):
    width = 40
    height = 40

    grid = [["." for i in range(width)] for j in range(height)]

    for i, point in enumerate(rope.points):
        if i == 0:
            grid[-point.y+height//2][point.x+width//2] = "H"
        elif i == len(rope.points) - 1:
            grid[-point.y+height//2][point.x+width//2] = "T"
        else:
            grid[-point.y+height//2][point.x+height//2] = str(i)

    print("  " + "".join([str(i) for i in range(width)]))
    for i, row in enumerate(grid):
        print(f"{i} "+"".join(row))

    print("\n\n")

def main():
    with open("test.txt", "r") as f:
        lines = f.readlines()

    commands = []
    for line in lines:
        command, value = line.strip().split(" ")
        commands.append((command, int(value)))

    # Part 1
    rope = Rope(2)
    for command, value in commands:
        rope.move(command, value)

    print(f"Part 1: {len(rope.get_tail().positions)}")

    # Part 2
    rope = Rope(10)
    for command, value in commands:
        rope.move(command, value)
        print_grid(rope)
    
    print(f"Part 2: {len(rope.get_tail().positions)}")

if __name__ == '__main__':
    main()