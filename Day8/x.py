class Tree:
    def __init__(self, height) -> None:
        self._height = height
        self._is_visible = False
        self._vd_right = 0
        self._vd_left = 0
        self._vd_top = 0
        self._vd_bottom = 0

    def set_visibility(self, is_visible: bool) -> None:
        self._is_visible = is_visible

    def get_visibility(self) -> bool:
        return self._is_visible

    def get_height(self) -> int:
        return self._height

    def __repr__(self) -> str:
        return f"Tree(height={self._height}, is_visible={self._is_visible})"

    def is_higher(self, tree) -> bool:
        if tree is not None:
            return self._height > tree.get_height()
        return True

    def set_vd_right(self, vd_right: int) -> None:
        self._vd_right = vd_right
    
    def set_vd_left(self, vd_left: int) -> None:    
        self._vd_left = vd_left

    def set_vd_top(self, vd_top: int) -> None:
        self._vd_top = vd_top
    
    def set_vd_bottom(self, vd_bottom: int) -> None:
        self._vd_bottom = vd_bottom
    
    def compute_scenic_score(self) -> int:
        return self._vd_right * self._vd_left * self._vd_top * self._vd_bottom

    def compute_viewing_distance_on_line(self, line):
        if not line:
            return 0
        vd = 1
        for tree in line[:-1]:
            if self._height <= tree.get_height():
                break
            vd += 1
        return vd

class Forest:
    def __init__(self, height: int) -> None:
        self._trees = [[] for _ in range(height)]

    def add_tree(self, tree: Tree, row: int) -> None:
        self._trees[row].append(tree)

    def compute_visibilities(self):
        for i in range(len(self._trees)):
            for j in range(len(self._trees[i])):
                curr_tree = self._trees[i][j]
                left_row = self._trees[i][:j]
                right_row = self._trees[i][j+1:]
                top_row = [self._trees[x][j] for x in range(i)]
                bottom_row = [self._trees[x][j] for x in range(i+1, len(self._trees))]

                if i == 0 or i == len(self._trees) - 1 or j == 0 or j == len(self._trees[i]) - 1:
                    curr_tree.set_visibility(True)
                elif all([curr_tree.is_higher(tree) for tree in left_row]) or all([curr_tree.is_higher(tree) for tree in right_row]) or all([curr_tree.is_higher(tree) for tree in top_row]) or all([curr_tree.is_higher(tree) for tree in bottom_row]):
                    curr_tree.set_visibility(True)

    def number_of_visible_trees(self) -> int:
        return sum([1 for row in self._trees for tree in row if tree.get_visibility()])

    def compute_viewing_distances(self):
        for i in range(len(self._trees)):
            for j in range(len(self._trees[i])):
                curr_tree = self._trees[i][j]
                left_row = self._trees[i][:j][::-1]
                right_row = self._trees[i][j+1:]
                top_row = [self._trees[x][j] for x in range(i)][::-1]
                bottom_row = [self._trees[x][j] for x in range(i+1, len(self._trees))]

                curr_tree.set_vd_left(curr_tree.compute_viewing_distance_on_line(left_row))
                curr_tree.set_vd_right(curr_tree.compute_viewing_distance_on_line(right_row))
                curr_tree.set_vd_top(curr_tree.compute_viewing_distance_on_line(top_row))
                curr_tree.set_vd_bottom(curr_tree.compute_viewing_distance_on_line(bottom_row))

    def max_scenic_score(self) -> int:
        return max([tree.compute_scenic_score() for row in self._trees for tree in row])
                
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    forest = Forest(len(lines))
    for i in range(len(lines)):
        for j in range(len(lines[i].strip("\n"))):
            forest.add_tree(Tree(int(lines[i][j])), i)

    # PART 1
    forest.compute_visibilities()
    visible_trees = forest.number_of_visible_trees()
    print(f"Part 1: {visible_trees}")   

    # PART 2
    forest.compute_viewing_distances()
    max_scenic_score = forest.max_scenic_score()
    print(f"Part 2: {max_scenic_score}")
    
if __name__ == '__main__':
    main()