class FS:
    def __init__(self):
        self._root = Dir("/")
        self._existing_dirs = {self._root.get_path(): self._root}
        self._current_dir = self._root

    def cd(self, path):
        if path == "/":
            self._current_dir = self._root
            return
        elif path == "..":
            self._current_dir = self._current_dir.get_parent()
        else:
            self._current_dir = self._existing_dirs[self._current_dir.get_path() + path]

    def add_child_to_curr(self, name, type, size=0):
        if type == "dir":
            new_dir = Dir(self._current_dir.get_path() + name, self._current_dir)
            self._current_dir.add_child(new_dir)
            self._existing_dirs[new_dir.get_path()] = new_dir
        elif type == "file":
            self._current_dir.add_child(FakeFile(self._current_dir.get_path(), size))

    def compute_sizes_below_thresholds(self, threshold):
        return [dir.get_size() for dir in self._existing_dirs.values() if dir.get_size() <= threshold]

    def compute_sizes_above_thresholds(self, threshold):
        return [dir.get_size() for dir in self._existing_dirs.values() if dir.get_size() >= threshold]

    def compute_total_size(self):
        return self._existing_dirs["/"].get_size()

class Dir:
    def __init__(self, path, parent=None):
        self._path = path
        self._children = []
        self._parent = parent
        self._size = 0

    def add_child(self, child):
        self._children.append(child)
        self.update_size(child.get_size())

    def get_path(self):
        return self._path

    def get_parent(self):
        return self._parent

    def get_size(self):
        return self._size
    
    def update_size(self, size):
        self._size += size
        if self._parent is not None:
            self._parent.update_size(size)

    def __repr__(self):
        return "dir: " + self._path + ", size: " + str(self._size)

class FakeFile:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_size(self):
        return self._size

    def __repr__(self):
        return "file: " + self._name + ", size: " + str(self._size)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    command_indices = []
    for i in range(len(lines)):
        if lines[i].startswith("$"):
            command_indices.append(i)

    commands = []
    for i in range(len(command_indices)):
        if i == len(command_indices) - 1:
            commands.append(lines[command_indices[i]:])
        else:
            commands.append(lines[command_indices[i]:command_indices[i+1]])

    fs = FS()
    for command in commands:
        if command[0].startswith("$ cd"):
            path = command[0].strip("\n").split(" ")[2]
            fs.cd(path)

        elif command[0].startswith("$ ls"):
            for arg in command[1:]:
                arg = arg.strip("\n")
                if arg.startswith("dir"):
                    fs.add_child_to_curr(arg.split(" ")[1], "dir")
                else:
                    fs.add_child_to_curr(arg.split(" ")[1], "file", int(arg.split(" ")[0]))

    # PART 1
    # print(fs._existing_dirs)
    print(f"Sum of sizes of directories below the given threshold: {sum(fs.compute_sizes_below_thresholds(100000))}")

    # PART 2
    print(f"Total space used: {fs.compute_total_size()}/70000000")
    print(f"Minimum that would free up enough space: {min(fs.compute_sizes_above_thresholds(fs.compute_total_size() - 40000000))}")

if __name__ == "__main__":
    main()