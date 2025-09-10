import bisect
import matplotlib.pyplot as plt
import numpy as np

class Chord:
    def __init__(self, m, nodes):
        self.m = m
        self.ring_size = 2 ** m
        self.nodes = sorted(nodes)

    # ---------- Chord logic ----------
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

    def print_finger_tables(self, title=None):
        if title:
            print(title)
        for n in self.nodes:
            print(f"\nNode {n}:")
            table = self.finger_table(n)
            for i, (start, succ) in enumerate(table, 1):
                print(f"  Entry {i}: start={start:>2}, successor={succ}")

    def find(self, k):
        return self.successor(k)

    # ---------- Drawing ----------
    def _pos_xy(self, pos, radius):
        angle = np.pi/2 - 2 * np.pi * pos / self.ring_size
        return radius * np.cos(angle), radius * np.sin(angle)

    def draw_ring(self, label_all=False):
        radius = 5
        fig, ax = plt.subplots(figsize=(8,8))
        circle = plt.Circle((0, 0), radius, color='lightgray', fill=False)
        ax.add_artist(circle)

        for pos in range(self.ring_size):
            x, y = self._pos_xy(pos, radius)

            if pos in self.nodes:
                # Node chính: điểm to + nhãn đỏ đậm
                ax.plot(x, y, 'o', markersize=10, color='blue')
                ax.text(x*1.18, y*1.18, str(pos), ha='center', va='center',
                        fontsize=12, color='red', fontweight='bold')
            else:
                # Node phụ: chấm nhỏ xám, không nhãn (trừ khi label_all=True)
                ax.plot(x, y, 'o', markersize=4, color='gray')
                if label_all:
                    ax.text(x*1.12, y*1.12, str(pos), ha='center', va='center',
                            fontsize=8, color='black')

        ax.set_xlim(-radius*1.55, radius*1.55)
        ax.set_ylim(-radius*1.55, radius*1.55)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.title(f"Chord Ring (m={self.m}, nodes={self.nodes})")
        plt.show()


# ===== Demo theo đề bài =====
# 1) Vòng ban đầu
initial_nodes = [1, 5, 9, 12]
chord = Chord(m=4, nodes=initial_nodes)
# 2) In finger table ban đầu
print("== Finger tables ban đầu ==")
chord.print_finger_tables()

# 3) Thêm node 7
print("\n== Thêm node 7 ==")
chord.add_node(7)

# 4) In finger table sau khi thêm 7
chord.print_finger_tables(title="\n== Finger tables sau khi thêm node 7 ==")

# 5) Test find(k)
print("\n== Test find(k) ==")
for k in [0, 3, 6, 8, 14, 15]:
    print(f"Key {k:>2} -> Node {chord.find(k)}")

#Vẽ vòng:
chord.draw_ring(label_all=False) 