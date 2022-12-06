
class Buffer:

    def __init__(self, dim):
        self.buff = ""
        self.dim = dim
        self.total_chars = 0

    def add(self, c):
        if len(self.buff) < self.dim:
            self.buff += c
        else:
            self.buff = self.buff[1:] + c

        self.total_chars += 1

    def get_count(self):
        return self.total_chars

    def get_buffer(self):
        return self.buff

    def all_different(self):
        return all(self.buff.count(x) == 1 for x in self.buff)

def compute_solution(dim, content):

    b = Buffer(dim)
    for c in content:
        if len(b.get_buffer()) == dim and b.all_different():
            return b.get_count()
        else:
            b.add(c)

def main():
    with open("input.txt", "r") as f:
        content = f.read()

    print(compute_solution(4, content))
    print(compute_solution(14, content))
        

if __name__ == '__main__':
    main() 