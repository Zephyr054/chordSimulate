import bisect

class Chord:
    def __init__(self, m, nodes):
        self.m = m
        self.ring_size = 2 ** m
        self.nodes = sorted(nodes)

    def successor(self, x):
        idx = bisect.bisect_left(self.nodes, x)
        if idx == len(self.nodes):
            return self.nodes[0]
        return self.nodes[idx]

    def finger_table(self, node):
        table = []
        for i in range(1, self.m + 1):
            start = (node + 2 ** (i - 1)) % self.ring_size
            table.append((start, self.successor(start)))
        return table

    def add_node(self, new_node):
        if new_node not in self.nodes:
            bisect.insort(self.nodes, new_node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

    def print_finger_tables(self, title=None):
        if title:
            print(title)
        for n in self.nodes:
            print(f"\nNode {n}:")
            for i, (start, succ) in enumerate(self.finger_table(n), 1):
                print(f"  Entry {i}: start={start:>2}, successor={succ}")

    def find(self, k):
        return self.successor(k)


# Demo
initial_nodes = [2, 7, 11, 14]
chord = Chord(m=4, nodes=initial_nodes)
# Test case 1: Finger table
chord.print_finger_tables("== Finger tables ban đầu ==")

# Test case 2: Lookup ban đầu
print("\n== Lookup ban đầu ==")
for k in [0, 3, 6, 8, 13, 15]:
    print(f"Key {k:>2} -> Node {chord.find(k)}")

# Thêm node 9
chord.add_node(9)
chord.print_finger_tables("\n== Finger tables sau khi thêm node 9 ==")

# Test case 2: Lookup sau khi thêm node
print("\n== Lookup sau khi thêm node 9 ==")
for k in [6, 8, 13]:
    print(f"Key {k:>2} -> Node {chord.find(k)}")

# Xóa node 14
chord.remove_node(14)
chord.print_finger_tables("\n== Finger tables sau khi xóa node 14 ==")

# Test case 3: Lookup sau khi xóa node
print("\n== Lookup sau khi xóa node 14 ==")
for k in [3, 6, 8, 13, 15]:
    print(f"Key {k:>2} -> Node {chord.find(k)}")
